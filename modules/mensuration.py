# Module 1: Length, Area, Volume Conversions

''' ___________________ DEFINING UNITS ___________________'''

# defining all units of length with metre as standard unit
length_units = {
    "mm": 0.001,
    "cm": 0.01,
    "m": 1,
    "km": 1000,
    "inch": 0.0254,
    "foot": 0.3048,
    "yard": 0.9144,
    "mile": 1609.34,
}

# defining all units of area with sq. metre as standard unit
area_units = {
    "sq mm": 0.000001,
    "sq cm": 0.0001,
    "sq m": 1,
    "sq km": 1000000,
    "sq inch": 0.00064516,
    "sq foot": 0.092903,
    "sq yard": 0.836127,
    "acre": 4046.86,
    "hectare": 10000,
}

# defining all units of volume with litre as standard unit
volume_units = {
    "ml": 0.001,
    "cl": 0.01,
    "dl": 0.1,
    "l": 1,
    "gallon": 3.78541,
    "cubic meter": 1000,
    "cubic cm": 0.001,
}

''' ___________________ MAIN CODE ___________________'''

# converting length units
def convert_length(value, unit, to_unit):

    change = length_units.get(unit) / length_units.get(to_unit)
    return value * change

# converting area units
def convert_area(value, unit, to_unit):

    change = area_units.get(unit) / area_units.get(to_unit)
    return value * change

# converting volume units
def convert_volume(value, unit, to_unit):

    change = volume_units.get(unit) / volume_units.get(to_unit)
    return value * change