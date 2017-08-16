from tkinter import *



class ChatUI:
    def __init__(self):
        ui = Tk()
        ui.title("Chat")
        ui.geometry("400x600")
        ui.resizable(width=FALSE, height=FALSE)

        #ui.master = Master
        #ui.materFrame = Frame(Master)
        #ui.masterFrame.pack(fill=X)

        ui.f1=Frame(ui)
        ui.f1.pack(fill=X)

        ui.messageLog = Text(ui.f1)
        ui.scrollbar = Scrollbar(ui.f1, command=ui.messageLog.yview)
        ui.messageLog.configure(width=56, height=40, state="disabled", yscrollcommand=ui.scrollbar.set)
        ui.messageLog.grid()
        ui.messageLog.pack(side=LEFT, fill="both", expand=True)
        
        ui.scrollbar.pack(side=RIGHT, fill=Y, expand=False)

        ui.f2 = Frame(ui)
        ui.f2.pack(fill=X)
        ui.label = Label(ui.f2, text="채팅창")
        ui.label.pack(fill=X)

        ui.f3 = Frame(ui)
        ui.f3.pack(fill=X)

        ui.f3_1 = Frame(ui.f3, padx=2, pady=1)
        ui.f3_1.pack(fill=X)
        ui.input = Text(ui.f3_1, width=48, height=4)
        ui.input.pack(side=LEFT)
        ui.sendButton = Button(ui.f3_1, text="보내기")
        ui.sendButton.pack()
        #ui.sendButton.bind("<Return>", ui.buttonClicked_sub)
        #ui.input.bind("<KeyRelease-Return>", ui.buttonClicked_sub)

        ui.mainloop()

    def logRefresh(self, data):
        ui.messageLog.configure(state="normal")
        ui.messageLog.insert(END, "\n"+data)
        ui.messageLog.configure(state="disabled")

    def buttonClicked(self):
        ui.sendMessage()

    def buttonClicked_sub(self, event):
        ui.sendMessage()

    def sendMessage(self):
        global flag
        message = ui.input.get(1.0, END)
        sock.send(message)
        if flag:
            ui.label.configure(text="당신의 닉네임은"+"'"+message[:message.Index("\n")]+"'")
            flag = False
        ui.input.delete(1.0, END)

#-------------------------------------------------------
        
class ServInfo:
    def __init__(self):
        #self.master = Master
        #Master.geometry("200x67")
        #self.mainFrame = Frame(self.master)
        #self.mainFrame.pack(fill=X)

        t = Tk()
        t.title("Client ServInfo")
        t.geometry("250x67")
        t.resizable(width=FALSE, height=FALSE)

        t.f1 = Frame(t)
        t.f1.pack(fill=X)
        t.ipLabel = Label(t.f1)
        t.ipLabel.configure(text="서버 IP", width=10)
        t.ipLabel.pack(side=LEFT)
        self.entry1 = Entry(t.f1)
        self.entry1.pack(side=LEFT)

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

        
             
        """
        self.frame1 = Frame(self.mainFrame)
        self.frame1.pack(fill=X)
        self.ipLabel = Label(self.frame1)
        self.ipLabel.configure(text="Server IP", width=10)
        self.ipLabel.pack(side=LEFT)
        self.entry1 = Entry(self.frame1)
        self.entry1.pack(side=LEFT)

        self.frame2 = Frame(self.mainFrame)
        self.frame2.pack(fill=X)
        self.portLabel = Label(self.frame2)
        self.portLabel.configure(text="Port", width=10)
        self.portLabel.pack(side=LEFT)
        self.entry2 = Entry(self.frame2)
        self.entry2.pack(side=LEFT)


        self.frame3 = Frame(self.mainFrame)
        self.frame3.pack(fill=X)
        self.button = Button(self.frame3)
        self.button.configure(text = "OK", command=self.submit)
        self.button.pack(fill=X)"""
        
    def submit(self):
        global HOST, PORT
        HOST = self.entry1.get()
        PORT = int(input(self.entry2.get()))
        self.quit()
        self.destroy()
        ChatUI()
    def interface():
        root.mainloop()
    def network():
        sock.connect((HOST, PORT))
        while True:
            data = sock.recv(1024)
            if data:
                app.logRefresh(data)

        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        root2 = Tk()
        app2 = subApp(root2)
        root2.mainloop()

        root = Tk()
        app = myApp(root)

        thread1 = threading.Thread(target = interface)
        thread2 = threading.Thread(target = network)

        thread1.start()
        thread2.start()

        t.mainloop()
        
"""
        disp=Label(f, text='chat')
        disp.grid(row=300, column=500)
        self.name=StringVar()    
        dime=Entry(f,textvariable=self.name)
        dime.grid(row=300, column=500)
"""

ServInfo()

