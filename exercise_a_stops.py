stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

stops.append("Edinburgh Waverly")
#appends to end of list

stops.insert(0, "Glasgow Queen Street")
#inserts at element 0

stops.insert(4, "Polmont")
#inserts at element 4

print(stops.index("Linlithgow"))
#prints the index position of "Linlithgow"

stops.remove("Livingston")
#removes "Livingston"

stops.pop(2)
#removes element at index 2: Cumbernauld

print (len(stops))
#prints length (number of elements) in list stops

stops = sorted(stops)
#Sorts list alphabetically

stops.reverse()
#reverses list with .reverse() method

for stations in stops:
    print(stations)
#for loop prints each station individually per loop