'''Exercise: Assignment-4
#We are now ready to begin writing the code that interacts with the player.
We'll be implementing the playHand function. This function allows the user to
play out a single hand. First, though, you'll need to implement the helper
calculateHandlen function, which can be done in under five lines of code.'''


def calculate_hand_len(hand):
    """
    Returns the length (number of letters) in the current hand.
    hand: dictionary (string int)
    returns: integer
    """
    sum_v = 0
    for letters in hand:
        sum_v = sum_v + hand[letters]
    return sum_v

def main():
    '''func defined'''
    n_v = input()
    adict = {}
    for _ in range(int(n_v)):
        data = input()
        l_v = data.split()
        adict[l_v[0]] = int(l_v[1])
    print(calculate_hand_len(adict))
if __name__ == "__main__":
    main()

