from tkinter import*
root=Tk()
root.title("ASCII codes")
root.configure(background="yellow")
root.geometry("500x500")

lbl_1=Label(root,text="ASCII Converter")
lbl_1.place(relx=0.5,rely=0.1,anchor=CENTER)

lbl_2=Label(root, text="Enter your name below")
lbl_2.place(relx=0.5, rely=0.3, anchor=CENTER)

text=Entry(root)
text.place(relx=0.5,rely=0.4,anchor=CENTER)

lbl_3=Label(root,text="Your converted name is ")
lbl_3.place(relx=0.5,rely=0.7,anchor=CENTER)

def convert():
    insert=text.get()
    for i in insert:
        asci=str(ord(i))
        lbl_3["text"]+=asci+" "

btn=Button(root,text="Convert",command=convert)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)




root.mainloop()




