#!/usr/bin/env python3
"""
Author : patarajarina
Date   : 2019-04-22
Purpose: Rock the Casbah
"""

import os
import sys


# --------------------------------------------------
def main():
    answers = sys.argv[1:]

    qset = {'Cacophony' : 'A harsh, discordant mixture of sounds',
            'Fallow' : 'Inactive',
            'Grovel' : 'Act in an obsequious manner in order to obtain someone\'s forgiveness or favor',
            'Loll' : 'Sit, lie, or stand in a lazy, relaxed way',
            'Plethora' : 'A large or excessive amount'}
    anset = {1: ['Cacophony', 'Credulous'],
            2: ['Acerbic' , 'Fallow'],
            3: ['Waft' , 'Grovel'],
            4: ['Loll' , 'Tawdry'],
            5: ['Prophetic' , 'Plethora']}


    if len(answers) != 1:
        print('Usage: {} Choose the correct answer (A or B) for questions below...\n'.format(os.path.basename(sys.argv[0])))
        for i, eachq in enumerate(qset):
            print('Question# {}. Which word is corresponding to: {}'.format(i+1, qset.get(eachq)))
            a = anset[i+1][0]
            b = anset[i+1][1]
            print('A: {}        B: {}\n'.format(a,b))
        sys.exit(1)

     
    answer = answers[0]
    if not len(answer) == 5:
        print('Please enter all 5 answers.')
        sys.exit(1)

    if 'a' not in answer.lower() and 'b' not in answer.lower():
        print('Please enter A[a] or B[b] for the answer.')
        sys.exit(1)

    for i, us_ans in enumerate(answer):
        a = anset[i+1][0]
        b = anset[i+1][1]
        
        if a in qset:
            print('{}: {}'.format(a,qset[a]))
            print('A is a correct answer')
            if us_ans.lower() == 'a':
                print('You got this one right!\n')
            else:
                print('You missed, loser!!!\n')

        elif b in qset:
            print('{}: {}'.format(b,qset[b]))
            print('B is a correct answer')
            if us_ans.lower() == 'b':
                print('You got this one right!\n')
            else:
                print('You missed, loser!!!\n')

# --------------------------------------------------
main()
