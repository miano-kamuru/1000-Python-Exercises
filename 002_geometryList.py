#Author:Miano
#Geometry: Container for geometry operators (SOPs) that define a modeled object
#The Geometry object represents a high-level modeled object, such as a character or a prop. It contains geometry operators that define its shape.
#List exercise 

translate = [0,0,0] #Translation along XYZ axes.
rotate = [0,0,0] #Degrees rotation about XYZ axes.
scale = [1,1,1] #Non-uniform scaling about XYZ axes.
pivotTranslate = [0,0,0]
pivotRotate = [0,0,0]
uniformScale = 1.0 #Scale the object uniformly along all three axes.

Transform = [] #geometry parameters stored in this list
parameters=[translate,rotate,scale,pivotRotate,pivotTranslate,uniformScale]

#append parameters to Transform 
for parameter in parameters:
	Transform.append(parameter)
print("=> len: {} parameters".format(len(Transform)))

#display Transform parameters
count = 1
for parameter in Transform:
	print("parameter {} : {}".format(count,parameter))
	count = count+1

