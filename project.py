""" A parcel service office wants to develop a system to manage their dispatch service. The
parcel should be assigned a unique tracking number using which the status of the parcel can
be tracked. The sender and the receiver address, and contact details have to be maintained in
the system. Once the parcel has reached the destination office, the sender and the receiver
should be notified. It should be possible to fetch a location and date-wise list of deliveries
from the system. Even after completion of the delivery, the system should be able fetch the
relevant details using the tracking number. """


from tkinter import *
import json
import os
from datetime import date

def login(username,password,label):
    if username=="admin" and password=="123":
        label.config(text="")
        new1=Toplevel()
        new1.title("Courier System")
        new1.geometry('800x450+300+300')
        new1.iconbitmap("untitled.jpg")

        label1=Label(new1,text="Hi Administrator",font = ('',20))
        label1.grid(row=2,column=0)

        label2=Label(new1,text="Click any button",font = ('',15))
        label2.grid(row=4,column=0)

        button7=Button(new1,text="Add a delivery",font = ('',15),command=details)
        button7.grid(row=4,column=1)

        button2=Button(new1,text="Parcel Information",font = ('',15),command=bar)
        button2.grid(row=6,column=1)
            
        button3=Button(new1,text="Date-wise list of deliveries",font = ('',15),command=dwise)
        button3.grid(row=8,column=1)

        btn=Button(new1,text="Location-wise list of deliveries",font=('',15),command=lwise)
        btn.grid(row=10,column=1)
        
        btn=Button(new1,text="Pending deliveries",font=('',15),command=pending)
        btn.grid(row=12,column=1)

        btn2=Button(new1,text="Delivered packages",font=('',15),command=delivered)
        btn2.grid(row=14,column=1)

        button4=Button(new1,text="Help",font = ('',15),command=help)
        button4.grid(row=16,column=1)

        

        store1=e.get()

        store2=f.get()

    else:
        label.config(text="wrong credentials. please try again")

def bar():

    new2=Toplevel()
    new2.title("Status")
    new2.geometry('800x450+300+300')
    new2.iconbitmap("untitled.jpg")

    label3=Label(new2,text="Tracking Number")
    label3.grid()

    g=Entry(new2,width=50)
    g.grid()

    button5=Button(new2,text="->",command=lambda:parcel_info(g.get()))
    button5.grid()

def change(lbl,status,trackno,saddress,raddress,location):
    if (status=="not delivered"):
        dt=date.today().strftime("%d/%m/%Y")
        f=open("data.json","r")
        g=open("temp.json","w")
        l=json.load(f)
        l[trackno]["status"]="delivered"
        l[trackno]["date"]=dt
        g.write(json.dumps(l))
        g.close()
        f.close()
        os.remove("data.json")
        os.rename("temp.json","data.json")
        
        lbl.config(text="delivered")
    
        s1={"from":saddress,"to":raddress,"trackno":trackno}
        s2={"from":saddress,"date":dt,"trackno":trackno,"to":raddress}
        f=open("datewise.json","r")
        g=open("locationwise.json","r")
        h=open("temp1.json","w")
        i=open("temp2.json","w")
        try:
            d1=json.load(f)
        except:
            d1={}
        try:
            d2=json.load(g)
        except:
            d2={}
        if dt in d1.keys():
            d1[dt].append(s1)
        else:
            d1[dt]=[s1]

        if location.lower() in d2.keys():
            d2[location.lower()].append(s2)
        else:
            d2[location.lower()]=[s2]
   
        h.write(json.dumps(d1))
        i.write(json.dumps(d2))
        f.close()
        g.close()
        h.close()
        i.close()
        os.remove("datewise.json")
        os.remove("locationwise.json")
        os.rename("temp1.json","datewise.json")
        os.rename("temp2.json","locationwise.json")

        

