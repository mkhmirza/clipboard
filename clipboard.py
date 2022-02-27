#!/usr/bin/python env


import pyperclip as pc
import argparse

#TODO:
# 1. copy line starting with a character 
# 2. copy line containing a character
# 3. read from standard input

parser = argparse.ArgumentParser(description="Copy text to clipboard")
parser.add_argument("-f", "--file", help="text file to copy")
parser.add_argument("-t", "--text", help="text to copy to clipboar")
args = vars(parser.parse_args())

f = args['file']
t = args['text']

if f:
    with open(f, "r") as f:
        data = f.readlines()

    pc.copy(''.join(data))
if t:
    pc.copy(t)
print("Text copied to clipboard")
