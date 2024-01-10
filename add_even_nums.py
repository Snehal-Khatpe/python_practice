"""
write a program that calculates the sum of all the even numbers from 1 to X.
If X is 100 then the first even number would be 2 and the last one is 100:

"""
#Program is as below
target=int(input())

initial_value=0
for num in range(1, target+1):
    if num%2==0:
        initial_value+=num

print(initial_value)
