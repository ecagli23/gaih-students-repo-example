#The answer of Homework-1
oddList = [num for num in range(10) if num % 2 ==1]
print("OddList = ",oddList)
evenList = [num for num in range(10) if num % 2 ==0]
print("EvenList = ", evenList)

#newList = oddList + evenList
#print(newList)

oddList.extend(evenList)
print("Merge 2 Lists ", oddList*2)

multipliedList = [i * 2 for i in oddList]
print("MultipliedList =",multipliedList)

j = 0
while (j < len(multipliedList)) :
  print(j, ". item value is:", (multipliedList[j]) , " and ", j, ". item type is: ",  type(multipliedList[j]), sep = '')
  j+=1