Control Flow
============

There are two useful ways to change the control flow of a program. One is to introduce conditional blocks. The other is to introduce loops. Conditional blocks are gated by boolean conditions. They take the form of `if`/`elif`/`else` statements and the block that gets executed depends on the result of evaluating a boolean expression. Loops repeat a block (potentially with changing input variables) until a condition no longer holds. They are usually implemented using `for`, which is a special case of `while`.

Conditionals
------------
Conditional statements are structured as blocks of `if`/`elif`/`else` statements. Each `if` or `elif` block takes an expression that evaluates to a boolean as the argument. If the expression evaluates to True, that block is executed. The first that has the expression evaluated to true gets executed or the `else` block gets executed. There are other forms of conditionals, but they're often confusing. Using the simple `if`/`elif`/`else` conditionals is usually the best way to go.

```python
# return a lowercase version of the input string if it's less than 4 chars long
# len() is a python builtin that returns the length of a string or collection
def lowercase_if_short(input):
    if len(input) < 4:
        return input.lower()
    else:
        return input

# return a lowercase version of the input string if it's less than 4 chars long
# return an uppercase version of the input string if it's more than 15 chars long
def lowercase_if_short_uppercase_if_long(input):
    if len(input) < 4:
        return input.lower()
    elif len(input) > 15:
        return input.upper()
    else:
        return input
```

Loops
-----
Loops repeatedly execute a block of code while a condition remains true. This is the standard `while` loop which takes a boolean expression. The block will be executed repeatedly so long as that expression remains true. Usually, code in the block itself affects variables used in the boolean expression in such a way that it will eventually become false.

while example:
```python
# declare control variable
start_number = 2000
# boolean expression 
while start_number > 5:
    print str(start_number)
    #change the control variable
    start_number = start_number / 2
```

Most loops act over a defined collection of items.
```python
# print 'hello' five times. Effectively loops over the list [0, 1, 2, 3, 4]
i = 0
while i < 5:
    print 'hello'
    i = i + 1
```

The above `while` loop, can be written more concisely as a `for` loop. `for` works on anything that can be iterated over. Lists are the simplest example of an iterable data structure.

```python
# print 'hello' five times
# xrange will produce an iterable with values [0, 1, 2, 3, 4]
for i in xrange(5)
    print 'hello'
```

As implied by the previous example, for loops iterate through collections of values and designate a variable to represent the current value for each block. To print the numbers 0 through 9, I could do this:

```python
for n in xrange(10):
    print str(n)
```

Often the iterable is more interesting than a range of numbers. It may have the list of car manufacturers referenced earlier. To print those, simply do this:

```python
cars = ['Subaru', 'Nissan', 'Toyota', 'Honda']
for car in cars:
    print car
```

Links
-----
* Next: *[Data Structures](data_structures.md)*
* Previous: *[Values, Functions, and Identity](values_functions_identity.md)*
* [README](README.md)
