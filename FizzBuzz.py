i = int(input("Enter a number:"))
for i in range(101):
    if i%3==0:
        print ("Fizz")
    if i%5==0:
        print ("Buzz")
    if i%5 + 3==0:
        print ("FizzBuzz")
    else:
        print (i)