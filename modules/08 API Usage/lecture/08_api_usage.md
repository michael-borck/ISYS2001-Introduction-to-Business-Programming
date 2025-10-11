---
title: "API Basics for Python Programmers"
subtitle: "Understanding APIs with Weather Examples"
author: "Michael Borck"
execute:
  echo: false
jupyter: python3
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
# Copyright Information

![](../../../_assets/curtin-copy-right.png)

# Acknowledge of Country
I acknowledge the traditional custodians of the land on which I work and live,
and recognise their continuing connection to land, water and community. I pay
respect to elders past, present and emerging.

![](../../../_assets/ack_country.png)

# Today's Overview
- Introduction to APIs
- Understanding the Web
- URLs and Endpoints
- HTTP Methods
- Working with JSON Data
- Python's `requests` Library
- Building a Simple Weather App

::: {.notes}
**Aim**
The aim of this slide is to provide an overview of the key topics that will be covered in today's presentation on APIs and machine learning.

**Context**
This slide follows the "Acknowledgement of Country" and "Copyright Information" slides, setting the stage for the main content of the presentation. The topics listed on this slide will be expanded upon in the subsequent slides, providing a more in-depth understanding of APIs and their role in machine learning.

**Introduction to APIs**
APIs, or Application Programming Interfaces, are a fundamental concept in modern software development. They allow different software systems to communicate and exchange data with each other, enabling developers to build more complex and feature-rich applications by leveraging existing services and functionality.

**Understanding the Web**
To fully grasp the concept of APIs, it's essential to have a basic understanding of how the web works. This includes familiarity with the client-server model, the role of web browsers and servers, and the various protocols used for communication, such as HTTP and HTTPS.

**URLs and Endpoints**
URLs (Uniform Resource Locators) are a crucial component of APIs, as they specify the location of the resources being accessed. Endpoints are the specific URLs that an API exposes for different functionalities, allowing developers to interact with the API by making requests to these endpoints.

**HTTP Methods**
HTTP (Hypertext Transfer Protocol) is the foundation of data communication on the web. Understanding the different HTTP methods, such as GET, POST, PUT, and DELETE, is essential for working with APIs effectively, as these methods determine the type of operation being performed on the server.

**Working with JSON Data**
JSON (JavaScript Object Notation) is a lightweight data interchange format that is widely used in APIs. It provides a structured way to represent data in a human-readable and machine-parsable format, making it easy to transmit data between different systems and languages.

**Python's `requests` Library**
Python's `requests` library is a powerful tool for making HTTP requests and interacting with APIs. It simplifies the process of sending requests, handling responses, and working with JSON data, making it an essential library for any Python developer working with APIs.

**Building a Simple Weather App**
To demonstrate the practical application of APIs, the presentation will guide attendees through the process of building a simple weather app using a weather API. This hands-on example will showcase how to make API requests, handle responses, parse JSON data, and display the retrieved information in a user-friendly manner.
:::

# What is an API?
- **API** stands for **Application Programming Interface**
- It allows different software applications to communicate
- Think of it as a **bridge** between your code and external services

::: {.notes}
**Aim**
This slide aims to introduce the concept of an API, explaining what it is and how it facilitates communication between different software applications.

**Context**
After providing an overview of the presentation, this slide serves as the starting point for diving into the world of APIs. It lays the foundation for subsequent slides that will explore key concepts related to APIs, such as URLs, endpoints, HTTP methods, and RESTful architecture.

**API stands for Application Programming Interface**
An Application Programming Interface, or API, is a set of rules, protocols, and tools that define how different software components should interact with each other. It acts as a contract between the provider of a service and the developer who wants to use that service, specifying the types of requests that can be made, the data formats that should be used, and the conventions to follow.

**It allows different software applications to communicate**
The primary purpose of an API is to enable communication between different software applications. It provides a way for applications to share data and functionality, even if they are built using different programming languages or running on different platforms. By exposing a well-defined interface, an API allows developers to integrate external services into their own applications without needing to understand the internal workings of those services.

**Think of it as a bridge between your code and external services**
A helpful analogy for understanding APIs is to think of them as bridges connecting your code to external services. Just as a physical bridge allows people and vehicles to cross from one side to the other, an API acts as a bridge that enables your application to send requests to external services and receive responses back. It provides a structured way for your code to interact with and leverage the functionality provided by those services, making it easier to build powerful and feature-rich applications.
:::

# Understanding the Web
- The **Web** is a network of interconnected documents and resources
- **Clients** (like your Python script) request resources from **servers**
- Communication happens over the **Internet**

::: {.notes}
**Aim**
This slide aims to provide a high-level overview of how the Web works, introducing key concepts such as clients, servers, and the Internet.

**Context**
Before diving into the specifics of APIs, it's important to establish a foundational understanding of the Web. This slide sets the stage for subsequent slides that cover topics like URLs, endpoints, and HTTP methods, which are essential for working with APIs effectively.

**The Web is a network of interconnected documents and resources**
The Web, short for World Wide Web, is a vast network of linked documents and resources, such as web pages, images, videos, and more. These resources are connected through hyperlinks, allowing users to navigate from one resource to another seamlessly. The Web has revolutionised the way we access and share information, making it possible to retrieve data from servers located anywhere in the world.

**Clients (like your Python script) request resources from servers**
In the context of the Web, clients are the devices or software applications that request resources from servers. A common example of a client is a web browser, but in the case of this presentation, we'll be focusing on using Python scripts as clients. When a client sends a request to a server, it specifies the resource it wants to access using a URL (Uniform Resource Locator). The server then processes the request and sends back the requested resource or an appropriate response.

**Communication happens over the Internet**
The Internet is the global network infrastructure that enables communication between clients and servers. When a client sends a request to a server, the request travels through a series of interconnected networks, known as the Internet, to reach the server. The server then sends its response back to the client using the same network infrastructure. This communication is made possible by a set of standardised protocols, such as HTTP (Hypertext Transfer Protocol), which define the rules for data exchange between clients and servers.
:::

# Key Concept: URLs
- **URL** stands for **Uniform Resource Locator**
- It's the address used to access resources on the Web
- Example: `https://api.openweathermap.org/data/2.5/weather`

::: {.notes}
**Aim**
The aim of this slide is to introduce the concept of URLs and explain their role in accessing resources on the Web.

