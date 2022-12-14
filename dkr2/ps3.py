# 6.0001 Problem Set 3
#
# The 6.0001 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
#
# Name          : Savchuk Ivan
# Collaborators : None
# Time spent    : ~5 hours

import math
import random
import string
import itertools

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 8
NUM_WILDCARDS = 2   #shouldn't be more than third of HAND_SIZE

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def get_frequency_dict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

def get_word_score(word:str, n):
    """
    Returns the score for a word. Assumes the word is a
    valid word.

    You may assume that the input word is always either a string of letters, 
    or the empty string "". You may not assume that the string will only contain 
    lowercase letters, so you will have to handle uppercase and mixed case strings 
    appropriately. 

	The score for a word is the product of two components:

	The first component is the sum of the points for letters in the word.
	The second component is the larger of:
            1, or
            7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
            and n is the hand length when the word was played

	Letters are scored as in Scrabble; A is worth 1, B is
	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.

    word: string
    n: int >= 0
    returns: int >= 0
    """
    if word == '':
        return 0
    score = 0
    for i in word.lower():
        if i != '*':
            score += SCRABBLE_LETTER_VALUES[i]
    return score * max(7 * len(word) - 3 * (n - len(word)), 1)


def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    
    for letter in hand.keys():
        for j in range(hand[letter]):
             print(letter, end=' ')      # print all on the same line
    print()                              # print an empty line


def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters.
    ceil(n/3) letters in the hand should be VOWELS (note,
    ceil(n/3) means the smallest integer not less than n/3).

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    global NUM_WILDCARDS
    hand={}
    num_vowels = int(math.ceil(n / 3)) - NUM_WILDCARDS
    if num_vowels < 0:
        num_vowels += NUM_WILDCARDS
        NUM_WILDCARDS = 0
        print('Invalid number of wildcards, please adjust setings.',
                'For this run number of wildcards changed to 0')
    
    for _ in range(num_vowels):
        x = random.choice(VOWELS)
        hand[x] = hand.get(x, 0) + 1
    
    for _ in range(num_vowels + NUM_WILDCARDS, n):    
        x = random.choice(CONSONANTS)
        hand[x] = hand.get(x, 0) + 1
    
    hand['*'] = NUM_WILDCARDS
    
    return hand


def update_hand(hand, word):
    """
    Does NOT assume that hand contains every letter in word at least as
    many times as the letter appears in word. Letters in word that don't
    appear in hand should be ignored. Letters that appear in word more times
    than in hand should never result in a negative count; instead, set the
    count in the returned hand to 0 (or remove the letter from the
    dictionary, depending on how your code is structured). 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    new_hand = hand.copy()
    for letter in word.lower():
        if letter in new_hand.keys():
            new_hand[letter] -= 1
    new_hand = {key: value for key, value in new_hand.items() if value > 0}
    return new_hand


def is_valid_word(word:str, hand, word_list):
    """
    Returns True if word is in the word_list and is entirely
    composed of letters in the hand. Otherwise, returns False.
    Does not mutate hand or word_list.
   
    word: string
    hand: dictionary (string -> int)
    word_list: list of lowercase strings
    returns: boolean
    """
    word = word.lower()
    word_letters = get_frequency_dict(word)
    for key in word_letters.keys():
        if word_letters[key] > hand.get(key, 0):
            return False
    for i in itertools.permutations(VOWELS, word.count('*')):   #acounts for multiple wildcards
        possible_word = word
        for j in i:
            possible_word = possible_word.replace('*', j, 1)
        if possible_word in word_list:
            return True
    return word.lower() in word_list


def calculate_handlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    return sum(hand.values())


def play_hand(hand, word_list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * When any word is entered (valid or invalid), it uses up letters
      from the hand.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.

    * The sum of the word scores is displayed when the hand finishes.

    * The hand finishes when there are no more unused letters.
      The user can also finish playing the hand by inputing two 
      exclamation points (the string '!!') instead of a word.

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
      returns: the total score for the hand
      
    """

    total_score = 0
    user_input = ''
    while calculate_handlen(hand):
        print('Current hand: ', end='')
        display_hand(hand)
        user_input = input('Enter word, or "!!" to indicate that you are finished: ')
        if user_input == '!!':
            break
        if is_valid_word(user_input, hand, word_list):
            word_score = get_word_score(user_input, calculate_handlen(hand))
            total_score += word_score
            print(f'"{user_input}" earned {word_score} points. Total: {total_score} points')
        else:
            print('That is not a valid word. Please choose another word.')
        hand = update_hand(hand, user_input)
        print()
    else:
        print('Ran out of letters')
    print('Total score for this hand:', total_score)
    print('-'*10)
    return total_score

