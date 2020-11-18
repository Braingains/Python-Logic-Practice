united_kingdom = [
  {
    "name": "Scotland",
    "population": 5295000,
    "capital": "Edinburgh"
  },
  {
    "name": "Wales",
    "population": 3063000,
    "capital": "Swansea"
  },
  {
    "name": "England",
    "population": 53010000,
    "capital": "London"
  }
]

united_kingdom[1]["capital"] = "Cardiff"
#accesses element 1 in list and changes capital to Cardiff

united_kingdom.append({
    "name": "Northern Ireland",
    "population": 1811000,
    "capital": "Belfast"
}
)
print(united_kingdom[3])
# uses append() to add NI info

for countries in united_kingdom:
    print(countries ["name"])
# print info stored at "name" key for each item in list

def count_pop( list ):
    total_pop = 0

    for country in list:
        total_pop += country["population"]
    
    return f"{total_pop} people in UK"

print(count_pop(united_kingdom))
#creates function that iterates through list with for loop that adds value stored at "population" tag to variable total_pop.
#based on chicken example




