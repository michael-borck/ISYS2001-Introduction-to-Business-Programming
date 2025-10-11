---
title: "Unravelling Python Dictionaries: A Beginner's Guide"
subtitle: "Mastering the Art of Key-Value Storage"
author: "Michael Borck"
format: 
  pptx:
    reference-doc: ../../../_assets/template.pptx
  pdf:
    toc: false
    colorlinks: true
  docx:
    toc: false
    highlight-style: github
  html:
    toc: true
    toc-expand: 2
    embed-resources: true
---

# What is a Python Dictionary?

- A dictionary is a collection of key-value pairs
- Keys are unique identifiers used to access values
- Values can be any data type, including other collections
- Dictionaries are unordered, unlike lists or tuples

::: {.notes}
In Python, a dictionary is a powerful data structure that allows you to store and retrieve data using unique keys. Unlike lists or tuples, which are ordered collections, dictionaries are unordered. Each piece of information in a dictionary is stored as a key-value pair, where the key acts as a unique identifier to access the corresponding value.

The keys in a dictionary can be any immutable data type, such as strings, numbers, or tuples, while the values can be any valid Python object, including other collections like lists or even other dictionaries. This flexibility makes dictionaries incredibly versatile and useful for a wide range of applications, from storing configuration settings to building complex data models.
:::

# Creating a Dictionary

```python
# Create an empty dictionary
my_dict = {}

# Create a dictionary with initial key-value pairs
person = {
    "name": "Alex",
    "age": 30,
    "city": "Sydney"
}
```

::: {.notes}
To create a dictionary in Python, you can use curly braces `{}` to enclose the key-value pairs. Each pair is separated by a colon `:`, with the key on the left and the value on the right.

You can create an empty dictionary by simply using the curly braces, like `my_dict = {}`. This gives you a blank canvas to start building your dictionary.

Alternatively, you can create a dictionary with some initial key-value pairs, as shown in the `person` example. Here, we have three key-value pairs: "name" is associated with the string "Alex", "age" is associated with the integer 30, and "city" is associated with the string "Sydney".

The keys in a dictionary can be any immutable data type, such as strings, numbers, or tuples, while the values can be any valid Python object, including other collections like lists or even other dictionaries.
:::

# Accessing Dictionary Values

```python
person = {
    "name": "Alex",
    "age": 30,
    "city": "Sydney"
}

# Access values using keys
print(person["name"])  # Output: "Alex"
print(person["age"])   # Output: 30

# Use the get() method to handle missing keys
print(person.get("occupation", "Not found"))  # Output: "Not found"
```

::: {.notes}
To access the values stored in a dictionary, you can use the keys as indices, just like you would with a list or tuple. Simply place the key inside square brackets `[]` after the dictionary name.

In the example, we access the values associated with the keys "name" and "age" by using `person["name"]` and `person["age"]`, respectively. This will output the corresponding values: "Alex" and 30.

If you try to access a key that doesn't exist in the dictionary, you'll get a `KeyError`. To handle this, you can use the `get()` method, which allows you to provide a default value to return if the key is not found. In the example, we use `person.get("occupation", "Not found")` to retrieve the value for the "occupation" key, but since it doesn't exist, the method returns the default value "Not found".

Using the `get()` method is a safe way to access dictionary values, as it prevents your code from crashing if a key is missing.
:::

# Adding and Updating Entries

```python
person = {
    "name": "Alex",
    "age": 30,
    "city": "Sydney"
}

# Add a new key-value pair
person["occupation"] = "Software Engineer"

# Update an existing value
person["age"] = 31

print(person)
# Output: {'name': 'Alex', 'age': 31, 'city': 'Sydney', 'occupation': 'Software Engineer'}
```

::: {.notes}
Dictionaries are mutable, which means you can add new key-value pairs or update the values of existing keys.

To add a new key-value pair, simply assign a value to a new key. In the example, we add the key "occupation" and assign it the value "Software Engineer".

To update an existing value, you can assign a new value to the corresponding key. Here, we change the value of the "age" key from 30 to 31.

After making these changes, the `person` dictionary now contains four key-value pairs: "name" is associated with "Alex", "age" is associated with 31, "city" is associated with "Sydney", and "occupation" is associated with "Software Engineer".

Modifying dictionaries in this way is a common operation and allows you to keep your data up-to-date and relevant.
:::

# Removing Entries

```python
person = {
    "name": "Alex",
    "age": 30,
    "city": "Sydney"
}

# Remove a key-value pair
del person["age"]

# Use the pop() method to remove a key-value pair and get the value
occupation = person.pop("occupation", "Not found")
print(occupation)  # Output: "Not found"

print(person)
# Output: {'name': 'Alex', 'city': 'Sydney'}
```

::: {.notes}
Dictionaries also allow you to remove key-value pairs. There are a few ways to do this:

1. Using the `del` keyword: You can remove a specific key-value pair by using the `del` keyword followed by the dictionary name and the key you want to remove. In the example, we use `del person["age"]` to remove the "age" key-value pair.

