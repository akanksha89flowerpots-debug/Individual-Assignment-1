# PROBLEM 1 --> BMI Calculator
weightPounds = float(input("Enter weight in pounds: "))
heightInches = float(input("Enter height in inches: "))
#Imerial formula
bmi_imperial = (weightPounds /( heightInches **2)) * 703
#Convert to metric
weightKg = weightPounds * .453592
heightMeters = heightInches * .0254
#Using metric formula
bmi_metric = weightKg / (heightMeters**2)
#Output results
print("BMI (imperial) is ", round(bmi_imperial, 2))
print("BMI (metric) is ", round(bmi_metric, 2))
# PROBLEM 2 --> Vehicle Routing
#user input
time = float(input("Enter time in hours: "))
speed = float(input("Enter speed in miles per hour: "))
#processing
distance = speed * time
#display
print("Traveled distance (in miles): ", round(distance, 2))
#Route calculations
local = 1.00*30
parkway= 0.88*40
highway = .87*55
print("local route: ",local,"miles")
print("parkway: ",parkway,"miles")
print("highway: ",highway,"miles")
#determine the shortest route
shortestDistance = min(local, parkway, highway)
if shortestDistance == local:
print("Shortest Route: Local")
elif shortestDistance == parkway:
print("Shortest Route: Parkway")
else:
print("Shortest Route: Highway")
