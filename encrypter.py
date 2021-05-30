from tkinter import *
root=Tk()
root.title('encryptor')
#root.geometry('400x600')

label=Label(root,text='enter your message to encrypt or decrpyt',bg='#acc4f1',borderwidth=10).grid(row=0,columnspan=4,column=0,pady=20)

entry1=Entry(root)
entry1.grid(row=1,rowspan=3,columnspan=2,column=0,pady=20)

label1=Label(root,text='your encrypted/decrpyted message :',bg='#acc4f1').grid(row=5,columnspan=4,column=0,pady=20)
en_label=Entry(root)
en_label.grid(row=6,column=0,columnspan=2,pady=20)




def encrypter(*args):
	en_label.delete(0,END)
	message=entry1.get()
	entry1.delete(0,END)
	en_message=list(map(lambda a:chr(ord(a)+5),message))
	en_message1=''.join(map(str,en_message))
	en_label.insert(0,en_message1)

def decrypter(*args):
	en_label.delete(0,END)
	message=entry1.get()
	entry1.delete(0,END)
	en_message=list(map(lambda a:chr(ord(a)-5),message))
	en_message1=''.join(map(str,en_message))
	en_label.insert(0,en_message1)

encrypt_button=Button(root,text='encrypt',command=encrypter).grid(row=4,column=0,pady=20)
encrypt_button=Button(root,text='decrypt',command=decrypter).grid(row=4,column=1,pady=20)









root.mainloop()