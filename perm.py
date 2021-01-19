'''

(not graded)

Implement a function that returns all permutations of a given string:

>>> perm("ab")
['ab', 'ba']
>>> perm("abc")
['abc', 'bac', 'bca', 'acb', 'cab', 'cba']
>>> perm("abcd")
['abcd', 'bacd', 'bcad', 'bcda', 'acbd', 'cabd', 'cbad', 'cbda', 'acdb', 
 'cadb', 'cdab', 'cdba', 'abdc', 'badc', 'bdac', 'bdca', 'adbc', 'dabc', 
 'dbac', 'dbca', 'adcb', 'dacb', 'dcab', 'dcba']


'''

def perm(string):
    chars = list(string)
    if len(chars)== 2:
        return [chars[0]+chars[1],chars[1]+chars[0]]
    else:
        strings = perm(chars[1:])
        return [chars[0]+s for s in strings]+[s+chars[0] for s in strings]

if __name__ == '__main__':
    print(perm("abc"))
    print(perm("abcd"))

