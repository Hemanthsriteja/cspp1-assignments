'''
Write a python program to read multiple lines of text input and store the input into a string.
'''

def multi_input():
    try:
        while True:
            data=input()
            if not data: break
            yield data
    except KeyboardInterrupt:
        return


def main():
    userInput = list(multi_input())

if __name__ == '__main__':
    main()
