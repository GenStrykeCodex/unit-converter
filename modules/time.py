# Module 4: Time Conversions

''' ___________________ DEFINING UNITS ___________________'''

# defining all units of time with second as standard unit
time_units = {
    'ms': 0.001,
    's': 1,
    'minute': 60,
    'hour': 3600,
    'day': 86400,
    'week': 604800,
    'month': 2592000,  # Approximate: 30 days
    'year': 31536000   # 365 days
}

''' ___________________ MAIN CODE ___________________'''

# converting length units
def convert_time(value, unit, to_unit):

    change = time_units.get(unit) / time_units.get(to_unit)
    return value * change