Composing Code
==============

Limit variable scope
--------------------
The complexity of programs increases as the number of variables increase. One way to limit this complexity is to declare variables close to where they're used in scopes of limited size. Take, for example, a function. The longer the function, the larger the scope of the variables declared within that function. Other functions can be extracted from the longer function to limit the number of variables in the top level function and in the extracted functions.

```python
# all variables in one scope
def do_everything(names):
    lookup = {}
    size = len(names)
    for name in names:
        lowercase = name.lower()
        lookup[name] = lowercase
    for name in names:
        print 'normal: ' + name
        print 'lower: ' + lookup[name]
    print 'total names: ' + str(size)
    print str(lookup)
```

The above example is contrived, but there are already confusing aspects. For example, `size` is available to the for loops in the function with no benefit. Just looking at the function, it's not clear where it's used. Additionally, the second for loop iterates over `names` unnecessarily. We could refactor this code like so:

```python
def create_lowercase_map(names):
    lookup = {}
    for name in names:
        lookup[name] = name.lower()
    return lookup

def print_names(lookup):
    for name, lowercase in lookup.iteritems():
        print 'normal: ' + name
        print 'lower: ' + lowercase

def do_everything(names):
    lookup = create_lowercase_map(names)
    print_names(lookup)
    print 'total names: ' str(len(names))
    print str(lookup)
```

In this reworked example, two functions have been extracted. In the main function, there is only one argument and one variable in scope. The two new functions no longer have access to a variable representing the size of `names`, which has been eliminated altogether. `print_names` no longer has access to the `names` iterable because it's unnecessary for printing out name -> lowercase entries. Another benefit of smaller scopes is reduced pressure on naming variables. If there are few variables and a small scope, the purpose of the variables should be obvious, which means they won't require complicated names.

