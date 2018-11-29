import mystack



def check(x):
    brackets = {"<":">","(":")","[":"]"}

    stack = mystack.mystack()
    for element in x:
        if element in brackets.keys():
            stack.push(element)
        elif element in brackets.values():
            if stack.peek() != None:
                if element == brackets[stack.peek()]:
                    stack.pop()
                else:
                    print("found " + element + " in string, and " + stack.peek() + " on the stack")
                    return False       
            else:
                return False
        else:
            print("invalid list")
            return False
    if stack.isEmpty() == False:
        return False
    return True


hahah = "(()"
print(check(hahah))