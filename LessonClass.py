f = open('reminder.txt', 'w') # opens text file

class Lesson(): # lesson class

    def __init__(self, coach, month, day, year, time, length): # initializes
        self.coach = coach
        self.month = month
        self.day = day
        self.year = year
        self.time = time
        self.length = length

    def createReminder(self): # writes reminder to text file
        price = self.coach.getRate() * self.length
        f.write(f"~~~REMINDER~~~\nDate: {self.month}/{self.day}/{self.year}\nTime: {self.time}\nCoach: {self.coach.getName()}\nPrice: ${price}.00")
        print("Your reminder has been saved in reminder.txt!")
        f.close() # closes file

        
