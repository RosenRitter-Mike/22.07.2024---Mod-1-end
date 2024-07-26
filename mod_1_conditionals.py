import statistics as st

#______________Conditionals 1__________________
num1: float = float(input("input the first number: "));
num2: float = float(input("input the second number: "));
print(f"{num1}\n"*3) if num1 < num2 else print(f"{num2}\n"*3);

#______________Conditionals 2__________________
num3: int = int(input("input the first number: "));
num4: int = int(input("input the second number: "));
print(f"Mean of numbers: {st.mean([num3,num4])}");

#______________Conditionals 3__________________
num_a: int = int(input("input the first number: "));
num_b: int = int(input("input the second number: "));
num_c: int = int(input("input the third number: "));
print(num_a) if num_a > num_b and num_a > num_c else print(num_b) if num_b > num_a and num_b > num_c else print(num_c);

#______________Conditionals 4__________________
film_len: int = int(input("What is the films length in minutes? "));
hours: int = film_len // 60;
minutes: int = film_len % 60;
print(f"The films length is {hours} hours and {minutes} minutes, enjoy!")

#______________Conditionals 5__________________
num_4d: int = int(input("input a four digit number: "));
print(f"The rightmost digit is {num_4d%10}");

#______________Conditionals 6__________________
num_4d2: int = int(input("input a four digit number: "));
print(f"The second digit from the right is {(num_4d2%100)//10}");

#______________Conditionals 7__________________
num_2d: int = int(input("input a two digit number: "));
print(f"The sum of the digits is {num_2d//10 + num_2d%10}");

#______________Conditionals 8__________________
num_2d2: int = int(input("input a two digit number: "));
print(f"The reverse of the digits is {num_2d2//10 + (num_2d2%10)*10}");

#______________Conditionals 9__________________
num: int = int(input("input a number: "));
print("even") if not num % 2 else print("odd");

#______________Conditionals 10__________________
salary: float = float(input("How much do you earn? "));
income_tax: float = 0;

if salary > 50000:
    income_tax += (salary - 50000) * 0.51;
    salary = 50000;

if salary > 35000:
    income_tax += (salary - 35000) * 0.45;
    salary = 35000;

if salary > 25000:
    income_tax += (salary - 25000) * 0.4;
    salary = 25000;

if salary > 18000:
    income_tax += (salary - 18000) * 0.3;
    salary = 18000;

if salary > 12000:
    income_tax += (salary - 12000) * 0.2;
    salary = 12000;

if salary > 6000:
    income_tax += (salary - 6000) * 0.1;
    salary = 6000;

print(f"Your income tax is: {income_tax:.2f}");

#______________Conditionals 11__________________
age: int = int(input("Input your age: "));
height: int = int(input("Input your height in cm: "));
print("Welcome in, enjoy!") if height > 115 or age > 18 and height > 100 else print("You are too short! You cant enter!");
