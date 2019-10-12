# Programming Assignment 02 from Universitas Indonesia [KI]

For future references and education purposes only.
Use wisely.

# Task Description
## Purpose
This assignment will give you useful experience with functions, strings, lists, text processing, and file I/O. You will also learn to use plotting module matplotlib and the numeric module numpy.

## Problem
A common text processing application needs word frequencies of a document. More frequent words are considered more important.
You are going to analyze a text document given by the user and create a table and a bar chart of word frequencies for it.

## Stop Words
Not all words are worth counting. 'a', 'the', 'was', 'and', etc. are just junk. A list of such words is provided in the file **'stopWords.txt'**. Each line has a single word. No word in the stop word list should be counted in the final word frequencies table or chart.

## Background
You are provided with a number of elements to help with this assignment:
- text documents for processing: CommencementSpeechByGates2014.txt, JokoWidodoSpeechAPEC2014.txt
- a file containing stop words
- an example of using matplotlib and numpy.

## Program Specification
- Prompt the user for the name of the text file to be processed.
- Print the top 36 counts (word and count pairs), in the format of 2 columns. Sort the words **by count (frequency)** for printing. (For the next step you will sort the words **alphabetically** for the bar chart.)
- Generate a **horizontal bar chart** for the top 36, which are sorted alphabetically. The bar chart looks more interesting that way.

## Hints:
There are a couple of problems here. Think about each one before you start to program:
1. You have to read in the file and separate the contents into words.
2. Once you have the words separated, you must remove all stop words (using the provided file "stopWords.txt"). Also, remember to **remove punctuation** from words, just because a word comes at the end of a sentence and has a period at the end of it doesn't make it a different word. (Importing *string* and using *string.punctuation* is a useful way to specify punctuation.)
3. You must then count the frequency of each word collected. YOu may use the **list** data structure or the **dictionary** data structure.
4. Once you have a complete list, sort the list. Put count first in the tuple because sorting (using either *sort* or *sorted*) will sort on the first item.
5. Use the module matplotlib for creating a bar chart.
6. Define your own functions as needed.

## For more information, see *assg02_fprog2019.pdf* inside the *Specifications and Files* folder.
