users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

print (users["Jonathan"]["twitter"])
# accesses the users dictionary, the nested Jonathan dictionary and prints the value at the key "twitter"

print (users["Erik"]["home_town"])
# accesses the users dictionary, the nested Erik dictionary and prints the value at the key "home_town"

print (users["Erik"]["lottery_numbers"])
# accesses the users dictionary, the nested Erik dictionary and prints the array at the key "lottery_numbers"

print (users["Avril"]["pets"][0]["name"])
# ...accesses pets list, at index 0 is a dictionary with the "name" key

smallest = min(users["Erik"]["lottery_numbers"])
print(smallest)
#prints the smallest of Eric's lottery numbers

for numbers in (users["Avril"]["lottery_numbers"]):
    if (numbers % 2) == 0:
        print(numbers)
#for the values in ["Avril"]["Lottery Numbers"] if the value leaves no remainder when divided by 2 (and is therefore even), then print it.

users["Erik"]["lottery_numbers"].append(7)
print(users["Erik"]["lottery_numbers"])
#accesses Erik's lottery numbers list and adds int 7

users["Erik"]["home_town"] = "Edinburgh"
print(users["Erik"]["home_town"])
# changes the value stored at "home_town"

users["Erik"]["pets"].append({"name" : "Fluffy", "species" : "dog"})
print(users["Erik"]["pets"])
#uses append() to add fluffy the dog to ["pets"]

users.update({
    "Ewan": {
    "status": "doing homework at 11pm",
    "pin number": "aye right",
    "home_town": "Edinburgh"}
    }
    )
print(users["Ewan"])
#uses .update() to add new user to dictionary