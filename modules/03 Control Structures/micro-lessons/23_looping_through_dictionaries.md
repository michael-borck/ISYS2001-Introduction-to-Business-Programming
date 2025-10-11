---
title: "Looping Through Dictionaries"
format:
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

**Aim**
This lesson aims to cover how to work with dictionaries in Python, focusing on accessing and iterating through key-value pairs.

**Context**
After learning about branching, repetition, and functions in previous lessons, we now explore dictionaries as a flexible way to store and work with structured data. The next lessons discuss using GenAI to learn Python effectively and apply these concepts in a weather analysis project.

**Access key-value pairs** In Python dictionaries, data is stored as key-value pairs. To access a value, you use its corresponding key inside square brackets. For example, if `weather` is a dictionary, you can access the temperature with `weather["temperature"]`. This allows for quick and direct access to specific data points.

**Iterate through dictionary entries** You can loop through a dictionary using a `for` loop. By default, iterating over a dictionary gives you its keys. To access both keys and values, use the `.items()` method, like `for key, value in weather.items():`. This lets you process all the data in a dictionary efficiently.

**Useful for structured data** Dictionaries are ideal for representing structured data where each piece of information has a unique label or key. For instance, a weather report could have keys like "temperature", "humidity", "wind_speed", etc. This key-value structure keeps the data organised and easy to understand.

**Flexible data representation** Unlike lists which are ordered sequences, dictionaries are unordered and can hold various types of data as values. The values can be of any data type, like numbers, strings, booleans, or even lists and other dictionaries. This flexibility makes dictionaries suitable for complex, hierarchical data structures.

**Example: detailed weather report** A practical example is a detailed weather report stored in a dictionary. It could have keys for different aspects of the weather, like:
```python
weather = {
    "temperature": 25.3,
    "humidity": 0.6,
    "wind_speed": 10,
    "wind_direction": "NE",
    "forecast": ["sunny", "cloudy", "rainy"]
}
```
You can then access and work with this data easily using the keys.