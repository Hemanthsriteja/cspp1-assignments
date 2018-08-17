'''Exercise: Assignment-2'''
#Implement the updateHand function. Make sure this function has no side effects: i.e.,

#it must not mutate the hand passed in. Before pasting your function definition here,
#be sure you've passed the appropriate tests in test_ps4a.py.

def update_hand(hand_v, word_v):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it.
    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.
    word: string
    hand: dictionary (string -> int)
    returns: dictionary (string -> int)
    """
    a_v = {}
    for j in word_v:
        if j in hand_v:
            a_v[j] = hand_v[j]-1
    return a_v
def main():
    '''main'''
    n_v = input()
    a_dict = {}
    for _ in range(int(n_v)):
        data = input()
        l_v = data.split()
        a_dict[l_v[0]] = int(l_v[1])
    data1_v = input()
    print(update_hand(a_dict, data1_v))
if __name__ == "__main__":
    main()
