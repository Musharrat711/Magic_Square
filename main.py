import Even_Magic_Sqaure_Not_div_by4
import Even_Magic_Square_divisible_by_4
import Magic_Square_1

num = int(input("Input a number to print its magic square: "))

if num%2 != 0:
    Magic_Square_1.Odd_Magic_Square(num)
else:
    if num%4 == 0:
        Even_Magic_Square_divisible_by_4.Even_magic_div4(num)
    else:
        Even_Magic_Sqaure_Not_div_by4.Magic_Not_div4(num)

