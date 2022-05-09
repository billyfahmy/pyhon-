#If the bill was $150.00, split between 5 people, with 12% tip. 
print("hey you reached to our restaurant final step which you hate and we love :* \n")
#Each person should pay (150.00 / 5) * 1.12 = 33.6

#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
bill = float(input("What was the total bill? $ " ) ) 
percent = int(input("How much tip would you like to give? 10, 12, or 15? " ) )
people = int(input("How many people to split the bill? " ) )
reslutls = percent / 100 * bill + bill
reslutls1 = "{:.2f}" .format(reslutls)
print(f" each should pay {reslutls1} $")
