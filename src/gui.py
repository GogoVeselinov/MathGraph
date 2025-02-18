from tkinter import Tk, Label, Entry, Button, StringVar, Frame, OptionMenu
import matplotlib.pyplot as plt
import numpy as np
from plotter import plot_function

class MathGraphApp:
    def __init__(self, master):
        self.master = master
        master.title("Math Graph Renderer")

        self.frame = Frame(master)
        self.frame.pack()

        self.function_var = StringVar(value="sin")
        self.amplitude_var = StringVar(value="1")
        self.frequency_var = StringVar(value="1")
        self.phase_var = StringVar(value="0")

        self.create_widgets()

    def create_widgets(self):
        Label(self.frame, text="Function:").grid(row=0, column=0)
        OptionMenu(self.frame, self.function_var, "sin", "cos", "tan", "cot").grid(row=0, column=1)

        Label(self.frame, text="Amplitude:").grid(row=1, column=0)
        Entry(self.frame, textvariable=self.amplitude_var).grid(row=1, column=1)

        Label(self.frame, text="Frequency:").grid(row=2, column=0)
        Entry(self.frame, textvariable=self.frequency_var).grid(row=2, column=1)

        Label(self.frame, text="Phase (radians):").grid(row=3, column=0)
        Entry(self.frame, textvariable=self.phase_var).grid(row=3, column=1)

        self.plot_button = Button(self.frame, text="Plot", command=self.plot)
        self.plot_button.grid(row=4, columnspan=2)

    def plot(self):
        function = self.function_var.get()
        amplitude = float(self.amplitude_var.get())
        frequency = float(self.frequency_var.get())
        phase = float(self.phase_var.get())

        x = np.linspace(-10, 10, 400)
        if function == "sin":
            y = amplitude * np.sin(frequency * x + phase)
        elif function == "cos":
            y = amplitude * np.cos(frequency * x + phase)
        elif function == "tan":
            y = amplitude * np.tan(frequency * x + phase)
        elif function == "cot":
            y = amplitude * (1/np.tan(frequency * x + phase))
        else:
            return

        plot_function(x, y, function)

def main():
    root = Tk()
    app = MathGraphApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()