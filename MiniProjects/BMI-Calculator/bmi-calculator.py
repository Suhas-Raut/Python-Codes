"""
Takes a Input from user,
Height in Inches(IN) And Weight In Kilograms(KG).

"""

height = float(input("Hello, What is Your Height(IN) "))
weight = float(input("Hello, What is Your Weight(KG) "))

# Calculates The BMI

bmi = round(weight / (height ** 2)) 
if bmi <= 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi <= 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi <= 30:
  print(f"Your BMI is 28, you are slightly overweight.")
elif bmi <= 35:
  print(f"Your BMI is 33, you are obese.")
else:
  print(f"Your BMI is 40, you are clinically obese.")
