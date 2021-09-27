# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]

# def generateParenthesis(n):
#     def generate(p, left, right, parens=[]):
#         if left:
#             generate(p + '(', left-1, right)
#         if right > left:
#             generate(p + ')', left, right-1)
#         if not right:
#             parens += p,
#         return parens
#     return generate('', n, n)


# print(generateParenthesis(3))

def generateParenthesis(n):
    stack = []
    res = []

    def backtrack(openN, closedN):
        print(f"res {res} openN {openN} closedN {closedN} stack {stack}")
        if openN == closedN == n:
            res.append("".join(stack))
            return
        if openN < n:
            stack.append("(")
            backtrack(openN + 1, closedN)
            stack.pop()
            print("pop open paran", stack)
        if closedN < openN:
            stack.append(")")
            backtrack(openN, closedN + 1)
            stack.pop()
            print("pop closed paran", stack)
    backtrack(0, 0)

    return res


print(generateParenthesis(3))
