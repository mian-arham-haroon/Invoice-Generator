import tkinter
from tkinter import ttk
from tkinter import *
from docxtpl import DocxTemplate
import datetime
from tkinter import messagebox

invoice_list=[]
def add_item():
    qty= int (qty_spinbox.get())
    desc = desc_entry.get()
    price= float(price_spinbox.get())
    line_total=qty*price
    invoice_item=[qty,desc,price,line_total]
    tree.insert('',0,values=invoice_item)
    clear_item()
    invoice_list.append(invoice_item)
def clear_item():
    qty_spinbox.delete(0,END)
    qty_spinbox.insert(0,"1")
    desc_entry.delete(0,END)
    price_spinbox.delete(0,END)
    price_spinbox.insert(0,"0.0")
def new_invoice():
    first_name_entry.delete(0,END)
    last_name_entry.delete(0,END)
    phone_entry.delete(0,END)
    clear_item()
    tree.delete(*tree.get_children())
    invoice_list.clear()
def generate_invoice():
    doc=DocxTemplate("invoice_template.docx")
    name=first_name_entry.get()+last_name_entry.get()
    phone=phone_entry.get()
    subtotal=sum(item[3] for item in invoice_list)
    salestex=0.1
    total=subtotal*(1-salestex)

    doc.render({"name":name, 
                "phone":phone,
                "invoice_list": invoice_list,
                "subtotal":subtotal,
                "salestax":str(salestex*100)+"%",
                "total":total})  
    doc_name= "new_invoice"+name+datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S p")+".docx"
    doc.save(doc_name) 
    messagebox.showinfo("Sucessfully Update","Invoice Completed")
    new_invoice()


window = tkinter.Tk()
window.title("Inovice Generator Form")

frame=Frame(window)
frame.pack(padx=20,pady=10)

first_name_label=Label(frame,text="First Name")
first_name_label.grid(row=0,column=0)
first_name_entry=Entry(frame)
first_name_entry.grid(row=1,column=0)

last_name_label=Label(frame,text="Last Name")
last_name_label.grid(row=0,column=1)
last_name_entry=Entry(frame)
last_name_entry.grid(row=1,column=1)

phone_label=Label(frame,text="Phone")
phone_label.grid(row=0,column=2)
phone_entry=Entry(frame)
phone_entry.grid(row=1,column=2)

qty_label=Label(frame,text="Qty")
qty_label.grid(row=2,column=0)
qty_spinbox= Spinbox(frame,from_=1,to=100)
qty_spinbox.grid(row=3,column=0)

desc_label=Label(frame,text="Description")
desc_label.grid(row=2,column=1)
desc_entry=Entry(frame)
desc_entry.grid(row=3,column=1)

price_label=Label(frame,text="Unit Price")
price_label.grid(row=2,column=2)
price_spinbox= Spinbox(frame,from_=1,to=1000,increment=0.5)
price_spinbox.grid(row=3,column=2)

add_item_button=Button(frame,text="Add  Item",command=add_item)
add_item_button.grid(row=4,column=2,pady=5)

columns=('qty','desc','price','total')
tree=ttk.Treeview(frame,columns=columns,show="headings")
tree.heading('qty',text='Qty')
tree.heading('desc',text='Decsription')
tree.heading('price',text='Unit Price')
tree.heading('total',text='Total')

tree.grid(row=5,column=0,columnspan=3,padx=20,pady=10)


save_invoice_button=Button(frame,text="Generate Invoice",command=generate_invoice)
save_invoice_button.grid(row=6,column=0,columnspan=3,sticky="news",padx=20,pady=5)
new_invoice_button=Button(frame,text="New Invoice",command=new_invoice)
new_invoice_button.grid(row=7,column=0,columnspan=3,sticky="news",padx=20,pady=5)


window.mainloop()