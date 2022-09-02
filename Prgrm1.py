details=[['Anu',21],['Divya',40],['chandu',50],['Ak',19]]
print("The list of names nad ages before sorting is")
print(details)
print("The list after sorting based on age is")
print(sorted(details,key=lambda x:x[-1]))
