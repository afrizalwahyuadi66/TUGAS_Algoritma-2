# Perpustakaan----------------
import os
from subprocess import call
import shutil
#-----------------------------


# Function to print colored text---------------
def print_color(text, color):
    if color == 'red':
        print("\033[91m" + text + "\033[00m")
    elif color == 'green':
        print("\033[92m" + text + "\033[00m")
    elif color == 'yellow':
        print("\033[93m" + text + "\033[00m")
    elif color == 'blue':
        print("\033[94m" + text + "\033[00m")
    else:
        print(text)
#---------------------------------------------


# Define the logo-----------------------------------------------------------------------
logo = (
    "\033[34m  ██╗░░░██╗████████╗░██████╗░░░░░░░█████╗░███╗░░██╗░██████╗███████╗ \n" 
    "\033[34m  ██║░░░██║╚══██╔══╝██╔════╝░░░░░░██╔══██╗████╗░██║██╔════╝╚════██║ \n"
    "\033[34m  ██║░░░██║░░░██║░░░╚█████╗░█████╗███████║██╔██╗██║╚█████╗░░░░░██╔╝ \n"
    "\033[34m  ██║░░░██║░░░██║░░░░╚═══██╗╚════╝██╔══██║██║╚████║░╚═══██╗░░░██╔╝░ \n"
    "\033[34m  ██║░░░██║░░░██║░░░░╚═══██╗╚════╝██╔══██║██║╚████║░╚═══██╗░░░██╔╝░ \n" 
    "\033[34m  ╚██████╔╝░░░██║░░░██████╔╝░░░░░░██║░░██║██║░╚███║██████╔╝░░██╔╝░░ \n"
    "\033[34m  ░╚═════╝░░░░╚═╝░░░╚═════╝░░░░░░░╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░░░╚═╝░░░ \n\n"
    "\033		    	Tugas UTS Algoritma 2\n\n"
                                                                                                                                                                     
    "\033	[91m 1. Afrizal Wahyu Adi Putra\t 11230070\n"
    "\033  	 2. Nadia Zahira Sofa\t\t 11230056 \n"
    "\033          3. Syifa Susila Pratama\t 11230068 \n"
    "\033[0m"
)
#---------------------------------------------------------------------------------------


# Clear screen------------------------------------
os.system('cls' if os.name == 'nt' else 'clear')
#-------------------------------------------------


# Print the logo---------
print(logo)
#------------------------



# Input from a directory program-----------
def program1():
    call(["python", "program1.py"])

def program2():
    call(["python", "program2.py"])

def program3():
    call(["python", "program3.py"])

def program4():
    call(["python", "program4.py"])

def program5():
    call(["python", "program5.py"])

def program6():
    call(["python", "program6.py"])

def program7():
    call(["python", "program7.py"])

def program8():
    call(["python", "program8.py"])

def program9():
    call(["python", "program9.py"])    

def program10():
    call(["python", "program10.py"])
#---------------------------------------


# Genarate Tabel-------------------------------------------------------------------------------------------
def display_programs_table():
    print("-" * 57)
    print("|\t\tPILIH SALAH SATU PROGRAM\t\t|")
    print("-" * 57)
    for i, (name, program) in enumerate(programs.items(), 1):
        print(f"|  {i}.\t{name.ljust(10,' ')}\t\t\t\t\t|")
    print("-" * 57)
    
    
# Print word-------------------
programs = {
    "Program 1": program1,
    "Program 2": program2,
    "Program 3": program3,
    "Program 4": program4,
    "Program 5": program5,
    "Program 6": program6,
    "Program 7": program7,
    "Program 8": program8,
    "Program 9": program9,
    "Program 10": program10,
}
#------------------------------



def main():
    display_programs_table()
    while True:
        try:
            choice = int(input("\nEnter the number of the program to run: "))
            if 1 <= choice <= len(programs):
                programs[list(programs.keys())[choice-1]]()
                return
                
            print("Invalid choice, please enter a number between 1 and {}".format(len(programs)))
        except ValueError:
            print("Invalid input, please enter a number between 1 and {}".format(len(programs)))

if __name__ == "__main__":
    main()
#--------------------------------------------------------------------------------------------------------
