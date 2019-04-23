#!/usr/bin/env python3
"""
Author : patarajarina
Date   : 2019-04-22
Purpose: Test for grevocabtest.py
"""

import os.path
import sys
from subprocess import getstatusoutput, getoutput
import re

voc = './grevocabtest.py'

#--------------------------------------------------
def test_exists():
    """scripts exist"""
    assert os.path.exists(voc)

#--------------------------------------------------
def test_usage():
    """usage"""
    (retval, out) = getstatusoutput(voc)
    assert retval > 0
    assert re.match("usage", out, re.IGNORECASE)

# --------------------------------------------------
def test_bad_input():
    """bad input"""
    (rv1, out1) = getstatusoutput('{} {}'.format(voc, 'aab'))
    assert rv1 > 0
    assert out1.rstrip() == 'Please enter all 5 answers.'

    (rv2, out2) = getstatusoutput('{} {}'.format(voc, 'ddddd'))
    assert rv2 > 0
    assert out2.rstrip() == 'Please enter A[a] or B[b] for the answer.'

# --------------------------------------------------
def test_voc():
    """working"""
    # aaaaa
    voc1 ="""Cacophony: A harsh, discordant mixture of sounds
A is a correct answer
You got this one right!

Fallow: Inactive
B is a correct answer
You missed, loser!!!

Grovel: Act in an obsequious manner in order to obtain someone's forgiveness or favor
B is a correct answer
You missed, loser!!!

Loll: Sit, lie, or stand in a lazy, relaxed way
A is a correct answer
You got this one right!

Plethora: A large or excessive amount
B is a correct answer
You missed, loser!!!

"""
    (rv1, out1) = getstatusoutput('{} {}'.format(voc, 'aaaaa'))
    assert rv1 == 0
    assert out1.strip() == voc1.strip()


# --------------------------------------------------
