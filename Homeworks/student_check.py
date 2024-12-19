# ## Name: Kevin Zhang
# ## ID: 2661252
# """
# This code was my own work, it was written without consulting any sources
# outside of those approved by the instructor. 
# Initial: KZ
# """

# Question 1
# Write a function named filter_odd_numbers that takes a list of integers as input and returns a 
# new list that contains only the odd numbers from the original list. 
# Prompt the user to input a list of integers (comma-separated) and use the filter_odd_numbers 
# function to display the odd numbers in the list. 


print ("Question 1")
def filter_odd_numbers(numbers):
    return list(filter(lambda x:x%2!=0, numbers))
x = input("Enter a list of integers that are seperated with commas: ")
original = list(int(num)for num in x.split(','))
odd = filter_odd_numbers(original)
print("The original list is", x)
if not odd:
    print("There are no odd numbers in the list")
else:
    print("The list with only odd numbers is", odd)

# Question 2: Weekday List Challenge
# Create a list that represents the days of the week, with each day of the week as a string.
# Perform the following tasks
# 1. Create the list: Initialize a list that contains the days of the week (from "Monday" to
# "Sunday").
# 2. Access Days: Print the third day in the list (hint: use index 2).
# 3. Change a Day: Change the last day in the list to "FunDay". Print the updated list.
# 4. Add New Day: Add "Holiday" to the end of the list and print the updated list.
# 5. Remove a Day: Remove "Wednesday" from the list and print the updated list

print("Question 2")
days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
days_string = ",".join(days)
print(days)
print("The third day in the list is", days[2])
days[6]='FunDay'
print("The new list is: ",days)
days.append('Holiday')
print("The new list is: ", days)
days.remove('Wednesday')
print("The new list is", days)


#  Question 3: Create a Simple Bank Account Class 
# Write a class BankAccount that represents a simple bank account. The class should have the 
# following: 
# 1. Attributes: 
# a. account_holder: The name of the account holder (string). 
# b. balance: The current balance of the account (float). 
# 2. Methods: 
# a. deposit(amount): Adds the given amount to the balance. 
# b. withdraw(amount): Subtracts the given amount from the balance (if there are 
# enough funds). 
# c. get_balance(): Returns the current balance. 
# Tasks: 
# 1. Create a BankAccount for a person named "Alice" with an initial balance of 1000. 
# 2. Call the deposit() method on the Alice object to add 500 to her balance. 
# 3. Use the withdraw() method to subtract 200 from Alice's account. 
# 4. Use the get_balance() method to print Alice's final balance. 

print("Question 3")

class Bankaccount():
    def __init__(self,account_holder,balance):
        self.account_holder = account_holder
        self.balance = float(balance)
    def deposit(self,amount):
        if amount <=0:
            print("Please input a value greater than 0")
        else:
            self.balance += amount
            return self.balance


    def withdraw(self,amount):
        if self.balance<0:
            print("Insufficient funds")
        else:
            self.balance -= amount
            return self.balance

    def get_balance(self):
        if self.balance<0:
            print("There is no more money left in the bank account")
        else:
            return self.balance
    
    def __str__(self):
        return self.account_holder + " " + str(self.balance)


account = Bankaccount("Alice", 1000)
account.deposit(500)
account.withdraw(200)
account.get_balance()
print(account)


#  Question 4: Movie Class 
# Create a class called Movie that represents a movie. The class should have the following 
# attributes and methods: 
# Attributes: 
# • title: The title of the movie (string). 
# • director: The name of the director (string). 
# • year: The year the movie was released (integer). 
# • rating: The rating of the movie (float, between 1 and 10). 
# Methods: 
# • get_info(): Returns a string with the movie’s title, director, year, and rating. 
# • update_rating(new_rating): Updates the rating of the movie. 
# Tasks: 
# 1. Create a movie object with the title "Inception", directed by "Christopher Nolan", 
# released in 2010, with a rating of 8.8. 
# 2. Use the get_info() method to print out the details of the movie. 
# 3. Use the update_rating() method to change the movie's rating to 9.2. 
# 4. Print the updated details using get_info() again. 

print("Question 4")
class Movie():
    def __init__(self,title,director,year,rating):
        self.title = title
        self.director = director
        self.year = int(year)
        self.rating = float(rating)
    def get_info(self):
        return {"Title":self.title,"Director":self.director,"Year":self.year,"Rating":self.rating}
    def update_rating(self,new_rating):
        self.rating = new_rating
        return self.rating


movie = Movie("Inception","Christopher Nolan", 2010, 8.8)
print(movie.get_info())
movie.update_rating(9.2)
print(movie.get_info())
   



# Question 5: The School Yearbook 
# Imagine you're working on a digital yearbook for a school. You have a table (a list of lists) that 
# contains student information such as their name, grade, and favorite subject. Your task is to 
# organize this data and perform a few operations on it. 
# Here is the students table, which contains the following information: 
# students = [ 
# ["Alice", 10, "Math"],   # Name, Grade, Favorite Subject 
# ["Bob", 11, "History"], 
# ["Charlie", 10, "Science"], 
# ["Daisy", 12, "Math"], 
# ["Eve", 11, "Art"] 
# ] 
# Tasks: 
# 1. What is the grade of Charlie? 
# • Write a function find_grade(students, name) that takes the list of students and a 
# student's name as input and returns the grade of that student. For example: 
# find_grade(students, "Charlie")  # Expected Output: 10 
# 2. Write a function find_favorite_subject(students, subject) that takes the list of 
# students and a subject as input and prints the names of students whose favorite 
# subject matches the input. If multiple students have the same favorite subject, print 
# all their names. For example: 
# find_favorite_subject(students, "Art")  # Expected Output: Eve 
# 3. Write a function average_grade(students) that calculates and returns the average 
# grade of all the students in the list.
print("Question 5")
students = [ ["Alice", 10, "Math"],  ["Bob", 11, "History"], ["Charlie", 10, "Science"], ["Daisy", 12, "Math"], ["Eve", 11, "Art"]]

def find_grade(students, name):
    for student in students:
        if student[0] == name:
            return student[1]
        else:
            None
        
def find_favorite_subject(students,subject):
    people = []
    for student in students:
        if student[2] == subject:
            people.append(student[0])
    return people
        

def average_grade(students):
    total = sum(student[1] for student in students)
    number = len(students)
    return total/number

Charlie = find_grade(students, "Charlie")
print (Charlie)
art = find_favorite_subject(students,"Art")
print(art)
grade = average_grade(students)
print(grade)

