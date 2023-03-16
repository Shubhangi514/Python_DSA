# calculate Average Temprature

numDays = int(input("How many days Temprature do you want? "))
total = 0
temp = []
for i in range(numDays):
    nextDay = int(input("Day " +str(i+1) + "'s high Temperature: "))
    temp.append(nextDay)
    total += temp[i]
avg = round(total/numDays,2)
print("\nAverage = " +str(avg))
above = 0
for i in temp :
    if i > avg:
        above += 1
print(str(above) + "days temperature is above average")