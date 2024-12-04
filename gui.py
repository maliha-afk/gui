from tkinter import *

screen=Tk()
screen.title("My AI")
screen.config(bg="mistyrose2")


def sendmessage():
    usermessage=prompt.get()
    chatlog.config(state=NORMAL)
    chatlog.insert(END,f"YOU: {usermessage}\n")
    

chatlog=Text(screen,height=20,width=50)
chatlog.pack(padx=10,pady=5)


prompt=Entry(screen,width=40)
prompt.pack(padx=10,pady=10)


send=Button(screen,text="send",command=sendmessage,padx=10,pady=5)
send.pack(padx=10,pady=10)


screen.mainloop()