**Context**
After discussing the fundamentals of APIs and the Web, this slide focuses on URLs as a key concept. It sets the stage for the following slides that delve into the anatomy of URLs and how they relate to endpoints in RESTful APIs.

**URL stands for Uniform Resource Locator**
A URL is a standardised naming convention used to identify and locate resources on the internet. It provides a consistent and uniform way to reference web pages, images, videos, and other types of content accessible via the internet.

**It's the address used to access resources on the Web**
Just like a physical address helps you locate a specific building or residence, a URL acts as the address for a resource on the Web. By entering a URL into a web browser, you can navigate to and access the corresponding resource, such as a web page, image, or API endpoint.

**Example: `https://api.openweathermap.org/data/2.5/weather`**
This example URL demonstrates a typical structure. It starts with the protocol (`https://`), followed by the domain name (`api.openweathermap.org`), and then the path to the specific resource (`/data/2.5/weather`). In this case, the URL points to the weather endpoint of the OpenWeatherMap API, which can be used to retrieve current weather data for a specified location.
:::

# Anatomy of a URL
- **Scheme:** `https://`
- **Domain:** `api.openweathermap.org`
- **Path:** `/data/2.5/weather`
- **Query Parameters:** `?q=London&units=metric&appid=YOUR_API_KEY`

::: {.notes}
**Aim**
To break down the structure of a URL and explain the purpose of each component, using a real-world API example.

**Context**
This slide follows the "Key Concept: URLs" slide, which introduced the importance of URLs in web communication. It precedes the "Understanding Endpoints" slide, which will build upon the knowledge of URL components to explain how APIs use specific endpoints for different functionality.

**Scheme: `https://`**
The scheme specifies the protocol used to access the resource on the web. In this example, `https://` indicates that the Hypertext Transfer Protocol Secure (HTTPS) is being used, which provides an encrypted and secure connection between the client and the server.

**Domain: `api.openweathermap.org`**
The domain represents the unique address of the website or API provider on the internet. It consists of the subdomain (`api`), the second-level domain (`openweathermap`), and the top-level domain (`.org`). In this case, `api.openweathermap.org` points to the API server of the OpenWeatherMap service.

**Path: `/data/2.5/weather`**
The path specifies the location of the resource within the website or API. It can include multiple segments separated by forward slashes. In the given example, `/data/2.5/weather` indicates that we are accessing the current weather data endpoint of the OpenWeatherMap API, with version 2.5.

**Query Parameters: `?q=London&units=metric&appid=YOUR_API_KEY`**
Query parameters are used to pass additional information to the API server. They are appended to the URL after a question mark (`?`) and consist of key-value pairs separated by ampersands (`&`). In this example:
- `q=London` specifies the location for which we want to retrieve weather data.
- `units=metric` sets the units of measurement to metric.
- `appid=YOUR_API_KEY` is used for authentication, where `YOUR_API_KEY` should be replaced with the actual API key provided by OpenWeatherMap.
:::

# Understanding Endpoints
- An **Endpoint** is a specific URL where APIs can be accessed
- Each endpoint corresponds to a specific function
- Example: `/weather` for current weather data

::: {.notes}
**Aim**
The aim of this slide is to introduce the concept of endpoints in the context of APIs and explain their role in accessing specific functions.

**Context**
Having covered the fundamentals of APIs and the web, including URLs, this slide dives deeper into the structure of APIs by examining endpoints. This lays the groundwork for understanding how to interact with APIs using different HTTP methods, which will be covered in the next slide.

**An Endpoint is a specific URL where APIs can be accessed**
An API endpoint is a unique URL that serves as the entry point for accessing a particular API. When you make a request to an API, you send that request to a specific endpoint. The endpoint URL contains the base URL of the API, followed by the path to the specific resource or functionality you want to access. For example, if the base URL of an API is `https://api.example.com`, an endpoint for retrieving weather data might be `https://api.example.com/weather`.

**Each endpoint corresponds to a specific function**
Each endpoint within an API is designed to perform a specific function or provide access to a particular resource. APIs often have multiple endpoints, each serving a different purpose. For instance, an API for a weather service might have separate endpoints for retrieving current weather data, fetching a five-day forecast, or accessing historical weather information. By making requests to these specific endpoints, you can retrieve the desired data or perform the corresponding actions.

**Example: `/weather` for current weather data**
To illustrate the concept of endpoints, let's consider an example. In a weather API, there might be an endpoint specifically for retrieving the current weather data. This endpoint could be represented by the path `/weather`. To access the current weather information, you would make a request to the complete URL, such as `https://api.example.com/weather`. This endpoint would respond with the relevant data, such as temperature, humidity, wind speed, and other current weather conditions for a specified location.
:::

# HTTP Methods
- **GET:** Retrieve data
- **POST:** Send data
- **PUT:** Update data
- **DELETE:** Remove data
- **Example:** Using GET to fetch weather information

::: {.notes}
**Aim**
This slide aims to introduce the core HTTP methods used in interacting with APIs, focusing on their primary functions.

**Context**
Having covered the basics of APIs, URLs, and endpoints, this slide delves into the specific HTTP methods employed when making API requests. It lays the foundation for understanding RESTful APIs and sets the stage for practical examples using Python's `requests` library in subsequent slides.

**GET: Retrieve data**
The GET method is used to retrieve data from an API. When a GET request is sent to a specific endpoint, the API returns the requested information without modifying any data on the server. GET requests are the most common type of API request and are used when you need to fetch data, such as retrieving weather information or user profiles.

**POST: Send data**
The POST method is used to send data to an API for creating new resources. When you want to submit data to an API, such as creating a new user account or posting a comment, you would send a POST request to the appropriate endpoint. The data being sent is typically included in the request body and processed by the API to create a new resource on the server.

**PUT: Update data**
The PUT method is used to update existing data through an API. When you need to modify a specific resource, you send a PUT request to the corresponding endpoint, along with the updated data in the request body. The API then processes the request and updates the resource on the server accordingly. PUT requests are idempotent, meaning that multiple identical requests will have the same effect as a single request.

**DELETE: Remove data**
The DELETE method is used to remove or delete a resource via an API. When you send a DELETE request to a specific endpoint, the API processes the request and deletes the corresponding resource from the server. DELETE requests are typically used when you want to remove data permanently, such as deleting a user account or removing a blog post.

**Example: Using GET to fetch weather information**
To illustrate the usage of the GET method, consider an example where you want to fetch weather information from an API. You would send a GET request to the API's weather endpoint, specifying the necessary parameters such as location or date. The API would then process the request and return the requested weather data in the response, which you can parse and use in your application.
:::

