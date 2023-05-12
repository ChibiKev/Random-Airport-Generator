import json
import string
import random

listOfCities = [
  'Garnet',
  'Amethyst',
  'Aquamarine',
  'Diamond',
  'Emerald',
  'Pearl',
  'Ruby',
  'Peridot',
  'Sapphire',
  'Opal',
  'Citrine',
  'Turquoise'
]

listOfCountries = [
  'Java Kotlin Empire',
  'C Family Empire',
  'JavaScript TypeScript Empire',
  'Python Empire',
  'PHP Empire',
  'Ruby Empire',
  'MatLab Empire',
  'Assembly Empire',
  'Go Empire',
  'HTML CSS Empire',
  'SQL Empire',
  'NoSQL Empire',
  'Unity Empire',
  'Rust Empire',
  'Swift Empire',
  'Unreal Engine Empire',
  'R Empire',
  'Dart Empire',
  'Perl Empire',
  'Scala Empire'
]

allAirports = True
totalAirports = 17576
airportSet = set()
seperator = 50
start = 1
end = len(listOfCountries) * seperator

result = []

def generateAirport(id, value):
  code = random.randint(start, end)
  
  name = value + " Airport"
  
  countryIndex = (code - 1) // seperator
  country = listOfCountries[countryIndex]
  
  cityIndex = (code - 1) % len(listOfCities)
  city = listOfCities[cityIndex]
  
  airport = {
    'id': id,
    'name': name,
    'city': city,
    'country': country,
    'value': value,
    'code': code
  }
  return airport

if allAirports:
  for firstLetter in string.ascii_uppercase:
    for secondLetter in string.ascii_uppercase:
      for thirdLetter in string.ascii_uppercase:
        value = firstLetter + secondLetter + thirdLetter
        result.append(generateAirport(len(result) + 1, value))
else:
  while len(airportSet) != totalAirports:
    uppercaseLetters = string.ascii_uppercase
    firstLetter = uppercaseLetters[random.randint(0, len(uppercaseLetters) - 1)]
    secondLetter = uppercaseLetters[random.randint(0, len(uppercaseLetters) - 1)]
    thirdLetter = uppercaseLetters[random.randint(0, len(uppercaseLetters) - 1)]
    
    value = firstLetter + secondLetter + thirdLetter
    if value in airportSet:
      continue
    airportSet.add(value)
    result.append(generateAirport(len(result) + 1, value))
 
# Serializing json
json_object = json.dumps(result, indent=2)
 
# Writing to AirportsData.json
with open("AirportsData.json", "w") as outfile:
  outfile.write(json_object)