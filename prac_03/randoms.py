dir(str)
import random
['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']
dir(random)
random.randintrandinthelp()

import random

print(random.randint(5, 20))  # This line generates a random integer between 5 and 20 (inclusive) and prints it to the console. The smallest number that could be printed is 5, and the largest is 20
print(random.randrange(3, 10, 2))  # The smallest number that could be printed is 3, and the largest is 9. It is not possible for this line to produce a 4 because 4 is an even number.
print(random.uniform(2.5, 5.5))  # The smallest number that could be printed is 2.5, and the largest is 5.5. The output could be any decimal number between 2.5 and 5.5, with the probability of any specific number being proportional to the range of numbers.