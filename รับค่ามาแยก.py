print("  Summation of each digit ")
n = int(input('Enter a positive number : '))
sum = 0

while (n!=0) :
    m = n % 10;
    sum = sum + m
    n = n/10

print("Summation of each digit = %d "%sum)