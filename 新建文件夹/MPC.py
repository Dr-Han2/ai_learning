import numpy as np
import casadi as ca
class MPC:
    def __init__(self):
        self.N=50       #预测步长
        self.dt=0.02    #控制周期
        self.Lf=2.5     #轴距
        self.Velocity_Max=100.0 #最大速度

        self.Number_of_states=6 #状态 px,py,psi,v,cte,epsi
        self.Number_of_actuations=2 #控制量:delta转角，a加速度

        #优化变量总维度 NX=N*states+(N-1)*actuations
        self.NX=self.N * self.Number_of_states + (self.N - 1) * self.Number_of_actuations
        self.NG=self.N * self.Number_of_states

        # -------- 状态变量索引 -------
        self.ID_First_px = 0
        self.ID_First_py = self.ID_First_px + self.N
        self.ID_First_psi= self.ID_First_psi + self.N
        self.ID_First_v = self.ID_First_psi + self.N
        self.ID_First_cte = self.ID_First_v + self.N
        self.ID_First_epsi = self.ID_First_cte + self.N

        # -------- 控制变量索引 -------
        self.ID_First_delta = self.ID_First_epsi + self.N
        self.ID_First_a = self.ID_First_delta + (self.N-1)

        # -------- 代价权重 -------
        self.W_cte = 1500.0
        self.W_epsi = 1500.0
        self.W_v = 1.0

        self.W_delta = 10.0
        self.W_a = 10.0

        self.W_ddelta = 150.0 #转角变换惩罚
        self.W_da = 15.0      #加速度变化惩罚

        #输出结果
        self.steer = 0.0 # 输出方向盘转角
        self.throttle =0.0 #输出油门/加速度

        #存储预测轨迹点
        self.future_xs = []
        self.future_ys = []

    def solve(self, state: np.ndarray , K : np.ndarray):
        '''‘’‘求解MPC优化问题
        :param state: 当前状态 [px , py , psi , v , cte ,epsi](6维)
        :param K :  参考轨迹系数 拟合参考路径多项式
        :return None , 结果保存在self.steer, self.throttle, future_xs/ys
        '''
        #清空预测轨迹
        self.future_xs.clear()
        self.future_ys.clear()

        #定义优化变量
        opt_var=ca.MX.sym('opt_var',self.NX)

        # ========== 提取状态和控制变量（从一维优化向量中切片）==========
        # 状态序列
        px = opt_var[self.ID_First_px : self.ID_First_px + self.N]
        py = opt_var[self.ID_First_py : self.ID_First_py + self.N]
        psi = opt_var[self.ID_First_psi : self.ID_First_psi + self.N]
        v = opt_var[self.ID_First_v : self.ID_First_v + self.N]
        cte = opt_var[self.ID_First_cte : self.ID_First_cte + self.N]
        epsi = opt_var[self.ID_First_epsi : self.ID_First_epsi + self.N]

        #控制序列(N-1个控制变量)
        delta = opt_var[self.ID_FIRST_delta: self.ID_FIRST_delta + (self.N - 1)]
        a = opt_var[self.ID_FIRST_a: self.ID_FIRST_a + (self.N - 1)]

        # ========== 构建代价函数 Cost ==========
        cost = 0
        for t in range(self.N):
            cost += self.W_cte * cte[t]**2
            cost += self.W_epsi * epsi[t]**2
            cost +=self.W_v * (v[t] - self.Velocity_Max)**2

        #控制惩罚
        for t in range(self.N-1):
            cost +=self.W_delta * delta[t]**2
            cost +=self.W_a * a[t]**2
        #控制增量惩罚(相邻时刻控制量变化)
        for t in range(self.N-2):
            cost +=self.W_ddelta * (delta[t+1]-delta)**2
            cost +=self.W_da * (a[t+1]-a[1])**2

        #=========== 车辆动力学约束 ==========#
        g = []
        for t in range(self.N-1):
            px_t = px[t]
            py_t = py[t]
            psi_t = psi[t]
            v_t = v[t]
            cte_t = cte[t]
            epsi_t = epsi[t]

            delta_t = delta[t]
            a_t = a[t]

            #离散自行车动力学
            px_next = px_t + v_t* ca.cos(psi_t) * self.dt
            py_next = py_t + v_t* ca.sin(psi_t) * self.dt
            psi_next = psi_t + v_t / self.Lf * delta_t * self.dt
            v_next = v_t +a_t* self.dt

            # 参考路径 y = K0 + K1*x + K2*x^2 + K3*x^3
            poly_ref = K[0] + K[1] * px_t + K[2] * px_t ** 2 + K[3] * px_t ** 3
            poly_der = K[1] + 2 * K[2] * px_t + 3 * K[3] * px_t ** 2
            psi_ref = ca.atan(poly_der)

            cte_next = poly_ref - py_t + v_t * ca.sin(epsi_t) * self.dt
            epsi_next = psi_t - psi_ref + v_t / self.Lf * delta_t * self.dt

            # 等式约束：下一时刻状态 = 动力学预测
            g.append(px[t + 1] - px_next)
            g.append(py[t + 1] - py_next)
            g.append(psi[t + 1] - psi_next)
            g.append(v[t + 1] - v_next)
            g.append(cte[t + 1] - cte_next)
            g.append(epsi[t + 1] - epsi_next)

        g = ca.vertcat(*g)

        # ========== 变量上下界设置 ==========
        # 初始状态硬约束：t=0状态等于当前测量state
        self.x_lowerbound[:] = -1e20
        self.x_upperbound[:] = 1e20

        # t=0状态固定为当前状态
        self.x_lowerbound[self.ID_FIRST_px] = state[0]
        self.x_upperbound[self.ID_FIRST_px] = state[0]

        self.x_lowerbound[self.ID_FIRST_py] = state[1]
        self.x_upperbound[self.ID_FIRST_py] = state[1]

        self.x_lowerbound[self.ID_FIRST_psi] = state[2]
        self.x_upperbound[self.ID_FIRST_psi] = state[2]

        self.x_lowerbound[self.ID_FIRST_v] = state[3]
        self.x_upperbound[self.ID_FIRST_v] = state[3]

        self.x_lowerbound[self.ID_FIRST_cte] = state[4]
        self.x_upperbound[self.ID_FIRST_cte] = state[4]

        self.x_lowerbound[self.ID_FIRST_epsi] = state[5]
        self.x_upperbound[self.ID_FIRST_epsi] = state[5]

        # 控制量限幅 转角[-25°,25°]，加速度[-1,1]，和原知乎工程常用设置
        max_steer = 0.4363
        for t in range(self.N - 1):
            idx_delta = self.ID_FIRST_delta + t
            self.x_lowerbound[idx_delta] = -max_steer
            self.x_upperbound[idx_delta] = max_steer

            idx_a = self.ID_FIRST_a + t
            self.x_lowerbound[idx_a] = -1.0
            self.x_upperbound[idx_a] = 1.0

        # 等式约束全部等于0
        self.g_lowerbound[:] = 0
        self.g_upperbound[:] = 0

        # ========== 构建求解器Ipopt ==========
        nlp = {
            'x': opt_var,
            'f': cost,
            'g': g
        }
        opts = {
            'ipopt': {
                'max_iter': 1000,
                'print_level': 0,  # 0关闭控制台输出，调试改成>0
                'tol': 1e-4
            },
            'print_time': False
        }
        solver = ca.nlpsol('solver', 'ipopt', nlp, opts)

        # 初始猜测值
        x0 = np.zeros(self.NX)
        sol = solver(x0=x0, lbx=self.x_lowerbound, ubx=self.x_upperbound, lbg=self.g_lowerbound, ubg=self.g_upperbound)

        # 提取解
        sol_x = sol['x'].full().flatten()

        # 取第一个控制输出
        self.steer = sol_x[self.ID_FIRST_delta]
        self.throttle = sol_x[self.ID_FIRST_a]

        # 保存预测轨迹
        for t in range(self.N):
            self.future_xs.append(sol_x[self.ID_FIRST_px + t])
            self.future_ys.append(sol_x[self.ID_FIRST_py + t])

    # ========== 简单测试示例 ==========
    if __name__ == "__main__":
        mpc = MPC()
        # 初始状态 [px, py, psi, v, cte, epsi]
        current_state = np.array([0, 0, 0, 10, 0.5, 0.1])
        # 参考路径多项式系数 K0 K1 K2 K3
        poly_K = np.array([0, 0, 0.01, 0.0001])
        mpc.solve(current_state, poly_K)
        print(f"输出转角 steer = {mpc.steer:.4f} rad")
        print(f"输出加速度 throttle = {mpc.throttle:.4f} m/s^2")





