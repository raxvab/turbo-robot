#Author: @raxvab
#Here's a basic implementation of a stack and queue using a linked list in an object-oriented style,
#So like, I'm making a Node here for the stack thingy
class Node:
    def __init__(self, data):
        self.data = data  # This stores the actual value
        self.next = None  # And this is the thing that points to the next Node


# Now, let's do the stack part... I think it should be called Stack, duh
class Stack:
    def __init__(self):
        self.top = None  # Top is like, the most recent item, I think

    # So this is the push thingy, it adds stuff to the stack
    def push(self, data):
        new_node = Node(data)  # Make a new thing with data
        new_node.next = self.top  # Make it point to the old top
        self.top = new_node  # Now this new thing is the top
        print(f"Pushed {data} to stack")

    # This should remove the top thing from the stack (I hope it works)
    def pop(self):
        if self.top is None:  # Uh oh, there's nothing to pop!
            print("Stack is empty, nothing to pop")
            return None
        popped_node = self.top  # Let's grab the top thingy
        self.top = self.top.next  # Now the new top is the one under it
        print(f"Popped {popped_node.data} from stack")
        return popped_node.data  # Here's the data that was on top

    # This shows what's on top without removing it (like a sneak peek)
    def peek(self):
        if self.top is None:  # If it's empty, just say so
            print("Stack is empty, nothing to peek")
            return None
        print(f"Top of the stack is {self.top.data}")
        return self.top.data

    # This checks if the stack is totally empty
    def is_empty(self):
        return self.top is None


#For basic Runs refer to below TC
# stack = Stack()
# stack.push(10)
# stack.push(20)
# stack.push(30)

# print(stack.peek())  # Should output 30
# print(stack.pop())   # Should remove and output 30
# print(stack.pop())   # Should remove and output 20
# print(stack.is_empty())  # Should return False

#Do Follow if you like my code
