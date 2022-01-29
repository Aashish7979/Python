def RecurFactorial(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * RecurFactorial(num - 1)



output = RecurFactorial(int(input("Enter any number: ")))
print("Factorial : ", output)

# S1: 5! = 5 * 4!
# S2: 4! = 4 * 3!
# S3: 3! = 3 * 2!
# S4: 2! = 2 * 1!
# S5: 1! = 1