'''
*Retrieved: https://gist.github.com/mauricioaniche/671fb553a81df9e6b29434b7e6e53491
*Tutorial: https://www.youtube.com/watch?v=tBAj2FqgIwg
*Used for pytest inputs and outputs
'''
import builtins
import os

input_values = []
print_values = []


def mock_input(s):
    print_values.append(s)
    return input_values.pop(0)


def mock_input_output_start():
    global input_values, print_values

    input_values = []
    print_values = []

    builtins.input = mock_input
    builtins.print = lambda s: print_values.append(s)


def get_display_output():
    global print_values
    return print_values


def set_keyboard_input(mocked_inputs):
    global input_values

    mock_input_output_start()
    input_values = mocked_inputs


def clearFile(fileName):
    os.remove(fileName)
    f = open(fileName, "x")
    f.close()


def writeToFile(fileName, lineToWrite):
    with open(fileName, "w") as file:
        file.write(lineToWrite)


def appendToFile(fileName, lineToAppend):
    with open(fileName, "a") as file:
        file.write(lineToAppend)