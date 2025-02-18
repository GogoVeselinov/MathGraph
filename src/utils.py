def evaluate_sine(x):
    import math
    return math.sin(x)

def evaluate_cosine(x):
    import math
    return math.cos(x)

def evaluate_tangent(x):
    import math
    return math.tan(x)

def evaluate_cotangent(x):
    if math.tan(x) == 0:
        raise ValueError("Cotangent is undefined for this value.")
    return 1 / math.tan(x)