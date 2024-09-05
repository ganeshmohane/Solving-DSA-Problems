# A person’s body mass index is a simple calculation based on height and weight that classifies the person as underweight, overweight, or normal. The formula for metric unit is,

# BMI = weight in kilograms / (height in meters)2

# You are given a function,

# Int GetBMICategory(int weight, float height);

# The function accepts the weight (an integer number) and height (a floating point number) of a person as its arguments. 
# Implement the function such that it calculations the BMI of the person and returns an integer, the person’s BMI category as per the given rules:

# If BMI < 18, return 0.
# If 18 >= BMI < 25, return 1.
# If 25 >= BMI <30, return 2.
# If 30 >= BMI < 40, return 3.
# If BMI >= 40, return 4.

def GetBMICategory():
    height = float(input("Enter Height in cm: "))
    height_m = height / 100
    weight = int(input("Enter Weight in Kgs: "))
    BMI = weight / (height_m**2)
    print(BMI)
    
    if BMI < 18:
        return 0
    elif 18 >= BMI < 25:
        return 1
    elif 25 >= BMI < 30:
        return 2
    elif 30 >= BMI < 40:
        return 3
    else :
        return 4
BMI = GetBMICategory()
print("You come under category: ",BMI)