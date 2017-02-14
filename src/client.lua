zmq=require "zmq"
ctx=zmq.init(1)
socket=ctx:socket(zmq.REQ)
socket:connect("tcp://localhost:5555")

socket.send("test.com")

r=socket:recv()
if r == "false" then
    print "bad dns"
end
socket:close()
ctx:term()
