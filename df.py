Spheres = ['Career','Finances','Family','Environment','Self-Development','Impressions','Rest','Health']
Dreams = ['Head of science','10k Euro/month','Nadya, 3-rd child, time for children','Meetings for impression','No loans','dance Tournament, Public activities','Meditations for all','Active trainings']
Points = [7,3,7,7,6,4,7,6]
Goals = ['Training center','4k Euro/month in may','Strong contact with childrens','Quenue for meetings','Plan for health','Dance','Half day meditation + trip throw Dunaue','Doctors']

lifebalance = {'Spheres':Spheres,'Dreams':Dreams,'Points':Points,'Goals':Goals}

import pandas as pd
df = pd.DataFrame(lifebalance)


df.head(8)

df.describe()

df.Points

for el in df.Points:
    print(el)

sum = 0
for el in df.Points:
    sum += el
print(sum)

sum = 0
number = 0
for el in df.Points:
    sum += el
    number +=1
avg = sum / number
print(avg)