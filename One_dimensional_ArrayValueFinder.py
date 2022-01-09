#Millborne A. Galamiton BS-CPE-2B
c=[]  #Initialize an empty array

size = int(input("Enter the size of your array: "))  #ask the user to input the size of an array

for i in range(size): # It will display the index then ask the user to input a value on certain index
    print("Index[",i,"]:",end=" ")
    c.append(input())

locate = int(input("Enter index to locate the element: "))#ask the user to input the index to locate the element

for i in range(size):  
    if c[locate]==c[i]:#check if there is match
        
        print("Element found:","Index[",i,"]:",c[locate],"is on the",i+1,"position")#display the located position of the element
 
                        