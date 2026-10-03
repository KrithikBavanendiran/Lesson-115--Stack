from sys import maxsize
def create_stack():
    stack=[]
    return stack

def isEmpty(stack):
    return len(stack)==0

def push(stack, item):
    stack.append(item)
    print("New item added: ", item)

def pop(stack):
    if isEmpty(stack):
        return str(-maxsize-1)
    else:
        return stack.pop()
    
def peek(stack):
    if isEmpty(stack):
        return str(-maxsize-1)
    else:
        return stack[len(stack)-1]
    
    
s=create_stack()
push(s, str(10))
push(s, str(20))
push(s, str(30))
print("Item popped: ", pop(s))
print("Item popped: ", pop(s))
print("Item popped: ", pop(s))
print("Item popped: ", pop(s))