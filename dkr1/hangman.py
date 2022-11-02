# Problem Set 2, hangman.py
# Name: Savchuk Ivan
# Collaborators: None
# Time spent: ~5 hours

# Hangman Game

import random
import string

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
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print(len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)


# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    letters_guessed = set(letters_guessed)
    for i in secret_word:
      if i not in letters_guessed:
        return False
    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    letters_guessed = set(letters_guessed)
    output = ''
    for i in secret_word:
      if i in letters_guessed:
        output += i
      else:
        output += '_'
    return output

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    alphabet = set(string.ascii_lowercase)
    for i in letters_guessed:
      alphabet.remove(i)
    return ''.join(sorted(alphabet))

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []
    sep_string = '-'*13

    print('Welcome to the game Hangman!',
          f'I am thinking of a word that is {len(secret_word)} letters long.', sep='\n')

    while guesses_remaining > 0 and not is_word_guessed(secret_word, letters_guessed):
      print(sep_string, f'You have {guesses_remaining} guesses left.',
            f'Available letters: {get_available_letters(letters_guessed)}', sep ='\n')

      warnings_raised = False
      user_input = input('Please guess a letter: ').lower()

      if len(user_input) != 1:  #this check is not in specifications, but seems necessary
        print('Oops! Wrong number of characters.', end=' ')
        warnings_raised = True
      elif not user_input in string.ascii_lowercase:
        print('Oops! That is not a valid letter.', end=' ')
        warnings_raised = True
      elif user_input in letters_guessed:
        print("Oops! You've already guessed that letter.")
        warnings_raised = True
      else:
        letters_guessed.append(user_input)
        if user_input in secret_word:
          print('Good guess:', get_guessed_word(secret_word, letters_guessed))
        else:
          if user_input in {'a', 'i', 'e', 'o', 'u'}:
            guesses_remaining -= 2
          else:
            guesses_remaining -= 1
          print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))
      if warnings_raised:
        if warnings_remaining > 0:
          warnings_remaining -= 1
          print(f'You have {warnings_remaining} warnings:', 
                get_guessed_word(secret_word, letters_guessed))
        else:
          guesses_remaining -= 1
          print('You have no warnings left so you lose one guess:',
                get_guessed_word(secret_word, letters_guessed))
    print(sep_string)
    if guesses_remaining > 0:
      print('Congratulations, you won!')
      print('Your total score for this game is:', guesses_remaining * len(set(secret_word)))
    else:
      print(f'Sorry, you ran out of guesses. The word was {secret_word}.')
    


def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    if len(my_word) != len(other_word):
      return False
    setA = set(my_word.replace('_', ''))
    if not setA.issubset(set(other_word)):
      return False
    else: 
      for i, j in zip(my_word, other_word):
        if i == '_':
          if j in setA:
            return False
        elif i != j:
          return False
    return True


def show_possible_matches(my_word):
  '''
  my_word: string with _ characters, current guess of secret word
  returns: nothing, but should print out every word in wordlist that matches my_word
            Keep in mind that in hangman when a letter is guessed, all the positions
            at which that letter occurs in the secret word are revealed.
            Therefore, the hidden letter(_ ) cannot be one of the letters in the word
            that has already been revealed.

  '''
  #this approach if flawed, because this function can't see which letters were already tested
  #so even if 'a' already yielded no matches with secret_word, this function will print words that
  #include letter 'a'. This is an architectural flaw, to fix it this function would have to take
  #letters_guessed[] as an argument and encorporate it to check if new letters required
  #for a word suggestions were already tested by user. This check can be done either in this
  #function or in match_with_gaps(). Combining guessed_word and guessed_letters into a single object
  #would work too. Or you can always say it's a feature to make the game harder.

  matching_words = []
  for i in wordlist:
    if match_with_gaps(my_word, i):
      matching_words.append(i)
  if matching_words:
    print(*matching_words)
  else:
    print('No matches found')


def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    guesses_remaining = 6
    warnings_remaining = 3
    letters_guessed = []
    sep_string = '-'*13

    print('Welcome to the game Hangman!',
          f'I am thinking of a word that is {len(secret_word)} letters long.', sep='\n')

    while guesses_remaining > 0 and not is_word_guessed(secret_word, letters_guessed):
      print(sep_string, f'You have {guesses_remaining} guesses left.',
            f'Available letters: {get_available_letters(letters_guessed)}', sep ='\n')

      warnings_raised = False
      user_input = input('Please guess a letter: ').lower()

      if len(user_input) != 1:  #this check is not in specifications, but seems necessary
        print('Oops! Wrong number of characters.', end=' ')
        warnings_raised = True
      elif user_input == '*':
        print('Possible matches are:')
        show_possible_matches(get_guessed_word(secret_word, letters_guessed))
      elif not user_input in string.ascii_lowercase:
        print('Oops! That is not a valid letter.', end=' ')
        warnings_raised = True
      elif user_input in letters_guessed:
        print("Oops! You've already guessed that letter.")
        warnings_raised = True
      else:
        letters_guessed.append(user_input)
        if user_input in secret_word:
          print('Good guess:', get_guessed_word(secret_word, letters_guessed))
        else:
          if user_input in {'a', 'i', 'e', 'o', 'u'}:
            guesses_remaining -= 2
          else:
            guesses_remaining -= 1
          print('Oops! That letter is not in my word:', get_guessed_word(secret_word, letters_guessed))
      if warnings_raised:
        if warnings_remaining > 0:
          warnings_remaining -= 1
          print(f'You have {warnings_remaining} warnings:', 
                get_guessed_word(secret_word, letters_guessed))
        else:
          guesses_remaining -= 1
          print('You have no warnings left so you lose one guess:',
                get_guessed_word(secret_word, letters_guessed))
    print(sep_string)
    if guesses_remaining > 0:
      print('Congratulations, you won!')
      print('Your total score for this game is:', guesses_remaining * len(set(secret_word)))
    else:
      print(f'Sorry, you ran out of guesses. The word was {secret_word}.')
    

if __name__ == "__main__":
    secret_word = choose_word(wordlist)
    
    # hangman(secret_word)
    hangman_with_hints(secret_word)
