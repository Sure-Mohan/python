#Tuple example
my_tuple=("banana","apple","avacado")
print(my_tuple)
#Length of an tuple
my_tuple=("banana","apple","avacado")
print(len(my_tuple))
#in tuples it allows duplicates
my_tuple=("banana","apple","avacado","apple","orange")
print(my_tuple)
#Type of the tuple
my_tuple=("banana","apple","avacado")
print(type(my_tuple))
#Accesing an element in a tuple
my_tuple=("banana","apple","avacado","dragon")
print(my_tuple[1])
#if you to print elements in between given range
print(my_tuple[1:3])
#updating the list(adding elmemt into the tuple)
my_tuple=("banana","apple","avacado","dragon")
y=list(my_tuple)
y.append("kiwi")
my_tuple=tuple(y)
print(my_tuple)
#updating the list(remove elmemt into the tuple)
my_tuple=("banana","apple","avacado","dragon","kiwi")
y=list(my_tuple)
y.remove("kiwi")
my_tuple=tuple(y)
print(my_tuple)
#unpacking the tuple
fruits=("apple","banana","avacado")
(red,yellow,green)=fruits
print(red)
print(yellow)
print(green)
#Loops
my_tuple = ("apple", "banana", "avacado")
for x in my_tuple:
  print(x)
#Loops
my_tuple = ("apple", "banana", "avacado")
for i in range(len(my_tuple)):
  print(my_tuple[i])
#joining of multiple tuples
tuple1 = ("apple", "banana", "avacado")
tuple2=(1,2,3,4,5,6,7,8)
tuple3=("a","b","c","d")
tuple4=tuple1+tuple2+tuple3
print(tuple4)
#Multiplying the tuples
fruits= ("apple", "banana", "avacado")
numbers=(1,2,3,4,5,6,7,8)
alphabets=("a","b","c","d")
tuple1=fruits*2
tuple2=numbers*9
tuple3=alphabets*3
print(tuple1)
print(tuple2)
print(tuple3)
#count() method
my_tuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = my_tuple.count(5)
print(x)

