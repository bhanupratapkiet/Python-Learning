#iterator.py
list1 = [1,2,3,4]
a = iter(list1)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
#1
#2
#3
#4
========================
list1 = [1,3,4,5,6]
a = list1.__iter__()
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
#1
#3
#4
#5
#6
=========================
list1 = [1,2,3,4]
a = iter(list1)
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
#1
#Traceback (most recent call last):
#2
#3
#4
    print(next(a))
StopIteration
=========================
list1= [1,2,3,4,5,6]
a = iter(list1)
while True:
    try:
        b = next(a)
        print(b)
    except StopIteration:
        print("list ends")
        break
#1
#2
#3
#4
#5
#6
#list ends
=========================
list1= [1,2,3,4,5,6]
a = iter(list1)
while True:
    try:
        b = next(a)
        print(b)
    except StopIteration:
        print("list ends")
        break
    finally:
        print("All Ok")
#1
#All Ok
#2
#All Ok
#3
#All Ok
#4
#All Ok
#5
#All Ok
#6
#All Ok
#list ends
#All Ok
=======================
print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
    print(i)
# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("geeks", "for", "geeks")
for i in t:
    print(i)
# Iterating over a String
print("\nString Iteration")
s = "Geeks"
for i in s:
    print(i)
# Iterating over dictionary
print("\nDictionary Iteration")
d = dict()
d['xyz'] = 123
d['abc'] = 345
for i in d:
    print("%s  %d" % (i, d[i]))
#List Iteration
#geeks
#for
#geeks

#Tuple Iteration
#geeks
#for
#geeks

#String Iteration
#G
#e
#e
#k
#s

#Dictionary Iteration
#xyz  123
#abc  345
=============================
class InfIter:
    """Infinite iterator to return all
        odd numbers"""

    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num
a = iter(InfIter())
print(next(a))
print(next(a))
print(next(a))
print(next(a))
print(next(a))
#1
#3
#5
#7
#9
========================