def parcel_info(trackno):

    new3=Toplevel()
    new3.title("Parcel information")
    new3.geometry('800x450+300+300')
    new3.iconbitmap("untitled.jpg")

    label4=Label(new3,text="Status:")
    label4.grid()
    f=open("data.json",'r')
    try:
        l=json.load(f)
        status=l[trackno]["status"]
        sname=l[trackno]["sender name"]
        rname=l[trackno]["receiver name"]
        saddress=l[trackno]["sender address"]
        raddress=l[trackno]["receiver address"]
        scontact=l[trackno]["Sender contact"]
        rcontact=l[trackno]["Recever contact"]
        loc=l[trackno]["location"]
        
    except:
        labelerror=Label(new3,text="Invalid track number")
        labelerror.grid()
        f.close()
        return
    
    label5=Label(new3,text=status)
    label5.grid()


    label6=Label(new3,text="Sender name:")
    label6.grid()

    label7=Label(new3,text=sname)
    label7.grid()

    label8=Label(new3,text="Sender address:")
    label8.grid()

    label9=Label(new3,text=saddress)
    label9.grid()

    label10=Label(new3,text="Sender Contact number:")
    label10.grid()

    label11=Label(new3,text=scontact)
    label11.grid()

    label12=Label(new3,text="Reciever name:")
    label12.grid()

  
    label13=Label(new3,text=rname)
    label13.grid()

    label14=Label(new3,text="Reciever address:")
    label14.grid()

    label15=Label(new3,text=raddress)
    label15.grid()

    label16=Label(new3,text="Reciever Contact number:")
    label16.grid()

    label17=Label(new3,text=rcontact)
    label17.grid()

    lbll=Label(new3,text="Location of delivery:")
    lbll.grid()
    
    lbl=Label(new3, text=loc)
    lbl.grid()

    btn=Button(new3, text="change status to delivered",command=lambda:change(label5,status,trackno,saddress,raddress,loc))
    btn.grid()

    

def dwise():

    new5=Toplevel()
    new5.title("Datewise List")
    new5.geometry('800x450+300+300')
    new5.iconbitmap("untitled.jpg")

    label18=Label(new5,text="Enter the date (DD/MM/YYYY):")
    label18.grid()

    h=Entry(new5,width=50)
    h.grid()

    button6=Button(new5,text="Check",command=lambda:dispd(h.get()))
    button6.grid()
    
def lwise():

    new5=Toplevel()
    new5.title("Datewise List")
    new5.geometry('800x450+300+300')
    new5.iconbitmap("untitled.jpg")

    label18=Label(new5,text="Enter the location:")
    label18.grid()

    h=Entry(new5,width=50)
    h.grid()

    button6=Button(new5,text="Check",command=lambda:displ(h.get()))
    button6.grid()
    
def dispd(dt):

    new6=Toplevel()
    new6.title("Datewise List")
    new6.geometry('800x450+300+300')
    new6.iconbitmap("untitled.jpg")
    f=open("datewise.json","r")
    try:
        l=json.load(f)
        r=l[dt]
    except:
        r=[]
        lbl=Label(new6,text="No records with given date")
        lbl.grid()
        f.close()
        return
    f.close()
    fr=Frame(new6)
    fr.pack(fill=BOTH,expand=1)
    cnv=Canvas(fr)
    cnv.pack(side=LEFT, fill=BOTH, expand=1)
    sc=Scrollbar(fr,orient=VERTICAL, command= cnv.yview)
    sc.pack(side=RIGHT,fill=Y)
    cnv.configure(yscrollcommand=sc.set)
    cnv.bind('<Configure>',lambda e: cnv.configure(scrollregion=cnv.bbox("all")))
    fr2=Frame(cnv)
    cnv.create_window((0,0),window=fr2,anchor="nw")
    c=0
    for i in r:
        f=i["from"]
        t=i["to"]
        tr=i["trackno"]
        lbl=Label(fr2,text="from: "+f+"|")
        lbl.grid(row=c,column=0)
        lb2=Label(fr2,text="to: "+t+"|")
        lb2.grid(row=c,column=4)
        lb3=Label(fr2,text="track no: "+tr)
        lb3.grid(row=c,column=8)
        c+=1

