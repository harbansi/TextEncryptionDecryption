import tkinter as tk
import tkinter.font as tkfont
from tkinter import *  
from tkinter.ttk import *

# Creating a window
root = tk.Tk()

# For changing the icon of the title bar
root.iconbitmap(r'favicon.ico')
root.title("Text Encryptor-Decryptor Using Caeser cipher")
root.geometry("450x550") 
root.resizable(width=FALSE, height=FALSE)

# Creating a canvas 
canvas = tk.Canvas(root, height=550, width=450, bg='#222831')
canvas.pack()
bold_font = tkfont.Font(family="Lora",size=15,weight="bold")

# Creating a label1 
label1 = tk.Label(root,text= "Enter the Text",width=21,fg="#f9f3f3",bg="#30475e")
label1.config(font=bold_font)
canvas.create_window(225,100,window=label1)
user_text1 = tk.Entry(root)
user_text1.config(font=bold_font)
canvas.create_window(225,140,window=user_text1,width=200,height=27)

#create label2 
key_value = tk.Label(root,text= "Enter the Key",width=21,fg="#f9f3f3",bg="#30475e")
key_value.config(font=bold_font)
canvas.create_window(225,180,window=key_value)
user_text2 = tk.Entry(root)
user_text2.config(font=bold_font)
canvas.create_window(225,220,window=user_text2,width=200,height=27)


#create label3
label2 = tk.Label(root,text= "Choose the Operation",width=21,fg="#f9f3f3",bg="#222831")
label2.config(font=bold_font)
canvas.create_window(225,270,window=label2)

# Tkinter Variable 
v = tk.IntVar()

# Defined a function choice
def choice():
  # Retrieve the value of the radio button
    x = v.get()
    if(x==1):
        encryption()
    elif(x==2):
        decryption()


# Encryption function
def encryption():
  # Get the user entered value
    plain_text = user_text1.get()
    cipher_text = ""
    key = int(user_text2.get())

    for i in range(len(plain_text)):
        letter = plain_text[i]
  # UpperCase Condition
        if(letter.isupper()):
            cipher_text+=chr((ord(letter)+key-65)%26+65)
        else:
  # LowerCase Condition
            cipher_text+=chr((ord(letter)+key-97)%26+97)

    label3 =tk.Label(root,text=cipher_text,width=21,bg="light yellow")
    label3.config(font=bold_font)
    canvas.create_window(220,420,window=label3)

#decryption function 
def decryption():
  # Get the user entered values
    cipher_text = user_text1.get()
    plain_text = ""
    key = int(user_text2.get())

    for i in range(len(cipher_text)):
        letter = cipher_text[i]
  # Uppercase condition
        if(letter.isupper()):
            plain_text+=chr((ord(letter)-key-65)%26+65)
        else:
  # Lowercase condition
            plain_text+=chr((ord(letter)-key-97)%26+97) 

    label4 =tk.Label(root,text=plain_text,width=21,bg="light yellow")
    label4.config(font=bold_font)
    canvas.create_window(220,420,window=label4)

# Radio Button for Encryption and Decryption
label5=tk.Radiobutton(root, text="Encryption",padx = 20, variable=v, value=1,command=choice,bg="light yellow")
label5.config(font=bold_font)
canvas.create_window(120,320,window=label5)
 
label6=tk.Radiobutton(root, text="Decryption",padx = 20, variable=v, value=2,command=choice,bg="light yellow")
label6.config(font=bold_font)
canvas.create_window(320,320,window=label6)

# Creating a label with a text and attaching it to the root
label7 =tk.Label(root,text="Converted Text ",width=21,fg="#f9f3f3",bg="#30475e")
label7.config(font=bold_font)
canvas.create_window(220,380,window=label7)
root.mainloop()

