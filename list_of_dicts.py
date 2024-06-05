china_cities = []
china_cities.append({"name":"Shanghai","country":"China","status":"Direct-Administered Municipality","population":21909814})
china_cities.append({"name":"Beijing","country":"China","status":"Direct-Administered Municipality","population":18960744})
china_cities.append({"name":"Shenzhen","country":"China","status":"City with Independent Planning Status","population":17444609})
china_cities.append({"name":"Guangzhou","country":"China","status":"Sub-Provincial City","population":10641408})
china_cities.append({"name":"Chengdu","country":"China","status":"Sub-Provincial City","population":13568357})
china_cities.append({"name":"Tianjin","country":"China","status":"Direct-Administered Municipality","population":11052404})
china_cities.append({"name":"Wuhan","country":"China","status":"Sub-Provincial City","population":10494879})
china_cities.append({"name":"Dongguan","country":"China","status":"Prefecture-Level City","population":9644871})
china_cities.append({"name":"Chongqing","country":"China","status":"Direct-Administered Municipality","population":9580819})
china_cities.append({"name":"Xi'an","country":"China","status":"Sub-Provincial City","population":9392938})
print("|City name | country | status | population|")
print("|---|---|---|---|")

for city in china_cities:
    print(f"|{city['name']} | {city['country']} | {city['status']} | {city['population']} |")