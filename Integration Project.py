# Integration Project
#Ver. 1.0.4
version_num = "1.0.4"
# Matthew McManus

# Calculator Dev Info
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

#Calculates the input given for Velocity
def velocity_calc():
    print("\n -- Velocity Calculator --")
    velo_calc_dist = float(input("\n What is the distance? "))
    velo_calc_time = float(input("What is the time? "))
    velo_calc_final = (velo_calc_dist / velo_calc_time)
    print("The Velocity Result is: ", "{:.2f}".format(velo_calc_final))
    input("\n Press Any Key To Return To Menu")
    Main()

#Calculates the input given for Specific Heat
def spef_heat_calc():
    print("\n -- Specific Heat Calculator --")
    spef_heat_delta_te = float(input("\n What is the change in thermal energy "))
    spef_heat_mass = float(input("What is the mass? "))
    spef_heat_delta_temp = float(input("What is change in temp? "))
    spef_heat_calc_final = (spef_heat_delta_te / (spef_heat_mass * spef_heat_delta_temp))
    print("The Specific Heat Capacity Result is: ", "{:.2f}".format(spef_heat_calc_final))
    input("\n Press Any Key To Return To Menu")
    Main()

#Calculates the input given for Voltage
def voltage_calc():
    print("\n -- Voltage Calculator --")
    voltage_amp = float(input("\n What is the amperage? "))
    voltage_res = float(input("What is the resistance? "))
    voltage_calc_final = (voltage_amp * voltage_res)
    print("The Voltage is: ", "{:.2f}".format(voltage_calc_final))
    input("\n Press Any Key To Return To Menu")
    Main()

#Calculates the input given for Amperage
def amperage_calc():
    print("\n -- Amperage Calculator --")
    amperage_watts = float(input("\n What is the wattage? "))
    amperage_volts = float(input("What is the voltage? "))
    amperage_calc_final = (amperage_watts / amperage_volts)
    print("The Amperage is: ", "{:.2f}".format(amperage_calc_final))
    input("\n Press Any Key To Return To Menu")
    Main()

#Help / Info for the calculator
def calc_help():
    print("""
    -- Help / Info --
    
    Welcome to the General Physics calculator! Thank you for choosing our product to help aid in
    your physics calculations! You can use the main menu for your calculation selection. If you 
    experience any issues you can contact our support at (xxx)-xxx-xxxx or via email xxx@xxx.com.
    """)
    print("Version Number", version_num)
    input("\n Press Any Key To Return To Menu")
    Main()

Main()
