
# # Definite loop, indefintite loop
# #Iterative control - loops - while loop, for loop, nested loops
# #while // indefinite

# # #Find all even numbers between 0 and n. where, n is given by the user

# # x = 0
# # n = int(input("Enter the last number: "))
# # while( x < n ):
# #     print(x)
# #     n = n + 2

# # #print all even numbers n to m. m should be greater than n.

# # # n = int(input("Enter the first number: "))
# # # m = int(input("Enter the last number: "))
# # n = n % m
# # # while( n < m ):
# #     print(n)
# #     n = n +2



# # write a program to take numbers from the user until he enter 0 as input. then print sum of all entered numbers

# # n = int(input("Enter the numbers until 0: "))
# # 


# #write an effecient program to determine sum of N natural numbers where N is given by the user

# #for loop // definite 

# # for i in range(1, 10, 3): #( start, stop, skip/step)
# #   print(i)

# # for i in range(1, 6):
# #   print(i)

# # fruits = ["apple", "oranges", "grapes"]
# # for i in range(len(fruits)):
# #   print()

# # for x in range 'JNNFLK':
# #     print(x)
# # for i in [123, 'def', 'efg', 'ijk']:
# #   print(i)

# # for x in range(1, 20, 2):
# #   print(x *2)

# #given number is prime or not?? 
# # x = int(input("Enter a number"))
# # flag = True
# # for i in range(2, x):
# #     if(x % i == 0):
# #         flag = false
# # if(flag):
# #     print("the number is prime")


# #nested loops
# for i in range(5):
#     print("outside loop is: i = ", i)
#     for j in range(i):
#         print("inside loop is: j = ", j)

# for i in range(1,5):
#     for j in range(1,6):
#         print(i,end=" ")
#     print()

#     #if the sum of the facotiral of the digits in a number is equal to the original number, the number is a strong number
#     # 145 = 1! + 4! + 5!
    

#     #infinite loop
    
#     #loop control statements - break, continue, pass
#     a = 30
#     b = 100
#     if b > a:
#         pass
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     if x == "banana":
#         continue
#     print(x)


#     #tuples, dictionary.


#     # list

#     colors = ["red", "Green", "Blue", "Orange", "Purple", "White", "black" ]
#     print(colors[1])


    
#     colors.append("grey")
#     colors.insert(1,"grey")

#     colors.remove("red")
#     print(colors)

   
   

#     numbers = [56,47,65,32,43]
#     numbers.sort() #uses ASCII values to sort the elements
#     print(numbers)

#     numbers.reverse()
#     print(numbers)

#     numbers.pop(3) #pop function is not going to return what's been popped out
#     print(numbers)
        
#     #casting
#     casper = [32,435,12,35,12,45]
#     numbers.extend(casper)
#     print(numbers)
#     # numbers+ (casper)

#     numbers.index(32)
#     numbers.clear()



#Tuples
'''Immutable linear data structure,
once a tuple is defined, it cannot be altered.'''

# num = [1,4,6]
# #converting list into tuple

# tuple(num)

# jdfj = (1, )
# print(jdfj)

#tuples are unchangable

# t = (10,20,30)
# t[0]
# t.insert(1,15)
# print(t)


# tuple1 = ("akshaya", 1, 8)
# print(tuple1)

# tuple2 = tuple1 + ("Moksha", 0 ,1)
# print(tuple2)

# NT = (1,2, ("POP", "ROCK"), (3,4), ("DISCO", (1,2)))
# print(NT[4][1][1])

# #nested tuples
# SF = (1,4,("snake", "cat"), (7,0), ("sonic", (1,2,(3,7,("dog", "sparrow")))))
# print(SF[4][1][2][2][0])

# SF_set = set(SF)
# print(SF_set)



# #sets
# '''no indexing
# un ordered, unchangable

# but can move remove items and add new items
# cannot have duplicates'''

# hbfhj = {"ajans","jdj", "jdj"}
# print(hbfhj)

# hbfhj.add("hjf")
# print(hbfhj)

# hbfhj.remove("jdj")
# print(hbfhj)



# # hbfhj_list = list(hbfhj)
# # print(hbfhj_list) #converting set to list

# # hbfhj_tuple = tuple(hbfhj)
# # print(hbfhj_tuple) # converting set to tuple



# album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
# album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])
# print(album_set1.union(album_set2))
# print(set(album_set1).issuperset(album_set2))
# print(set(album_set2).issubset(album_set1))




#Write a code to create a student database, using tuples which have student name, marks for 5 subjetcs, total percentage
#create at least 5 students and sort them based on the toatl percentage 
#for each subject find the person who got the highest and lowest marks

# Tuple_1 = ("Akshaya", "Jahnavi", "Vinyana", "Pooja", "Prachi", (90,85,100,67,98), (50, 89, 30, 95, 80), (40,30,20,10,0), (76, 70, 89,80,90),(30,50,40,20,90) )
# print(" Marks of Akshaya of subjects Phy,Chem,Math,Eng,San: ", Tuple_1[5] )
# print(" Marks of Jahnavi of subjects Phy,Chem,Math,Eng,San: ", Tuple_1[6] )
# print(" Marks of Vinyana of subjects Phy,Chem,Math,Eng,San: ", Tuple_1[7] )
# print(" Marks of Pooja of subjects Phy,Chem,Math,Eng,San: ", Tuple_1[8] )
# print(" Marks of Prachi of subjects Phy,Chem,Math,Eng,San: ", Tuple_1[9] )
# print("percentage of Akshaya: ", ((Tuple_1[5][0] +Tuple_1[5][1] + Tuple_1[5][2] + Tuple_1[5][3] + Tuple_1[5][4])/500 )*100)
# print("percentage of Jahnavi: ", ((Tuple_1[6][0] +Tuple_1[6][1] + Tuple_1[6][2] + Tuple_1[6][3] + Tuple_1[6][4])/500 )*100)
# print("percentage of Vinyana: ", ((Tuple_1[7][0] +Tuple_1[7][1] + Tuple_1[7][2] + Tuple_1[7][3] + Tuple_1[7][4])/500 )*100)
# print("percentage of Pooja: ", ((Tuple_1[8][0] +Tuple_1[8][1] + Tuple_1[8][2] + Tuple_1[8][3] + Tuple_1[8][4])/500 )*100)
# print("percentage of Prachi: ", ((Tuple_1[9][0] +Tuple_1[9][1] + Tuple_1[9][2] + Tuple_1[9][3] + Tuple_1[9][4])/500 )*100)

students_data = (
    ("Akshaya", (90,85,100,67,98)),
    ("Jahnavi", (50,89,30,95,80)),
    ("Vinyana", (40,30,20,10,0)),
    ("Pooja", (76,70,89,80,90)),
    ("Prachi", (30,50,40,20,90))
)
students = []

for student in students_data:
    name = student[0]
    marks = student[1]
    total = sum(marks)
    percentage = (total/500)*100
    students.append((name, marks,percentage))

students = list(students)















