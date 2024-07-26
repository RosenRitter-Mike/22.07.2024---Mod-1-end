# #______________Data Proc 1__________________
# my_sum: int = None;
# while True:
#     num: int = int(input("Input a number: "));
#     if num == -99:
#         break;
#     else:
#         if not my_sum:
#             my_sum = num;
#         else:
#             my_sum += num;
# print(f"Sum: {my_sum}");
#
# #______________Data Proc 2__________________
# my_min: int = None;
# my_max: int = None;
# while True:
#     num: int = int(input("Input a number: "));
#     if num == -99:
#         break;
#     else:
#         if not my_min or my_min > num:
#             my_min = num;
#         if not my_max or my_max < num:
#             my_max = num;
# print(f"Min: {my_min}    Max: {my_max}");
#
# #______________Data Proc 3__________________
# imax: int = 0;
# my_max: int = None;
# for i in range(5):
#     my_num: int = int(input("Input a number: "));
#     if not my_max or my_num > my_max:
#         imax = i + 1;
#         my_max = my_num;
#
# print(f"Max Input at {imax} try, max value is {my_max}");
#
# #______________Data Proc 4__________________
# num1: int = int(input("num1: "));
# num2: int = int(input("num2: "));
# neg: bool = False;
# res: int = 0;
# if not num1 or not num2:
#     res = 0;
# elif num1 < 0 and num2 < 0:
#     num1 *= -1;
#     num2 *= -1;
# else:
#     if num1 < 0 or num2 < 0:
#         neg = True
#         if num1 < 0:
#             num1 *=-1
#         else:
#             num2 *=-1;
#     else:
#         neg = False;
#
# for _ in range(num2):
#     res += num1;
#
# print(f"Result: {res if not neg else -1 * res}");
#
# #______________Data Proc 5__________________
# num: int = int(input("Input a number: "));
# my_pow: int = int(input("To the power of: "));
# res: float = 1.00;
# if not num:
#     print(f"Result: {num}");
# elif not my_pow:
#     print(f"Result: {res}");
# else:
#     if my_pow < 0:
#         n: float = 1 / num;
#         my_pow *= -1;
#     else:
#         n = num;
#     for _ in range (my_pow):
#         res *= n;
#
#     print(f"Result: {res}");
#
# #______________Data Proc 6__________________
# numb: int = int(input("input a number: "));
# dig: int = int(input("Input the digit: "));
# flg: bool = False;
# tmp: int = numb;
# while tmp:
#     if tmp%10 == dig:
#         flg = True;
#
#     tmp = tmp//10;
#
# print(f"the digit {dig} is present in the number {numb}: {flg}");

#______________Data Proc 7__________________
num_a: int = int(input("Input the first number: "));
num_b: int = int(input("Input the second number: "));
min_n: int = num_a if num_b > num_a else num_b;
divisor: int = None;
neg: bool = False;

if min_n < 0:
    neg = True;
    min_n *= -1;

for i in range(1, min_n+1):
    if not num_a%i and not num_b%i:
        divisor=i;

print(f"Highest common divisor is: {divisor}");

#______________Data Proc 8__________________
p_num: int = int(input("Please Input a number: "));
prim: bool = True;

if p_num <2:
    print("Input error, please input a number larger then 1");
else:
    for i in range(2, p_num):
        if not p_num%i:
            prim = False;

    print(f"The number is primary: {prim}");
