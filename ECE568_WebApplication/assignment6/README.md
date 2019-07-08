# ECE 568: Web application (Assignment 6)

**Network Programming.**

A pair of web client and server. Achieved simple TCP transfer functions.

## environment

macOS Mojave(10.14.4)

python(3.7.1)

## getting started

open the command console and switch to the root directory of py files.

run the server at first.

```python
python server.py
```

the server would open the port 5680 of computer.

then run the client.

```python
python client.py
```

if the client can connect the server, it would show

```python
connect successfully!
```

## function instruction

- GET:
  
  Client input: GET <Test.txt>  Server output: The content of Test.txt

- BOUNCE
  
  Client input BOUNCE \<Hello World>  Server output: Hello World

- EXIT
  
  For EXIT command, print out the default value/message.
  
  For EXIT \<code> command, you should print out the "code".

## example

client :

```txt
python client.py

please enter your command:GET hello.txt
hello world

please enter your command:BOUNCE heelo world
heelo world

please enter your command:EXIT bye
```

server:

```txt
python server.py

wating for connection
Accept new connection from 127.0.0.1:58372...

Filename: hello.txt
File content: hello world

bounce content: heelo world

Exit infomation: bye

Connection from 127.0.0.1:58372 closed.
```

## shutdown

You can close the client directly, or you can ues EXIT command to close.

If you want to close the server, use

```bash
macOS: command + c
Windows/Linux: Crtl + c
```

to make sure the process is killed.
