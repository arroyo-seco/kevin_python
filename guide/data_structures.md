Data Structures
===============

Proper use of data structures is the most important part of writing a computer program. There are two data structures that are overwhelmingly more important than others: lists and dictionaries. Lists are ordered collections of items that can be added to and iterated through. They are also a simple 'catch all' collection if you just need to store some junk in memory for a while. Dictionaries are lookup tables that make it easy to store and retrieve values using unique keys. The key can be anything that has a concept of equality, such as a string.

Lists
-----
Python lists are ordered collections of values. New values can be appended to the back of them. Additionally, individual indexes can be read or set to a value. Here are the core functions on lists:

```python
# construction:
my_list = []

# addition:
my_list.append('word')

# multiple additions
my_list.extend(other_list)

# iteration
for word in my_list:
    print word

# size
size = len(my_list)

# index lookup
first_value = my_list[0]

# set index value
my_list[0] = 'fun'

# Lists containing value equals values in the same order are value equals
[1, 2, 3] == [1, 2, 3] # True
```

There are many more functions on python lists, but these are the core functions. The important takeaway is that a list is an ordered and iterable collection of values. If you care about order, you should be using a list. Furthermore, while values can be set and retrieved by index, this should be done relatively infrequently. In these situations, consider using a dictionary or tuple instead.

Lists are also used as catch all collections. If lookups and uniqueness aren't important, a list is probably the correct data structure.

Dictionaries
------------
Dictionaries are lookup tables. They are collections of keys and values that are best used to store and retrieve data by a unique lookup key. There are methods that provide iterables views over the keys, values, and key-value pairs of the dictionary as well.

```python
# construction
my_dict = {}

# put value for key
my_dict['name'] = 'jim'

# put many keys and values
my_dict.update(other_dict)

# retrieve value for key
some_name = my_dict['name']

# key existence check
exists = 'name' in my_dict

# iteration (no order guarantees)
for key, value in my_dict.iteritems()
    print str(key)
    print str(value)

# size (number of key-value pairs)
size = len(my_dict)

# Dictionaries containing value equals keys and values are value equals
{ 'one': 'two', 'three': 'four'} == { 'three': 'four', 'one': 'two' } # True
```

Dictionaries are fantastic when at storing values by unique keys for later retrieval. Because of this property, they can also represent real life objects. For example, let's say we wanted to represent a car object which has a few properties. One way to do so is to use a dictionary:

```python
car = {}
car['make'] = 'Honda'
car['weight_pounds'] = 2500
car['color'] = 'black'
```

Dictionary keys are usually simple values like strings, but anything with a concept of equality can be used as a dictionary key. For example, lists, tuples, and other dictionaries could be used as dictionary keys. However, dictionaries will not work correctly if keys are modified after insertion. Dictionary keys should be immutable, meaning that the value does not change. Simple values like strings are immutable at a language level, while dictionaries and lists are not immutable at a language level, so care should be taken when using them as dictionary keys.


Other Important Data Structures
===============================

Sets
----
A set is a dictionary that only has keys. They are very useful when it's important that only unique values exist within a collection. Like dictionaries, sets do not have an order of elements.

```python
# construction
my_set = set()
my_set = set(list_of_names)

# addition
my_set.add('jim')

# add many values
my_set.update(list_of_names)

# existence
exists = 'jim' in my_set

# iteration
for name in my_set:
    print name

# size
size = len(my_set)

# Sets containing the same value equals elements are equal
set([1, 2, 4, 3]) == set([2, 1, 3, 4]) # True
```

There are also a number of set operations that can be done with sets such as union, difference, and intersection.

Here's an example of common use cases for a set

```python
# list of first names including many duplicates
first_name_list =  load_first_names()
# 10,000 names in list
print str(len(first_name_list))

unique_names = set(first_name_list)
# 5,000 unique names in list
print str(len(unique_names))

# is the name jim in there?
contains_jim = 'jim' in unique_names
```

Tuples
------
Tuples are immutable lists of values usually declared in place for convenience. Python provides convenient ways to de-structure them into multiple variables assignments. They are often used when there are a fixed small number of values that need to be grouped and then sent somewhere.