# RESTful APIs
- **REST** stands for **Representational State Transfer**
- A common architectural style for APIs
- Uses standard HTTP methods and status codes

::: {.notes}
**Aim**
The aim of this slide is to introduce RESTful APIs and explain their key characteristics.

**Context**
Having covered the basics of APIs, HTTP methods, and URLs in the previous slides, this slide focuses on RESTful APIs specifically. It serves as a foundation for understanding how to interact with APIs using Python's `requests` library in the upcoming slides.

**REST stands for Representational State Transfer**
REST is an architectural style that defines a set of constraints for designing networked applications. It relies on a stateless, client-server communication protocol, typically HTTP. RESTful APIs expose a set of resources that can be accessed and manipulated using standard HTTP methods.

**A common architectural style for APIs**
RESTful APIs have become the most popular and widely adopted style for building web APIs. They provide a simple, scalable, and uniform interface for interacting with web services. Many popular web services, such as Twitter, GitHub, and Google Maps, provide RESTful APIs for developers to access their functionality and data.

**Uses standard HTTP methods and status codes**
RESTful APIs leverage the existing HTTP methods (GET, POST, PUT, DELETE) to perform operations on resources. Each method has a specific purpose: GET for retrieving data, POST for creating new resources, PUT for updating existing resources, and DELETE for removing resources. Additionally, RESTful APIs use standard HTTP status codes to indicate the success or failure of a request, such as 200 (OK), 201 (Created), 400 (Bad Request), and 404 (Not Found).
:::

# Data Formats: JSON
- **JSON** stands for **JavaScript Object Notation**
- A lightweight data-interchange format
- Easy to read and write for humans and machines
- Example:
  ```json
  {
    "temp": 20,
    "unit": "Celsius",
    "condition": "Sunny"
  }
  ```

::: {.notes}
**Aim**
The purpose of this slide is to introduce JSON as a lightweight data format and explain its key characteristics and readability for both humans and machines.

**Context**
Following the discussion of RESTful APIs and data formats in the previous slides, this slide focuses specifically on JSON. It will be followed by slides demonstrating how to use Python's `requests` library to make API requests and parse JSON responses.

**JSON stands for JavaScript Object Notation**
JSON, which is short for JavaScript Object Notation, is a popular data format used for exchanging data between web services and applications. Despite its name, JSON is language-independent and can be used with various programming languages, not just JavaScript.

**A lightweight data-interchange format**
JSON is designed to be a lightweight and efficient format for transmitting structured data over a network. Its simplicity and small file size make it ideal for web applications and APIs where fast data transfer is crucial. JSON files are plain text, which contributes to their lightweight nature.

**Easy to read and write for humans and machines**
One of the key advantages of JSON is its readability. JSON uses a simple and intuitive syntax that closely resembles JavaScript object notation. This makes it easy for developers to read, write, and understand JSON data. At the same time, JSON's structured format allows machines to parse and generate JSON data effortlessly.

**Example:**
To illustrate the structure and readability of JSON, an example is provided on the slide. The example demonstrates how data can be represented as key-value pairs and arrays in JSON format. This helps the audience visualise what JSON data looks like and understand its hierarchical nature.
:::

# Introduction to Python's `requests` Library
- `requests` is a powerful HTTP library in Python
- Simplifies making API calls
- Installation:
  ```bash
  pip install requests
  ```

::: {.notes}
**Aim**
The aim of this slide is to introduce the `requests` library in Python and highlight its key features for making HTTP requests.

**Context**
Having covered the fundamentals of APIs, HTTP methods, and data formats like JSON, this slide focuses on the practical aspect of interacting with APIs using Python. It sets the stage for the upcoming slides that demonstrate how to use `requests` for making API calls and handling responses.

**`requests` is a powerful HTTP library in Python**
The `requests` library is a widely-used and feature-rich library in Python for making HTTP requests. It provides a simple and intuitive interface for sending GET, POST, PUT, DELETE, and other types of requests to web servers. With `requests`, developers can easily interact with APIs, fetch data from websites, and send data to remote servers.

**Simplifies making API calls**
One of the key advantages of using `requests` is that it abstracts away the complexities of making HTTP requests. It handles low-level details such as establishing connections, encoding request data, and handling cookies and authentication. This allows developers to focus on the high-level logic of their application without worrying about the intricacies of the HTTP protocol.

**Installation:**
To start using the `requests` library, you need to install it in your Python environment. The easiest way to install `requests` is by using `pip`, the package installer for Python. You can install `requests` by running the following command in your terminal or command prompt:

```
pip install requests
```

Once installed, you can import the `requests` library in your Python scripts and start making HTTP requests.
:::

# Making Your First API Request
```python
import requests

response = requests.get("https://api.openweathermap.org/data/2.5/weather", params={
    "q": "London",
    "units": "metric",
    "appid": "YOUR_API_KEY"
})
print(response.status_code)
```

- **Status Code 200:** Success

::: {.notes}
**Aim**
The aim of this slide is to introduce the concept of a successful API request and the meaning of the HTTP status code 200.

**Context**
After covering the basics of APIs, HTTP methods, and RESTful APIs, this slide focuses on making the first API request using Python's `requests` library. It leads into subsequent slides that cover handling API responses, parsing JSON data, and practical examples using a weather API.

**Status Code 200: Success**
When making an API request, the server will respond with an HTTP status code indicating the outcome of the request. A status code of 200 means that the request was successful, and the server has returned the requested data. This is the ideal response you want to see when interacting with an API, as it confirms that your request was properly formatted and the API was able to process it without any issues. In the upcoming examples, we'll demonstrate how to check the status code of an API response using Python's `requests` library and handle different status codes gracefully.
:::

# Making Data More Readable with `pprint`

- **`pprint`** stands for **Pretty Print**
- Part of Python's built-in `pprint` module
- Enhances the readability of complex data structures
- Especially useful for:
  - **JSON responses** from APIs
  - **Nested dictionaries** and **lists**

::: {.notes}
**Aim**
The aim of this slide is to introduce the `pprint` module in Python and explain how it can be used to improve the readability of complex data structures.

**Context**
This slide follows on from the discussion of data formats like JSON and how to make API requests using Python's `requests` library. It provides a useful tool for handling the often complex and nested data returned by APIs, before moving on to parsing JSON responses and practical examples using a weather API.

