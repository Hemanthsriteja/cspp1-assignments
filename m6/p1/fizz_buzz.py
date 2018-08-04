'''
Write a short program that prints each number from 1 to num on a new line.
For each multiple of 3, print "Fizz" instead of the number.
For each multiple of 5, print "Buzz" instead of the number.
For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
'''
def main():
    '''Read number from the input, store it in variable num.'''
    num = int(input())
    str = "FizzBuzz"
    for i in range(1,num+1):
        for i in range(1,num+1,2):
            print("Fizz")
        for i in range(1,num+1,4):
            print("Buzz")
        for i in range(1,num+1,14):
            print("FizzBuzz")




if __name__ == "__main__":
    main()
