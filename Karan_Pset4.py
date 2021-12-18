from pathlib import Path
import os
from subprocess import run
import subprocess

##########################################################################################
############################## Testing for functions #####################################
##########################################################################################
####                                                                                    ##
##########################################################################################
############################## Testing check_output() ####################################
##########################################################################################
# When both files are equal, expected = True,                                       works.
# When both files are un-equal, expected = False,                                   works.
# When one of the files doesn't exist, expected = False,                            works.
# When both files don't exist, expected = True,                                     works.
# What happens when both files are the same? Should return true,                    works.
##########################################################################################
##########################################################################################
##########################################################################################
############################## Testing generate_output() #################################
##########################################################################################
# When input file exists and program runs fine, output file should have output
# When input file doesn't exist, but program runs fine, empty output file
# When input file doesn't exist, and program errors out, empty output file
# When input file exists, but program errors out, empty output file
##########################################################################################
##########################################################################################

def check_output(e_file, a_file):
    """
    This function takes in paths (strings) to two files and outputs True if contents of file match and False if they don't match
    """
    
    # Path object makes it cross-compatible with different OS's
    e_file = Path(e_file)
    a_file = Path(a_file)

    # Checking whether files exist, and then comparing contents of file
    if e_file.is_file() and a_file.is_file():
        if open(e_file, 'r').read() == open(a_file, 'r').read():
            return True
        else:
            return False

    # If one of the files (but not both) don't exist, return False. If both of them don't exist, return True
    elif ( e_file.is_file() and ( not a_file.is_file() ) ) or ( a_file.is_file() and ( not e_file.is_file() ) ):
        return False
    else:
        return True

def generate_output(program_path, input_path):
    """
    Takes a program path, input path, runs program based on input and returns output of program in a new file 'actual_output_file.txt'.
    """

    input_path = Path(input_path)

    result = run(['python', program_path, "<", input_path],shell=True ,capture_output=True, text=True)

    output = result.stdout[0:-1]        # [0:-1] is to get rid of the \n at the end
    error = result.stderr[0:-1]         # same here

    with open('actual_output_file.txt', 'w') as output_file:
        # len(error) == 0 means no error
        if len(error) == 0 and input_path.is_file():
            output_file.write(output)

def check(program_path, input_path, expected_output_file):
    
    # Generates output in actual_output_file.txt
    generate_output(program_path, input_path)
    return check_output(expected_output_file ,'actual_output_file.txt')

# print(check("check.py", "input.txt", "e.txt"))
