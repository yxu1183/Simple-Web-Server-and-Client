"""
Name : Yunika Upadhayaya
ID: 1001631183
Date: 03/08/2021
CSE 4344 - Project 1
"""

# importing modules
from time import *
import sys
import time
import http.client

# default values for host name, port number and file name
HOST = "127.0.0.1"
PORT = 8080
fileName = "index.html"


# this class creates client on HTTPServer
class HTTP():
    # function that instantiates
    def __init__(self, name_host, number_port, name_file):
        self.hostname = name_host
        self.portnumber = number_port
        self.filename = name_file

    # function that makes request
    # creates the http request, sends it, and prints the html file
    # prints other important connection parameters
    def request(self):
        connect = http.client.HTTPConnection(self.hostname + ':' + str(self.portnumber))

        try:
            requested_time = time.time()
            connect.request("GET", '/' + self.filename)
            received_time = time.time()
        except ConnectionRefusedError:
            print("Server could not provide connection. Refused!\n")
            return

        # connection parameters - socket details
        family_socket = connect.sock.family
        protocol_socket = connect.sock.proto
        type_socket = connect.sock.type
        name_peer = connect.sock.getpeername()

        try:
            get = connect.getresponse()
        except:
            print("No response. Remote is closed.\n")
            return
        print("\n~~~~~~~~~~~~~Received~~~~~~~~~~~~~\n")

        # prints the header details in server
        print(get.headers)
        # check the version of http and display accordingly
        if get.version == 11:
            print("HTTP/1.1")
        elif get.version == 10:
            print("HTTP/1.0")
        # check the status of http and display accordingly
        if get.code == 200:
            print("200 OK\n")
        elif get.code == 404:
            print("404 NOT FOUND\n")
        # print the html file contents in the terminal
        print(get.read().decode('utf-8') + '\n')
        rtt = str(received_time - requested_time)
        # print other connection parameters in the server
        print("RTT: " + rtt)
        print("Server Port Number: " + str(connect.port))
        print("Host Name: " + connect.host)
        print("Socket Family: " + str(family_socket))
        print("Socket Type: " + str(type_socket))
        print("Socket Protocol: " + str(protocol_socket))
        print("Peer Name: " + str(name_peer))
        print("\n~~~~~~~~~~~~~Completed~~~~~~~~~~~~~\n")


def main():
    # check for number of arguments provided
    # use default values if no parameters provided
    if len(sys.argv) == 2:
        host_name = sys.argv[1]
        HOST = host_name
        print("No port number provided. Default value 8080 is used.")
        PORT = 8080
        print("No file name provided. Default filename is used.")
        fileName = "index.html"

    elif len(sys.argv) == 3:
        host_name = sys.argv[1]
        port_number = sys.argv[2]
        HOST = host_name
        PORT= port_number
        print("No file name provided. Default filename is used.")
        fileName = "index.html"

    elif len(sys.argv) == 4:
        host_name = sys.argv[1]
        port_number = sys.argv[2]
        file_name = sys.argv[3]
        HOST = host_name
        PORT= port_number
        fileName = file_name
    else:
        print("No arguments provided. All default values are used.")
        HOST = "127.0.0.1"
        PORT = 8080
        fileName = "index.html"

    # create the client and make request
    user = HTTP(HOST, PORT, fileName)
    user.request()


if __name__ == "__main__":
    main()