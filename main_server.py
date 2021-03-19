"""
Name : Yunika Upadhayaya
ID: 1001631183
Date: 03/08/2021
CSE 4344 - Project 1
"""

# importing modules
from socketserver import ThreadingMixIn
from http.server import BaseHTTPRequestHandler, HTTPServer
import glob
import os
import sys

# default values
HOST = "127.0.0.1"
PORT = 8080
MAIN_DEFAULT = "./index.html"


# this class handles the request send by client
class HandleRequest(BaseHTTPRequestHandler):
    def do_GET(self):
        print("\n~~~~~~~~~~~~~Connected~~~~~~~~~~~~~\n")
        print("Client Port Number: " + str(self.client_address[1]))
        print("Client IP Address: " + self.address_string())
        print("Socket Family: " + str(self.connection.family))
        print("Socket Type: " + str(self.connection.type))
        print("Socket Address: " + str(self.connection.getsockname()))
        print("Socket Protocol: " + str(self.connection.proto))
        print("Peer Name: " + str(self.connection.getpeername()))

        path_file = check_file(self.path)

        # if the file is in the directory
        if path_file is not None:
            self.send_response(200)
            self.end_headers()

            with open(path_file, 'rb') as upload:
                file = upload.read()
                self.wfile.write(file)
            print("\n~~~~~~~~~~~~~Processed~~~~~~~~~~~~~\n")
        # if no file in the directory
        else:
            self.send_response(404)
            self.end_headers()
        return


class MultiThreadedHTTP(ThreadingMixIn, HTTPServer):
    """
    Class to handle the threads for httpserver
    """


# function that checks for the validity of port number
def check_port(portNum):
    try:
        PORT = int(portNum)
    except:
        print("Using port number 8080 by default. Provided port number cannot be accepted.")
    return portNum


# function to check the validity of the path of the file name
def check_file(name_file):
    if name_file == '/':
        return MAIN_DEFAULT
    # if the path of the file is valid
    else:
        track = glob.glob("." + name_file)
        if not track:  # path is not valid
            return None
        else:
            for path in track:
                if os.path.isfile(path):
                    return path  # path is found
            return None


def main():
    global PORT
    if len(sys.argv) <= 1:
        print("No port number provided. Default value 8080 is used.")
    else:
        port_number = int(sys.argv[1])
        PORT = check_port(port_number)

    try:
        server = MultiThreadedHTTP((HOST, PORT), HandleRequest)
        print("Server started....\n")
        server.serve_forever()
    except:
        server.server_close()  # close the server


if __name__ == '__main__':
    main()
