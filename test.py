# print("Hello world")

# varOne = 15
# varTwo = 20
# varThree = 55

# midArithmetic = (varOne + varThree + varThree) / 3

# print midArithmetic

# print ("this is the second commit")

#======================================== Functions, Conditions And Loops ============================================================

# def say_hi():
#     age =int(input("Please enter your age: "))
#     if age > 18 :
#         print("Hi adult")
#     elif age < 18 and age > 0 :
#         print("Hi child")

# say_hi()

# def check_numbers():
#     firstNum = input("Enter the number of columns: ")
#     secondNum = input("Enter the number of rows: ")
    # print(type(firstNum))
    # print(type(secondNum))
    # if type(firstNum) != int or  type(secondNum) != int:
    #     raise Exception ("Only numbers accepted")
    # else:
    #     print (f"you have two numbers: {firstNum}, and {secondNum}")

# check_numbers()

#========================================== Loops ===================================
# A simple programm to save five user's favorite sites

listSites = []
counter = 0

# for item in [1,2,3,4,5,6,7,8,9]:
#     siteAdress = input("Enter your favorite site: ")
#     listSites.append(item)
# print(listSites)

while counter < 5:
    counter += 1
    siteAdress = input("Enter your favorite site: ")
    listSites.append(siteAdress)

print(listSites)
