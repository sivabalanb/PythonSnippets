# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

from itertools import combinations
from itertools import combinations_with_replacement


def generateParenthesis(n):
    def generate(p, left, right, parens=[]):
        if left:
            generate(p + '(', left-1, right)
        if right > left:
            generate(p + ')', left, right-1)
        if not right:
            parens += p,
        return parens
    return generate('', n, n)


print(generateParenthesis(3))