def displ(loc):

    new6=Toplevel()
    new6.title("Locationwise List")
    new6.geometry('800x450+300+300')
    new6.iconbitmap("untitled.jpg")
    f=open("locationwise.json","r")
    try:
        l=json.load(f)
        r=l[loc]
    except:
        r=[]
        lbl=Label(new6,text="No records with given location")
        lbl.grid()
        f.close()
        return
    f.close()
    fr=Frame(new6)
    fr.pack(fill=BOTH,expand=1)
    cnv=Canvas(fr)
    cnv.pack(side=LEFT, fill=BOTH, expand=1)
    sc=Scrollbar(fr,orient=VERTICAL, command= cnv.yview)
    sc.pack(side=RIGHT,fill=Y)
    cnv.configure(yscrollcommand=sc.set)
    cnv.bind('<Configure>',lambda e: cnv.configure(scrollregion=cnv.bbox("all")))
    fr2=Frame(cnv)
    cnv.create_window((0,0),window=fr2,anchor="nw")
    c=0
    for i in r:
        f=i["from"]
        to=i["to"]
        t=i["date"]
        tr=i["trackno"]
        lbl=Label(fr2,text="from: "+f+"|")
        lbl.grid(row=c,column=0)
        lb3=Label(fr2,text="to: "+to+"|")
        lb3.grid(row=c,column=4)
        lb2=Label(fr2,text="date: "+t+"|")
        lb2.grid(row=c,column=8)
        lb3=Label(fr2,text="track no: "+tr)
        lb3.grid(row=c,column=16)
        c+=1

def pending():

    new6=Toplevel()
    new6.title("Pending packages")
    new6.geometry('800x450+300+300')
    new6.iconbitmap("untitled.jpg")
    f=open("data.json","r")
    try:
        l=json.load(f)
    except:
        r=[]
        lbl2=Label(new6,text="No pending deliveries")
        lbl2.grid()
        f.close()
        return
    f.close()
    fr=Frame(new6)
    fr.pack(fill=BOTH,expand=1)
    cnv=Canvas(fr)
    cnv.pack(side=LEFT, fill=BOTH, expand=1)
    sc=Scrollbar(fr,orient=VERTICAL, command= cnv.yview)
    sc.pack(side=RIGHT,fill=Y)
    cnv.configure(yscrollcommand=sc.set)
    cnv.bind('<Configure>',lambda e: cnv.configure(scrollregion=cnv.bbox("all")))
    fr2=Frame(cnv)
    cnv.create_window((0,0),window=fr2,anchor="nw")
    flag=0
    for i in l:
        if l[i]["status"]=="not delivered":
            flag=1
            lb3=Label(fr2,text="track no: "+i)
            lb3.grid()
    if (not flag):
        lbl2=Label(fr2,text="No pending deliveries")
        lbl2.grid()
        
def delivered():

    new6=Toplevel()
    new6.title("Delivered packages")
    new6.geometry('800x450+300+300')
    new6.iconbitmap("untitled.jpg")
    f=open("data.json","r")
    try:
        l=json.load(f)
    except:
        r=[]
        lbl2=Label(new6,text="No records")
        lbl2.grid()
        f.close()
        return
    f.close()
    fr=Frame(new6)
    fr.pack(fill=BOTH,expand=1)
    cnv=Canvas(fr)
    cnv.pack(side=LEFT, fill=BOTH, expand=1)
    sc=Scrollbar(fr,orient=VERTICAL, command= cnv.yview)
    sc.pack(side=RIGHT,fill=Y)
    cnv.configure(yscrollcommand=sc.set)
    cnv.bind('<Configure>',lambda e: cnv.configure(scrollregion=cnv.bbox("all")))
    fr2=Frame(cnv)
    cnv.create_window((0,0),window=fr2,anchor="nw")
    flag=0
    c=0
    for i in l:
        if l[i]["status"]=="delivered":
            flag=1
            lbl=Label(fr2,text="track no: "+i +"|")
            lbl.grid(row=c,column=0)
            lb2=Label(fr2,text="location: "+l[i]["location"]+"|")
            lb2.grid(row=c,column=4)
            lb3=Label(fr2,text="date: "+l[i]["date"])
            lb3.grid(row=c,column=8)
            c+=1
    if (not flag):
        lbl2=Label(fr2,text="No records")
        lbl2.grid()
        
  