**`pprint` stands for Pretty Print**
The `pprint` module in Python is short for "pretty print". Its purpose is to format and display complex data structures in a more readable and visually appealing way. By using `pprint`, you can make your code output easier to understand and debug, especially when working with large or deeply nested data.

**Part of Python's built-in `pprint` module**
`pprint` is a built-in module in Python, which means you don't need to install any additional libraries to use it. To start using `pprint` in your Python code, you simply need to import it at the beginning of your script with `import pprint`. This makes it a convenient tool that's always available in your Python environment.

**Enhances the readability of complex data structures**
The main benefit of using `pprint` is that it enhances the readability of complex data structures. When you print a dictionary or a list using the standard `print()` function, the output can be difficult to read, especially if the data is nested or contains long strings. `pprint` formats the data with indentation and line breaks, making it much easier to see the structure and content of the data.

**Especially useful for JSON responses from APIs**
`pprint` is particularly handy when working with JSON data returned by APIs. API responses often contain deeply nested dictionaries and lists, which can be challenging to read and understand using the standard `print()` function. By using `pprint` to display the JSON data, you can quickly get a clear picture of the structure and content of the response, making it easier to extract the information you need.

**Especially useful for nested dictionaries and lists**
In addition to JSON data, `pprint` is useful for displaying any complex data structure in Python, such as nested dictionaries and lists. When you have data with multiple levels of nesting, `pprint` can help you visualise the hierarchy and relationships between the different elements. This is especially valuable when debugging or trying to understand the structure of your data.
:::

# Handling API Responses
- **Response Object** contains data from the server
- Access response content:
  ```python
  from pprint import pprint
  data = response.json()
  print(data)
  ```
- Handle errors gracefully

::: {.notes}
**Aim**
The aim of this slide is to explain how to handle the response received from an API and access the data it contains.

**Context**
After learning how to make API requests using Python's `requests` library and format the response data with `pprint`, the next step is to understand how to handle the response object and extract the relevant data. This slide builds on the previous concepts and sets the stage for parsing JSON data in the following slide.

**Response Object contains data from the server**
When you make an API request, the server sends back a response object that contains the data you requested. This response object is a crucial part of working with APIs, as it holds the information you need to process and use in your application. The response object includes not only the data itself but also metadata such as the status code, headers, and more.

**Access response content:**
To access the actual data within the response object, you need to know how to retrieve it properly. Depending on the format of the data (e.g., JSON, XML), you'll use different methods to extract the content. For example, if the API returns JSON data, you can use the `response.json()` method to parse the JSON and convert it into a Python dictionary or list. This allows you to easily access and manipulate the data in your Python code.

**Handle errors gracefully**
When working with APIs, it's important to handle errors gracefully. API requests can fail for various reasons, such as invalid requests, authentication issues, or server-side problems. By implementing proper error handling, you can catch and manage these errors to prevent your application from crashing or behaving unexpectedly. This involves checking the response status code and using try-except blocks to handle exceptions that may occur during the API request or data parsing process.
:::

# Parsing JSON in Python

```python
data = response.json()
temperature = data['main']['temp']
condition = data['weather'][0]['description']
print(f"Temperature: {temperature}°C, Condition: {condition}")
```

- Extract specific information from the response

::: {.notes}
**Aim**
This slide aims to explain how to extract specific information from a JSON response using Python.

**Context**
After learning about JSON data format and making API requests using Python's `requests` library, this slide focuses on parsing the JSON response to extract the desired information. The following slides will demonstrate this concept with a practical example using a weather API.

**Extract specific information from the response**
Once you have made an API request and received a JSON response, you often need to extract specific pieces of information from the structured data. Python's built-in `json` module allows you to parse the JSON response and access the data using dot notation or square bracket notation, depending on whether you're working with an object or an array. By carefully examining the structure of the JSON response, you can navigate through the hierarchy of data and retrieve the values you need for your application.
:::

# Weather API Example: Current Weather

```python
import requests

location='New York'
api_key = "YOUR_API_KEY_HERE"
api_url = f'http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}'
response = requests.get(api_url)
weather = response.json()

print(f"Current temperature in New York: {weather['main']['temp']}°C")
print(f"Condition: {weather['weather'][0]['description']}")
```

::: {.notes}
**Aim**
This slide demonstrates how to retrieve current weather data using a weather API, showcasing a practical application of API usage in Python.

**Context**
Having covered the fundamentals of APIs, HTTP methods, and data formats like JSON, this slide presents a concrete example of using a weather API to fetch current weather information. It builds upon the knowledge gained from previous slides and sets the stage for the upcoming example of retrieving a 5-day forecast.
:::

# Weather API Example: 5-Day Forecast

```python
import requests

city = 'New York'
api_key = "YOUR_API_KEY_HERE"
forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}'
response = requests.get(api_url)
forecast = response.json()

for entry in forecast['list']:
    date = entry['dt_txt']
    temp = entry['main']['temp']
    condition = entry['weather'][0]['description']
    print(f"Date: {date}, Temp: {temp}°C, Condition: {condition}")
```

::: {.notes}
**Aim**
This slide demonstrates how to retrieve a 5-day weather forecast using a weather API, building upon the previous example of fetching the current weather.

**Context**
After introducing the concept of APIs, explaining key terms, and demonstrating how to make a basic API request to retrieve the current weather, this slide expands on that knowledge by showing how to fetch a 5-day forecast. This example leads into the subsequent slides on error handling, authentication, and building a simple weather app.
:::

# Error Handling in API Requests

```python
import requests

try:
    response = requests.get(api_url, params=params)
    response.raise_for_status()
    data = response.json()
except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
except Exception as err:
    print(f"An error occurred: {err}")
```

- Always handle potential errors to prevent crashes

::: {.notes}
**Aim**
The aim of this slide is to emphasise the importance of implementing error handling when making API requests to ensure the stability and reliability of your application.

**Context**
This slide follows the introduction to making API requests using Python's `requests` library and handling API responses. It precedes slides on authenticating with APIs and building a simple weather app, providing a critical consideration for developing robust API-based applications.

**Always handle potential errors to prevent crashes**
When making API requests, it's crucial to anticipate and handle potential errors that may occur. These errors can range from network issues to invalid requests or server-side problems. By implementing proper error handling, you can gracefully manage these situations and prevent your application from crashing unexpectedly. Use try-except blocks to catch and handle exceptions, display informative error messages to users, and implement fallback mechanisms or retry logic when appropriate. By proactively handling errors, you enhance the reliability and user experience of your application.
:::

