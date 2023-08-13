from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from windows import set_dpi_awareness
from vaccine_data import Read_data

import bot_gui
from bot_gui import chat_bot


def Execution():
    # print("working")

    c1111.config(state ="normal")
    textc110.config(state ="disabled")
    user = user_input.get()
    try :
        result = chat_bot(user)
    except :
        result = ["You : "+user,"Bot : "+"Sorry I don't have answer.\n\n" ]
    c1111.insert("end"," "+result[0]+"\n"+" "+result[1]+"\n")
    c1111.config(state ="disabled")
    textc110.config(state ="normal")
    textc110.delete(0,END)


    


def Create_vaccine_center():
    """
    creates 6 labels for text,type(paid,free),state,district,pincodes,go button
    
    """
    typ =StringVar()
    state =StringVar()
    district =StringVar()
    pincode =StringVar()
    data =Read_data()
    def _type():
        state.set('')
        district.set('')
        pincode.set('')
        options = tuple(data.keys())
        ct.config(values = options)
    def states():
        district.set('')
        pincode.set('')
        t =typ.get()
        print(t)
        if(t!= ''):
            options = tuple(data[t].keys())
            cs.config(values = options)
        else:
            cs.config(values=())
    def districts():
        pincode.set('')
        t =typ.get()
        s =state.get()
        if(t!='' and s!=''):
            opt = tuple(data[t][s].keys())
            cd.config(values = opt)
        else:
            cd.config(values=())
    def pincodes():
        t =typ.get()
        s =state.get()
        d = district.get()
        if(t!='' and s!='' and d!=''):
            opt = tuple(data[t][s][d].keys())
            cp.config(values = opt)
        else:
            cp.config(values = ())
    def vaccination_centers():
        t = typ.get()
        s = state.get()
        d = district.get()
        p = pincode.get()
        m = (t =='' and s=='' and d=='' and p =='')
        result_string =str()
        if(not m):
            if(s==''):
                result =data[t]
                for x,y in result.items():
                    result_string+=(x+"\n")
                    for i,j in y.items():
                        result_string+=("\t"+i+"\n")
                        for k,l in j.items():
                            result_string+=("\t\t"+k+"\n")
                            for m in l:
                                result_string+=("\t\t\t"+"Center name : "+m["Center name"]+"\n")
                                result_string+=("\t\t\t"+"Location : "+m["Location"]+"\n")
                                result_string+=("\t\t\t"+"Vaccine Name : "+m["Vaccine Name"]+"\n")
                                result_string+=("\t\t\t"+"Age : "+m["Age"]+"\n\n")                     
            else:
                if(d ==''):
                    result = data[t][s]
                    for x,y in result.items():
                        result_string+=(x+"\n")
                        for i,j in y.items():
                            result_string+=("\t"+i+"\n")
                            for m in j:
                                result_string+=("\t\t"+"Center name : "+m["Center name"]+"\n")
                                result_string+=("\t\t"+"Location : "+m["Location"]+"\n")
                                result_string+=("\t\t"+"Vaccine Name : "+m["Vaccine Name"]+"\n")
                                result_string+=("\t\t"+"Age : "+m["Age"]+"\n\n")
                                
                        
                else:
                    if(p == ''):
                        result = data[t][s][d]
                        for x,y in result.items():
                            result_string+=(x+"\n")
                            for m in y:
                                result_string+=("\tCenter name : "+m["Center name"]+"\n")
                                result_string+=("\tLocation : "+m["Location"]+"\n")
                                result_string+=("\tVaccine Name : "+m["Vaccine Name"]+"\n")
                                result_string+=("\tAge : "+m["Age"]+"\n\n")
                    else:
                        result = data[t][s][d][p]
                        for m in result:
                            result_string+=("Center name : "+m["Center name"]+"\n")
                            result_string+=("Location : "+m["Location"]+"\n")
                            result_string+=("Vaccine Name : "+m["Vaccine Name"]+"\n")
                            result_string+=("Age : "+m["Age"]+"\n\n")
            
            
            text.config(state='normal')
            text.delete('1.0',"end")
            text.insert("end",result_string)
            text.config(state='disabled')
            
            
            
        

    L1 =ttk.Label(c100,text ="Vaccination Centers",padding=(5,5),font=("aerial",12,"bold"))
    L1.pack(side="top",pady=(5,0))
    L2 =ttk.Label(c100,anchor="n",padding=(5,5))
    lt =ttk.Label(L2,text="Type : ")
    ct =ttk.Combobox(L2,width =5,postcommand = _type,textvar = typ,state='readonly')    #   reference  https://anzeljg.github.io/rin2/book2/2405/docs/tkinter/ttk-Combobox.html
    lt.pack(side="top",padx=(0,2))
    ct.pack(side="top",padx=2)
    L2.pack(side="left",pady=(5,0),anchor ="n")
    L3 =ttk.Label(c100,anchor="n",padding=(5,5))
    ls =ttk.Label(L3,text="State : ")
    cs =ttk.Combobox(L3,width =20,postcommand = states,textvar = state,state='readonly')
    ls.pack(side ="top",padx=2)
    cs.pack(side="top",padx=2)
    L3.pack(side="left",pady=(5,0),anchor ="n")
    L4 =ttk.Label(c100,anchor="n",padding=(5,5))
    ld =ttk.Label(L4,text="District : ")
    cd =ttk.Combobox(L4,width =20,postcommand = districts,textvar = district,state='readonly')
    ld.pack(side ="top",padx=2)
    cd.pack(side="top",padx=2)
    L4.pack(side="left",pady=(5,0),anchor ="n")
    L5 =ttk.Label(c100,anchor="n",padding=(5,5))
    lp =ttk.Label(L5,text="Pincode : ")
    cp =ttk.Combobox(L5,width =7,postcommand = pincodes,textvar = pincode,state='readonly')
    lp.pack(side ="top",padx=2)
    cp.pack(side="top",padx=(2,2))
    L5.pack(side="left",pady=(5,0),anchor ="n")
    b =ttk.Button(c100,text ="Go",width=5,command =vaccination_centers)
    b.pack(side="left",padx =(4,0),anchor ="n",pady =(20,0))

