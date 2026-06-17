# Problem Statement: Given an integer N, return the number of digits in N.


def count_digits(N):
    N1 = str(N)
    return len(N1)

N = int(input("Enter an integer: "))
print("Number of digits in", N, "is:", count_digits(N))