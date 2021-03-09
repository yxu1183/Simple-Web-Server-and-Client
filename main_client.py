
"""
Name : Yunika Upadhayaya
ID: 1001631183
Date: 03/08/2021
CSE 4344 - Project 1
"""

import socket
from time import *
import sys
import time
import http.client

HOST = "127.0.0.1"
PORT = 8080
fileName = "hello.html"


def check_host(name):
    if name != HOST:
        if name != "localhost":
            print("Using local server by default. Host name is not 127.0.0.1 or localhost")
    else:
        name = HOST
    return name


def check_port(number):
    if int(number) != PORT:
        print("Using port number 8080 by default. Provided port number cannot be accepted.")
    else:
        number = PORT
    return number


def check_file(file):
    file = fileName
    return file


def main():
    if len(sys.argv) == 2:
        host_name = sys.argv[1]
        host = check_host(host_name)
        print(host)
        print("No port number provided. Default value 8080 is used.")
        print("No file name provided. Default filename is used.")

    elif len(sys.argv) == 3:
        host_name = sys.argv[1]
        port_number = sys.argv[2]
        host = check_host(host_name)
        port = check_port(port_number)
        print(host)
        print(port)
        print("No file name provided. Default filename is used.")

    elif len(sys.argv) == 4:
        host_name = sys.argv[1]
        port_number = sys.argv[2]
        file_name = sys.argv[3]
        host = check_host(host_name)
        port = check_port(port_number)
        file = check_file(file_name)
        print(host)
        print(port)
        print(file)
    else:
        print("No arguments provided. All default filenames are used.")


if __name__ == "__main__":
    main()