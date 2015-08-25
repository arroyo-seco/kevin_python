Values, Functions, and Identity
===============================

All programs are made up of functions, values, and variables (identities). Thinking in terms of these three concepts will simplify programming dramatically. A value is a data item or a collection of data items, such as a string of characters or a list of names. A function takes values as inputs and produces new values from them. Variables are named identities that alias a value. The identity 'age' could alias the value 28 one day and 29 the next day. Importantly, the variable 'age' and the value 28 are not the same, both conceptually and in the program.

Values
------
Information stored in a type such as a string of characters or a number. A value is often a collection of other values, such as a list of strings. These collections are called data structures. Generally, after a value is constructed, it is no longer modified. We call this quality 'immutability' meaning that it doesn't get changed (or 'mutated'). Few programming languages enforce this philosophy as a core rule.

Examples:
* String: 'Jim'
* Tuple of numbers: (1, 2)
* Floating point number: 0.5
* List of strings: ['Subaru', 'Nissan', 'Toyota', 'Honda']
* Boolean: True
* Dictionary: { 'first': 'Jim', 'last': 'Simth' }
* Set: set(['a', 'b', 'c'])
* There are other types which can be looked up online

Functions
---------
Functions take values as inputs and produce other values. In some cases, they produce no values within the program (for example, a function that prints to standard out does not produce a new data value). A simple 'lowercase' function may take a string name and produce a lowercased version of it. The input value would be 'Jim' and the output value would be 'jim'. 

```python
# produces a new number
def sum_two_numbers(a, b):
    return a + b
# use the function to produce a value of 17
sum_two_numbers(7, 10)


# produces a new string
def lowercase(to_lowercase):
    return to_lowercase.lower()

# does not produce anything. writes out to the console
def call_print(to_print):
    print to_print
```

Identity
--------
Variables assign a value or function to a named identity. We can use this identity to as an alias within the program. Importantly, we can also change which value or function the variable aliases, but this is done less frequently.

```python
# variable first_name set to value 'Jim'
first_name = 'Jim'

# change values associated with variable first_name
first_name = 'Jim'
first_name = 'Steve'

# assign a function to a variable
function_to_use = sum
result = function_to_use(7, 10)
# result now set to value 17
```

All three together
------------------
```python
# define a summing function. a and b are 'parameters' to the function. They're like variables, but unlike other variables, they should never be reassigned
def sum_two_numbers(a, b):
    return a + b

# a function that writes to standard out and produces no new value
# str() is a python builtin that converts values to strings
def print_uppercase(to_print):
    print str(to_print).upper()

# the main sequence of actions. Variables are assigned to values and functions are executed
num_one = 6
num_two = 33
# apply the function 'sum_two_numbers' to the values represented by variables
# 'num_one' and 'num_two'
# this produces a new sum value which is assigned to the variable 'result'
result = sum_two_numbers(num_one, num_two)
# function produces no value so variable assignment isn't possible
print_uppercase(result)
```

Immutability and Mutability of Types
------------------------------------
Simple values like strings, tuples, numbers, and booleans are immutable at the language level. That means that an instance of a string has a particular value and that value can never be changed. Despite this there are modification functions on these immutable values, but they produce new values instead of modifying the existing value. Lists, Dictionaries, and Sets are mutable. That means that the underlying value can be changed.

```python
def change_list(l):
	l.append('d')

list_var = ['a','b','c']
change_list(list_var)

# ['a','b','c','d']
print list_var

def change_string(s):
	s += 'bar'

string_var = 'foo'
change_string(string_var)

#foo
print string_var
```

Links
-----
* Next: [Control Flow](control_flow.md)
* Previous: [Python Resources](python_resources.md)
* [README](README.md)
