# Homework14

This program aims to create GRE vocabulary test. You can get sets of word-definition and answer-option below, create a program called ‘grevocabtest.py’, and make sure to get all the conditions right.

1. Sets of data:

Question set is 
```python
{'Cacophony': 'A harsh, discordant mixture of sounds',
'Fallow': 'Inactive',
'Grovel': 'Act in an obsequious manner in order to obtain someone\'s forgiveness or favor',
'Loll': 'Sit, lie, or stand in a lazy, relaxed way',
'Plethora': 'A large or excessive amount'}
```
Answer set is 
```python
{1: ['Cacophony', 'Credulous'],
 2: ['Acerbic', 'Fallow'],
 3: ['Waft', 'Grovel'],
 4: ['Loll', 'Tawdry'],
 5: ['Prophetic', 'Plethora']}
```
2. Provide usage statement that also show all questions at once

3. Check for bad input:
- There should be 5 answers, corresponding to the number of the questions
- The answer should be only ‘a’ or ‘b’ (Should accept both lower case and upper case)

4. Provide the correct answer and check if the user gets the right answer or not

# Expected behavior
Usage statement
```python
$ ./grevocabtest.py
Usage: grevocabtest.py Choose the correct answer (A or B) for questions below...

Question# 1. Which word is corresponding to: A harsh, discordant mixture of sounds
A: Cacophony        B: Credulous

Question# 2. Which word is corresponding to: Inactive
A: Acerbic        B: Fallow

Question# 3. Which word is corresponding to: Act in an obsequious manner in order to obtain someone's forgiveness or favor
A: Waft        B: Grovel

Question# 4. Which word is corresponding to: Sit, lie, or stand in a lazy, relaxed way
A: Loll        B: Tawdry

Question# 5. Which word is corresponding to: A large or excessive amount
A: Prophetic        B: Plethora

```
Handle bad inputs
```python
$ ./grevocabtest.py aab
Please enter all 5 answers.

$ ./grevocabtest.py qwert
Please enter A[a] or B[b] for the answer.
```

Handle appropriate input
```python
$ ./grevocabtest.py ababa
Cacophony: A harsh, discordant mixture of sounds
A is a correct answer
You got this one right!

Fallow: Inactive
B is a correct answer
You got this one right!

Grovel: Act in an obsequious manner in order to obtain someone's forgiveness or favor
B is a correct answer
You missed, loser!!!

Loll: Sit, lie, or stand in a lazy, relaxed way
A is a correct answer
You missed, loser!!!

Plethora: A large or excessive amount
B is a correct answer
You missed, loser!!!

```

# test.py
You have been provide a Makefile that will run a test suit. Shown below is how it should look like after all tests pass.
```python
$ make test
pytest -v test.py
=============================== test session starts ================================
platform linux -- Python 3.7.1, pytest-4.0.2, py-1.7.0, pluggy-0.8.0 -- /rsgrps/bh_class/conda/bin/python
cachedir: .pytest_cache
rootdir: /rsgrps/bh_class/patarajarina/firstrepo, inifile:
plugins: remotedata-0.3.1, openfiles-0.3.1, doctestplus-0.2.0, arraydiff-0.3
collected 4 items

test.py::test_exists PASSED                                                  [ 25%]
test.py::test_usage PASSED                                                   [ 50%]
test.py::test_bad_input PASSED                                               [ 75%]
test.py::test_voc PASSED                                                     [100%]

============================= 4 passed in 2.81 seconds =============================
```

## Contact info.
Patarajarin Akarapipad
email: patarajarina@email.arizona.edu
