import os
import subprocess
import winreg

def list_startup_programs():
    startup_programs = []
    registry_locations = [
        r"Software\Microsoft\Windows\CurrentVersion\Run",
        r"Software\Microsoft\Windows\CurrentVersion\RunOnce"
    ]

    for location in registry_locations:
        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, location) as key:
                count = winreg.QueryInfoKey(key)[1]
                for i in range(count):
                    name, value, _ = winreg.EnumValue(key, i)
                    startup_programs.append((name, value))
        except WindowsError as e:
            print(f"Error accessing registry: {e}")

    return startup_programs

def disable_startup_program(name):
    registry_locations = [
        r"Software\Microsoft\Windows\CurrentVersion\Run",
        r"Software\Microsoft\Windows\CurrentVersion\RunOnce"
    ]

    for location in registry_locations:
        try:
            with winreg.OpenKey(winreg.HKEY_CURRENT_USER, location, 0, winreg.KEY_SET_VALUE) as key:
                winreg.DeleteValue(key, name)
                print(f"Disabled startup program: {name}")
                return True
        except WindowsError as e:
            print(f"Error disabling program {name}: {e}")
            continue

    return False

def main():
    print("StartSwift - Manage Your Windows Startup Programs")
    print("1. List all startup programs")
    print("2. Disable a startup program")
    print("3. Exit")
    
    while True:
        choice = input("Choose an option (1-3): ")
        if choice == '1':
            programs = list_startup_programs()
            if programs:
                print("Startup Programs:")
                for name, path in programs:
                    print(f"- {name}: {path}")
            else:
                print("No startup programs found.")
        elif choice == '2':
            program_name = input("Enter the name of the program to disable: ")
            if disable_startup_program(program_name):
                print(f"Successfully disabled {program_name}.")
            else:
                print(f"Failed to disable {program_name}.")
        elif choice == '3':
            print("Exiting StartSwift.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()