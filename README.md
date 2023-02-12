#### API architecture refers to the design of an API and how it is organized. It encompasses the structure of an API and how it is built, including the endpoints, methods, and parameters.
There are a few different types of API architectures that developers can use to create APIs.

The most popular type of API architecture is the REST API.

Other popular types of API architectures include SOAP, XML-RPC, and JSON-RPC.

1. REST

A REST (Restful) API is a web service that uses HTTP requests (GET, PUT, POST, and DELETE) to manipulate data. 

A REST API can access resources such as HTML pages, images, and other resources identified by a URL.

2. SOAP

SOAP API refers to the application programming interface for communication in Simple Object Access Protocol. 

It defines the rules and standards for how two applications can interact with each other over the internet. 

This type of API is often used in web services.

3.  RPC

RPC stands for Remote Procedure Call Application Programming Interface.

It is a platform-independent communications protocol that allows different software components to communicate with each other.

RPC API is based on the concept of remote procedure calls, which allows a program to execute a procedure or function on a remote machine as if it were local.

Let's show the two most famous examples.

3.1 XML-RPC 

XML-RPC is a remote procedure call system that uses XML to encode its calls and HTTP as a transport mechanism. 

It is designed to be simple and extensible.

3.2 JSON-RPC

JSON-RPC is a remote procedure call protocol encoded in JSON. 

It is a simple and lightweight protocol that allows for accessible communication between computers.

curl is nothing but a command-line tool that provides a more programmatic way to interact with APIs.
curl stands for client URL.

It is used to establish communication between the client and the server.

You can fetch data and transfer data to the server using curl.

The latest modern OS has to curl pre-installed, so you don't need to install it to work with it.

Or you can install it from here:

https://curl.se/download.html
Working with curl is super fast and convenient.

Open your terminal and run the following command.

`curl --version` 

It will give you the version of curl you're currently using.

A typical HTTP request has four different components:

- Method
- Endpoint
- HTTP headers
- Body

You can pass all of these using curl.
https://twitter.com/Rapid_API/status/1574433386214694916/photo/1
https://twitter.com/Rapid_API/status/1574433402035511296/photo/1
https://twitter.com/Rapid_API/status/1574433407618236416/photo/1
https://twitter.com/Rapid_API/status/1574433416589840386/photo/1

### Anatomy of an HTTP Response
https://twitter.com/Rapid_API/status/1580906033324564485/photo/1
https://twitter.com/Rapid_API/status/1580906038936489984/photo/1
https://twitter.com/Rapid_API/status/1580906044712026112/photo/1
https://twitter.com/Rapid_API/status/1580906050777100289/photo/1
https://twitter.com/Rapid_API/status/1580906057123368960/photo/1
https://twitter.com/Rapid_API/status/1580906062974054400/photo/1

Cross-Origin Resource Sharing (CORS) is a mechanism that enables the browser to access resources outside a given domain.

Resources can be requested from one URL to another.

A web page may freely embed cross-origin images, stylesheets, scripts, iframes, and videos.

CORS introduces a standard mechanism for all browsers to implement cross-domain requests.

The specification defines a set of headers that allow the browser and server to determine which type of requests are allowed.

This is important because it allows for a more secure and efficient way of loading resources from different origins.
The same-origin policy prevents a web application running on a client from requesting an API operating on a different domain.

An in-browser script often just needs to access resources from the same origin.

Therefore, this is advantageous for security.

What does it mean that the origin is different?

It may have a:

- different domain
- different port
- different scheme (HTTP used instead of HTTPS and vice versa)

The HTTP response headers provide information about the permitted origin(s).

If you want to allow all origins to use:

Access-Control-Allow-Origin: *

To authorize access from a specific host, follow these steps:

Access-Control-Allow-Origin: https://example .com

Commonly, public APIs that accept requests from all sources use the header:

Access-Control-Allow-Origin: *

1. REST API

It is a web service based on REST architecture that allows communication between different systems.

It uses HTTP requests to GET, PUT, POST, and DELETE data. REST API is often used in web applications to access data from a server.

2. API Client

An API Client is a software program that makes it easy to work with Application Programming Interfaces (APIs).

It can be used to access data or perform actions on behalf of a user.

API Clients are often used by developers to test APIs.

3. API Resource

An API resource is a specific type of data that can be accessed by an application programming interface (API).

4. API Server

An API server allows two different systems to communicate with each other.

In most cases, an API server enables a web application to interact with a database.

5. API Scalability

API scalability refers to the ability of an API to handle increased loads of data or traffic without adversely affecting performance.

