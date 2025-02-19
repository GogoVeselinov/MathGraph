import matplotlib.pyplot as plt

def plot_function(x, y, function_name, periodicity):
    plt.figure()
    plt.plot(x, y, label=function_name)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'{function_name} function')
    plt.legend()
    plt.grid(True)
    plt.annotate(f'Periodicity: {periodicity}', xy=(0.05, 0.95), xycoords='axes fraction', fontsize=10, ha='left', va='top', bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="white"))
    plt.show()