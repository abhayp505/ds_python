
queue=[]

def push(data):
    if data is None:
        return
    else:
        queue.append(data)

def pop():
    element = queue[0]
    queue.pop(0)
    return element

def length():
    return len(queue)

def queues():
    return queue