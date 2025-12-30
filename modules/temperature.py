# Module 3: Temperature Conversions

''' ___________________ MAIN CODE ___________________'''

# converting celsius into fahrenheit
def degC_to_degF(value):

    new_val = (9 / 5) * value + 32
    return new_val

# converting fahrenheit into celsius
def degF_to_degC(value):

    new_val = (5 / 9) * (value - 32)
    return new_val

# converting kelvin into celsius
def K_to_degC(value):

    new_val = value - 273.15
    return new_val

# converting celsius into kelvin
def degC_to_K(value):

    new_val = value + 273.15
    return new_val