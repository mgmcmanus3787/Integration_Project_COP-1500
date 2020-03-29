# Integration Project
# Matthew McManus

# Calculator Dev Info
print("""
      
Welcome To The Physics Test Simulator""")
print("Developed By Matthew McManus")


# Main Menu Options
def Main():
    print("""
        1. Velocity
        2. Specific Heat Capacity
        3. Voltage
        4. Amperage
        5. End Program
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
        print("Thanks For Using My Program")
    else:
        print("Invalid Selection Try Again")


# Functions
def velocity_calc():
    velo_calc_dist = float(input("What is the distance? "))
    velo_calc_time = float(input("What is the time? "))
    velo_calc_final = (velo_calc_dist / velo_calc_time)
    print("The Velocity Result is: ", "{:.2f}".format(velo_calc_final))
    input("\n Press Any Key To Continue")
    Main()

def spef_heat_calc():
    spef_heat_delta_te = float(input("What is the change in thermal energy "))
    spef_heat_mass = float(input("What is the mass? "))
    spef_heat_delta_temp = float(input("What is change in temp? "))
    spef_heat_calc_final = (spef_heat_delta_te / (spef_heat_mass * spef_heat_delta_temp))
    print("The Specific Heat Capacity Result is: ", "{:.2f}".format(spef_heat_calc_final))
    input("\n Press Any Key To Continue")
    Main()

def voltage_calc():
    voltage_amp = float(input("What is the amperage? "))
    voltage_res = float(input("What is the resistance? "))
    voltage_calc_final = (voltage_amp * voltage_res)
    print("The Voltage is: ", "{:.2f}".format(voltage_calc_final))
    input("\n Press Any Key To Continue")
    Main()

def amperage_calc():
    amperage_watts = float(input("What is the wattage? "))
    amperage_volts = float(input("What is the voltage? "))
    amperage_calc_final = (amperage_watts / amperage_volts)
    print("The Voltage is: ", "{:.2f}".format(amperage_calc_final))
    input("\n Press Any Key To Continue")
    Main()


Main()
