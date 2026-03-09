#author: Miano
#Geometry: Container for the geometry operators (SOPs) that define a modeled object.
#dictionary study
doc = {
    "translate":"Translation along XYZ axes.",
    "rotate":"Degrees rotation about XYZ axes.",
    "scale":"Non-uniform scaling about XYZ axes.",
    "pivot":"Local origin of the object.",
    "uniform scale":"Scale the object uniformly along all three axes."
}

print("documenation length: ",len(doc))
for key,value in doc.items():
    print(key,":",value)
doc["Modify Pre-Transform"]="This menu contains options for manipulating the pre-transform values."
print("documentation length: ",len(doc))
print(doc)
print("============================================================================================================\n")

transform = {
    "translate":[0,0,0],
    "rotate":[0,0,0],
    "scale":[1,1,1],
    "pivot translate":[0,0,0],
    "pivot rotate":[0,0,0],
    "uniform scale":1
}

for key,value in transform.items():
    print(key,":",value)
print("parameter count=> ",len(transform))
print("\n")

del transform["pivot translate"]
del transform["pivot rotate"]

if "pivot translate" in transform:
    print(transform["pivot translate"])
else:
    print("key does not exist")
    
if "translate" in transform:
    print("translate found!")
    print("translate x:{} translate y:{} translate z:{}".format(transform["translate"][0],transform["translate"][1],transform["translate"][2]))
print("\n")

#change translate values
transform["translate"][0]=1
transform["translate"][1]=10
transform["translate"][2]=100
print("translate x:{} translate y:{} translate z:{}".format(transform["translate"][0],transform["translate"][1],transform["translate"][2]))
print("transform length=> ",len(transform))
print("\n")
transform["help"]=doc
print("transform length=> ",len(transform))

for key,value in transform.items():
    print("{} : {}".format(key,value))
print("\n")

print("uniform scale help: ",transform["help"]["uniform scale"])
print("rotate help: ",transform["help"]["rotate"])