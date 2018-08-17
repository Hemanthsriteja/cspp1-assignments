'''
    Document Distance - A detailed description is given in the PDF
'''
import math
FILE_NAME = "stopwords.txt"
def similarity(dict_1, dict_2):
    '''
        Compute the document distance as given in the PDF
    '''
    list1_v = ""
    list2_v = ""
    for i in dict_1:
        if i not in '!@#$%^&*()_+-=,.?1234567890':
            if i not in"'":
                list1_v += i
    for i in dict_2:
        if i not in '!@#$%^&*()_+-=,.?1234567890':
            if i not in "'":
                list2_v += i
    list1_v = list1_v.split()
    list2_v = list2_v.split()
    list3_v = list1_v + list2_v
    a_dict = {}
    for word in list3_v:
        if word not in load_stopwords(FILE_NAME).keys():
            a_dict[word] = (list1_v.count(word), list2_v.count(word))
    numerator, add_1, add_2 = 0, 0, 0
    for a_check in a_dict:
        numerator += a_dict[a_check][0]*a_dict[a_check][1]
        add_1 += a_dict[a_check][0] ** 2
        add_2 += a_dict[a_check][1] ** 2
        denominator = math.sqrt(add_1) * math.sqrt(add_2)
    value_check = numerator/denominator
    return value_check
def load_stopwords(filename):
    '''
        loads stop words from a file and returns a dictionary
    '''
    stopwords = {}
    with open(filename, 'r') as filename:
        for line in filename:
            stopwords[line.strip()] = 0
    return stopwords

def main():
    '''
        take two inputs and call the similarity function
    '''
    input1 = input().lower()
    input2 = input().lower()
    print(similarity(input1, input2))

if __name__ == '__main__':
    main()
