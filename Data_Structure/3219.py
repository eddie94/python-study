from Data_Structure.class_stack import *

def correct_bracket(bracket):

    brackets = stack()

    try:
        for letter in bracket:
            if letter == '(':
                brackets.Push(letter)
            else:
                brackets.Pop()
    except stack_pointer_exception:
        return 'bad'

    return 'good'

print(correct_bracket('))()(('))