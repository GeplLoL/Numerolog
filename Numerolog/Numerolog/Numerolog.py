from tkinter import *
def Loe_failist(fail:str)->list:
    f=open(fail,'r',encoding="utf-8-sig")
    jarjend=[]
    for rida in f:
        jarjend.append(rida)
    f.close()
    return "".join(jarjend)
def Kirjuta_failisse(fail:str,jarjend:list):
     f=open(fail,'w',encoding="utf-8-sig")
     for line in jarjend:
        f.write(line)
     f.close()
n=0
def findArv(event):
    global n
    n+=1
    if n>0:
        global name
        name=ent.get()
        name=name.lower()
        intab = "аисъбйтывкуьглфэдмхюенцяёочжпшзрщ"
        intabList=list(intab)
        propet=Tk()
        propet.geometry("1920x1080")
        propet.title("Propeties")
        lblTest=Label(propet, text="",font="Arial 15")
        lblTest.pack()
        if all(char in intabList for char in name):
            intab = "аисъбйтывкуьглфэдмхюенцяёочжпшзрщ"
            out="111122223333444455556666777888999"
            trans=name.maketrans(intab,out)
            outi=name.translate(trans)
            outii=list(map(int,outi))
            outii=sum(outii)
            outii=str(outii)
            outii=list(outii)
            outii=list(map(int,outii))
            outii=sum(outii)
            outii=str(outii)
            outii=list(outii)
            outii=list(map(int,outii))
            outii=sum(outii)
            if outii==1:
                lblTest.configure(text=Loe_failist("TextFile1.txt"))
                Kirjuta_failisse("Nimi.txt",name)
            elif outii==2:
                lblTest.configure(text=Loe_failist("TextFile1 - Copy.txt"))
                Kirjuta_failisse("Nimi.txt",name)
            elif outii==3:
                lblTest.configure(text=Loe_failist("TextFile1 - Copy (2).txt"))
                Kirjuta_failisse("Nimi.txt",name)
            elif outii==4:
                lblTest.configure(text=Loe_failist("TextFile1 - Copy (3).txt"))
                Kirjuta_failisse("Nimi.txt",name)
            elif outii==5:
                lblTest.configure(text=Loe_failist("TextFile1 - Copy (4).txt"))
                Kirjuta_failisse("Nimi.txt",name)
            elif outii==6:
                lblTest.configure(text=Loe_failist("TextFile1 - Copy (5).txt"))
                Kirjuta_failisse("Nimi.txt",name)
            elif outii==7:
                lblTest.configure(text=Loe_failist("TextFile1 - Copy (6).txt"))
                Kirjuta_failisse("Nimi.txt",name)
            elif outii==8:
                lblTest.configure(text=Loe_failist("TextFile1 - Copy (7).txt"))
                Kirjuta_failisse("Nimi.txt",name)
            elif outii==9:
                lblTest.configure(text=Loe_failist("TextFile1 - Copy (8).txt"))
                Kirjuta_failisse("Nimi.txt",name)  
        else:
            intabEng ="ajsbktcludmvenwfoxgqzir"
            out="11112222333344445555666"
            trans=name.maketrans(intabEng,out)
            outi=name.translate(trans)
            print(name)
            outii=list(map(int,outi))
            outii=sum(outii)
            outii=str(outii)
            outii=list(outii)
            outii=list(map(int,outii))
            outii=sum(outii)
            outii=str(outii)
            outii=list(outii)
            outii=list(map(int,outii))
            outii=sum(outii)
            if outii==1:
                lblTest.configure(text=Loe_failist("TextFile1.txt"))
                Kirjuta_failisse("Nimi.txt",name)
            elif outii==2:
                lblTest.configure(text=Loe_failist("TextFile1 - Copy.txt"))
                Kirjuta_failisse("Nimi.txt",name)
            elif outii==3:
                lblTest.configure(text=Loe_failist("TextFile1 - Copy (2).txt"))
                Kirjuta_failisse("Nimi.txt",name)
            elif outii==4:
                lblTest.configure(text=Loe_failist("TextFile1 - Copy (3).txt"))
                Kirjuta_failisse("Nimi.txt",name)
            elif outii==5:
                lblTest.configure(text=Loe_failist("TextFile1 - Copy (4).txt"))
                Kirjuta_failisse("Nimi.txt",name)
            elif outii==6:
                lblTest.configure(text=Loe_failist("TextFile1 - Copy (5).txt"))
                Kirjuta_failisse("Nimi.txt",name)
            elif outii==7:
                lblTest.configure(text=Loe_failist("TextFile1 - Copy (6).txt"))
                Kirjuta_failisse("Nimi.txt",name)
            elif outii==8:
                lblTest.configure(text=Loe_failist("TextFile1 - Copy (7).txt"))
                Kirjuta_failisse("Nimi.txt",name)
            elif outii==9:
                lblTest.configure(text=Loe_failist("TextFile1 - Copy (8).txt"))
                Kirjuta_failisse("Nimi.txt",name)
aken=Tk()
aken.geometry("500x500")
aken.title("Numerologia")
lbl=Label(aken, text="Numerologia", font="Arial 50", width=30)
lbl1=Label(aken, text="Sisse nimi", font="Arial 24", width=10)
ent=Entry(aken, font="Arial 15", width=18)
btn=Button(aken, font="Arial 30", text="Enter", bg="lightgrey")
btn.bind('<Button-1>',findArv)
obj=[lbl,lbl1, ent, btn]
for item in obj:
    item.pack(pady=5)
aken.mainloop()