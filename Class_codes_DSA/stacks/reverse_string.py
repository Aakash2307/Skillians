def reverse_string(s):
    stack = []

    reverstring =' '

    for char in s :
        stack.append(char)
    for i in range(len(stack)):
        reverstring += stack.pop()

    return reverstring


s = "stupid"

print(reverse_string(s))


    

