#remove an item from a set if it is present in the set
a={1,2,3,4,5,"Abhyas"}
if "Abhyas" in a:
    a.remove("Abhyas")
print(a)