# Authenticating with APIs

- Many APIs require **API Keys** for access
- Obtain an API key by signing up with the service
- Include the key in your requests

::: {.notes}
**Aim**
This slide aims to explain the process of authenticating with APIs, which often requires obtaining and using API keys to access the service.

**Context**
After introducing APIs, how they work, and how to make requests using Python's `requests` library, this slide focuses on the important aspect of authentication. It leads into the next slides on securely managing API keys and building a practical weather app using an authenticated API.

**Many APIs require API Keys for access** 
To protect their services and manage access, many API providers require users to obtain an API key. This key acts as a unique identifier and allows the API provider to track and control how their service is being used. Without a valid API key, requests to the API may be rejected or limited in functionality.

**Obtain an API key by signing up with the service**
To get an API key, you typically need to sign up for an account with the API provider. This process usually involves providing some basic information and agreeing to their terms of service. Once you have an account, you can generate or request an API key through their developer portal or API management dashboard.

**Include the key in your requests**
Once you have obtained an API key, you need to include it in your API requests to authenticate yourself and gain access to the service. The exact method of including the API key varies between different APIs. Common approaches include adding the key as a query parameter in the URL, including it in the request headers, or sending it in the request body. It's important to refer to the API documentation for specific instructions on how to include the API key in your requests.
:::

# Building a Simple Weather App

1. **Get User Input:** Ask for a city name
2. **Make API Request:** Fetch current weather
3. **Display Results:** Show temperature and condition

```python
import requests

city = input("Enter city name: ")
api_url = "https://api.openweathermap.org/data/2.5/weather"
params = {
    "q": city,
    "units": "metric",
    "appid": "YOUR_API_KEY"
}

response = requests.get(api_url, params=params)
weather = response.json()

print(f"Current temperature in {city}: {weather['main']['temp']}°C")
print(f"Condition: {weather['weather'][0]['description']}")
```

::: {.notes}
**Aim**
The aim of this slide is to demonstrate how to build a simple weather app using the concepts and techniques covered in the presentation.

**Context**
This slide builds upon the knowledge gained from previous slides about APIs, data formats, Python libraries, and handling API responses. It serves as a practical example that ties together the concepts covered throughout the presentation, allowing the audience to see how they can be applied to create a functional weather app.
:::

# Secure API Key Management

* Why
  - Protect Your Account
  - Avoid Accidental Exposure
  - Maintain Control
 
* Best Practices for API Key Management
  - Never Hardcode API Keys
  - Use External Files or Prompts
  - Exclude Secrets from Version Control

::: {.notes}
**Aim**
This slide aims to educate the audience on the importance of securely managing API keys and provide practical methods to protect sensitive information.

**Context**
Having learned about APIs, making requests, and handling responses, it is crucial to address the security aspects of using APIs. This slide serves as a bridge between the technical understanding of APIs and the best practices for securely managing API keys, leading to the practical implementation of secure key management in the subsequent slides.

**Protect Your Account**
API keys are like passwords for your account, granting access to sensitive data and functionality. Protecting your API keys is essential to maintain the security of your account and prevent unauthorised access. Treat your API keys with the same level of confidentiality as you would with your passwords.

**Avoid Accidental Exposure**
Accidentally exposing your API keys can have serious consequences, such as allowing others to make requests on your behalf or incurring unexpected charges. It is crucial to be cautious when handling API keys and ensure they are not inadvertently shared or made public, especially in code snippets or public repositories.

**Maintain Control**
Keeping your API keys secure gives you control over who can access your account and the associated resources. If your API keys are compromised, it is important to revoke them immediately and generate new ones. Regularly rotating your API keys adds an extra layer of security and helps maintain control over your account.

**Never Hardcode API Keys**
Hardcoding API keys directly into your source code is a dangerous practice. If your code is version-controlled or shared, anyone with access to the code repository can easily find and misuse your API keys. Instead, use alternative methods to store and access your API keys securely.

**Use External Files or Prompts**
One recommended approach is to store API keys in external files, such as configuration files or environment variables, separate from your code. Another option is to prompt the user to enter the API key at runtime, ensuring that the key is not stored in the code itself. These methods help keep your API keys secure and prevent accidental exposure.

**Exclude Secrets from Version Control**
When using version control systems like Git, it is essential to exclude files containing sensitive information, such as API keys, from being tracked. Use techniques like adding these files to your `.gitignore` file to ensure they are not accidentally committed and pushed to remote repositories, where they could be accessed by others.
:::

# Method 1: Using a Secrets File (`api_key.txt`)

- **Advantages:**
  - Keeps API keys separate from your code.
  - Easy to manage and update without altering the codebase.

- **Disadvantages:**
  - Requires handling the file securely.
  - Must ensure the file is not uploaded to public repositories.

```python
with open('api_key.txt', 'r') as file:
    api_key = file.read().strip()
```

::: {.notes}
**Aim**
To introduce students to the method of using a separate file to store API keys, highlighting its advantages and disadvantages.

**Context**
After covering the basics of APIs and how to make requests using Python, this slide is part of a section on secure API key management. It is followed by another method of handling API keys, which prompts the user to enter the key when running the script.

**Advantages:**

**Keeps API keys separate from your code.** Storing API keys in a separate file, such as `api_key.txt`, ensures that sensitive information is not mixed with the main codebase. This separation makes it easier to manage and maintain the code, as changes to the API key do not require modifying the script itself.

**Easy to manage and update without altering the codebase.** When API keys need to be updated or changed, having them in a separate file allows for quick and easy modifications without touching the main script. This approach reduces the risk of accidentally introducing errors or bugs into the codebase while updating the API key.

**Disadvantages:**

**Requires handling the file securely.** When using a separate file to store API keys, it is critical to ensure that the file itself is handled securely. This means setting appropriate file permissions to restrict access to the file and ensuring that only authorized users or processes can read its contents.

**Must ensure the file is not uploaded to public repositories.** When working with version control systems like Git, it is crucial to prevent the accidentally uploading of the API key file to public repositories. This can be achieved by adding the file to the `.gitignore` file, which instructs Git to exclude the specified files from version control. Failing to do so may result in the API key being exposed to the public, compromising the security of the associated API account.
:::

# Method 2: Prompting the User to Enter the API Key

