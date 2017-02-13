#!/usr/bin/python
import zmq
import sys

context=zmq.Context()

socket=context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

if len(sys.argv) < 2:
    sys.exit()
query=sys.argv[1]
socket.send(query)
answer=socket.recv()

print "{} {}".format(answer, query)


