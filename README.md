# Math Graph Application

This project is a Python GUI desktop application designed for rendering mathematical functions such as sine, cosine, tangent, and cotangent. Users can input values to change the parameters of the functions and visualize the results.

## Project Structure

```
math-graph-app
├── src
│   ├── main.py        # Entry point of the application
│   ├── gui.py         # Contains the GUI setup
│   ├── plotter.py     # Function for plotting graphs
│   └── utils.py       # Utility functions for mathematical calculations
├── requirements.txt    # Lists project dependencies
└── README.md           # Documentation for the project
```

## Installation

To install the required dependencies, navigate to the project directory and run:

```
pip install -r requirements.txt
```

## Usage

To run the application, execute the following command:

```
python src/main.py
```

This will launch the GUI where you can input parameters for the functions and render the corresponding graphs.

## Dependencies

The project requires the following Python packages:

- `matplotlib`: For rendering the graphs.
- `tkinter`: For creating the graphical user interface.

Make sure you have these packages installed before running the application.