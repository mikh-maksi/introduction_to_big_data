# Collecting data to separate variables (dicts)
country1 = {"name":"USA","region":"Americas","GDP":25462700}
country2 = {"name":"China","region":"Asia","GDP":17963171}
country3 = {"name":"Germany","region":"Europe","GDP":17963171}
country4 = {"name":"Japan","region":"Asia","GDP":4231141}
country5 = {"name":"India","region":"Asia","GDP":3385090	}
# print(country1,country2,country3,country4,country5)
# Create list of dictionaries
countries = [] # Create empty list
countries.append(country1) # add first element
countries.append(country2) 
countries.append(country3) 
countries.append(country4) 
countries.append(country5) 
# print(countries)
# make loop for show elements
# for country in countries:
#     print(country)

# Sum calculating algorythm
sum = 0
for country in countries:
    sum += country['GDP']

print(sum)
# Avreage value calculating algorythm
sum = 0
number = 0
for country in countries:
    sum += country['GDP']
    number+= 1
average = sum / number
print(average)

# find maximum element
max = countries[0]['GDP']
for country in countries:
    if country['GDP']>max:
        max = country['GDP']
print(max)

# find position of maximum element
max = countries[0]['GDP']
max_position = 0
number = 0
for country in countries:
    if country['GDP']>max:
        max = country['GDP']
        maxposition = number
    number+=1
print(max)
print(max_position)


# find minimum element
min = countries[0]['GDP']
for country in countries:
    if country['GDP']<min:
        min = country['GDP']
print(min)

# find position of minimum element
min = countries[0]['GDP']
number = 0
min_position = 0
for country in countries:
    if country['GDP']<min:
        min = country['GDP']
        min_position = number
    number +=1
print(min)
print(min_position)