Limit mutability (create, don't modify)
---------------------------------------
Python dictionaries and lists are mutable. If they couldn't be modified after instantiation, they would be very difficult to use, if not impossible. However, this means that programs are free to manipulate these data structures whenever they want which adds complexity and mental overhead to anyone trying to understand them. To simplify programs, the best practice is to only modify lists and dictionaries during the process of construction and to extract that process into a self contained function. That way, the return value of that function can be treated as immutable for future reads. Functions that work on data structures such as `map`, `filter`, and `sorted` do not modify the inputs, they produce new outputs. Similarly, if you ever need to change data structures after construction, consider creating a new data structure instead.

```python
def do_everything(db_one, db_two, db_three):
    people_dict = {}
    people_one = db_one.load_people()
    for person in people_one:
        people_dict[person['name_one']] = person
    people_two = db_two.load_people()
    for person in people_two:
        people_dict[person['name_two']] = person
    people_three = db_three.load_people()
    for person in people_three:
        people_dict[person['name_three']] = person
    write_dict_to_file(people_dict)
    # do more stuff
```

In the above example, the people_dict is constructed in the same function in which it's used. This can be confusing because it's not obvious that the modification stops after the third people db is loaded. To simplify this, the `people_dict` will be constructed in its own function.

```python
def load_people_from_db(db, name_key):
    return index(lambda p: p[name_key], db.load_people())

def create_people_dict(db_one, db_two, db_three):
    people_dict = {}
    people_dict.update(load_people_from_db(db_one, 'name_one'))
    people_dict.update(load_people_from_db(db_two, 'name_two'))
    people_dict.update(load_people_from_db(db_three, 'name_three'))
    return people_dict

def do_everything(db_one, db_two, db_three):
    people_dict = create_people_dict(db_one, db_two, db_three)
    write_dict_to_file(people_dict)
    # do more stuff
```

In this example, modifications to `people_dict` occur only within `create_people_dict`. This is a one-liner in the main `do_everything` function and we can assume that the `people_dict` is only read from then on. In this version, we also refactored the db reads to construct their own people dictionaries, which are then used to update the main people_dict during construction. So, both `load_people_from_db` and `create_people_dict` create dictionaries, they do not modify existing dictionaries.

Assign variables once if possible
---------------------------------
There are often multiple lines of code that assign a value to the same variable unnecessarily. Like 'immutable' data structures, variables that are only assigned on a single line of code simplify programs. Here are two examples of multiple assignments that appear commonly:

```python
def print_meridian(time):
    meridian = None
    if is_before_noon(time):
        meridian = 'AM'
    else:
        meridian = 'PM'
    print meridian

def print_time(clock):
    time = None
    try:
        time = clock.get_time()
    except ClockException as e:
        print 'kablamo'
        raise e
    print 'time'
```

While these code snippets are not wrong, they do make the program more complicated, especially if they're surrounded by other code in the same scope. These examples do two things that make programs harder to understand: they assign the same variable multiple times unnecessarily and they allow a variable to be referenced before the proper value has been assigned. Both of these issues can be fixed by writing functions that produce the values in question.

```python
def get_meridian(time):
    if is_before_noon(time):
        return 'AM'
    else:
        return 'PM'

meridian = get_meridian(time)

def get_time(clock):
    try:
        return clock.get_time()
    except ClockException as e:
        print 'kablamo'
        raise e

time = get_time(clock)
```

Write simple, pure functions and use them in higher order functions
-------------------------------------------------------------------
In previous examples, the solution to complexity issues was to extract smaller and simpler functions. This made the resulting code easier to understand. Although there were more functions, they were all simpler than the original function. Pure functions (as described in the [functions](functions.md) section) are the simplest kind of functions. Given this, if a complicated function with side effects can be broken down into one or more pure functions and a single impure function, the code could be greatly simplified. Another advantage of these simple functions is that they're often compatible with useful higher order functions like `map` and `filter`. Let's look at two examples from the previous section: `is_before_noon` and `get_meridian`.

`is_before_noon` takes in a time and produces a boolean value that indicates whether or not that time occurs before noon. So, if we had several times and we only wanted the times before noon, we could use `filter`:

```python
times_before_noon = filter(is_before_noon, times)
```

`get_meridian` takes in a time and produces the appropriate meridian. If we wanted to convert all times to meridians, we could use `map`.

```python
meridians = map(get_meridian, times)
```

Maintain consistent levels of abstraction within functions
----------------------------------------------------------
Functions are easier to understand if the actions within them happen at the same level of abstraction. For example, code that does very specific work inside a loop is at a lower level of abstraction that the loop itself. If you mix many of these levels, it will be hard to read the function. It's like an instruction manual that breaks the overall process of building a desk into steps, which each have substeps. Maybe the top level function is called `build_desk`. There may be seven steps to building a desk which all happen in order inside the `build_desk` function. All of the substeps for those functions should be given their own functions to keep the `build_desk` function operating at the same high level of abstraction.

```python
def build_desk():
    empty_box()
    build_chair()
    assemble_legs()
    put_legs_on_desk()
    attach_keyboard_tray()
    install_desk()
    throw_away_box()
```

The above function would be more difficult to read if the details of tray assembly were written right into the middle of it.

While keeping functions at the same or a similar level of abstraction is an art, there are indicators that it's being done incorrectly. The first is over-nesting. If there are too many levels of nesting (try, if, etc), the function is almost certainly mixing levels of abstraction in a negative way. The other negative indicator is the shape of the function. The `build_desk` function has a very straightforward shape because a series of high level steps are executed sequentially. It reads like english. Let's replace the `attach_keyboard_tray` function with its implementation.

```python
def build_desk():
    empty_box()
    build_chair()
    assemble_legs()
    put_legs_on_desk()
    tray = new Tray()
    assert 10 == len(tray['screws'])
    for screw in tray['screws']
        attach_screw(screw)
        print 'screw attached'
    install_desk()
    throw_away_box()
```

This looks really odd. In the middle of these high level functions, we have a loop in which really specific tasks are performed. These should clearly be extracted into a `attach_keyboard_tray` function.

The purpose of writing tests
----------------------------
Writing tests is all about fear management. We're not afraid that the code doesn't work now, we're afraid that making a change to the code later will break it. It's this fear that will stagnate future development. All useful code will be edited. The more useful it is, the more you will want to change it to adapt to increased feature requests. Tests provide confidence that these changes won't break existing clients. In short, without tests it becomes prohibitively expensive to change useful code to be even more useful. That means business use cases aren't being met.

Links
-----
* Previous: [Functions on Data Structures](functions_on_data_structures.md)
* [Table of Contents](toc.md)
