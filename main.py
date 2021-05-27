#1.input module

num1 = int(input("Enter a number "))
num2 = int(input("Enter a number "))
num3 = int(input("Enter a number "))

largest_number = max(num1, num2, num3)

print("The largest number is: ", largest_number)
print()

#2.tax calculation(dought)
Income = float(input("Enter your annual income"))
tax = 15000

tax = round(tax, 0)
print("The tax is: ", tax, "Thalars")
print()

#3.Leap year or common year

year = int(input("Enter a year: "))
	
if year % 4:
    print("It's a common year")
elif year <= 1580:
    print("Not within the Greorian calender")
else:
    print("It's a leap year")

print()

#4.True or False

x = 10

if x == 10:  # True
    print("x == 10")

if x > 15:  # False
    print("x > 15")

elif x > 10:  # False
    print("x > 10")

elif x > 5:  # True
    print("x > 5")

else:
    print("else will not be executed")
print()

#5.

x = int(input("Enter x value"))

if x > 5:  # True
    if x == 6:  # False
        print("nested: x == 6")
    elif x == 10:  # True
        print("nested: x == 10")
    else:
        print("nested: else")
else:
    print("else")
print()

#6.

x = 1
y = 1.0
z = "1"

if x == y:
  print("one")
if y == int(z):
  print("two")
elif x == y:
  print("three")
else:
  print("four")
print()

#7.while loop

while True:
  print("I'm stuck in a loop")
print()

#8.

#print smallest_number
# Store the current smaller number here.
smallest_number = -50000

# Input the first value.
number = int(input("Enter a number or #type -1 to stop: "))

# If the number is not equal to -1, continue.
while number != -1:
    # Is number smaller than smallest_number?
    if number < smallest_number:
        # Yes, update smallest_number.
        smallest_number = number
    # Input the next number.
    number = int(input("Enter a number or type -1 to stop: "))

# Print the smallest_number.
print("The smallest number is:", smallest_number)
print()

#9.print largest_number

# Store the current largest number here.
largest_number = -999999999

# Input the first value.
number = int(input("Enter a number or type -1 to stop: "))

# If the number is not equal to -1, continue.
while number != -1:
    # Is number larger than largest_number?
    if number > largest_number:
        # Yes, update largest_number.
        largest_number = number
    # Input the next number.
    number = int(input("Enter a number or type -1 to stop: "))

# Print the largest number.
print("The largest number is:", largest_number)
print()

#9.print secret number

secret_number_is = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

float(input("Enter any number : "))
print()


print("Your secret number is:", secret_number_is)
print()

#10.Looping code with for

for i in range(1, 5):
    print("The value of i is currently", i)

print()

#The third argument is an increment 

for i in range(1, 10, 2):
  print("The value of i is currently", i)

print()

#11. break - example

print("The break instruction:")
for i in range(1, 6):
    if i == 3:
        break
    print("Inside the loop.", i)
print("Outside the loop.")
print()

# continue - example

print("\nThe continue instruction:")
for i in range(1, 6):
    if i == 3:
        continue
    print("Inside the loop.", i)
print("Outside the loop.")
print()

#12.Let's have a look at a short program whose task is to write some of the first powers of two:

power = 1
for expo in range(16):
    print("2 to the power of", expo, "is", power)
    power *= 10
print()

#13.
import time

# Write a for loop that counts to five.
for Mississipi in range(1, 6):
    print("Mississipi")
    use: time.sleep(1)
    # Body of the loop - print the loop iteration number and the word "Mississippi".
     #Body of the loop - use: time.sleep(1)

# Write a print function with the final message.
print("Ready or not, here I come!")

print()


#14. enter password using while loop

while True:

    word = input("Please enter your password:")

    if word =="Deepu":

        print("You've successfully left the loop")
                   
        break

    else:
        print("Please enter a correct password ")
print()

#15.Example-1 for eating vowels
#Prompt the user to enter a word

word_without_vowels = ""

user_word = input("Enter a word : ")

# and assign it to the user_word variable.
user_word = user_word.upper()

for letter in user_word:
    if letter == "A":
      
      word = letter

      continue

    elif letter == "E":
      
      continue
    
    elif letter == "I":
      
      continue

    elif letter == "O":
      
      continue

    elif letter == "U":
      
      continue

    else:
      word_without_vowels += letter
      
      print(word_without_vowels)

     #Complete the body of the for loop.
print()

#16.Example-2:

word_without_vowels = ""

user_word = input("Enter a word : ")

user_word = user_word.upper()

vowels = 'AaEeIiOoUu'

for letter in user_word:

  if letter not in vowels:

    word_without_vowels += letter

print(word_without_vowels)

#17.multiplication table

number = int(input("Enter number"))

count =1

while count <=10:

  product = number * count

  print(number, "x", count, "=", product)
  
  count +=1

print()