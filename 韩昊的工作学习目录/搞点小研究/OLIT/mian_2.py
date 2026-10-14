"""
@Author  : 韩昊
@Company : ******
@Date    : 
@Desc    : 
@Version : 1.0
"""
# plot_results.py
import numpy as np
import matplotlib.pyplot as plt

from OLIT import run_experiment


def f_sigmoid(x):
    return 1.0 / (1.0 + np.exp(-x / 2.0))


def f_cubic(x):
    return np.sign(x) * x ** 2


def collect_results():
    ns = [2, 3, 4, 5]
    noises = ["beta", "gaussian", "uniform"]
    f_funcs = {
        "sigmoid": f_sigmoid,
        "cubic": f_cubic,
    }

    results = {}
    for noise in noises:
        for name, f in f_funcs.items():
            accs = []
            for n in ns:
                acc = run_experiment(
                    n=n,
                    noise=noise,
                    N=1000,
                    f=f,
                    k=3,
                    n_trials=10,   # 正式复现可调成 50
                    base_seed=0,
                )
                accs.append(acc)
            results[(noise, name)] = accs
    return ns, noises, f_funcs, results


def plot_results(ns, noises, f_funcs, results):
    fig, axes = plt.subplots(1, len(noises), figsize=(15, 4), sharey=True)

    x = np.arange(len(ns))
    width = 0.35

    for ax, noise in zip(axes, noises):
        acc_sig = results[(noise, "sigmoid")]
        acc_cub = results[(noise, "cubic")]

        ax.bar(x - width/2, acc_sig, width, label="f = sigmoid")
        ax.bar(x + width/2, acc_cub, width, label="f = cubic")

        ax.set_title(f"noise = {noise}")
        ax.set_xticks(x)
        ax.set_xticklabels([f"n={n}" for n in ns])
        ax.set_ylim(0, 1.05)
        ax.set_ylabel("accuracy")
        ax.grid(axis="y", linestyle="--", alpha=0.4)

    axes[0].legend()
    plt.suptitle("OLIT accuracy under different noise and f", fontsize=14)
    plt.tight_layout()
    plt.savefig("olit_accuracy.png", dpi=150)
    plt.show()


if __name__ == "__main__":
    ns, noises, f_funcs, results = collect_results()
    plot_results(ns, noises, f_funcs, results)