def substitute_hand(hand:dict, letter):
    """ 
    Allow the user to replace all copies of one letter in the hand (chosen by user)
    with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
    should be different from user's choice, and should not be any of the letters
    already in the hand.

    If user provide a letter not in the hand, the hand should be the same.

    Has no side effects: does not mutate hand.

    For example:
        substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
    might return:
        {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
    The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
    already in the hand.
    
    hand: dictionary (string -> int)
    letter: string
    returns: dictionary (string -> int)
    """
    if letter not in hand:
        return hand
    new_hand = hand.copy()
    replacements = string.ascii_lowercase
    for i in hand.keys():
        replacements = replacements.replace(i, '')
    try:
        i = random.choice(replacements)
    except IndexError:  #if hand has all possible letters, there's nothing to replace with
        print('Nothing to replace with')
        return hand
    new_hand[i] = hand[letter]
    del new_hand[letter]
    return new_hand
    
    
def play_game(word_list):
    """
    Allow the user to play a series of hands

    * Asks the user to input a total number of hands

    * Accumulates the score for each hand into a total score for the 
      entire series
 
    * For each hand, before playing, ask the user if they want to substitute
      one letter for another. If the user inputs 'yes', prompt them for their
      desired letter. This can only be done once during the game. Once the
      substitue option is used, the user should not be asked if they want to
      substitute letters in the future.

    * For each hand, ask the user if they would like to replay the hand.
      If the user inputs 'yes', they will replay the hand and keep 
      the better of the two scores for that hand.  This can only be done once 
      during the game. Once the replay option is used, the user should not
      be asked if they want to replay future hands. Replaying the hand does
      not count as one of the total number of hands the user initially
      wanted to play.

            * Note: if you replay a hand, you do not get the option to substitute
                    a letter - you must play whatever hand you just had.
      
    * Returns the total score for the series of hands

    word_list: list of lowercase strings
    """
    while True:
        try:
            hands_left = int(input('Enter total number of hands: '))
            if hands_left <= 0:
                print('Number must be >=1, please try again!')
                continue
            break
        except ValueError:  #verifying appropriate hands count
            print("Sorry, couldn't convert to a number, try again!")
            continue
    substitutions_left = 1
    replays_left = 1
    total_score = 0
    while hands_left > 0:
        current_hand = deal_hand(HAND_SIZE)
        if substitutions_left:
            print('Current hand: ', end='')
            display_hand(current_hand)
            while True:
                user_input = input('Would you like to substitute a letter? ').lower()   #acepts only yes/no answers
                if user_input == 'yes':
                    while True:
                        letter = input('Which letter would you like to replace: ')
                        if letter.lower() in string.ascii_lowercase:    #wildcards can't be replaced
                            break
                        print("That's not a letter, please try again")
                    current_hand = substitute_hand(current_hand, letter)
                    substitutions_left -= 1
                    break
                if user_input == 'no':
                    break
                print("I didn't get that, please answer yes or no.")
            print()
        hand_score = play_hand(current_hand, word_list)
        if replays_left:
            while True:
                user_input = input('Would you like to replay the hand? ').lower()    #acepts only yes/no answers
                if user_input == 'yes':
                    replays_left -= 1
                    hand_score = max(play_hand(current_hand, word_list), hand_score)
                    break
                if user_input == 'no':
                    break
                print("I didn't get that, please answer yes or no.")
        total_score += hand_score
        hands_left -= 1
    print('Total score over all hands:', total_score)


if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)
