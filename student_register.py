# This program produces a register for examination candidates to sign.
# The user enters the number of students to be registered, & then the identification number for each student.
# A for loop is used to print to an external text file (reg_form.txt), that produces the register for the examination.
# The register file is formated so that the students can sign it beside their identification number.

num_on_register = int(input("\nHow many students are you registering?: "))  # user inputs the number of students to be registered; this is cast into an integer

with open('reg_form.txt', 'a') as file:                                     # uses implicit method to append a file & automatically close it at the end of the program
        file.write("       EXAMINATION CANDIDATE REGISTER      \n")                        # writes headers for the register sheet, & formats with empty lines
        file.write("\nStudent Identification Numbers & Signatures:\n ")

        for line in range((num_on_register)):                               # uses a for loop to add the identification number as a line to the register
                id_number = input("Enter new student Identification Number: ")          # asks the user for the id number
                file.write('\n')                                            # prints an empty line for more space to be writte signature clearly
# adds the line to the register by concatenating the id number and signature's dotted line
                file.write(id_number + "   " + '...................................\n')  
                file.write('\n')                                            # prints space for ease of writing signature
        
                 
                 
                 
                 
              
       
