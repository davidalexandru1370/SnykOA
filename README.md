# 1. Explain the difference between a stack and a queue. Provide real life examples of real-life scenarios where each of them are used appropriately.

Stack is a data structure which works on the LIFO (Last In First Out) principle meaning that the last element which was
added will be the first popped/retrieved. We can only access the top (last added) element in stack (even if some programming
languages such as Java do not obey this rule, it should be respected _[1]_). It is also worth mentioning that we can implement the Stack using different data structures such as arrays or single linked lists, each of them having different trade-offs for adding or deleting. The difference between pop and retrieve(also known as _get_) is that pop gets the top of the stack, deletes it and return the deleted element, while the retrieve only returns the top of the stack without altering the stack.

A real life application of stack is the web browser history. We can only go behind one step until there are no more pages. This
functionality can be also be seen as an undo operation. Pages are stored in stack and when we click the back button in browser, the current page is popped from the stack and the top one is displayed. When are going on a new page, the current page we are looking at is added at the top of the stack the new one is displayed. Another example of stack usage is the stack of memory addresses in the internal computer architecture: every time a function is called, the current memory address is added at the top of stack, the function executes its code and when done the program will go at the address indicated by the top of the stack. After this the top of the stack is popped.

Queue is a data structure which works on the FIFO (First In First Out)principle meaning that the first element added will be also the first element popped/retrieved from the queue. In the same manner as with stacks, we can use for internal representation of the queue different data structures such as arrays, or singly linked lists, each of them having different trade-offs for inserting and deleting.

A real life application of the queue is the load balancer of an API. When a request is coming and the server is full, the request will be placed in a queue waiting until the server can handle the request. If multiple requests arrives they will be placed in the queue in the order they land on the server. When the server can handle new requests, it will pop the request from the queue.

The difference between a Stack and a Queue is that stack is working on LIFO principle whereas the queue is working on FIFO principle.

_[1] This happens in Java because the Stack class inherits from Vector class._

---

# 2. What is the difference between an array and a linked list? Provide advantages and disadvantages of each data structure.
