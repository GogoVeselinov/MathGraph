from tkinter import Tk, Label, Entry, Button, StringVar, Frame, OptionMenu
import matplotlib.pyplot as plt
import numpy as np
from plotter import plot_function

class MathGraphApp:
    def __init__(self, master):
        self.master = master
        master.title("Math Graph Renderer")

        self.frame = Frame(master)
        self.frame.pack(padx=10, pady=10)

        self.function_var = StringVar(value="sin")
        self.amplitude_var = StringVar(value="1")
        self.frequency_var = StringVar(value="1")
        self.phase_var = StringVar(value="0")
        self.periodicity_var = StringVar(value="2π")
        self.x_values_var = StringVar(value="-10,10")
        self.y_values_var = StringVar(value="-10,10")

        self.create_widgets()

    def create_widgets(self):
        Label(self.frame, text="Select the function and parameters to plot:").grid(row=0, column=0, columnspan=2, pady=(0, 10))

        Label(self.frame, text="Function:").grid(row=1, column=0, sticky="e")
        OptionMenu(self.frame, self.function_var, "sin", "cos", "tan", "cot", "radians", "circle", "ellipse").grid(row=1, column=1, sticky="w")

        Label(self.frame, text="Amplitude:").grid(row=2, column=0, sticky="e")
        Entry(self.frame, textvariable=self.amplitude_var).grid(row=2, column=1, sticky="w")

        Label(self.frame, text="Frequency:").grid(row=3, column=0, sticky="e")
        Entry(self.frame, textvariable=self.frequency_var).grid(row=3, column=1, sticky="w")

        Label(self.frame, text="Phase (radians):").grid(row=4, column=0, sticky="e")
        Entry(self.frame, textvariable=self.phase_var).grid(row=4, column=1, sticky="w")

        Label(self.frame, text="Periodicity:").grid(row=5, column=0, sticky="e")
        Entry(self.frame, textvariable=self.periodicity_var).grid(row=5, column=1, sticky="w")

        Label(self.frame, text="X Values (comma-separated):").grid(row=6, column=0, sticky="e")
        Entry(self.frame, textvariable=self.x_values_var).grid(row=6, column=1, sticky="w")

        Label(self.frame, text="Y Values (comma-separated):").grid(row=7, column=0, sticky="e")
        Entry(self.frame, textvariable=self.y_values_var).grid(row=7, column=1, sticky="w")

        self.plot_button = Button(self.frame, text="Plot", command=self.plot)
        self.plot_button.grid(row=8, column=0, columnspan=2, pady=(10, 0))

    def plot(self):
        function = self.function_var.get()
        amplitude = float(self.amplitude_var.get())
        frequency = float(self.frequency_var.get())
        phase = float(self.phase_var.get())
        periodicity = self.periodicity_var.get()

        x_values = list(map(float, self.x_values_var.get().split(',')))
        y_values = list(map(float, self.y_values_var.get().split(',')))

        x = np.linspace(x_values[0], x_values[1], 400)
        if function == "sin":
            y = amplitude * np.sin(frequency * x + phase)
        elif function == "cos":
            y = amplitude * np.cos(frequency * x + phase)
        elif function == "tan":
            y = amplitude * np.tan(frequency * x + phase)
        elif function == "cot":
            y = amplitude * (1/np.tan(frequency * x + phase))
        elif function == "radians":
            y = np.radians(x)
        elif function == "circle":
            theta = np.linspace(0, 2*np.pi, 400)
            x = amplitude * np.cos(theta)
            y = amplitude * np.sin(theta)
        elif function == "ellipse":
            theta = np.linspace(0, 2*np.pi, 400)
            x = amplitude * np.cos(theta)
            y = frequency * np.sin(theta)
        else:
            return

        plot_function(x, y, function, periodicity)

def main():
    root = Tk()
    app = MathGraphApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()