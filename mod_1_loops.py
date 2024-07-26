#______________Loops 1__________________
top: int = int(input("What is the top? "));
for i in range (1, top+1):
    print(i, end="   ");
print();

#______________Loops 2__________________
num1: int = int(input("Input num 1: "));
num2: int = int(input("Input num 2: "));

if num1 > num2:
    for i in range(num2, num1+1):
        print(i, end="   ");
else:
    for i in range(num1, num2+1):
        print(i, end="   ");

#______________Loops 3__________________
n: int = int(input("Input n: "));
list_n: list[int] = [i for i in range(n+1) if not i % 2];
print(list_n);

#______________Loops 4__________________
max: int = int(input("Input max: "));
den: int = int(input("Input denominator: "));
list_n: list[int] = [i for i in range(max+1) if not i % den];
print(list_n);