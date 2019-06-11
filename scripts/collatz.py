def collatz(number)
{
    if number % 2 == 0:
        print(number / 2)
        num = number / 2
    else:
        print(number / 3 + 1)
        num = number / 3 + 1

    return num
}
while(collatz(input) != 1)
