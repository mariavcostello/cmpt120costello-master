# pi.py
# Value of Pi
def main():
    n = int(input("Enter the number of terms to use:"))

    pi = 0
    sign = 1
    for i in range(1, n * 2 + 1, 2):
        term = 4 / i * sign
        pi = pi + term
        sign = sign * -1

    print("The approximated value of pi is:", pi)
main()
