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
for country in countries:
    print(country)