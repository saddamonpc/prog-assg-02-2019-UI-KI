## Author: Mohammad Saddam Mashuri
## FIle name: TP2_MohammadSaddamMashuri_1906426891_MS
##
## A Python application to count words of a text.
## Module used: matplotlib, numpy, and string

# Import matplotlib, numpy, and string module.
import matplotlib.pyplot as plt
import numpy as np
import string

# Print the introduction of the software, and asks user for input
print("Create word frequency table and bar chart from a text file")
print("----------------------------------------------------------", end="")

# Ask the user for a valid text file.
while True:
    try:
        userText = input("Please enter the file name: ")
        f = open(userText, "r")     # Tries to open the file.
        break
    except FileNotFoundError:       # Print the following statement if file does not exist / incompatible
        print("Sorry, that file does not exist / incompatible.")
        
print()
print("36 words in frequency order as \"(count, 'word')\" pairs\n")

# Open the wanted .txt file to be counted, and read the contents
f = open(userText, "r")
text = f.read()                     # Assign the .txt file to variable 'text'
f.close()

# Open stopWords.txt file, and read the contents
f = open("stopWords.txt", "r")
stopWords = f.read()                # Assign the .txt file to variable 'stopWords'
f.close()
stopWordsList = stopWords.split()   # Split the words into a list

# Remove punctuation and lower casing all words
for punc in string.punctuation:
    text = text.replace(punc, '') # Take the punctuation character and replace with an empty space
text = text.lower()                 # Lower case the letters
textList = text.split()             # Split the words into a list

# Filter out stopWords
cleanText = [word for word in textList if word not in stopWordsList]
cleanText.sort()

# Initializing Dictionary
d = {}

# Counting number of times each word comes up in cleanText (in dictionary)
for word in cleanText:
    d[word] = d.get(word, 0) + 1

# This next bit of code reverses the key and values so they can be sorted
# using tuples
wordFreq = []
wordAlpha = []
for word, value in d.items():
    wordFreq.append((value, word))
wordFreq.sort(reverse = True)       # Sort from highest to lowest
wordFreq = wordFreq[0:36]           # Keep the top 36 word frequencies

# Print the top 36 counts, in format of 2 columns by frequency
for i in range(0, 36):
    if (i % 2) == 0:
        print('{:<30s}'.format(str(wordFreq[i])), end="")   # Prints left column
    else:
        print('{}'.format(str(wordFreq[i])), end="\n")      # Prints right column

# Swap the values in the wordFreq list
wordAlpha = [(t[1], t[0]) for t in wordFreq]
# Sort the list z - a
wordAlpha.sort(reverse = True)

# Split the values in tuple list into two.
wordAlphaCount = [item[1] for item in wordAlpha]
wordAlpha = [item[0] for item in wordAlpha]

### THE MAKING OF BARCHART ###
# The dataset
frequency = wordAlphaCount
theWords = wordAlpha
y_pos = np.arange(36)

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
### END OF THE MAKING OF BARCHART ###

# Closes the program provided the user press Enter
print()
input("Please press Enter to exit ...")