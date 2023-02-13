# -*- coding: utf-8 -*-
"""
Created on Thu Jan 26 07:50:25 2023
@author: krzeczyca
"""

import string
import random

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print ("This is not a number!")


def generate_password(length=8, chars=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for i in range(length))


if __name__ =="__main__":
    file = input("What file name? ")
    much = input_int("How many password to generate? ")
    long = input_int("How long do you want the string to be?  ")  
    with open(file, 'x', encoding="utf-8") as f:
        for i in range(much):
            f.write(str(i+1)+". "+generate_password(long)+"\n")
    print("The results have been saved to a file",file)
    
    
    #print(generate_password(15))
