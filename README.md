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

Linked list and arrays are two different data structures with advantages and disadvanteges. The differences between these two data structures are:

- Array use linear memory (the length is the size of array) and hence we can access much faster elements at a given index. This works fine for fixed sized arrays, but in case we want to increase the number of elements in the array we have to allocate another slot of memory to fit our new desired size of array and copy the already existing data.

- Linked lists use dynamic allocation on the heap memory and we can create new nodes faster without (at first glance) caring about the size of the list. This might lead to a phenomena called _fragmentation of memory_ meaning the memory allocated to our application is fragmented and the operating system will require more time to allocate other resources in the future.

- In an array we can access elements at given index fast, in a complexity of O(1). This is not possible in a linked list and to access an element at a given index we have to traverse all the list resulting a worst case complexity of O(n) where n is the number the elements in the list.

- Deletion of an element works faster in a linked list because to delete an element we have to link the neighbours of that element (the previous and the next one). In an array to delete an element from a given index we have to move all elements after our desired index one position to the left.

## Advantages of array

- Getting an element at given index works very fast since we know the memory address of that element since array have contiguous memory.

- Adding a new element when we do not have to increase the size of the array can be done fast enough in O(1) time.

## Disadvanteges of array

- Adding an element can be both an advantage and a disadvantage, because when the array is full and we need to resize it, we have to allocate another zone of memory, copy the existing data and then add the new element and delete the old memory zone to avoid any memory leak. There are multiple ways/policies of how to allocate a new memory zone, increase the size by one, by a power two or doubling the size each time. This can be also a disadvantage because increasing the size with a small number will lead to very slow add operation since everytime we have to resize the array, but on the other hand, it is not often good to allocate to much memory because it can lead to unused memory.

- Deleting an element is done in worst case in a O(n) complexity, because we need to move all the elements after that position one position to the left of the array.

- Adding at a certain index (also known as inserting) is not an efficient operation because, like in case of delete, but this time we have to move all the element after our desired index one position to the right of the array, hence a worst case complexity of O(n).

## Advanteges of linked list

- Adding a new element to the end or begging of the linked list is done fast, in O(1) complexity, because we only allocate the new node on the heap and link it with head/tail of the linked list.

- Deleting an element have similar complexity with deleting an element from an array, O(n) in worst case. The complexity comes from the fact that we have to traverse until that node, because the actual delete operation works in O(1) since we only have to link the neighbours of that node and deallocate to the desired one to avoid memory leaks.

## Disadvanteges of linked list

- Too many elements in a linked list can lead to a phenomena _fragmentation of the memory_ meaning the operating system will need more time to allocate memory when creating a new object.

- Accessing an element is not as fast as in the array, because we have to traverse the list until that index, resulting a worst case complexity of O(n).

- Inserting an element given index is not so fast if we do not know the current existing element at that index (otherwise it could be an advantage, because inserting would be an O(1) complexity). This can lead to a worst case complexity of O(n) since we have to traverse the entire list.

# 3. What is HTTP? How is it different from HTTPS?

HTTP is the acronym for HyperText-Transfer-Protocol and it is a communication protocol for networks. It is also worth mentioning that is found at the application layer in the OSI model of network stack. An http request might be composed of header, body. The header of the request contains key value pairs such as Authorization for authenticating an user, Content-type like JSON, multiform/data, the verb of the request(GET, POST, PUT, DELETE, PATCH) and many more. The body contains data we want to send to the client (this do not apply to all the verbs since GET does not support body). The only problem with this protocol is that is not securely encrypted and someone can steal the data if the request is intercepted until the client. To solve this problem HTTPS (HyperText Transfer Protocol Secured) solved this problem using crytographic algorithms to encrypt and decrypt data. So HTTP is different from HTTPS in the way that it does not encrypt and decrypt the data for better security of requests.

# 4. Can you give some examples of common HTTP response codes?

The HTTP status codes can be split in 5 major categories such as:

- 1XX - Status codes for informational responses.

- 2XX - Status codes for success responses. In this category we can talk about the 200 status codes for Ok, 201 for Created when an entity is created on the server, 204 No content when there is not data on the server according the client needs

- 3XX - Status codes for 300 redirection messages. The most used ones are 301 Moved permanently when we have multiple versions of an api such as _/api/v1/_ and _/api/v2_ and v1 is outdated.

- 4XX - Status codes for client errors. The most used ones are 400 bad request when client does not respect some validations on entities or have missing fields, 401 Unauthorized when the client is not authenticated to access a resource or an endpoint, 403 Forbidden when client is authorized but it does not have granted rights to access that resource, 404 Not Found when something does not exists such as an entity, an endpoint, 409 Conflict when we might have an already existing entity in the system according to certain fields (i.e a duplicate entry).

- 5XX - Status codes for server errors. The most used one is 500 meaning server error and something bad happened on the server (exception not catched, validation errors)

# 5. What is the difference between authorization and authentication?

The authentication is the process of checking if the user is authenticated in the system using different approaches such as JWT (JSON Web Token) from the Authorization header in the request, or using a session id. This also involve that JWT is valid (not expired, signed). Authorization means the user is authenticated, but we check its rights to access a resource or to do a certain action. This rights can come from a role, a policy. This can also come from entitie's owner, meaning I am only allowed to alter state of my entities in the system.

# 6. How would you explain to a 5-year-old how the WWW works?

WWW works similarly with a bookshelf with books. Imagine each book contains text, stories, images. This books are called webpages in the internet. Imagine each book can redirect you to another books. Like after you read _Adventures of Tom Sawyer by Mark Twain_ you go to _Adventures of Huckleberry Finn by Tom Sawyer_. In internet this is called a link.

# 7. 4

[Solution](https://github.com/davidalexandru1370/SnykOA/blob/main/7.py)

The trick here was to use another ASCII character instead of space called _thin space_ which is 1/5 smaller than the normal space.

The problem with normal space is the same length as a normal character resulting it is possible to create that pyramidal effect.
Below is the output of the main function, the run of all tests.

![Result](https://github.com/davidalexandru1370/SnykOA/blob/main/static/002.png)

# 8.

[Solution](https://github.com/davidalexandru1370/SnykOA/blob/main/8.py)
