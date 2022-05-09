# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
result = name1.count('t') + name2.count('t') 

result1 = name1.count('r') + name2.count('r') 

result2 = name1.count('u') + name2.count('u') 

result3 = name1.count('e') + name2.count('e') 

total = result + result1 + result2 + result3

no = name1.count('l') + name2.count('l') 

no1 = name1.count('o') + name2.count('o') 

no2 = name1.count('v') + name2.count('v') 

no3 = name1.count('e') + name2.count('e')

numero_final = no + no1 + no2 + no3

love_score = total * 10 + numero_final

if love_score < 10 or love_score > 90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")

elif love_score > 40 and love_score < 50:
  print(f'Your score is {love_score}, you are alright together.')
else:
  print(f"Your score is {love_score}.")




