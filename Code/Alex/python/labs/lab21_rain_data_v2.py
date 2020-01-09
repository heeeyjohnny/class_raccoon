'''*not complete*
Lab 21: Rain data

Version 2

Now that you've successfully extracted the data, let's done some statistics.

1. Calculate the mean of the data:

mean

2. Use the mean to calculate the standard deviation, which is a measure of how "spread out" the data is:

standard_deviation

68.2% of the data falls within 1 standard deviation of the mean.

bell_curve

3. Find the day which had the most rain.

4. Find the year which had the most rain on average.
'''


import re
import datetime
import math


with open('rain_data.txt', 'r') as file:
    rain_data = file.read()

data = re.findall("(\d{2}-\w{3}-\d{4})\s+(\d+)", rain_data)
#print(data)
rain_data = []
for item in data:
    date = datetime.datetime.strptime(item[0], '%d-%b-%Y')
    rain_data.append((date, item[1]))
    #print(rain_data)
#for item in rain_data[:100]:
    #print(item[0].strftime('%d-%b-%Y'), item[1])

#calculate the mean of the DATA
    #print(data)
count_for_the_total = 0
for i in range(len(rain_data)):
    count_for_the_total += int(rain_data[i][1])
total = count_for_the_total
mean = total / len(rain_data)
print(f"\n\nThe mean of the data is {mean}\n")

#Use the mean to calculate the standard deviation
    # for each number: subtract the Mean and square the result.
    # Then work out the mean of those squared differences.
    # Take the square root of that and we are done!
standard_deviation = []
for i in range(len(rain_data)):
    standard_deviation.append((int(rain_data[i][1]) - mean)**2)
s_mean = sum(standard_deviation) / len(standard_deviation)
s_mean = math.sqrt(s_mean)
print(f"The standard deviation of the data is {s_mean}\n")

#Find the day which had the most rain.
day_most_rain = rain_data[0]
for item in rain_data:
    if item[1] > day_most_rain[1]:
        day_most_rain = item
print(f"The day with the most rain had {day_most_rain[1]} tips\n")




#todo

#
# #Find the year which had the most rain on average.
# list_of_years = []
# for i in range(len(rain_data))
#     list_of_years.append(i)
# print(f"The year with the most rain was {year_most_rain}")