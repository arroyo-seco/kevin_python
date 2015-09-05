Functions
=========

Functions typically take 0..n input values and produce an output value. For example, the python builtin `sum` function takes n input values and produces their sum. Python programs are made up of functions executed in a particular order. Because programs are expressed in terms of functions, it's important to use them in clear and simple ways.

Best Practices
--------------
* Never reassign argument variables
* Avoid modifying argument values if possible. It's always preferable to create new values
* Bias towards writing pure functions when possible
* Functions should do one thing
* Take care when naming functions

Pure Functions
--------------
The simplest and clearest type of function is called a pure function. A pure function is a function where the return value is only determined by its input values, without observable side effects. This has several implications:

* Inputs values are never modified
* The function produces a result
* Calling the function repeatedly with the same arguments always produces the same result
* The function does not internally reference any special or external state

Examples:

```python
# This function has no dependencies on internal state and no side effects.
# It always maps the same two argument values to the same resulting value.
def multiply_two_numbers(a, b):
  return a * b

# Same with this one
def construct_name_set():
  names = set()
  names.add('Jim')
  names.add('Steve')
  names.add('Joe')
  return names

# Counter example: this function changes the input list
def switch_places(l):
  temp = l[1]
  l[1] = l[0]
  l[0] = temp
```

Higher Order Functions
----------------------
Higher order functions are functions that take at least one function as an argument. These functions can be be extremely powerful and greatly simplify programming. Let's go through two examples, the first to show the syntax (there's barely any) and the second to give a real use case.

```python
def multiply_two_numbers(a, b):
   return a * b

# Higher order function that takes the function 'processor' as an argument
def process_two_arguments(processor, a, b):
    return processor(a, b)

result = process_two_arguments(multiply_two_numbers, 5, 2) # 10
```

In the above example, the function `process_two_arguments` took a processor function and applied it to the last two arguments. The function `muliply_two_numbers` was passed in as the processor and applied to those arguments. The result was the value 10.

For a more realistic example, let's say we need to perform a database backup. This will consist of reading data out of the database into a dictionary, transforming it, and writing to a file. However, we don't want to write to files right away, I want to do some dry runs where the output is printed to the console. Additionally, we may want to change the way the data is transformed. This is a good place to utilize higher order functions:

```python
def backup(db_conn, transformer, processor):
    data = db_conn.read_data()
    transformed_data = transformer(data)
    processor(data)

def remove_ssn(data):
    data_without_ssn = {}
    data_without_ssn.update(data)
    del data_without_ssn['ssn']
    return data_without_ssn

def print_transformed_data(transformed_data):
   print str(transformed_data)

def write_transformed_data(transformed_data):
   # do magic that writes data to file

# dry run for testing
backup(db_conn, remove_ssn, print_transformed_data)

# real run where data is written to file
backup(db_conn, remove_ssn, write_transformed_data)
```

In the above example, `backup` is a higher order function that takes in two other functions. The first is a function that transforms data after it's loaded out of the database. The second function processes that transformed data. Because we wrote `backup` this way, it would be easy to substitute different transformation or processing functions. There are two processors above, one that prints the transformed values for debugging and one that writes the transformed value to a file. One can imagine other transformation functions including an identity function that doesn't transform the data at all.

Anonymous Functions
-------------------
Python allows functions to be declared inline while calling higher order functions. In the `multiply_two_numbers` example, it would have been possible to skip that declaration and instead write a 'lambda' function when calling `process_two_arguments`.

```python
def process_two_arguments(processor, a, b):
    return processor(a, b)

result = process_two_arguments(lambda x, y: x * y, 5, 2) # 10
```

Links
-----
* Next: [Functions on Data Structures](functions_on_data_structures.md)
* Previous: [Data Structures](data_structures.md)
* [Table of Contents](toc.md)
