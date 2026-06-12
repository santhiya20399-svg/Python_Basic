print("Hello World")
n=23
print('even') if n%2 == 0 else print('odd')
name =['Santhiya','Sanjana','Sangeetha'] #list example
print(name)
print(name[1])
print(len(name))
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
thislist[1:3] = ["blackcurrant", "watermelon"]
thislist.insert(2, 'banana')
print(thislist)
thislist.append('grapes')
print(thislist)
thislist.remove('banana')
print(thislist)
thislist.pop(1)
print(thislist)
thislist.pop()
print(thislist)
tropical = ["pineapple", "papaya"]
del tropical[0]
print(thislist)
thislist.extend(tropical)
print(thislist)
newlist = []
for x in thislist:
  if "a" in x:
    newlist.append(x)

print('This is the new list:', newlist)
for i in range(len(thislist)):
  print(thislist[i])
thislist.sort()
print(thislist)
print(min(thislist))