def help():

    new7=Toplevel()
    new7.title("Help Desk")
    new7.geometry('800x450+300+300')
    new7.iconbitmap("untitled.jpg")

    rules=["Status helps us to track the parcel by entering the tracking number",
    "Parcel Information helps us to check the deatails of the parcel",
    "DateWise List helps us to show the parcel delivered at entered location"]
    
    for i7 in rules:
        label23=Label(new7,text=i7)
        label23.grid()
def writefile(i,j,k,l,m,n,o):
    d={}
    d["receiver name"]=l.get()
    d["receiver address"]=m.get()
    d["Recever contact"]=n.get()
    d["Sender contact"]=k.get()
    d["sender address"]=j.get()
    d["sender name"]=i.get()
    d["status"]="not delivered"
    d["location"]=o.get()
   
    with open("temp.json",'w') as g:
        f=open("data.json","r")
        try:
            l=json.load(f)
        except:
            l={}
        if (len(l)):
            t=int(list(l.keys())[-1])+1
            l[t]=d
            g.write(json.dumps(l))
        else:
            l[0]=d
            g.write(json.dumps(l))

        f.close()
    os.remove("data.json")
    os.rename("temp.json","data.json")

def details():
  

    new8=Toplevel()
    new8.title("Details")
    new8.geometry('800x450+300+300')
    new8.iconbitmap("untitled.jpg")

    label24=Label(new8,text="Sender Name:")
    label24.grid()

    i=Entry(new8,width=50)
    i.grid()
    

    label25=Label(new8,text="Sender Address:")
    label25.grid()

    j=Entry(new8,width=50)
    j.grid()


    label26=Label(new8,text="Sender Contact No:")
    label26.grid()

    k=Entry(new8,width=50)
    k.grid()
    

    label27=Label(new8,text="Reciever Name:")
    label27.grid()

    l=Entry(new8,width=50)
    l.grid()


    label28=Label(new8,text="Reciever Address:")
    label28.grid()

    m=Entry(new8,width=50)
    m.grid()


    label29=Label(new8,text="Reciever ContactNo:")
    label29.grid() 

    n=Entry(new8,width=50)
    n.grid()

    label30=Label(new8,text="city/town:")
    label30.grid()

    o=Entry(new8,width=50)
    o.grid()

  

    B=Button(new8,text="submit",font = ('',15),command=lambda: writefile(i,j,k,l,m,n,o))
    B.grid()

  



root=Tk()
root.title("Courier System")
root.geometry('800x450+300+300')
root.iconbitmap("untitled.jpg")



mylabel3=Label(root,text="Administrator Login",font = ('',20))
mylabel3.grid(row=0,column=0)

table=Frame(root,padx=10,pady=10)
table.configure(background="lightgreen")
table.grid(padx=50,pady=50)


e=Entry(table,width=50,font = ('',15),bd = 3)
e.grid(row=2,column=3)


f=Entry(table,width=50,bd = 3,font = ('',15),show = '*')
f.grid(row=4,column=3)

mylabel1=Label(table,text="Username",font = ('',15))
mylabel2=Label(table,text="Password",font = ('',15))
mylabel3=Label(root,text="",font = ('',8))
mylabel1.grid(row=2,column=2)
mylabel2.grid(row=4,column=2)
mylabel3.grid(row=30,column=0)

mybutton1=Button(table,text="Login",font = ('',15),command=lambda: login(e.get(),f.get(),mylabel3))
mybutton1.grid(row=6,column=3)
table.grid()

root.mainloop()