- **Advantages:**
  - No need to store the API key in a file.
  - Reduces the risk of accidental exposure through file sharing.

- **Disadvantages:**
  - Requires manual entry each time the notebook is run.
  - Less convenient for repetitive tasks.

```python
# Get the API key from user input
api_key = input("Enter your OpenWeatherMap API key: ")
```

::: {.notes}
**Aim**
This slide aims to present an alternative method for securely managing API keys by prompting the user to enter the key manually.

**Context**
Following the discussion on the first method of using a secrets file to store the API key, this slide introduces a second approach. It compares the advantages and disadvantages of both methods, providing the audience with options to choose from based on their specific requirements and preferences.

**Advantages:**

**No need to store the API key in a file.** By prompting the user to enter the API key manually, this method eliminates the need to store the key in a separate file. This approach reduces the risk of accidentally exposing the key if the file is shared or compromised. It provides an added layer of security, as the key is only present in memory during the execution of the notebook.

**Reduces the risk of accidental exposure through file sharing.** When the API key is not stored in a file, it significantly reduces the chances of accidentally sharing the key with others. This is particularly important when collaborating on projects or sharing the notebook with team members. By keeping the key input separate from the notebook itself, it minimizes the risk of unintentional exposure.

**Disadvantages:**

**Requires manual entry each time the notebook is run.** The main drawback of this method is that it requires the user to manually enter the API key every time the notebook is executed. This can be inconvenient, especially if the notebook needs to be run frequently or if multiple users are working on the same project. It adds an extra step to the workflow and may be prone to input errors.

**Less convenient for repetitive tasks.** If the notebook is part of a repetitive task or an automated process, manually entering the API key each time can be cumbersome. It disrupts the automation and requires human intervention, which may not be feasible in certain scenarios. In such cases, using a secrets file or an alternative method for securely storing the key may be more appropriate.

**[]**
To get the API key from user input, you can use the input() function in Python. This function prompts the user with a message and waits for them to enter a value, which is then returned as a string. For example:

api_key = input("Enter your API key: ")

This line of code will display the message "Enter your API key: " to the user and store their input in the api_key variable. It's important to note that the input() function always returns a string, so if you need the value in another data type (e.g., integer or float), you'll need to convert it accordingly.

When prompting the user for sensitive information like an API key, it's a good practice to remind them not to share the key with anyone and to keep it secure. You can also provide instructions on how to obtain an API key if they don't have one already.
:::

# Both methods into a function:

```python
# Function to get the API key securely
def get_api_key():
    """
    Reads the API key from a file or prompts the user to input it.
    """
    try:
        with open('api_key.txt', 'r') as file:
            api_key = file.read().strip()
    except FileNotFoundError:
        api_key = input("Enter your OpenWeatherMap API key: ")
    return api_key

# Get the API key
api_key = get_api_key()
```

::: {.notes}
**Aim**
To demonstrate how to securely manage API keys in Python by encapsulating key retrieval methods into a reusable function.

**Context**
After exploring two different methods for securely managing API keys (using a separate file and prompting the user for input), this slide shows how to combine both approaches into a single function. This allows for a more modular and reusable approach to API key management in the weather app being built throughout the presentation.

Encapsulating both API key retrieval methods (reading from a file and prompting the user) into a single function offers several benefits:

1. Reusability: The function can be called whenever an API key is needed, reducing code duplication.

2. Flexibility: The function can be modified to handle different scenarios or fallback options for obtaining the API key.

3. Modularity: Separating the key retrieval logic from the main application code improves readability and maintainability.

Here's an example of how such a function might be implemented in Python:

```python
def get_api_key():
    try:
        with open("api_key.txt", "r") as file:
            api_key = file.read().strip()
    except FileNotFoundError:
        api_key = input("Enter your API key: ")
    return api_key
```

This function attempts to read the API key from a file named `api_key.txt`. If the file is not found, it prompts the user to enter the key manually. The function returns the obtained API key, which can then be used in the weather app.
:::

# Implementing Secure API Key Management in Google Colab

- **Uploading `api_key.txt`:**
  - Use Colab's file upload feature to add `api_key.txt` to your environment.
  - Access the file using the provided function to read the API key.
  
- **Security Considerations:**
  - **Do Not Share the Notebook:** Ensure that the notebook is not shared publicly with the `api_key.txt` file.
  - **Use `.gitignore` If Using Git:** Add `api_key.txt` to `.gitignore` to prevent it from being committed to Git repositories.

::: {.notes}
**Aim**
This slide aims to provide instructions on securely managing API keys in Google Colab notebooks to prevent unauthorised access.

**Context**
Following the previous slide on secure API key management methods, this slide focuses specifically on implementing secure API key management in Google Colab. It provides practical steps for uploading the `api_key.txt` file and discusses important security considerations when working with API keys in Colab notebooks.

**Uploading `api_key.txt`:**
To use the `api_key.txt` file in Google Colab, you need to upload it to your Colab environment. Colab provides a built-in file upload feature that allows you to easily add external files to your notebook. By uploading the `api_key.txt` file, you can access its contents within your Colab notebook using the provided function, which reads the API key from the file.

**Use Colab's file upload feature to add `api_key.txt` to your environment.**
In Google Colab, you can find the file upload feature in the sidebar or under the "Files" menu. Click on the upload button and select the `api_key.txt` file from your local machine. Once uploaded, the file will be available in your Colab notebook's file system, allowing you to access its contents using the appropriate file reading functions.

**Access the file using the provided function to read the API key.**
To read the API key from the uploaded `api_key.txt` file, you can use the provided function in your Colab notebook. This function typically opens the file, reads its contents, and returns the API key as a string. By using this function, you can assign the API key to a variable and use it in your code to authenticate API requests.

**Security Considerations:**
When working with API keys in Google Colab, it's crucial to follow security best practices to protect your API key from unauthorised access. One important consideration is to avoid sharing the notebook publicly if it contains the `api_key.txt` file. Sharing the notebook with the API key file can expose your key to others, potentially leading to misuse or unauthorised access to the API.

**Do Not Share the Notebook:** Ensure that the notebook is not shared publicly with the `api_key.txt` file.
If you need to share your Colab notebook with others, make sure to remove the `api_key.txt` file before sharing. You can either delete the file from the notebook's file system or exclude it from the notebook's contents. By keeping the API key file separate and not including it in the shared notebook, you can prevent unauthorised access to your API key.

