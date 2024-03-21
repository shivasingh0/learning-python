# Conditions --->
# h = int(input())
# if( h > 10 ):
#     print('The value of h is grater than 10')
# elif(h == 10):
#     print("The value of h is equal to 10")
# else:
#     print('The value of h is less than 10')

# loop --->
# k = int(input())
# while(k > 10):
#     print("Hello")
#     k=k-1


# Excercise --->
import random
r = random.randint(0,10)

while True:
    num = int(input('Guess the number'))
    if(num > r):
        print("Try smaller no.")
    elif(num < r):
        print('Try greater no.')
    else:
       print("Congrates your value is equal now")
       break
