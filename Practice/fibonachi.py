# To print Fibonacci series up to n terms

def fibonacci(n):
    a, b = 0, 1
    i = 0
    for i in range(n):
        print(a)
        a , b = b , a+b
        i += 1

def main():
    n = int(input("Enter Number of Terms you want: "))
    fibonacci(n)

if __name__ == "__main__":
    main()