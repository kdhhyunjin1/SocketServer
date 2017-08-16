import socket
import time
import threading
from tkinter import *

self = Tk()

HOST = "127.0.0.1"
PORT = 22
conn1 = ""
addr1 = ""
name1 = ""
conn2 = ""
add2 = ""
name2 = ""


class ServInfo:
    def __init__(self):
        """self.master = Master
        Master.geometry("200x40")
        self.mainFrame = Frame(self.master)
        self.mainFrame.pack(fill=X)

        self.frame2 = Frame(self.mainFrame)
        self.frame2.pack(fill=X)
        self.portLabel = Label(self.frame2)
        self.portLabel.configure(text="Port", width=10)
        self.portLabel.pack(side=LEFT)
        self.portLabel.pack(side.frame2)
        self.entry2.pack(side=LEFT)

        self.frame3 = Frame(self.mainFrame)
        self.frame3.pack(fill=X)
        self.button = Button(self.frame3)
        self.button.configure(text = "OK", command=self.subnit)
        self.button.pack(fill=X)"""

        t = Tk()
        t.title("Server ServInfo")
        t.geometry("250x67")
        t.resizable(width=FALSE, height=FALSE)
        
        """t.f1 = Frame(t)
        t.f1.pack(fill=X)
        t.ipLabel = Label(t.f1)
        t.ipLabel.configure(text="서버 IP", width=10)
        t.ipLabel.pack(side=LEFT)
        self.entry1 = Entry(t.f1)
        self.entry1.pack(side=LEFT)"""

        t.f2 = Frame(t)
        t.f2.pack(fill=X)
        t.portLabel = Label(t.f2)
        t.portLabel.configure(text="포트", width=10)
        t.portLabel.pack(side=LEFT)
        self.entry2 = Entry(t.f2)
        self.entry2.pack(side=LEFT)

        t.f3 = Frame(t)
        t.f3.pack(fill=X)
        t.button = Button(t.f3)
        t.button.configure(text = "OK", width=10, command=self.submit)
        t.button.pack(fill=X)

    def submit(self):
        global PORT
        PORT = int(input(self.entry2.get()))
        t.quit()
        t.destroy()

        root = Tk()
        app = subApp(root)
        root.mainloop()

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.bind((HOST, PORT))
        sock.listen(2)

        flag=0
        connectflag = 0

    def socket1():
        global conn1, addr1, name1, flag, connectflag
        flag += 1
        conn1, addr1 = sock.accept()
        print ("System : "+str(addr1[1])+" is connected")
        connectflag += 1
        name1 = conn1.recv(1024)
        name1 = name1[:name1.Index("\n")]
        sendMessage("[System]", name1+" was joined")
        while True:
            data1 = conn1.recv(1024)
            if data1=="[QUIT]":
                break
            if data1:
                sendMessage(name1, data[:data1.index("\n")])
        print ("System : "+str(addr1[1])+" is disconnected")
        flag -= 1
        connectflag -= 1
        conn1.close()

        def socket2():
            global conn2, addr2, name2, flag, connectflag
            flag += 2
            conn2, addr2 = sock.accept()
            print ("System : "+str(addr2[1])+" is connected")
            connectflage += 2
            name2 = conn2.recv(1024)
            name2 = name2[:name2.index("\n")]
            sendMessage("[System]", name2+" was joined")
            while True:
                data2 = conn2.recv(1024)
                if data2 == "[QUIT]":
                    break
                if data2:
                    sendMessage(name2, data[:data2.indes("\n")])
            print ("System : "+str(addr1[1])+" is disconnected")
            flag -= 2
            connectflag -= 2
            conn2.close()

            def sendMessage(name, data):
                if connectflag==1:
                    conn1.send(name+" : "+data)
                if connectflag==2:
                    conn2.send(name+" : "+data)
                if connectflag==3:
                    conn1.send(name+" : "+data)
                    conn2.send(name+" : "+data)
            socket1_th = threading.Thread(target = socket1)
            socket2_th = threading.Thread(target = socket2)

            socket1_th.start()
            socket2_th.start()

            t.mainloop()
ServInfo()
