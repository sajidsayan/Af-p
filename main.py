data = {
    'c1' : 'Bangladesh',
    'c2' : 'India',
    'c3' : 'Bangladesh',
    'c4' : 'Nepal',
    'c5' : 'India',
    'c6' : 'Pakistan',
    'c7' : 'Potuegal',
    'c8' : 'Bangladesh',
    'c9' : 'India',
    'c10' : 'United States of America',
    'c11' : 'Bermia',
    'c12' : 'Guitar',
}
data2 = {
    'c1' : 'bangladesh',
    'c2' : 'india',
    'c3' : 'bangladesh',
    'c4' : 'nepal',
    'c5' : 'india',
    'c6' : 'pakistan',
    'c7' : 'potuegal',
    'c8' : 'bangladesh',
    'c9' : 'india',
    'c10' : 'united states of america',
    'c11' : 'bermia',
    'c12' : 'guitar',
}
print("Orginal Dictionary: ",data)
k = input("Search a country: ").lower()
c = 0
for key in data2:
    if data2[key] == k:
        c = c + 1
print(f"Frequency of {k} is: {c}")
