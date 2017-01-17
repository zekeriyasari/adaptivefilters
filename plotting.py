import matplotlib.pyplot as plt


def get_learning_curve_plot():
    fig, ax = plt.subplots()
    ax.grid(which='both')
    ax.set_xlabel(r'$Number \; of \; iterations, \; n$')
    ax.set_ylabel(r'$Ensemble-averaged \; square \; error$')
    plt.tight_layout()
    return fig, ax


def get_tap_weights_graph(n):
    if n:
        if n > 1:
            fig, ax = plt.subplots(n)
            for i in range(n):
                ax[i].set_xlabel(r'$k$')
                ax[i].set_ylabel(r'$\hat{w_a}_k$')
                ax[i].set_ylim([-2, 2])
        else:
            fig, ax = plt.subplots(1)
            ax.set_xlabel(r'$k$')
            ax.set_ylabel(r'$\hat{w}_k$')
            ax.set_ylim([-2, 2])
    else:
        fig, ax = plt.subplots(1)
        ax.set_xlabel(r'$k$')
        ax.set_ylabel(r'$\hat{w_a}_k$')
        ax.set_ylim([-2, 2])
    return fig, ax
