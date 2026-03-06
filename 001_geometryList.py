#Author:Miano
#Geometry: Container for geometry operators (SOPs) that define a modeled object
#The Geometry object represents a high-level modeled object, such as a character or a prop. It contains geometry operators that define its shape.
#List exercise 

transform = ["Translate","Rotate","Scale","Pivot Translate","Pivot Rotate","Uniform Scale"] #transform parameters
print("=> length: {} list: {}".format(len(transform),transform))

#add items to a list
transform.append("Uniform Scale")
transform.append("Modify Pre-Transform")
transform.append("Keep position when parenting")
transform.append("Child Compensation")
transform.append("Enable Constraints")
print("=> append to list ",transform)

#delete items from the list
del transform[len(transform)-1] 
del transform[len(transform)-1]
del transform[len(transform)-1]
del transform[len(transform)-1]
del transform[len(transform)-1]
print("=> del items ",transform)

#sorting a list
transform.sort()
print("=> sorted list: ",transform)

#iterate through the items of the list
print("Tranform Parameters: ")
for parameter in transform:   
	print(parameter)
