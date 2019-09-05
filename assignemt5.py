# I want to find the largest number from the entered numbers
# for example:
# I Enter: (1,5,3,19,2,70,71,-1)
# I should get "The maximum is 71"

num_int = int(input("Input a number: "))    # Do not change this line
max_int = 0
# Fill in the missing code
while num_int >= 0:
    num_int = int(input("Input a number: "))
    # Here am I saying that if the number that was entered 
    # the second time is higher then the first
    # then it becomes the max_int
    if num_int > max_int:
        max_int = num_int
print("The maximum is", max_int)    # Do not change this line
