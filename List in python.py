#Chapter-3 (List in Python)
marks=[94.4, 87.5, 95.2, 66.4, 45.2]
print(marks)
print(type(marks))
#Note: Listing works same like marks
print(marks[0])
print(marks[1])
print(len(marks)) #to find out the length same like string

#Multiple types of data we can store in a string
student= ["puja", 95.4,17,"Dhaka"]
print(student)

#differance between String and List
#1. in strring we can not change the data howewver we can identify the index
#2. in Lisiting we cab identify index as well as we can change the data.

str="Hello"
print(str[0])
#str[0]="Y" (this will not work)

print(student[0])
student[0]="Purba"
print(student)

#List Slicing
marks=[87,98,67.76, 34]
print(marks[1:4])
print(marks[:2])
print(marks[-2:])
print(marks[:-2]) #same with minus

#listing Methods

list= [1,6,9.9]
list.append(4) #adds an element
print(list)

list.sort() #shorts in accending order
print(list)

list.sort(reverse=True) #shorts in accending order
print(list)

list.reverse() #reverse list
print(list)

list.insert(1,3) #insert element in index
print(list)

list.remove(6) #remove element
print(list)

newlist=[1, 2, 1, 3, 4, 5, 1]

newlist.remove(1) #remove first element
print(newlist)

newlist.remove(1) #remove first element
print(newlist)

newlist.remove(1) #remove first element
print(newlist)

newlist2=[1, 2, 1, 3, 4, 5, 1]

newlist2.pop(2) #remove element at index
print(newlist2)

"""Tuples in Python"""

tup= (87,62,89,50,30)
print(type(tup))
List= [87,62,89,50,30]
print(type(List))
String= "87" "62" "89" "50" "30"
print(type(String))
Integer= 87
print(type(Integer))

#Tuple methods
#same as string we can not modify index to add value

tuple= (87,62,89,50,30,62)
"""tuple.index(87)
print(tuple)""" #tuple er index ayvabe kaj kortisena
print(tuple.count(62))
print(tuple.index(87))
print(tuple.index(62))


"""Practice qus"""
#1
#
# movie1=(input("1st movie: "))
# movie2=(input("2nd movie: "))
# # movie3=(input("3rd movie: "))
#
# Movie= [movie1, movie2, movie3]
# print(Movie)
# print(type(Movie))

#2. palindrome Element (samne piche dia same same 121, 121

list1=[ 1, 2, 3, 2, 1]
list2=[ 1, 2, 3, 2, 6]
copy_list1= list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome")

copy_list2= list2.copy()
copy_list2.reverse()

if(copy_list2 == list2):
    print("palindrome")
else:
    print("not palindrome")

#3

grade=("c","d","a","a","b","s","a")
print(grade.count("a"))
grade1=(1,2,3,1,1)
print(grade1.count(1))

#4

listofgrade= ["c","d","a","a","b","s","a"]
listofgrade.sort()
print(listofgrade)