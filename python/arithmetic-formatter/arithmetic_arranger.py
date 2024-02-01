import re

# Add a 'solver' parameter which has default value 'False', allows user to decide whether to display solutions or not
def arithmetic_arranger(problems, solver = False):

    # Check thqt numbers of problems is less than 5
    if (len(problems) > 5):
        return "Error: Too many problems."

    first = ""
    second = ""
    sumLine = ""
    sumx = ""

    # Run through each problem of the list of problems  
    for problem in problems:
        # Search for values that aren`t a space
        if (re.search("[^\s0-9.+-]", problem)):
            # Search to make sure the problem is a sum only
            if (re.search("[/]", problem) or re.search("[*]", problem)):
                return "Error: Operator must be '+' or '-'."
            return "Error: Numbers must only contain digits."
        # First number in the problem will be the one before the first space
        firstNumber = problem.split(" ")[0]
        # Operator will be the one after the first space
        operator = problem.split(" ")[1]
        # Second number in the problem will be the one after the second space
        secondNumber = problem.split(" ")[2]

        # Check that numbers don't have more than four digits
        if (len(firstNumber) > 4 or len(secondNumber) > 4):
            return "Error: Numbers cannot be more than four digits."

        sum = ""
        # Set operating rules based on the operator in the problem
        if (operator == "+"):
            sum = str(int(firstNumber) + int(secondNumber))
        elif (operator == "-"):
            sum = str(int(firstNumber) - int(secondNumber))

        # Set the indent length to be the length of the longest number
        length = max(len(firstNumber), len(secondNumber)) + 2
        # Align the top number to the length of the longest number
        top = str(firstNumber).rjust(length)
        # Align the bottom number to the length of the longest number
        bot = operator + str(secondNumber).rjust(length - 1)
        # Align the result to the length of the longest number
        result = str(sum).rjust(length)
      
        # Create a line of '-' to separate the bottom number and the result of the sum
        line= ""
        for i in range(length):
            line += "-"
        # Add spaces between each line and the next problem
        if problem != problems[-1]:
            first += top + "    "
            second += bot + "    "
            sumLine += line + "    "
            sumx += result + "    "
        # Last problem does not need spaces
        else:
            first += top
            second += bot
            sumLine += line
            sumx += result
    # Format the problem based on the value of the 'solver' parameter
    if solver:
        arranged_problems = first + "\n" + second + "\n" + sumLine + "\n" + sumx
    else:
        arranged_problems = first + "\n" + second + "\n" + sumLine
    return arranged_problems

