# Assignment-3
'''
At this point, we have written code to generate a random hand and display
that hand to the user. We can also ask the user for a word (Python's input)
and score the word (using your getWordScore). However, at this point we have
not written any code to verify that a word given by a player obeys the rules
of the game. A valid word is in the word list; and it is composed entirely
of letters from the current hand. Implement the isValidWord function.

Testing: Make sure the test_isValidWord tests pass. In addition, you
will want to test your implementation by calling it multiple times on
the same hand - what should the correct behavior be? Additionally, the
empty string ('') is not a valid word - if you code this function correctly,
you shouldn't need an additional check for this condition.

Fill in the code for isValidWord in ps4a.py and be sure you've passed
the appropriate tests in test_ps4a.py before pasting your function definition here.
'''

def is_valid_word(word_v, hand_v, wordlist_v):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or wordList.
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    c_v = 0
    l_v = len(wordlist_v)
    if word_v in wordlist_v:
        for i in hand_v:
            if i in word_v:
                c_v = c_v+1
    if c_v == l_v:
        return True
    return False
def main():
    '''func'''
    word_v = input()
    n_v = int(input())
    adict = {}
    for _ in range(n_v):
        data = input()
        l_v = data.split()
        adict[l_v[0]] = int(l_v[1])
    l2_v = list(input().split())
    print(is_valid_word(word_v, adict, l2_v))
if __name__ == "__main__":
    main()
