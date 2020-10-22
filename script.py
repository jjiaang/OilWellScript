import os
import sys
from tkinter import filedialog
from tkinter import*

"""
Code created by Jason Jiang. 2020-10-21
"""

"""
This function gets the user input from a tkinter GUI, the following GUI allows the user to upload from any directory they wish
"""

def getUserInput():
    fileName = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("txt files", "*.txt"),("all files", "*.*")))
    return fileName

"""
This function allows the user to specify what they would like to name the output file, and it will create a new output file
"""

def specifyOutputFile():
    print("Enter the name of the output file, this will create a new file. Remember to use .txt at the end.")
    outputFile = input()
    f = open(outputFile, "x")

    return outputFile

"""
The function takes in an input file and a output file, the resulting function outputs a output file.
For this, since we are given the file in the form
stage depthEnd depthStart

We would like to get it in the form
depthStart          Stage       Stage
depthStart + 1      Stage       Stage
. . .
depthStart + n      Stage       Stage

We can allow each line to be condensed into a two dimensional array.

We then iterate through the 2d array, and then calculate the difference between start and end at each individual index, ranging from 0,1,..,n

Then we do another for loop to iterate through and append the Stage + depthStart + j, where j is the amount of iterations from the max depth to min depth

We would also like to add the stage to where it is the middle between the difference, so (end - start) / 2.

Therefore, the array new will have the form [[Stage,depthStart], [Stage,depthStart + 1], ... , [Stage, depthStart + n]]
"""
def fileReadWrite(inputFile,outputFile):

    new = []

    with open(inputFile, 'r') as f:
        text = [line.split() for line in f]

    text = [[int(n) for n in row] for row in text]
    text = sorted(text, key=lambda x: x[2])

    for i in range(len(text)):
        diff = text[i][1] - text[i][2]

        for j in range(diff):
            if j == (diff / 2):
                new.append([text[i][0], text[i][2] + j, text[i][0]])
            else:
                new.append([text[i][0], text[i][2] + j])

    """
    Here is where we write to the new file. We would want to avoid list index out of range here in this situation.

    In this case, our first column would be the depth (in ft), and our second column is the stage, and if it suffices in the situation, our third column is stage as well.
    """

    with open(outputFile, 'w') as f:
        for item in new:
            if len(item) < 3:
                f.write("%s\n" % (str(item[1]) + " " + str(item[0])))
            else:
                f.write("%s\n" % (str(item[1]) + " " + str(item[0]) + " " + str(item[0])))

def main():
    inputFile = getUserInput()
    outputFile = specifyOutputFile()
    fileReadWrite(inputFile,outputFile)


main()