weight = float(input("Enter the weight: "))
height = float(input("Enter the height: "))
bmi = weight / (height ** 2)

if bmi <= 18.5:
    print("underweight")
elif bmi <= 25.0:
    print("Normal")
elif bmi <= 30.0:
    print("Overweight")
else:
    print("Obese")
