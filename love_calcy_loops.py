
"""
write a program that tests the compatibility between two people based on below conditions
Take both people's names and check for the number of times the letters in the word TRUE occurs.
Then check for the number of times the letters in the word LOVE occurs.
Then combine these numbers to make a 2 digit number.
For Love Scores less than 10 or greater than 90, the message should be:

"Your score is *x*, you go together like coke and mentos."
For Love Scores between 40 and 50, the message should be:

"Your score is *y*, you are alright together."
Otherwise, the message will just be their score. e.g.:

"Your score is *z*."
"""

#Program is as below #

print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ")  
name2 = input("What is their name? ") 


# First concatenate two names
name = name1 + name2
print(name.lower())

# Check how many times T R U E is occurred in the name
letter_true = ["t", "r", "u", "e"]
letter_love = ["l", "o", "v", "e"]

#calculation for T R U E
total_true = 0
for letter in letter_true:
    count = name.count(letter)
    total_true += count
    print(f"Count of {letter} = {count} times")
print(f"Total for TRUE = {total_true}")

#calculation for L O V E
total_love = 0
for letter in letter_love:
    count = name.count(letter)
    total_love += count
    print(f"Count of {letter} = {count} times")
print(f"Total for LOVE = {total_love}")

# Calculate Love_Score as the concatenation of total_true and total_love
Love_Score = str(total_true) + str(total_love)
love_score_int = int(Love_Score)

print(f"Love_Score = {love_score_int}")

#Print love scores and their predictions
if love_score_int < 10 or love_score_int > 90:
    print(f"Your score is {love_score_int}, you go together like coke and mentos.")
elif 40 <= love_score_int <= 50:
    print(f"Your score is {love_score_int}, you are alright together.")
else:
    print(f"Your score is {love_score_int}")
