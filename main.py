#Question 1 print only neagative numbers from the list
numbers = [1, -2, -13, 4, -5, 6,-7,8,9,11]
negative_numbers = [num for num in numbers if num < 0]
print("Negative numbers in the list:", negative_numbers)


#Question 2 : Multiplication table using while loop
start = int(input("Enter starting point for the multiplication: "))
end = int(input("Enter Ending point for the multiplication: "))

for i in range(start, end + 1):
    print(f"{start}X{i} = {i*start}")

#question3 : Temperature checker program



    

