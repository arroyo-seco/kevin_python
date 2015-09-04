Functions on Data Structures
============================

Most data in your program will be in the form of dictionaries and lists or in abstract iterables. There are several useful utility functions that make common operations on these structures straightforward. Using these will save work and reduce bugs.

map(function, iterable)
-----------------------
`map` transforms all values in an iterable to new values and returns them in a list. The transformation is done by a function which is passed as an argument into map with the iterable itself. The transformation function is a single argument function that produces a new value.

Imagine there's a list of string names. The strings are all uppercased and have exclamation points instead of the letter 'j'. We want to lowercase them and substitute 'j' for the exclamation points. Here's how that code might look.

```python
def fix_names(names):
    fixed_names = []
    for name in names:
        lower = name.lower()
        fixed = lower.replace('!', 'j')
        fixed_names.append(fixed)
    return fixed_names
```

This programming pattern occurs very frequently. We're effectively mapping each value of the original iterable to a different value. Let's do a bit of refactoring:

```python
def fix_name(name):
    lower = name.lower()
    fixed = lower.replace('!', 'j')
    return fixed

def fix_names(names):
    fixed_names = []
    for name in names:
        fixed_names.append(fix_name(name))
    return fixed_names
```

At this point, all of the interesting behavior has been moved to the function `fix_name` and `fix_names` is purely boilerplate. This is the exact boilerplate that `map` implements. So the above code could be written with `map` as follows:

```python
def fix_name(name):
    lower = name.lower()
    fixed = lower.replace('!', 'j')
    return fixed

fixed = map(fix_name, names)
```

This final form is very clean and concise. `map` may be the single most useful higher order function used in programming.

filter(function, iterable)
--------------------------
`filter` constructs a list with the items from an iterable that pass a predicate function. The predicate function takes a single argument and returns a boolean.

Imagine there's a list of dictionaries that represent cars. Each car dictionary has a key associated with the make. We want to filter out all cars that aren't Hondas.

```python
def get_hondas(cars):
    hondas = []
    for car in cars:
        if car['make'] == 'Honda':
            hondas.append(car)
    return hondas
```

Once again, this is a common programming pattern and the interesting bit can be refactored out:

```python
def is_honda(car):
    return car['make'] == 'Honda'

def get_hondas(cars):
    hondas = []
    for car in cars:
        if is_honda(car):
            hondas.append(car)
    return hondas
```

At this point `get_hondas` is just boilerplate that matches the functionality of filter, so the above code can be rewritten:

```python
def is_honda(car):
    return car['make'] == 'Honda'

hondas = filter(is_honda, cars)
```

sorted(iterable[, cmp[, key]])
------------------------------
`sorted` takes an iterable and returns a sorted list of its values. If an iterable is provided with no custom comparison functions, the sorting will be done according to the natural order of its items.

Natural ordering of different types:

numbers: Lower numbers come before larger numbers

```python
a = [5, 3, 4, 7, 1]
# [1, 3, 4, 5, 7]
b = sorted(a)
```

tuples/lists: Elements of corresponding indexes are compared until one is less than its counterpart. The tuple/list with that lesser element is less than the tuple/list with the larger element.

```python
a = [1. 2. 3.4]
b = [1, 2, 5, 4]
c = [a, b]
# [[1, 2, 3, 4], [1, 2, 5, 4]]
sorted(c)
```

strings: Each character has a number value. The numbers increase A-Z followed by a-z. The characters are then compared in order. In this way, you can think of string comparison as the comparison of two lists of numbers.

```python
a = ['abc', 'def', 'aBC', 'DEF']
# ['DEF', 'aBC', 'abc', 'def']
b = sorted(a)
```

dictionaries: While python does have a natural sort order for dictionaries, it's usually a mistake to depend on this non-obvious behavior.

Comparison functions: A comparison function takes two arguments of like kind and returns a number that indicates which one is smaller. If the number returned is negative, it means the first argument is smaller. If the number returned is positive, the first argument is larger. If zero is returned, the arguments are equal. You can pass this as an argument to sorted by writing a function and referencing it with the `cmp` keyword.

Example: Sort list of numbers by the result of modding them with 3.

```python
def cmp_mod_3(num_one, num_two):
    return num_one % 3 - num_two % 3

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# [3, 6, 9, 1, 4, 7, 10, 2, 5, 8]
sorted(a, cmp=cmp_mod_3)
```

Key functions: In the above example and many other examples, you may want to sort by treating each value as if it was a different value. In that case, we wanted to treat each value as if it was value % 3. sorted can take in a key function which transforms its single argument into a different value. A simple example is to sort strings in a case indifferent manner.

```python
def to_lower(string):
    return string.lower()

a = ['abc', 'Zbc', 'def']
# ['Zbc', 'abc', 'def']
sorted(a)
# ['abc', 'def', 'Zbc']
sorted(a, key=to_lower)
```

enumerate(sequence)
-------------------
Sometimes it's beneficial to iterate over an iterable and keep track of the index at the same time. This is the purpose of the function enumerate. It takes a sequence like a list, tuple, or string and produces an iterable of tuples of the index number and the value of that index. To demonstrate the value of this, I'll show two alternate implementations and show why using enumerate is easier:

```python
names = ['jim', 'steve', 'bob', …]
for i in xrange(len(names)):
    print 'element #' + str(i)
    print 'value: ' + names[i]
```

As I mentioned on the data structures page, directly reading from list indexes is unusual to see when programming because typically lists don't guarantee good performance for index lookups. Python lists do, but it may still look weird to other people. Additionally, this solution seems like a lot of work.

```python
names = ['jim', 'steve', 'bob', …]
i = 0
for name in names:
    print 'element #' + str(i)
    print 'value: ' + name
    i = i + 1
```

To get around the antipattern, one could declare a variable outside the scope of the loop and increment its value each time through. This solution works, but it's fairly verbose and allows a variable used exclusively within the loop to escape the scope of that loop.

```python
names = ['jim', 'steve', 'bob', …]
for i, name in enumerate(names):
    print 'element #' + str(i)
    print 'value: ' + name
```

`enumerate` produces tuples of the indexes and values which can be nicely destructured as shown above. This solution is concise, simple, and as efficient for all sequences as the more verbose example above.

index(function, iterable)
-------------------------
`index` is not a function built into python but it's something that is done all the time, so you may want to copy and paste its impl. Given an iterable of items, transform them in some way. Use the transformed value as the key in a dictionary and the original value as the corresponding value.

As an example, let's say we have an array of 100 entity dictionaries, which each have a key called `id`. We know these ids are all unique and we want to be able to lookup individual entities by their id. We might write this function to create the dictionary.

```python
def entities_by_id(entities):
    entities_by_id = {}
    for entity in entities:
        entities_by_id[entity['id']] = entity
    return entities_by_id
```

We could refactor this like so:

```python
def get_id(entity):
    return entity['id']

def entities_by_id(entities):
    entities_by_id = {}
    for entity in entities:
        entities_by_id[get_id(entity)] = entity
    return entities_by_id
```

At this point, the only interesting behavior is in `get_id`. `entities_by_id` is just boilerplate that actually matches the functionality of index.

```python
def index(function, iterable):
    result = {}
    for item in iterable:
        result[function(item)] = item
    return result

def get_id(entity):
    return entity['id']

entities_by_id = index(get_id, entities)
```

Links
-----
* Next: [Composing Code](composing_code.md)
* Previous: [Functions](functions.md)
* [Table of Contents](toc.md)