2. Using the `pop()` method: The `pop()` method allows you to remove a key-value pair and get the value associated with that key. If the key doesn't exist, you can provide a default value to be returned. In the example, we use `person.pop("occupation", "Not found")` to remove the "occupation" key-value pair (if it exists) and store the value in the `occupation` variable. Since the key doesn't exist, the method returns the default value "Not found".

After removing the key-value pairs, the `person` dictionary now only contains the "name" and "city" keys.

Removing entries from a dictionary is useful when you need to clean up or update your data, especially if certain information is no longer relevant or needed.
:::

# Looping through a Dictionary

```python
person = {
    "name": "Alex",
    "age": 30,
    "city": "Sydney"
}

# Loop through keys
for key in person:
    print(key)
# Output:
# name
# age
# city

# Loop through key-value pairs
for key, value in person.items():
    print(f"{key}: {value}")
# Output:
# name: Alex
# age: 30
# city: Sydney
```

::: {.notes}
Dictionaries are very versatile, and you can loop through them in various ways to access their contents.

The most basic way is to loop through the keys using a `for` loop. In the example, we simply iterate over the `person` dictionary, and for each iteration, the `key` variable will be assigned the current key.

A more common and useful way to loop through a dictionary is to use the `items()` method, which returns a view object containing the key-value pairs. This allows you to access both the keys and the values in each iteration. In the example, we use `for key, value in person.items()` to unpack each key-value pair into the `key` and `value` variables, respectively.

Looping through a dictionary is a great way to perform operations on all the key-value pairs, such as printing them out, modifying the values, or performing some other logic based on the data.
:::

# Dictionary Methods

- `len(dict)`: Returns the number of key-value pairs in the dictionary
- `dict.keys()`: Returns a view object containing the keys
- `dict.values()`: Returns a view object containing the values
- `dict.items()`: Returns a view object containing the key-value pairs
- `dict.get(key, default)`: Returns the value for the given key, or the default value if the key is not found
- `dict.pop(key, default)`: Removes the key-value pair and returns the value, or the default value if the key is not found
- `dict.update(other_dict)`: Merges the key-value pairs from another dictionary into the current one

::: {.notes}
Dictionaries in Python come with a variety of built-in methods that allow you to perform common operations on them. Here are some of the most useful methods:

- `len(dict)`: Returns the number of key-value pairs in the dictionary.
- `dict.keys()`: Returns a view object containing all the keys in the dictionary.
- `dict.values()`: Returns a view object containing all the values in the dictionary.
- `dict.items()`: Returns a view object containing the key-value pairs as tuples.
- `dict.get(key, default)`: Returns the value associated with the given key, or the default value if the key is not found.
- `dict.pop(key, default)`: Removes the key-value pair with the given key and returns the value. If the key is not found, it returns the default value.
- `dict.update(other_dict)`: Merges the key-value pairs from another dictionary into the current one, overwriting any existing keys.

These methods provide a wide range of functionality for working with dictionaries, from getting information about the dictionary's contents to modifying and manipulating the data.
:::

# Nested Dictionaries

```python
person = {
    "name": "Alex",
    "age": 30,
    "address": {
        "street": "123 Main St",
        "city": "Sydney",
        "state": "NSW"
    }
}

# Access nested values
print(person["address"]["city"])  # Output: "Sydney"

# Update a nested value
person["address"]["state"] = "Victoria"

print(person)
# Output: {'name': 'Alex', 'age': 30, 'address': {'street': '123 Main St', 'city': 'Sydney', 'state': 'Victoria'}}
```

::: {.notes}
Dictionaries can also contain other dictionaries, creating a nested data structure. This is particularly useful when you need to model more complex data, such as information about a person that includes their address details.

In the example, the `person` dictionary has a key called "address" that is associated with another dictionary containing the street, city, and state information.

To access the nested values, you can chain the keys together, separating them with square brackets `[]`. In the example, we use `person["address"]["city"]` to get the value "Sydney" for the "city" key in the nested "address" dictionary.

Similarly, you can update the values of the nested dictionary by assigning new values to the corresponding keys. Here, we change the "state" value in the "address" dictionary from "NSW" to "Victoria".

Nested dictionaries allow you to build sophisticated data models that reflect the real-world relationships and hierarchies in your data.
:::

# Conclusion

- Dictionaries are unordered collections of key-value pairs
- Keys must be unique and can be any immutable data type
- Values can be any valid Python object, including other collections
- Dictionaries are versatile and can be used for a wide range of applications
- Key operations include creating, accessing, modifying, and removing entries
- Dictionaries can be nested to model complex data structures

::: {.notes}
In this presentation, we've covered the basics of Python dictionaries, a powerful data structure that allows you to store and retrieve data using unique keys.

We've learned that dictionaries are unordered collections of key-value pairs, where the keys must be unique and can be any immutable data type, while the values can be any valid Python object, including other collections like lists or even other dictionaries.

We've explored how to create dictionaries, access and modify their contents, remove entries, an