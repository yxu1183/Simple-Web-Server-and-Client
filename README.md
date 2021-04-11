# Simple Web Server & Client
### Computer Networks/Project-1: Created by [Dr. Sajib Datta](http://crystal.uta.edu/~datta/)

## Description
A multi-threaded web server that interacts with any standard web clients using HTTP and displays the essential connection parameters.

## Functionality
* Multi-threaded server that handles multiple requests concurrently.
* Server is assumed to work only with HTTP get messages.
* Port number can be provided as an argument while running the program, otherwise default port number of 8080 is assigned.
* Server can handle incoming client requests and display essential client details.
* If no file is requested, then the server uses the default file to response.
* If the file requested by the client is not in the server, then it responses with “HTTP/1.1 404 Not Found”.
* If the file requested by the server is in the server, then it responses with “HTTP/1.1 200 OK”.
* Client connects the server and requests file to the server.
* Client displays the status and contents of the file requested.
* Client also displays essential server details.

## Compilation Instructions
The code is implemented using the following interpretor:

```
Python 3.9
```

Running main_server.py:
```
main_server.py <port_number>
```
Note: Port number is optional. If not provided, default value of 8080 is used.

Running main_client.py:
```
main_client.py <host_name> <port_number> <file_name>
```
Note: Host name, port number, and file name are optional. If not provided, default values of  "127.0.0.1", "8080", and "index.html" are used respectively. The order of arguments matters. 

## Author
[Yunika Upadhayaya](https://github.com/yxu1183) - *Student ID: 1001631183*

## References
* [BaseHTTPServer](https://documentation.help/Python-2.7.13/basehttpserver.html)
* [HTTPServer and implementations](https://python.readthedocs.io/en/v2.7.2/library/basehttpserver.html)
