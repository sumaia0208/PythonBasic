#problem1
name = 'Sumaia'
age = 28
print("My name is: "+name+ " and I am " + str(age)+ " years old") 

#problem2
num1 = 15
num2 = 5.5
num1_float = float(num1) 
num2_int = int(num2) 
print(num1_float)
print(num2_int)
print(type(num1_float))
print(type(num2_int))

#problem3
strVariable = 'Python programming is fun'
print(len(strVariable))
print(strVariable[7])
subString = strVariable[0:6]
print(subString)
test = 'I enjoy it'
print(subString+ " " + test)

#problem4
fruits = ["apple","banana","cherry","date"]
fruits.append("grape")
print(fruits)
fruits.remove('banana')
print(fruits)
print(len(fruits))
sliced_fruits = fruits[2:4]
extra_fruits = ['kiwi','lemon']
combined_sliced_fruits = sliced_fruits + extra_fruits
print(combined_sliced_fruits)

#problem5
num = int(input("Please enter an integer value: "))
if num%2 == 0:
    print('It is an even number')
else:
    print('It is a odd number')

#problem6
for number in range(1,11):
    print(number)
    
#problem6
sum = 0
for number in range(1,101):
    sum = sum + number
print("The summation value from 1 to 100 is: ",sum)

#problem7
def calculate_square():
    number = int(input("Please enter an integer number:"))
    square_value = number**2
    print("The square value is: ",square_value)
calculate_square()

def is_prime():
    number = int(input("Please enter a number for checking prime number:"))
    flag_value = False
    if number == 1:
        print(number, " is not a prime number")
    elif number > 1:
        for i in range(2,number):
            if (number%2) == 0:
                flag_value = True
                break
    if flag_value:
        print(number, " is not a prime number")
    else:
        print(number, " is a prime number")
is_prime()   
        
                

#problem8
dictionary = dict()
dictionary['name'] = 'Sumaia Rahman Ontora'
dictionary['age'] = 28
dictionary['grade'] = 3.99
print(dictionary)

for value in dictionary:
    print(value)