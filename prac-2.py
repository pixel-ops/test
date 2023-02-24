stack = []
result = []

def generate_praen(myopen,myclose,n):
    if myopen == myclose == n:
        result.append("".join(stack))
        return
    if myopen < n:
        stack.append('(')
        generate_praen(myopen + 1,myclose,n)
        stack.pop()
    if myclose < myopen:
        stack.append(')')
        generate_praen(myopen,myclose + 1,n)
        stack.pop()
    return result

print(generate_praen(0,0,3))