```python
# construction
name = ('Kevin', 'Richards')

# de-structure the tuple and assign to two variables
first, last = name
# prints 'Kevin'
print first
# prints 'Richards'
print last

# iteritems() produces (key, value) tuples
for key, value in my_dict.iteritems():
    print key
    print value

# using a tuple to return multiple values from a function
def load_items_from_db(conn):
    result_map = conn.get_items()
    return (result_map['items'], result_map['throughput_used'])

items, throughput = load_items_from_db(conn)

# Tuple equality works just like list equality
('A', 'B') == ('A', 'B') # True
```

Classes
-------
The class system is a concept from object oriented programming. We can use classes to give more structure to values that are essentially dictionaries. In a previous example, I showed how a dictionary could be used to model a car.

```python
car = {}
car['make'] = 'Honda'
car['weight_pounds'] = 2500
car['color'] = 'black'
```

If this car object will show up repeatedly and it would be advantageous to make it more of a first class thing, a car class can be written:

```python
class Car:

    def __init__(self, make, weight_pounds, color):
        self.make = make
        self.weight_pounds = weight_pounds
        self.color = color

honda = Car('Honda', 2500, 'black')
honda_two  = Car('Honda', 2500, 'black')
honda_three = Car('Honda', 3300, 'red')

honda == honda_two # True
honda == honda_three # True
```

Classes can do many more things, but those features often add complexity and headaches to programming. From a data structures perspective, the class is just syntactic sugar around a dictionary.

Extra: Iterables and Iteration
==============================

An iterable is an object that is capable of returning its members one at a time. All sequence data structures are iterable (list, tuple, string) and many other kinds of objects are iterable. Dictionaries have many functions that produce iterables of keys, values, and key-value pairs. Anything that is iterable can be used in a for loop (for i in iterable). Additionally, many important functions that act on iterables and data structures produce other iterables.

Iterables are not data structures and have no size. They are abstractions that are capable of producing an object called an iterator. An iterator has two basic functions: next() and hasNext(). next() produces the next value. has_next() indicates if there is a next value. A for loop can utilize these two functions to walk through an iterable one item at a time.

Many important functions that act on data structures produce iterables instead of concrete lists because it's more efficient if all you care about is iterating through the result. For example, let's say I had a function called every_third that takes an iterable as an input and puts every third item in a list and returns that list. If the only goal is to iterate through that 'every_third' list, it's wasteful to return a concrete list. Instead, every_third could return an iterable that has a reference to the original list. When the iterator is created, the iterator reads from the original list, but next() always grabs the item 3 indexes away. Less memory is used this way.

Extra: Python lists, arrays, and the list abstraction
=====================================================

An abstraction is a conceptual contract that abstracts away specifics of an implementation. It is common to 'program to the abstraction' or contract as opposed to the implementation even if we know the implementation. The list abstraction describes an ordered collection of elements of a definite size. The elements can be iterated through in order. The first element is the value of index '0' of the collection and the last element is the value of index 'size - 1'. Elements can be retrieved by their indexes. Python lists are an example of a list that is backed by arrays, a data structure for which index lookup is always fast. However, there are other ways to implement lists. For example, one could construct a list by making each element a node that has a reference to the next element. This sort of list is called a 'linked list'. Linked lists do not have the same performance guarantees for index lookups. To lookup a value associated with an index, one must start at the beginning element of the list and follow the references from element to element until the desired index is reached. Array based lists and linked lists are both lists, and as such conform to the general abstraction of a list which defines a way to retrieve the value of an index, but the performance of this call varies dramatically. Another way of saying this is: The list abstraction makes no guarantees about the performance of index lookups.

For this reason, in statically typed languages it's unusual to see an index lookup on a list without a clear indication that the type of the list being used is one which has the property of fast index lookup. Even then, it's rare to see index lookups compared to ordered iteration, which all list implementations should do efficiently. As a result, it's likely that there's a problem with your program if you find yourself depending on index lookups in lists.

Links
-----
* Next: [Functions](functions.md)
* Previous: [Control Flow](control_flow.md)
* [Table of Contents](toc.md)