**Use `.gitignore` If Using Git:** Add `api_key.txt` to `.gitignore` to prevent it from being committed to Git repositories.
If you're using version control systems like Git to manage your Colab notebooks, it's important to add the `api_key.txt` file to your `.gitignore` file. The `.gitignore` file specifies which files and directories should be ignored by Git and not committed to the repository. By including `api_key.txt` in `.gitignore`, you ensure that the file is not accidentally pushed to remote repositories, keeping your API key secure.
:::

# Building a Simple Weather App with Plot
1. **Get API Key:** Use best practice for eky management
2. **Get User Input:** Ask for a city name
3. **Make API Request:** Fetch current weather forecast
4. **Extract Dates and Temps:** Extract 4-hourly temps for each day
5. **Calculate Average Temp:** For each day, find the average temp
6. **Display/Plot Results:** Show average temperature plot

::: {.notes}
**Aim**
This slide aims to demonstrate how to build a simple weather application in Python that retrieves weather data from an API and visualises it using a plot.

**Context**
After covering the fundamentals of APIs, JSON parsing, and error handling, this slide builds upon the previous weather API examples to create a practical application. It ties together the concepts learned throughout the presentation, showcasing how to retrieve and process real-world data to build a functional weather app with visualisations.
:::

# Step 3: Get the five day forecast
```python
def get_five_day_forecast(city, api_key):
    forecast_url = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}'
    response = requests.get(api_url, params=params)
    forecast = response.json()
    return forecast
```

::: {.notes}
**Aim**
The aim of this slide is to explain the process of retrieving the five-day weather forecast data using the API.

**Context**
This slide is part of the "Building a Simple Weather App with Plot" section, following the introduction to the weather API example and the current weather data retrieval. It focuses on the next step of fetching the five-day forecast data, which will be used in subsequent slides to extract, process, and visualise the temperature data.
:::

# Step 4: Extract dates and temps
```python
def get_dates_temps(forecast):
    dates = []
    temps = []
        
    for entry in forecast:
        date = entry['dt_txt'].split(' ')[0]
        temp = entry['main']['temp']
        dates.append(date)
        temps.append(temp)
    return dates, temps
```

::: {.notes}
**Aim**
This slide aims to demonstrate how to extract specific data points from the JSON response, focusing on the dates and temperatures from the five-day forecast.

**Context**
After obtaining the five-day forecast data in the previous slide, the next step is to extract the relevant information, specifically the dates and temperatures. This process sets the stage for calculating the average temperature and plotting the data in the subsequent slides.
:::

# Step 5: Average Temp
```python
def get_average_temps_dates(dates,temps):
    # Get unique dates
    unique_dates = list(dict.fromkeys(dates))
    avg_temps = []
    
    # Calculate average temperature for each unique date
    for date in unique_dates:
        date_temps = [temp for d, temp in zip(dates, temps) if d == date]
        avg_temp = sum(date_temps) / len(date_temps)
        avg_temps.append(round(avg_temp, 2))
    
    return unique_dates, avg_temps
```

::: {.notes}
**Aim**
This slide aims to explain how to calculate the average temperature from the extracted five-day forecast data.

**Context**
After extracting the dates and temperatures from the five-day forecast data in the previous slide, this slide focuses on calculating the average temperature. The next slide will cover plotting the dates and temperatures to visualise the data.

**[No bullet points provided]**
As no bullet points were provided for this slide, I would suggest adding content that explains the process of calculating the average temperature from the extracted five-day forecast data. This could include:

1. Iterating through the list of temperatures
2. Summing up all the temperature values
3. Dividing the sum by the number of temperature values to obtain the average

Additionally, you may want to include a code snippet demonstrating how to calculate the average temperature using Python.
:::

# Step 6: Plot date and temps

```python
def plot_dates_temps(dates, temps):
    # Plot the temp and dates
    plt.figure(figsize=(10,6))
    plt.bar(dates, temps, color='skyblue')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')
    plt.title(f'6-Day Temperature Forecast for {city}')
    plt.xticks(dates, rotation=45) # Ensure all dates are shown on the x-axis
    plt.tight_layout()  # Adjust layout to prevent overlap
    plt.show()
```

::: {.notes}
**Aim**
The aim of this slide is to demonstrate how to plot the extracted date and temperature data using Python's matplotlib library.

**Context**
This slide follows the previous steps of getting the five-day forecast data, extracting the relevant date and temperature information, and calculating the average temperature. It is the final step in building the weather app, where the processed data is visualised using a plot.

**[No bullet points provided]**
As no specific bullet points were provided in the prompt, I will provide a general explanation of what could be covered in this slide.

To plot the date and temperature data, you can use Python's matplotlib library. First, import the necessary modules, such as matplotlib.pyplot. Then, create a figure and axis object using plt.subplots(). Set the x-axis values to the extracted dates and the y-axis values to the corresponding temperatures. You can customise the plot by adding labels for the x and y axes, a title for the plot, and adjusting the figure size if needed. Finally, display the plot using plt.show().

It's important to ensure that the date and temperature data are properly formatted and have the same length before plotting. You may need to convert the date strings to datetime objects and the temperature values to floats. If there are any missing or invalid data points, you should handle them appropriately, such as by removing or interpolating them.

By plotting the date and temperature data, you can provide a visual representation of the weather forecast, making it easier to interpret and analyse the trends over the five-day period.
:::

# Implement Weather App
1. **Get API Key:** Use best practice for eky management
2. **Get User Input:** Ask for a city name
3. **Make API Request:** Fetch current weather forecast
4. **Extract Dates and Temps:** Extract 4-hourly temps for each day
5. **Calculate Average Temp:** For each day, find the average temp
6. **Display/Plot Results:** Show average temperature plot

```python
api_key = get_api_key()
city = input("Enter city name: ")
forecast = get_five_day_forecast(city, api_key)
dates, temps = get_dates_temps(forecast['list'])
plot_dates_temps(dates,temps)
```

::: {.notes}
**Aim**
The aim of this slide is to provide an overview of the steps involved in implementing a weather app using APIs and Python.

**Context**
This slide builds upon the previous slides that introduced APIs, HTTP methods, JSON, and the Python `requests` library. It serves as a practical application of the concepts covered earlier, demonstrating how to integrate various components to create a functional weather app.
:::

# Best Practices When Using APIs

