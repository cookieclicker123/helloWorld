utensils = {"fork", "spoon", "knife"}
#no duplicates 
dishes = {"bowl", "plate", "cup", "knife"}
#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()

#utensils.update(dishes)

dinnerTable = utensils.union(dishes)

print(dishes.difference(utensils))

print(utensils.intersection(dishes))

#for x in dinnerTable:
    #print(x)

