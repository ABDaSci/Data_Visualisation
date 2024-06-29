# This program reads from the file DOB.txt & re-formats the information in 2 seperate sections.
# The sections are headed: Name, & Birthdate, in bold text.
# A for loop is used to read each line, split it into separate words, & then rejoin the 1st 2 words to form a name.
# Another for loop is then used to split, & rejoin the last 3 words to form a birthdate.
print("\n\033[1m Name  \033[0m")          # prints Name in bold text, with a new line before & after for readability

with open('DOB.txt', 'r') as file:       # opens the file DOB.txt to read it, & closes it after the for loop is completed
    for line in file:                     # loops through the file line by line
        split_line = line.split()         # splits the line into a list of items & passes the list to a variable called split_line
        joined_name = " ".join(split_line[0:2])   # joins the 1st 2 items in the list to form the full name
        print(joined_name)                # prints the full name

print("\n\033[1m Birthdate  \033[0m")     # prints Birthdate in bold text on a new line

with open('DOB.txt', 'r') as file:       # following block of code does the same as the above, for the last 3 items in the list
    for line in file:
        split_line = line.split()
        joined_date = " ".join(split_line[2:])   # these 3 items are joined to form the birthdate
        print(joined_date)
print("")     






       
