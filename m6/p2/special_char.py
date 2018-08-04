'''Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.'''
def main():
    '''Read string from the input, store it in variable str_input.'''
    str_input = input()
    str2_v = ""
    for i in str_input:
        if i in '*&^%$#@!':
            str2_v += " "
        else:
            str2_v += i
    print(str2_v)



if __name__ == "__main__":
    main()
