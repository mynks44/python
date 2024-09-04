# Initialize an empty dictionary to store courses
courses = {}

# Add some courses to the dictionary
courses['MATH1284'] = 'Maths'
courses['PROG12583'] = 'Python'
courses['SYST10049'] = 'Web development '

# Prompt the user to enter a course code
code = input("Enter a course code to delete: ")

# Check if the course code is in the dictionary
if code in courses:
    # Delete the course from the dictionary
    del courses[code]
    print("The course is deleted.")
else:
    print("There is no course for this code.")