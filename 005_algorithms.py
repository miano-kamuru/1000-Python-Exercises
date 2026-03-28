A= [9,18,100,1,3,21,109]
print(A)

#bubblesort
iterations = len(A)-1
for i in range(iterations):
    for j in range(iterations):
        if(A[j]>A[j+1]):
            temp=A[j]
            A[j]=A[j+1]
            A[j+1]=temp
print(A)

#Binary Search
def binarySearch(A,term):
    length=len(A)
    start=0
    end=length-1
    while(start<=end):
        mid=(start+end)//2
        if(term==A[mid]):
            return mid
        elif(term > A[mid]):
            start=mid+1
        else:
            end=mid-1
    if(start<end):
        return None
print("-> ",binarySearch(A,100))
print("-> ",binarySearch(A,109))

#linear search unsorted
def linearSearch(A,term):
    length=len(A)
    for i in range(length):
        if(term==A[i]):
            return i
            
#linear search Sorted
def linearSearchS(A,term):
    length=len(A)
    for i in range(length):
        if(term==A[i]):
            return i
        elif(A[i]>term):
            return None
       
print(linearSearchS(A,21))