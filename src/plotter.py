import matplotlib.pyplot as plt

def plot_function(x, y, function_name):
    plt.figure()
    plt.plot(x, y, label=function_name)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'{function_name} function')
    plt.legend()
    plt.grid(True)
    plt.show()