from linked_list import *

# a Stack is Stack(list)
class Stack:
    def __init__(self, l):
        self.l = l
    def __eq__(self, other):
        return(type(other) == Stack
            and self.l == other.l)
    def __repr__(self):
        return "Stack({!r})".format(self.l)

# None -> Stack
# returns an empty stack
def empty_stack():
    return Stack(empty_list())

# Stack value -> Stack
# pushes a value to a stack and returns the new stack
def push(stack, value):
    if(stack.l == empty_list()):
        stack.l = add(empty_list(), 0, value)
        return stack
    else:
        stack.l = add(stack.l, length(stack.l), value)
        return stack

# Stack -> Stack
# returns a 2-tuple containing the removed value and the resulting stack
def pop(stack):
    if(stack.l == None):
        raise IndexError()
    else:
        temp = remove(stack.l, length(stack.l) - 1)
        stack.l = temp[1]
        return (temp[0], stack)

# Stack -> value
# returns the top element from the stack
def peek(stack):
    if(stack.l == None):
        raise IndexError()
    else:
        return get(stack.l, length(stack.l) - 1)

# Stack -> integer
# returns the size of the stack
def size(stack):
    return length(stack.l)

# Stack -> boolean
# returns True if the stack is empty
def is_empty(stack):
    if(stack.l == empty_list()):
        return True
    else:
        return False
