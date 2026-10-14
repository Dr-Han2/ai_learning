"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
from classSharedBikeandMothd import SharedBike

if __name__ == '__main__':
    #实例化对象
    SharedBike1 = SharedBike("1001","blue","yes")
    SharedBike2 = SharedBike("1002","blue","yes")
    print(SharedBike1.__dict__)
    print(SharedBike2.__dict__)
    print(f"SharedBike1的品牌:{SharedBike1.brand}")
    print(f"SharedBike2的品牌:{SharedBike2.brand}")
    #将2的品牌改为青桔
    print("=" * 30)
    SharedBike2.brand = "青桔"
    print(f"修改后SharedBike2的品牌为:{SharedBike2.brand}")
    #将1的颜色改为黄色
    SharedBike1.color = "yellow"
    print(f"修改后SharedBike1的颜色:{SharedBike1.color}")