#Student Name:    Andrew Beaver
#Program Title:  Grade calculator
#Description: Tech Check 3 

# Grade Point Calculator

# Create a console-based program that will take a letter grade, such as B+ or C, and convert it to its 
# corresponding numeric value. It will use two prompts, one for the letter grade and a second for the
# modifier, if any (+ or -), and calculate, then output the proper number grade.

# •	Possible letter grades are A, B, C, D, and F
# •	Possible numeric values are 4, 3, 2, 1, and 0, respective to the letters listed above.
# •	Possible modifiers are a plus (+), a minus (–) or nothing. 
# •	There is no F+ or F–. 
# •	Using the + sign increases the numeric value by 0.3, using the – sign decreases it by 0.3. However, an A+ has 
#       still has a value of only 4.0. 
# •	A valid letter grade can be either uppercase or lowercase.
# •	If an invalid value is entered, display a warning message.


def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    #Establish letter grade value
    gradeA = 4
    gradeB = 3
    gradeC = 2
    gradeD = 1
    gradeF = 0

    #Establish modifier value
    modifierMinus = -0.3
    modifierPlus = 0.3
    modifierNil = 0

    #Display opening message
    print("Grade Point Calculator")

    #Display program rules to user
    print("\nValid letter grades that can enetered: A, B, C, D, F.")
    print("Valid grade modifiers are +, - or nothing.")
    print("All letter grades except F can inlcude a + or - symbol.")
    print("Calculated grade point value cannot exceed 4.0")

    #Prompt user for a letter grade
    userLetterGrade = input("\nEnter a letter grade: ").lower()


    #Prompt user for a modifier
    userModifier = input("Please enter a modifier (+, - or nothing): ")

    #Establish rules to assign the letter grade to it's grade value
    if userLetterGrade == "a":
        letterGradeValue = gradeA
    elif userLetterGrade == "b":
        letterGradeValue = gradeB
    elif userLetterGrade == "c":
        letterGradeValue = gradeC
    elif userLetterGrade == "d":
        letterGradeValue = gradeD
    elif userLetterGrade == "f":
        letterGradeValue = gradeF
    else:
        letterGradeValue = 0
        print("YOU HAVE ENTERED AN INVALID GRADE.") 

    #Establish rules to get the modifiers value
    if userModifier =="+":
        valueModifier = modifierPlus
    elif userModifier == "-":
        valueModifier = modifierMinus
    else:
        valueModifier = modifierNil


    #Create equation to get the users final grade.
    #Make rules to not allow modifier to affect grade A and F
    if letterGradeValue == gradeA and valueModifier == modifierPlus:
        usergrade = gradeA
    elif letterGradeValue == gradeF:
         usergrade = gradeF
    else:
        usergrade = letterGradeValue + valueModifier

    #Display final grade
    print("\nThe numeric value is: {0:.1f}".format(usergrade))

    # YOUR CODE ENDS HERE

main()
