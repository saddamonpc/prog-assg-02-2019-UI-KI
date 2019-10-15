## Author: Mohammad Saddam Mashuri
## FIle name: TP2_MohammadSaddamMashuri_1906426891_MS
##
## A Python application to count words of a text.
## Module used: matplotlib, numpy, and string

# Import matplotlib, numpy, and string module.
import matplotlib.pyplot as plt
import numpy as np
import string

###############################################################################
# START OF "PROGRAM INTRODUCTION"
###############################################################################

# Print the introduction of the software, and asks user for input
print("Create word frequency table and bar chart from a text file")
print("----------------------------------------------------------", end="")

# Ask the user for a valid text file.
while True:
    try:
        userText = input("Please enter the file name: ")
        f = open(userText, "r")     # Tries to open the file.
        break
    # Execute the following statement if file does not exist / incompatible
    except FileNotFoundError:
        print("Sorry, that file does not exist / incompatible.")

###############################################################################
# END OF "PROGRAM INTRODUCTION"
###############################################################################

###############################################################################
# START OF "OPENING FILES"
###############################################################################

# Open the wanted .txt file to be counted, and read the contents
f = open(userText, "r")             # Read user's input for selected text
text = f.read()                     # Assign user's .txt file to variable text
f.close()                           # Close the file

# Open stopWords.txt file, and read the contents
f = open("stopWords.txt", "r")      # Read stopWords.txt
stopWords = f.read()                # Assign stopWords.txt file to stopWords
f.close()                           # Close the file
stopWordsList = stopWords.split()   # Split the stopWords into a list

###############################################################################
# END OF "OPENING FILES"
###############################################################################

###############################################################################
# START OF "FILE CLEANING (remove punctuation, sorting, etc)"
###############################################################################

# Remove punctuation and lower casing all words
for punc in string.punctuation:
    text = text.replace(punc, '')   # Replace punctuation with an empty char
text = text.lower()                 # Lower case the letters
textList = text.split()             # Split the words into a list

# Remove words from textList if the word shows up in stopWordsList
cleanText = [word for word in textList if word not in stopWordsList]

# Initialize Dictionary
d = {}

# Counting number of times each word comes up in cleanText (in dictionary)
for word in cleanText:
    d[word] = d.get(word, 0) + 1

# This next bit of code reverses the key and values so they can be sorted
# using tuples
wordFreq = []                       # Initialize new list wordFreq
wordAlpha = []                      # Initialize new list wordAlpha
for word, value in d.items():
    wordFreq.append((value, word))  # Swap the value and word
wordFreq.sort(reverse = True)       # Sort from highest to lowest
wordFreq = wordFreq[0:36]           # Keep the top 36 word frequencies

###############################################################################
# END OF "FILE CLEANING (remove punctuation, sorting, etc)"
###############################################################################

###############################################################################
# START OF "36 WORDS IN FREQUENCY ORDERS IN 2 COLUMN FORMAT"
###############################################################################

print()
print("36 words in frequency order as \"(count, 'word')\" pairs\n")

# Print the top 36 counts, in format of 2 columns by frequency
for i in range(0, 36):
    if (i % 2) == 0:
        print('{:<30s}'.format\
        (str(wordFreq[i])), end="")   # Prints left column
    else:
        print('{}'.format\
        (str(wordFreq[i])), end="\n") # Prints right column

# Swap the values in the wordFreq list
wordAlpha = [(t[1], t[0]) for t in wordFreq]

# Sort the list z - a
wordAlpha.sort(reverse = True)

# Split the values in tuple list into two.
wordAlphaCount = [item[1] for item in wordAlpha]
wordAlpha = [item[0] for item in wordAlpha]

###############################################################################
# END OF "36 WORDS IN FREQUENCY ORDERS IN 2 COLUMN FORMAT"
###############################################################################

###############################################################################
# START OF "BAR CHART FOR TOP 36 WORDS IN ALPHABETICAL ORDER"
###############################################################################

# The dataset
frequency = wordAlphaCount
theWords = wordAlpha
y_pos = np.arange(36)       # Creates a list of integers from 0 - 35 to set
                            # the position of the words and length of the bars

# Creates a spacious environment for the bars
plt.figure(figsize=(14, 10))

# Create horizontal bars
plt.barh(y_pos, frequency, color="orange")

# Create names on the y-axis
plt.yticks(y_pos, theWords)

# Labels the x-axis and title
plt.xlabel('Frequency')
plt.title("Top 36 Words in Alphabetical Order (" + str(userText) + ")")

# Shows the barchart
plt.show()

###############################################################################
# END OF "BAR CHART FOR TOP 36 WORDS IN ALPHABETICAL ORDER"
###############################################################################

# Closes the program provided the user press Enter
print()
input("Please press Enter to exit ...")