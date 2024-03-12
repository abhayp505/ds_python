
stackk=[]

def push(data):
    if data is None:
        return
    else:
        stackk.append(data)
        stackk
    return data

def pop():
    # if length() >=0:
    #     element = stackk[length()-1]
    #     stackk.pop(length()-1)
    #     return element
    # else:
    #     return "stack empty"
    try:
        element = stackk[length()-1]
        stackk.pop(length()-1)
        return element
    except IndexError:
        return IndexError

def length():
    size = len(stackk)
    return size

def stacks():
    return stackk