set_dpi_awareness()  # gives high defination text


root = Tk()
text1 =StringVar()
root.title("Chat Bot")
root.geometry("920x720")
root.minsize(920,720)


frame0 = Frame(root,bg ='#CC7633')
frame1 = Frame(frame0,bg ="#e1d8b9",padx =8,pady=8)
contents = Frame(frame1,bg = "#CC9966")   # before color code #cccdcc
frame0.pack(fill ="both",expand =True)
frame1.pack(fill = "both",expand =True,padx =13,pady =13)
contents.pack(fill = "both",expand =True)

c0 = Frame(contents,bg ="#CC9966")            # before color code #cccdcc
c0.pack(fill = "x",side = 'top')
accuracy = StringVar(c0)
accuracy.set("Accuracy")   # use this for setting desired accuracy value

label_title = ttk.Label(c0,text = "COVID -19 CHAT BOT",padding =(5,5),background ="#FFFFCC")
label_accuracy = ttk.Label(c0,padding =(5,5),textvar =accuracy,background ="#FFFFCC")
label_title.pack(side ="left",padx =10,pady =10)
label_accuracy.pack(side ="right",padx =10,pady =10)

c1  = Frame(contents)
c1.pack(side = "left",fill = "both",expand=True,padx =10,pady =10)

c10 = ttk.Label(c1,width=28,padding=(0,10)) # upper frame for c1
c10.pack(fill = "y",side = "right",padx =(0,5),pady=(10,10))

c100 = ttk.Label(c10)
c100.pack(side="top")
c101 = ttk.Label(c10)                                             # for vaccination centers display
c101.pack(side="top",expand=True)
Create_vaccine_center()
text = Text(c101,width =50,height=28,state="disabled",wrap ="none")
scrollery =Scrollbar(c101,command =text.yview)
scrollerx =Scrollbar(c101,command =text.xview,orient =HORIZONTAL)
text.config(yscrollcommand = scrollery.set,xscrollcommand = scrollerx.set)
scrollery.pack(side="right",fill ="both")
scrollerx.pack(side="bottom",fill ="both")
text.pack(side ="right")



c11 = Frame(c1,bg = "#CC9966")      # has user input and display output
c11.pack(side = "right",fill = "both",expand=True,pady =(10,10),padx=(5,10))


c110 = Frame(c11,bg ="#CC9966")   # this frame is for user input and send button
c110.pack(side ="bottom",fill ="x")
buttonc110 = ttk.Button(c110,text = "send",padding=(2,2),width =8,command = Execution) # configure command property later
buttonc110.pack(side = "right",padx =(2,6),pady=(3,6))
user_input = StringVar(c110)
textc110 = ttk.Entry(c110,textvar = user_input)
textc110.pack(side ="right",fill = "both",expand =True,padx=(6,2),pady=(3,6))
output = StringVar(c11)


c111 = Frame(c11)
c111.pack(side ="bottom",fill = "both",expand =True,padx =6,pady=(6,2))

c1111 = Text(c111,wrap =WORD,state ="disabled")        #  state="disabled"alliging text to bottom right
c1110 =Scrollbar(c111,command =c1111.yview)
c1111.config(yscrollcommand = c1110.set)
c1110.pack(side="right",fill ='y')
c1111.pack(side="right",fill="both",expand=True)

root.mainloop()