A scalable API can handle large amounts of data and traffic without compromising speed or functionality.

6. Stateless API

A stateless API is an API that does not maintain a state between requests.

Each request is independent of any other request, and state information is not stored on the server.

7. API Cache

An API is cacheable if the data it returns can be stored in a cache.

Cache allows the same data to be returned for multiple requests without having to fetch it from the original source each time.

Caching can improve performance.

8. Layered System

A layered system, means that each layer is responsible for a specific set of tasks. 

The most common layers are the presentation layer, the business logic layer, and the data access layer.
	

With a REST API, a client requests a resource using an API endpoint where that particular resource is located on the server. Each resource has a unique endpoint.

This means needing multiple resources requires multiple requests, like below.

https://twitter.com/Rapid_API/status/1583147018377052160/photo/1

On the other hand, GraphQL functions using a single endpoint, and clients can request multiple resources in one call. 

GraphQL uses a strongly typed schema definition language that represents objects using nodes.

The GraphQL server responds with a nested set of objects.
https://twitter.com/Rapid_API/status/1583147024123580417/photo/1

API Security
https://twitter.com/Rapid_API/status/1583442985186136064/photo/1
https://twitter.com/Rapid_API/status/1583442991037177858/photo/1
https://twitter.com/Rapid_API/status/1583442997974212608/photo/1
https://twitter.com/Rapid_API/status/1583443003611709441/photo/1
https://twitter.com/Rapid_API/status/1583443009940901890/photo/1

Optimize API performance with these 5 tips.
1️⃣ Cache Response

Caching avoids excessive database queries. For endpoints that frequently return the same response, caching can be implemented to reduce the number of calls to the API and improve performance.

2️⃣ Compress data

The transfer of large payloads will slow down an API. Data compression combats this issue by decreasing the data size and improving speed.

There are various compression methods available, a common one being GZIP.

3️⃣ Prevent over and under-fetching

Over-fetching results in unnecessary and unusable data, and under-fetching results in an incomplete response.

Good architecture, planning, and appropriate API management tools are essential to avoid these.

4️⃣ Paginate and filter

Both pagination and filtering are great methods to reduce response complexity and improve user experience.

Pagination enables the separation and categorization of data, and filtering limits the results of parameters.

5️⃣ Use PATCH, not PUT

The PATCH and PUT methods are similar, but PATCH has performance advantages.

When modifying a resource, PUT updates the entire resource, which is often unnecessary, whereas PATCH only updates a specific part. Therefore PATCH has a smaller payload.

API Caching Techniques to improve performance.
📌 What is API Caching?

Caching enables us to store copies of frequently accessed data in several places along the request-response path. 

Today, APIs use caching extensively, which is also one of the architectural constraints of REST APIs.
There are two techniques of caching based on where you keep the cache.

👉 Client Caching
👉 Server Caching
1️⃣ Client Caching

If you take a good look at your API calls, you may notice several redundant requests that are called with every page load or when components are re-rendered. 

Besides slowing down your app, these redundant calls also put a load on the server.

Caching API responses on the client level improves both client and server efficiency.

We can store client-side caches in Cache Storage, Local Storage, Session Storage, IndexedDB, or Cookies depending on the type of data.

2️⃣ Server Caching

Server Caching reduces the load on the server by storing repeated calls in a cache. As a result, the server does not have to process these requests.

The client cache caches the response on the browser level. The server cache does the same but on the server.

📌 API Caching security measures

Care must be taken while caching APIs because not everything that can be cached should be cached. 

API keys, tokens, and other credentials can be a security hazard if cached improperly.

REST and GraphQL APIs. What are the differences between them?

1️⃣ Method to perform data operations

With RESTful APIs, you have different HTTP methods to perform CRUD operations.

Whereas with GraphQL, you use queries and mutations to perform data operations.

2️⃣ Overfetching and under fetching

With REST API, you either often fetch an unnecessary amount of data or fetch data in multiple API calls.

With GraphQL, you only get the data that you have requested.

3️⃣ Endpoints

REST API leads to fetching different data from multiple endpoints.

GraphQL provides a single endpoint from where you can read and manipulate data.

4️⃣ Cache

REST API leverages the caching feature. The different operations, like the GET, POST, etc., can be cached and stay in the browser history.

GraphQL doesn't follow the HTTP specs and uses a single endpoint. It is up to developers to ensure that caching is implemented.

5️⃣ Language

REST API is an API type that lets you perform CRUD operations between client and server.

GraphQL is a query language that allows you to read and mutate the data in APIs.