- **Read Documentation:** Understand endpoints and parameters
- **Handle Errors:** Anticipate and manage potential issues
- **Respect Rate Limits:** Avoid exceeding the allowed number of requests
- **Secure Your API Keys:** Do not expose them in public repositories

::: {.notes}
**Aim**
This slide aims to provide learners with essential best practices to follow when working with APIs to ensure efficient, secure, and reliable usage.

**Context**
Having covered the fundamentals of APIs, including their structure, usage, and practical examples using Python's `requests` library, this slide focuses on the important considerations developers should keep in mind when interacting with APIs. The best practices discussed here are crucial for building robust and secure applications that rely on APIs.

**Read Documentation: Understand endpoints and parameters**
Before using an API, it is essential to thoroughly read and understand its documentation. The documentation provides detailed information about the available endpoints, their functionality, and the required parameters. By familiarising yourself with the API's structure and capabilities, you can effectively utilise its features and avoid common pitfalls. Take the time to explore the documentation, including any code examples or tutorials, to gain a clear understanding of how to interact with the API correctly.

**Handle Errors: Anticipate and manage potential issues**
When working with APIs, it is crucial to anticipate and handle potential errors gracefully. API requests can fail for various reasons, such as invalid parameters, authentication issues, or server-side problems. Implement proper error handling mechanisms in your code to catch and manage these errors. This may involve checking the response status codes, parsing error messages, and providing informative feedback to the user. By handling errors effectively, you can ensure a smooth user experience and maintain the stability of your application.

**Respect Rate Limits: Avoid exceeding the allowed number of requests**
Many APIs enforce rate limits to prevent abuse and ensure fair usage among developers. These limits typically restrict the number of requests you can make within a specific timeframe. It is essential to be aware of and respect these rate limits to avoid being temporarily or permanently blocked by the API provider. Implement mechanisms to track and control the frequency of your API requests, such as using caching, implementing exponential backoff, or leveraging rate limit information provided in the API responses. By staying within the allowed limits, you can maintain a good relationship with the API provider and ensure the long-term viability of your application.

**Secure Your API Keys: Do not expose them in public repositories**
API keys are sensitive information that grant access to API services. It is crucial to keep your API keys secure and protect them from unauthorised access. Avoid exposing your API keys in public repositories, such as GitHub, where they can be easily discovered by others. Instead, use secure methods to store and manage your API keys, such as environment variables, configuration files, or secret management services. By keeping your API keys private, you can prevent misuse and ensure the security of your application and the API services you rely on.
:::

# Resources for Learning More

- [Official Python `requests` Documentation](https://docs.python-requests.org/)
- [OpenWeatherMap API](https://openweathermap.org/api)
- [REST API Tutorial](https://restfulapi.net/)

::: {.notes}
**Aim**
The aim of this slide is to provide learners with valuable resources to further expand their knowledge and skills in APIs, Python, and related topics.

**Context**
After covering the fundamentals of APIs, Python's `requests` library, and building a weather app, this slide offers learners the next steps in their learning journey. It directs them to official documentation and tutorials that can help solidify their understanding and explore more advanced concepts.

**[Official Python `requests` Documentation](https://docs.python-requests.org/)**
The official Python `requests` documentation is an essential resource for mastering the `requests` library. It provides comprehensive information on all the features, methods, and parameters available in the library. Learners can find detailed explanations, code examples, and best practices for making HTTP requests, handling responses, and working with different types of authentication. The documentation also covers advanced topics like session management, custom headers, and proxy support.

**[OpenWeatherMap API](https://openweathermap.org/api)**
The OpenWeatherMap API documentation is a valuable resource for learners interested in integrating weather data into their applications. It provides detailed information on the various endpoints available, such as current weather, weather forecasts, and historical data. The documentation explains the request parameters, response formats, and authentication requirements. It also includes code examples in multiple programming languages to help learners quickly get started with making API requests to OpenWeatherMap.

**[REST API Tutorial](https://restfulapi.net/)**
The REST API Tutorial is a comprehensive resource for learning about RESTful APIs. It covers the fundamental concepts of REST, including resources, URIs, HTTP methods, and status codes. The tutorial explains how to design and implement RESTful APIs, handle different data formats like JSON and XML, and secure APIs using authentication and authorization mechanisms. It also discusses best practices for API versioning, error handling, and documentation. Learners can gain a deep understanding of RESTful principles and apply them to their own API projects.
:::

# Conclusion

- **APIs** enable communication between applications
- **URLs** and **Endpoints** are key to accessing APIs
- Use Python's `requests` library to interact with APIs
- Weather examples make learning practical and engaging

::: {.notes}
**Aim**
The aim of this slide is to summarise the key points covered in the presentation and reinforce the main takeaways for the audience.

**Context**
This slide serves as the culmination of the presentation, tying together the concepts and examples discussed throughout the various sections. It follows the practical examples of using APIs with Python's `requests` library to interact with weather data, and precedes the slide on additional resources for further learning.

**APIs enable communication between applications**
Application Programming Interfaces, or APIs, are crucial for facilitating communication and data exchange between different software applications. They define a set of rules and protocols that allow applications to interact with each other seamlessly. By leveraging APIs, developers can access and utilise the functionality and data provided by external services or systems, enabling them to build more powerful and integrated applications.

**URLs and Endpoints are key to accessing APIs**
To interact with APIs effectively, it is essential to understand the role of URLs (Uniform Resource Locators) and endpoints. URLs serve as the addresses that identify the location of specific resources or services on the web. Endpoints, which are part of the URL, define the specific functionality or data that an API provides. By making HTTP requests to the appropriate URLs and endpoints, applications can retrieve data, send instructions, or perform various operations through the API.

**Use Python's `requests` library to interact with APIs**
Python's `requests` library simplifies the process of making HTTP requests and interacting with APIs. It provides a high-level, user-friendly interface for sending GET, POST, PUT, DELETE, and other HTTP methods. With `requests`, developers can easily send requests to API endpoints, pass parameters, handle authentication, and receive responses in various formats such as JSON. The library abstracts away the low-level details, making API communication more intuitive and efficient.

**Weather examples make learning practical and engaging**
Throughout the presentation, weather-related examples were used to demonstrate the practical application of APIs and Python's `requests` library. By focusing on real-world scenarios like retrieving current weather data and fetching five-day forecasts, the concepts become more relatable and easier to grasp. These examples showcase how APIs can be used to access valuable information and integrate it into custom applications, making the learning experience more engaging and meaningful for the audience.
:::

