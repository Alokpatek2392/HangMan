# 
# Hangman game
#

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    #
    #
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
    False otherwise
    '''
    count=0
    for a in secretWord:
        if(a in lettersGuessed):
            count+=1
        else:
            return False
    if(count==len(secretWord)):
        return True
    else:
        return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
    what letters in secretWord have been guessed so far.
    '''
    count=0
    temp=''
    for _ in secretWord:
        if (_ in lettersGuessed):
           count+=1 
           temp= temp + _
        else:
            temp=temp + '_' + ' '
    return temp

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
    yet been guessed.
    '''
    alphabets=string.ascii_lowercase
    for char in lettersGuessed:
        if(char in alphabets):
            alphabets=alphabets.replace(char,"")
    return alphabets
    

def hangman(secretWord):
    print('Welcome to the game Hangman!')
    secretWord = secretWord.lower()
    length=len(secretWord)
    guessLeft=8
    lettersGuessed=[]
    correctLetters=[]
    wrongLetters=[]
    #print(lettersGuessed)
    print('I am thinking of a word that is %d letters long.' % length)
    while(guessLeft>0):
        print('-------------')
        check=isWordGuessed(secretWord, lettersGuessed)
        if(check==True):
            print('Congratulations, you won!')
            break
        print('You have %d guesses left.' % guessLeft)
        alphabets=getAvailableLetters(lettersGuessed)
        print('Available letters: %s' % alphabets)
        guess=raw_input('Please guess a letter: ')
        guess=guess.lower()
        #print(guess)
        lettersGuessed.append(guess)

        #print(lettersGuessed)
        if(len(guess)==1):
            if(guess in secretWord):
                if(guess in correctLetters):
                    #print(lettersGuessed)
                    wordDisplay=getGuessedWord(secretWord, lettersGuessed)
                    print("Oops! You've already guessed that letter: %s" % wordDisplay)
                else:
                    #print(lettersGuessed)
                    wordDisplay=getGuessedWord(secretWord, lettersGuessed)
                    print("Good guess: %s" % wordDisplay)
                    correctLetters.append(guess)
            else:
                if(guess in wrongLetters):
                    wordDisplay=getGuessedWord(secretWord, lettersGuessed)
                    print("Oops! You've already guessed that letter: %s" % wordDisplay)
                    
                else:
                    #print(lettersGuessed)
                    wordDisplay=getGuessedWord(secretWord, lettersGuessed)
                    print('Oops! That letter is not in my word: %s' % wordDisplay)
                    wrongLetters.append(guess)
                    guessLeft-=1     
                
    check=isWordGuessed(secretWord, lettersGuessed)
    if(check==False):
        print('-----------')
        print('Sorry, you ran out of guesses. The word was %s' % secretWord)
    


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
