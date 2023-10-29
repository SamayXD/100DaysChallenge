print("BMI Calculator")

weight = input("Weight(in kg): ")
height = input("Height(in m): ")

bmi = float(weight) / (float(height)**2)

print(f"Your BMI is: {str(bmi)}")