# start building unit converter v1.0

# importing modules
import modules.mensuration as ms
import modules.temperature as tp
import modules.weight as wt
import modules.time as t

# greeting users with welcome
print("\nWelcome to Unit Converter v1.0!")

# defining important variables
length = ["mm", "cm", "m", "km", "inch", "foot", "yard", "mile"]
area = ["sq mm", "sq cm", "sq m", "sq km", "sq inch", "sq foot","sq yard", "acre", "hectare"]
volume = ["ml", "cl", "dl", "l", "gallon", "cubic meter", "cubic cm"]
weight = ['mg', 'g', 'kg', 'lb', 'ounce', 'ton', 'metric ton']
temperature = ["Celsius", "Fahrenheit", "Kelvin"]
time = ['ms', 's', 'minute', 'hour', 'day', 'week', 'month', 'year']

# helper function for pauses between actions
def pause():
    input("Press Enter to return")

# helper function to get units
def get_unit(var):

    for i, u in enumerate(var):          # display all units available for conversion
        print(f"{i+1}. {u}")

    while True:                         
        option = input(f"Choose an unit(1-{len(var)}): ")

        try:
            unit = var[int(option) - 1]     # getting unit from list
            return unit

        except Exception:
            print("Sorry! Please choose an valid option") # exception message

# helper function to get values
def get_value():

    while True:
        try:
            value = float(input("Enter the value: "))

            if value < 0:                       # values can't be negative for length, area, volume, weight and time
                print("Sorry! Please enter a positive value.")  
                continue

            return value
        
        except Exception:
            print("Sorry! Please enter a valid value.")

# helper function to get temperature values
def get_temp_value():

    while True:
        try:
            value = float(input("Enter the value: "))       # values can be -ve, +ve and 0 for temperature
            return value
        
        except Exception:
            print("Sorry! Please enter a valid value.")

# home menu of the application
def home_menu():

    print("\n------ Unit Converter ------\n")
    print("1. Length")
    print("2. Area")
    print("3. Volume")
    print("4. Weight")
    print("5. Temperature")
    print("6. Time")
    print("7. Exit")
    print("\n----------------------------")

# main function of the application
def main():

    while True:
        home_menu()         # call home menu

        while True:

            choice = input("\nChoose an option(1-7): ")

            if choice == "1":               # convert length units

                print("\nInitiating Length Converter..\n")
                value = get_value()

                len_copy = length.copy()
                print("\nUnit of value:")
                unit = get_unit(len_copy)

                len_copy.remove(unit)
                print("\nConvert to:")
                new_unit = get_unit(len_copy)

                new_value = ms.convert_length(value, unit, new_unit)
                
                print(f"\n{value} {unit} is equal to {new_value} {new_unit}")

                pause()
                break

            elif choice == "2":              # convert area units
                
                print("\nInitiating Area Converter..\n")
                value = get_value()

                area_copy = area.copy()
                print("\nUnit of value:")
                unit = get_unit(area_copy)

                area_copy.remove(unit)
                print("\nConvert to:")
                new_unit = get_unit(area_copy)

                new_value = ms.convert_area(value, unit, new_unit)
                
                print(f"\n{value} {unit} is equal to {new_value} {new_unit}")

                pause()
                break

            elif choice == "3":             # convert volume units
                
                print("\nInitiating Volume Converter..\n")
                value = get_value()

                vol_copy = volume.copy()
                print("\nUnit of value:")
                unit = get_unit(vol_copy)

                vol_copy.remove(unit)
                print("\nConvert to:")
                new_unit = get_unit(vol_copy)

                new_value = ms.convert_volume(value, unit, new_unit)
                
                print(f"\n{value} {unit} is equal to {new_value} {new_unit}")

                pause()
                break

            elif choice == "4":            # convert weight units
                
                print("\nInitiating Weight Converter..\n")
                value = get_value()

                weight_copy = weight.copy()
                print("\nUnit of value:")
                unit = get_unit(weight_copy)

                weight_copy.remove(unit)
                print("\nConvert to:")
                new_unit = get_unit(weight_copy)

                new_value = wt.convert_weight(value, unit, new_unit)
                
                print(f"\n{value} {unit} is equal to {new_value} {new_unit}")

                pause()
                break

            elif choice == "5":            # convert temperature units
                
                print("\nInitiating Temperature Converter..\n")
                value = get_value()

                temp_copy = temperature.copy()
                print("\nUnit of value:")
                unit = get_unit(temp_copy)

                temp_copy.remove(unit)
                print("\nConvert to:")
                new_unit = get_unit(temp_copy)

                if unit == "Celsius":

                    if new_unit == "Fahrenheit":        # celsius to fahrenheit
                        new_value = tp.degC_to_degF(value)

                    else:                               # celsius to kelvin
                        new_value = tp.degC_to_K(value)

                elif unit == "Fahrenheit":

                    m_val = tp.degF_to_degC(value)

                    if new_unit == "Celsius":           # fahrenheit to celsius
                        new_value = m_val

                    else:                               # fahreheit to kelvin
                        new_value = tp.degC_to_K(m_val)

                else:
                    
                    m_val = tp.K_to_degC(value)

                    if new_unit == "Celsius":           # kelvin to celsius
                        new_value = m_val
                    
                    else:                               # kelvin to fahrenheit
                        new_value = tp.degC_to_degF(m_val)

                print(f"\n{round(value, 2)} {unit} is equal to {round(new_value, 2)} {new_unit}")

                pause()
                break

            elif choice == "6":         # convert time units

                print("\nInitiating Time Converter..\n")    
                
                value = get_value()

                time_copy = time.copy()
                print("\nUnit of value:")
                unit = get_unit(time_copy)

                time_copy.remove(unit)
                print("\nConvert to:")
                new_unit = get_unit(time_copy)

                new_value = t.convert_time(value, unit, new_unit)
                
                print(f"\n{value} {unit} is equal to {new_value} {new_unit}")

                pause()
                break

            elif choice == "7":
                
                print("Exiting the application..")
                return

            else:
                print("Sorry! Please enter a valid choice.")


if __name__ == "__main__":
    main()

print("\nThanks for using our application!\n")