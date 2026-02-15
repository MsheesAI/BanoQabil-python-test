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
user_input = str(input("Enter your city name"))
temperature_input = int((input("Enter your city temperature")))

if temperature_input == 0:
    print(f"Its freezing outside in {user_input}")
elif temperature_input <0 and temperature_input>10:
    print(f"Its too cold in{user_input}")
elif temperature_input == 10 and temperature_input>20:
    print(f"ts getting cold in{user_input}")
elif temperature_input == 20 and temperature_input>30:
    print(f"Its a pleasant weather in{user_input}")
elif temperature_input == 30 and temperature_input>40:
    print(f"Its getting hot in{user_input}")
elif temperature_input == 40 and temperature_input>50:
    print(f"Its too much hot outside in {user_input} ")
elif temperature_input < 50:
    print(f"hahahhaha game over{user_input}")

#Question:4 Find the first Occurrence of a Number in a list 

list_num = [10,23,34,45,34,67,34,67,34,89]
for i in list_num:
    if len(list_num)==5:
        print(list_num)
        break

#Question 5:Print Numbers in a Given Range (Using For Loop and Range)
user_start = int(input("Enter a starting Number: "))
user_end = int(input("Enter a ending number: "))
for i in range(user_start,user_end):
    print(i)  

   










    

