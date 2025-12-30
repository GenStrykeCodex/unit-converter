# Module 2: Weight Conversions

''' ___________________ DEFINING UNITS ___________________'''

# defining all units of weight with kilogram as standard unit
weight_units = {
    'mg': 0.000001,
    'g': 0.001,
    'kg': 1,
    'lb': 0.453592,
    'ounce': 0.0283495,
    'ton': 1000,
    'metric ton': 1000,
}

''' ___________________ MAIN CODE ___________________'''

# converting length units
def convert_weight(value, unit, to_unit):

    change = weight_units.get(unit) / weight_units.get(to_unit)
    return value * change
