"""Physics Calculator"""
__author__ = "Matthew McManus"

version_num = "1.0.4"

"""Calculator Dev Info"""
print("""
      
Welcome To The Physics Test Simulator""")
print("Developed By Matthew McManus")
print("Version Number:", version_num)


# Main Menu Options
def Main():
    print("""
        1. Velocity
        2. Specific Heat Capacity
        3. Voltage
        4. Amperage
        5. Help / Info
        6. End Program
        """)

    # Main Menu Title
    ans = input("What Calculation Would You Like To Perform? ")
    if ans == "1":
        velocity_calc()
    elif ans == "2":
        spef_heat_calc()
    elif ans == "3":
        voltage_calc()
    elif ans == "4":
        amperage_calc()
    elif ans == "5":
        calc_help()
    elif ans == "6":
        print("Thanks For Using My Program")
    else:
        print("Invalid Selection Try Again")


# Functions


def velocity_calc():
    """Calculates the input given for Velocity"""
    print("\n -- Velocity Calculator --")
    got_good_input = False
    while got_good_input == False:
        try:
            velo_calc_dist = float(input("\n What is the distance? "))
            got_good_input = True
        except ValueError:
            print("Input is not a valid number")
    got_good_input = False
    while got_good_input == False:
        try:
            velo_calc_time = float(input("What is the time? "))
            if velo_calc_time != 0:
                got_good_input = True
            else:
                print("Input must be a number not equal to zero")
        except ValueError:
            print("Input must be a number not equal to zero")
    print("The Velocity Result is: ",
          "{:.2f}".format(calculate_velocity(velo_calc_dist, velo_calc_time)))
    input("\n Press Any Key To Return To Menu")
    Main()


def calculate_velocity(dist, time):
    return dist / time


def spef_heat_calc():
    """Calculates the input given for Specific Heat"""
    print("\n -- Specific Heat Calculator --")
    got_good_input = False
    while got_good_input == False:
        try:
            spef_heat_delta_te = float(
                input("\n What is the change in thermal energy "))
            got_good_input = True
        except ValueError:
            print("Input is not a valid number")
    got_good_input = False
    while got_good_input == False:
        try:
            spef_heat_mass = float(input("What is the mass? "))
            got_good_input = True
        except ValueError:
            print("Input is not a valid number")
    got_good_input = False
    while got_good_input == False:
        try:
            spef_heat_delta_temp = float(input("What is change in temp? "))
            got_good_input = True
        except ValueError:
            print("Input is not a valid number")
    spef_heat_calc_final = (
            spef_heat_delta_te / (spef_heat_mass * spef_heat_delta_temp))
    print("The Specific Heat Capacity Result is: ",
          "{:.2f}".format(spef_heat_calc_final))
    input("\n Press Any Key To Return To Menu")
    Main()


def voltage_calc():
    """Calculates the input given for Voltage"""
    print("\n -- Voltage Calculator --")
    got_good_input = False
    while got_good_input == False:
        try:
            voltage_amp = float(input("\n What is the amperage? "))
            got_good_input = True
        except ValueError:
            print("Input is not a valid number")
    got_good_input = False
    while got_good_input == False:
        try:
            voltage_res = float(input("What is the resistance? "))
            got_good_input = True
        except ValueError:
            print("Input is not a valid number")
    voltage_calc_final = (voltage_amp * voltage_res)
    print("The Voltage is: ", "{:.2f}".format(voltage_calc_final))
    input("\n Press Any Key To Return To Menu")
    Main()


def amperage_calc():
    """Calculates the input given for Amperage"""
    print("\n -- Amperage Calculator --")
    got_good_input = False
    while got_good_input == False:
        try:
            amperage_watts = float(input("\n What is the wattage? "))
            got_good_input = True
        except ValueError:
            print("Input is not a valid number")
    got_good_input = False
    while got_good_input == False:
        try:
            amperage_volts = float(input("What is the voltage? "))
            got_good_input = True
        except ValueError:
            print("Input is not a valid number")
    amperage_calc_final = (amperage_watts / amperage_volts)
    print("The Amperage is: ", "{:.2f}".format(amperage_calc_final))
    input("\n Press Any Key To Return To Menu")
    Main()


def calc_help():
    """Help / Info for the calculator"""
    print("""
    -- Help / Info --
    
    Welcome to the General Physics calculator! Thank you for choosing our 
    product to help aid in your physics calculations! You can use the main menu
    for your calculation selection. If you experience any issues you can 
    contact our support at (xxx)-xxx-xxxx or via email xxx@xxx.com.
    """)
    print("Version Number", version_num)
    input("\n Press Any Key To Return To Menu")
    Main()


Main()
