# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = int(weight/(height)**2)
if BMI < 18.5:
  print("underweight ")
elif BMI < 25:
  print("normal weight")
elif BMI < 30:
  print("slightly overweight")
elif BMI < 35:
  print(" obese ")
else:
  print("no fucking way")