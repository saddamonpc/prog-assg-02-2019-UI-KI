## Author: Mohammad Saddam Mashuri
## FIle name: TP2_MohammadSaddamMashuri_1906426891_MS
##
## A Python application to count words of a text.
## Module used: matplotlib & numpy

# Import matplotlib & numpy module.
import matplotlib.pyplot as plt
import numpy as np

## EXAMPLE FROM PDF
#words = ['Python', 'C/C++', 'Java', 'Haskell', 'Prolog', 'Lisp']
#y_pos = np.arange(len(words))
#usage = [10, 8, 6, 4, 2, 3]
#barWidth = 0.6
#plt.barh(y_pos, usage, barWidth, color='r')
#plt.yticks(y_pos, words)
#plt.xlabel('Usage')
#plt.title('Programming language usage')
#plt.show()

barWidth = 0.4
plt.barh(y_pos, frequency, barWidth, color='o') # EDIT THIS AGAIN
plt.xlabel('Frequency')
plt.title('Top 36 Words in Alphabetical Order')
plt.show()