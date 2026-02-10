import LessonClass as l #import module with lesson class

class Skater: #Skater class used as parent class for both Student and Coach

    def __init__(self, name, level): #initializes with name and level
        self.name = name
        self.level = level

    def getLevel(self): #returns level
        return self.level

class Student(Skater): #Student class subclass of Skater

    def __init__(self, name, level, age): #initializes with name, level and age
        super().__init__(name, level) #taking from super class Skater
        self.age = age

    def printProfile(self): #prints all profile information
        print(f"Name: {self.name} \nAge: {self.age} \nLevel: {self.level}")

class Coach(Skater): #Coach class subclass of Skater

    def __init__(self, name, level, rate):
        super().__init__(name, level)
        self.rate = rate

    def printInfo(self): #prints all coach information
        print(f"~~~PROFILE~~~\nName: {self.name} \nRate: ${self.rate}.00 per 30 minutes \nTeaches {self.level} students") #formats string info

    def getRate(self): #returns coaching rate
        return self.rate

    def getName(self): #returns coach name
        return self.name


def checkName(name): #checks user input name validity
    for char in name:
        if char.isalpha() or char.isspace(): #makes sure that name is all alphabetical besides spaces
            return True
        else:
            return False

def checkAge(age): # checks user input age validity
    if age.isdigit(): #makes sure that age is only digits
        if (int)(age) < 1 or (int)(age) > 110: #makes sure that age is between 1 and 110
            return False
        else:
            return True
    else:
        return False

def checkLevel(level): #checks user input level validity
    if level.isdigit(): #makes sure that user inputs a digit
        if (int)(level) < 1 or (int)(level) > 3: # makes sure that user input is 1, 2, or 3 which are the given options
            return False
        else:
            return True
    else:
        return False

# creating 6 Coach objects  

sam = Coach("Sam Pastrano", "Beginner", 35)
ayleen = Coach("Ayleen Gamez", "Beginner", 30)
victoria = Coach("Victoria Gorman", "Intermediate", 40)
alex = Coach("Alex Trieu", "Intermediate", 45)
alysa = Coach("Alysa Liu", "Advanced", 60)
amber = Coach("Amber Glenn", "Advanced", 65)

coaches = [sam, ayleen, victoria, alex, alysa, amber] #list for coaches

print("Welcome to ICETOWN! Please create your profile before booking a figure skating lesson.\n") #introduces profile creation
while True: #while loop to check name validity
    name = input("Enter your name: ")
    if checkName(name) == True:
        break
    else:
        print("Please enter a valid name.")
while True: #while loop to check age validity
    age = input("Enter your age: ")
    if checkAge(age) == True:
        break
    else:
        print("Please enter a valid age.")
while True: #while loop to check level validity 
    level = input("Please select the student's skill level:\n1. Beginner\n2. Intermediate\n3. Advanced\n")
    if checkLevel(level) == True:
        break
    else:
        print("Please choose a valid option.")

# assigns full title to whichever option chosen
if level == "1":
    level = "Beginner"
elif level == "2":
    level = "Intermediate"
elif level == "3":
    level = "Advanced"
    
s = Student(name, level, age) #creates Student object using the user input

print("\nThank you for completing your profile!\n")
s.printProfile() #prints user profile to user

print("\nCoaches Available:\n")

n = 1
for i in coaches:
    if s.getLevel() == i.getLevel(): #prints coaches based on user level, making sure that it matches
        print(n, "-")
        i.printInfo()
        n = n + 1
        print("\n")

while True: # while loop to choose coach
    coach_selection = input("Please enter the FIRST name of the coach you would like to book with: ") #prompting user input 
    coach_selection = coach_selection.lower() # makes user input all lowercase to function in next if statement
    if coach_selection == "sam": #if statement to assign coach based on user input
        coach_selection = sam
        break
    elif coach_selection == "ayleen":
        coach_selection = ayleen
        break
    elif coach_selection == "victoria":
        coach_selection = victoria
        break
    elif coach_selection == "alex":
        coach_selection = alex
        break
    elif coach_selection == "alysa":
        coach_selection = alysa
        break
    elif coach_selection == "amber":
        coach_selection = amber
        break
    else:
        print("Please enter a valid name.\n")

print("\nPlease select a date for your lesson (Lessons booking through February 2027!):")
month = (int)(input("\nMonth: "))
if month > 0 and month < 13: # makes sure month is valid
    print("")
else:
    raise Exception("Invalid Number") # raises Exception if month is invalid
day = (int)(input("Day: "))
if month % 2 == 1 and day > 30: # makes sure 31 can not be chosen for months with 30 days
    raise Exception("Invalid Number")
elif month == 2 and day > 28: # makes sure that number >28 cannot be chosen for February
    raise Exception("Invalid Number")
elif day < 1 or day > 31: # makes sure day is valid
    raise Exception("Invalid Number")
else:
    print("")
year = (int)(input("Year: "))
if year > 2027: # cannot exceed 2027
    raise Exception("Invalid Number")
elif month > 2 and year > 2026: # cannot exceed past February 2026
    raise Exception("Invalid Number")
elif year < 2026: # cannot be before current year
    raise Exception("Invalid Number")
else:
    print("")

print("Please select a time slot for your lesson:\n1. 10am\n2. 11am\n3. 12pm\n4. 1pm\n5. 2pm\n6. 3pm\n7. 4pm") # displays time options
time = (int)(input("\n"))
if time == 1: # assigns time based on user input
    time = "10am"
elif time == 2:
    time = "11am"
elif time == 3:
    time = "12pm"
elif time == 4:
    time = "1pm"
elif time == 5:
    time = "2pm"
elif time == 6:
    time = "3pm"
elif time == 7:
    time = "4pm"

length = (int)(input("How long would you like your lesson to be?\n1. 30 minutes\n2. 1 hour\n")) # gives length options

lesson = l.Lesson(coach_selection, month, day, year, time, length) # creates lesson object and calls back to LessonClass module

print("\n")
lesson.createReminder() # creates reminder in text file


        


    
