import os
import sys
import smtplib
import pymysql
from prettytable import PrettyTable
from prettytable import from_db_cursor
conn = pymysql.connect(host="localhost",user="root",passwd="dbzbloke98",db="Family")
myCursor = conn.cursor()
global income
global expenses
expense_list = []
expense_name = []
income_name = []
income_list = []
global income007
global expense007
global rmd007
global sp
global expenses
global income
global rem_amt
from tkinter import *
#sql table creation
myCursor.execute('USE Family')
myCursor.execute("""CREATE TABLE INCOME
(
Source varchar(50),
Amount int
);
""")
myCursor.execute("""
INSERT INTO INCOME VALUES('Salary',0);
""")
myCursor.execute("""
INSERT INTO INCOME VALUES('Business',0);
""")
myCursor.execute("""
INSERT INTO INCOME VALUES('Interest',0);
""")
myCursor.execute("""
INSERT INTO INCOME VALUES('Dividend',0);
""")
myCursor.execute("""
INSERT INTO INCOME VALUES('Capital Gains',0);
""")
myCursor.execute("""
INSERT INTO INCOME VALUES('Property',0);
""")
myCursor.execute("""
INSERT INTO INCOME VALUES('Others',0);
""")

myCursor.execute("""CREATE TABLE EXPENDITURE
(
Source varchar(50),
Amount int
);
""")
myCursor.execute("""
INSERT INTO EXPENDITURE VALUES('Electricity',0);
""")
myCursor.execute("""
INSERT INTO EXPENDITURE VALUES('Society',0);
""")
myCursor.execute("""
INSERT INTO EXPENDITURE VALUES('Mobile',0);
""")
myCursor.execute("""
INSERT INTO EXPENDITURE VALUES('EMI',0);
""")
myCursor.execute("""
INSERT INTO EXPENDITURE VALUES('Rent',0);
""")
myCursor.execute("""
INSERT INTO EXPENDITURE VALUES('Grocery',0);
""")
myCursor.execute("""
INSERT INTO EXPENDITURE VALUES('Housemaid',0);
""")
myCursor.execute("""
INSERT INTO EXPENDITURE VALUES('Travel',0);
""")
myCursor.execute("""
INSERT INTO EXPENDITURE VALUES('Others',0);
""")

myCursor.execute("""CREATE TABLE BUDGET
(
DESCRIPTION varchar(50),
Amount int
);
""")
myCursor.execute("""
INSERT INTO BUDGET VALUES('Saving Percentage',0);

""")

myCursor.execute("""CREATE TABLE PERSONAL_DETAILS
(
DESCRIPTION varchar(50),
Entry varchar(40)
);
""")
myCursor.execute("""
INSERT INTO PERSONAL_DETAILS VALUES('Email ID','abc');
""")

myCursor.execute("""CREATE TABLE VIEW_STATS
(
Source varchar(50),
Total_Amount int
);
""")
myCursor.execute("""
INSERT INTO VIEW_STATS VALUES('Total Income',0);
""")
myCursor.execute("""
INSERT INTO VIEW_STATS VALUES('Total Expenditure',0);
""")
myCursor.execute("""
INSERT INTO VIEW_STATS VALUES('Remaining Amount',0);
""")

    
#MATHEMATICAL FUNCTIONS OPEN

def sal():
     salary =   int(e.get())
     income_list.append(salary)
     myCursor.execute("UPDATE INCOME SET Amount='%d' WHERE Source='Salary'"%(salary))
     conn.commit()
def bus():
     business = int(f.get())
     income_list.append(business)
     myCursor.execute("UPDATE INCOME SET Amount='%d' WHERE Source='Business'"%(business))
     conn.commit()
def inte():
     interest = int(g.get())
     income_list.append(interest)
     myCursor.execute("UPDATE INCOME SET Amount='%d' WHERE Source='Intrest'"%(interest))
     conn.commit()
def divi():
     dividend = int(h.get())
     income_list.append(dividend)
     myCursor.execute("UPDATE INCOME SET Amount='%d' WHERE Source='Dividend'"%(dividend))
     conn.commit()
def capg():
     capitalgains = int(i.get())
     income_list.append(capitalgains)
     myCursor.execute("UPDATE INCOME SET Amount='%d' WHERE Source='Capital Gains'"%(capitalgains))
     conn.commit()
def prop():
     proprty = int(j.get())
     income_list.append(proprty)
     myCursor.execute("UPDATE INCOME SET Amount='%d' WHERE Source='Property'"%(proprty))
     conn.commit()
def oth():
     other = int(k.get())
     income_list.append(other)
     myCursor.execute("UPDATE INCOME SET Amount='%d' WHERE Source='Others'"%(other))
     conn.commit()
def lol1():
     global income007
     income007 = sum(income_list)
     global income
     income=income007
     myCursor.execute("UPDATE VIEW_STATS SET Total_Amount='%d' WHERE Source='Total Income'"%(income007))
     conn.commit()
     
def lol4():
    global sp
    sp = int(entry31.get())
    myCursor.execute("UPDATE BUDGET SET Amount='%d' WHERE DESCRIPTION='Saving Percentage'"%(sp))
    conn.commit()
    global email
    email = entry32.get()
    myCursor.execute("UPDATE PERSONAL_DETAILS SET Entry='%s' WHERE DESCRIPTION='Email ID'"%(email))
    conn.commit()
def limit1():
     global sp
     ep = 100-sp
     lp = ep-10
     em_limit = (lp/100.0) * income
     if sum(expense_list)< em_limit:
         return
     else:
         content = 'YOU HAVE SURPASSED YOUR 10% SAFE MARGIN '
         mail = smtplib.SMTP('smtp.gmail.com',587)
         mail.ehlo()
         mail.starttls()
         mail.login('familyexpenditure03@gmail.com','momentofsilence')
         mail.sendmail('familyexpenditure03@gmail.com',email,content)
         mail.close()
         return
         
     
def elec():
     electricity =   int(entry21.get())
     expense_list.append(electricity)
     myCursor.execute("UPDATE EXPENDITURE SET Amount='%d' WHERE Source='Electricity'"%(electricity))
     conn.commit()
     limit1()
def soc():
     society = int(entry22.get())
     expense_list.append(society)
     myCursor.execute("UPDATE EXPENDITURE SET Amount='%d' WHERE Source='Society'"%(society))
     conn.commit()
     limit1()
def mob():
     mobile = int(entry23.get())
     expense_list.append(mobile)
     myCursor.execute("UPDATE EXPENDITURE SET Amount='%d' WHERE Source='Mobile'"%(mobile))
     conn.commit()
     limit1()
def eemi():
     emi = int(entry24.get())
     expense_list.append(emi)
     myCursor.execute("UPDATE EXPENDITURE SET Amount='%d' WHERE Source='EMI'"%(emi))
     conn.commit()
     limit1()
def rentt():
     rent = int(entry25.get())
     expense_list.append(rent)
     myCursor.execute("UPDATE EXPENDITURE SET Amount='%d' WHERE Source='Rent'"%(rent))
     conn.commit()
     limit1()
def groc():
     grocery = int(entry26.get())
     expense_list.append(grocery)
     myCursor.execute("UPDATE EXPENDITURE SET Amount='%d' WHERE Source='Grocery'"%(grocery))
     conn.commit()
     limit1()
def houm():
     hm = int(entry27.get())
     expense_list.append(hm)
     myCursor.execute("UPDATE EXPENDITURE SET Amount='%d' WHERE Source='Housemaid'"%(hm))
     conn.commit()
     limit1()
def trav():
     travel = int(entry28.get())
     expense_list.append(travel)
     myCursor.execute("UPDATE EXPENDITURE SET Amount='%d' WHERE Source='Travel'"%(travel))
     conn.commit()
     limit1()
def otth():
     otherss= int(entry29.get())
     expense_list.append(otherss)
     myCursor.execute("UPDATE EXPENDITURE SET Amount='%d' WHERE Source='Others'"%(otherss))
     conn.commit()
     limit1()
def lol2():
     global expense007
     expense007 = sum(expense_list)
     global expenses
     expenses=expense007
     myCursor.execute("UPDATE VIEW_STATS SET Total_Amount='%d' WHERE Source='Total Expenditure'"%(expense007))
     conn.commit()
     #def lol3():
     global rmd007
     rmd007 = income-expenses
     global rem_amt
     rem_amt= rmd007
     myCursor.execute("UPDATE VIEW_STATS SET Total_Amount='%d' WHERE Source='Remaining Amount'"%(rmd007))
     conn.commit()

#MATHEMATICAL FUNCTIONS CLOSE

#TKINTER FUNCTIONS OPEN
def back():
    f_home.place(x=0,y=0,height=2000,width=2000)
    f_inc.place_forget()
    f_exp.place_forget()
    f_bud.place_forget()
    f_vis.place_forget()
    f_dis.place_forget()

def back1():
    f_vis.place(x=0,y=0,height=2000,width=2000)
    f_dis.place_forget()

    
def bne_inc():
    f_home.place_forget()
    f_inc.place(x=0,y=0,height=2000,width=2000)
    lbinc=Label(f_inc,image=inc1)
    lbinc.place(x=0,y=0)
    bi0=Button(f_inc,text="BACK",background="red",height=3,width=20,command=back)
    bi0.place(x=20,y=20)
    #INCOME SCREEN OPEN
    l1=Label(f_inc,text="SALARY",background="red",height=2,width=20)
    l1.place(x=200,y=150)
    b11=Button(f_inc,text="DONE",background="red",height=3,width=20,command=sal)
    b11.place(x=700,y=150)
    l2=Label(f_inc,text="BUSINESS",background="red",height=2,width=20)
    l2.place(x=200,y=220)
    b12=Button(f_inc,text="DONE",background="red",height=3,width=20,command=bus)
    b12.place(x=700,y=220)
    l3=Label(f_inc,text="INTEREST(BANK,FD)",background="red",height=2,width=20)
    l3.place(x=200,y=290)
    b13=Button(f_inc,text="DONE",background="red",height=3,width=20,command=inte)
    b13.place(x=700,y=290)
    l4=Label(f_inc,text="DIVIDEND",background="red",height=2,width=20)
    l4.place(x=200,y=360)
    b14=Button(f_inc,text="DONE",background="red",height=3,width=20,command=divi)
    b14.place(x=700,y=360)
    l5=Label(f_inc,text="CAPITAL GAINS",background="red",height=2,width=20)
    l5.place(x=200,y=430)
    b15=Button(f_inc,text="DONE",background="red",height=3,width=20,command=capg)
    b15.place(x=700,y=430)
    l6=Label(f_inc,text="PROPERTY",background="red",height=2,width=20)
    l6.place(x=200,y=500)
    b16=Button(f_inc,text="DONE",background="red",height=3,width=20,command=prop)
    b16.place(x=700,y=500)
    l7=Label(f_inc,text="OTHERS",background="red",height=2,width=20)
    l7.place(x=200,y=570)
    b17=Button(f_inc,text="DONE",background="red",height=3,width=20,command=oth)
    b17.place(x=700,y=570)
    b18=Button(f_inc,text="SUBMIT?",background="red",height=3,width=20,command=lol1)
    b18.place(x=550,y=650)
    global e
    e=Entry(f_inc)
    e.place(x=500,y=160)
    global f
    f=Entry(f_inc)
    f.place(x=500,y=230)
    global g
    g=Entry(f_inc)
    g.place(x=500,y=300)
    global h
    h=Entry(f_inc)
    h.place(x=500,y=370)
    global k
    k=Entry(f_inc)
    k.place(x=500,y=570)
    global i
    i=Entry(f_inc)
    i.place(x=500,y=440)
    global j
    j=Entry(f_inc)
    j.place(x=500,y=510)
    #INCOME SCREEN CLOSE
    
def bne_exp():
    f_home.place_forget()
    f_exp.place(x=0,y=0,height=2000,width=2000)
    lbexp=Label(f_exp,image=exp1)
    lbexp.place(x=0,y=0)
    bexp0=Button(f_exp,text="BACK",background="red",height=3,width=20,command=back)
    bexp0.place(x=20,y=20)
    #EXPENDITURE SCREEN OPEN
    l21=Label(f_exp,text="ELECTRICITY BILL",background="red",height=2,width=20)
    l21.place(x=200,y=150)
    b21=Button(f_exp,text="DONE",background="red",height=2,width=20,command=elec)
    b21.place(x=700,y=150)
    l22=Label(f_exp,text="SOCIETY BILL",background="red",height=2,width=20)
    l22.place(x=200,y=200)
    b22=Button(f_exp,text="DONE",background="red",height=2,width=20,command=soc)
    b22.place(x=700,y=200)
    l23=Label(f_exp,text="MOBILE & LANDLINE(WIFI,INTERNET)",background="red",height=2,width=30)
    l23.place(x=200,y=250)
    b23=Button(f_exp,text="DONE",background="red",height=2,width=20,command=mob)
    b23.place(x=700,y=250)
    l24=Label(f_exp,text="EMI",background="red",height=2,width=20)
    l24.place(x=200,y=300)
    b24=Button(f_exp,text="DONE",background="red",height=2,width=20,command=eemi)
    b24.place(x=700,y=300)
    l25=Label(f_exp,text="RENT",background="red",height=2,width=20)
    l25.place(x=200,y=350)
    b25=Button(f_exp,text="DONE",background="red",height=2,width=20,command=rentt)
    b25.place(x=700,y=350)
    l26=Label(f_exp,text="GROCERY(FOOD,MILK)",background="red",height=2,width=20)
    l26.place(x=200,y=400)
    b26=Button(f_exp,text="DONE",background="red",height=2,width=20,command=groc)
    b26.place(x=700,y=400)
    l27=Label(f_exp,text="HOUSE MAID",background="red",height=2,width=20)
    l27.place(x=200,y=450)
    b27=Button(f_exp,text="DONE",background="red",height=2,width=20,command=houm)
    b27.place(x=700,y=450)
    l28=Label(f_exp,text="TRAVEL & CONVIENCE",background="red",height=2,width=20)
    l28.place(x=200,y=500)
    b28=Button(f_exp,text="DONE",background="red",height=2,width=20,command=trav)
    b28.place(x=700,y=500)
    l29=Label(f_exp,text="OTHERS",background="red",height=2,width=20)
    l29.place(x=200,y=550)
    b29=Button(f_exp,text="DONE",background="red",height=2,width=20,command=otth)
    b29.place(x=700,y=550)
    b299=Button(f_exp,text="SUBMIT?",background="red",height=3,width=20,command=lol2)
    b299.place(x=550,y=650)
    #b298=Button(f_exp,text="SUBMIT?",background="red",height=3,width=20,command=lol3)
    #b298.place(x=150,y=650)
    global entry21
    entry21=Entry(f_exp)
    entry21.place(x=500,y=160)
    global entry22
    entry22=Entry(f_exp)
    entry22.place(x=500,y=210)
    global entry23
    entry23=Entry(f_exp)
    entry23.place(x=500,y=260)
    global entry24
    entry24=Entry(f_exp)
    entry24.place(x=500,y=310)
    global entry25
    entry25=Entry(f_exp)
    entry25.place(x=500,y=360)
    global entry26
    entry26=Entry(f_exp)
    entry26.place(x=500,y=410)
    global entry27
    entry27=Entry(f_exp)
    entry27.place(x=500,y=460)
    global entry28
    entry28=Entry(f_exp)
    entry28.place(x=500,y=510)
    global entry29
    entry29=Entry(f_exp)
    entry29.place(x=500,y=560)
    #EXPENDITURE SCREEN CLOSE

global rem_amt
global rmd007
global income007
global expense007
global expenses
global income

def bne_bud():
    f_home.place_forget()
    f_bud.place(x=0,y=0,height=2000,width=2000)
    lbbud=Label(f_bud,image=bud1)
    lbbud.place(x=0,y=0)
    bbud0=Button(f_bud,text="BACK",background="red",height=3,width=20,command=back)
    bbud0.place(x=20,y=20)
    #BUDGET SCREEN OPEN
    global entry31
    entry31=Entry(f_bud)
    entry31.place(x=200,y=270)
    global entry32
    entry32=Entry(f_bud,width=40)
    entry32.place(x=200,y=420)
    l31=Label(f_bud,text="WHAT PERCENTAGE OF YOR TOTAL MONTHLY INCOME DO YOU EXPECT TO SAVE?",background="red",height=2,width=80)
    l31.place(x=200,y=200)
    l31=Label(f_bud,text="WHAT IS YOUR EMAIL ID??",background="red",height=2,width=80)
    l31.place(x=200,y=350)
    b31=Button(f_bud,text="DONE",background="red",height=3,width=20,command=lol4)
    b31.place(x=300,y=500)
    #BUDGET SCREEN CLOSE

def bne_vis():
    f_home.place_forget()
    f_vis.place(x=0,y=0,height=2000,width=2000)
    lbvis=Label(f_vis,image=vis1)
    lbvis.place(x=0,y=0)
    bvis0=Button(f_vis,text="BACK",background="red",height=3,width=20,command=back)
    bvis0.place(x=20,y=20)
    bdis=Button(f_vis,text="DISPLAY TABLE",background="red",height=3,width=20,command=bne_dis)
    bdis.place(x=300,y=500)

    
    #STATICS SCREEN OPEN
    l41=Label(f_vis,text="TOTAL INCOME",background="red",height=2,width=40)
    l41.place(x=200,y=150)
    l43=Label(f_vis,text="TOTAL EXPENSES",background="red",height=2,width=40)
    l43.place(x=200,y=250)
    l45=Label(f_vis,text="REMAINING AMOUNT",background="red",height=2,width=40)
    l45.place(x=200,y=350)
    l46=Label(f_vis,text=rem_amt,background="red",height=2,width=40)
    l46.place(x=550,y=350)
    l44=Label(f_vis,text=expenses,background="red",height=2,width=40)
    l44.place(x=550,y=250)
    l42=Label(f_vis,text=income,background="red",height=2,width=40)
    l42.place(x=550,y=150)
    #STATICS SCREEN CLOSE

    
def bne_dis():
     f_vis.place_forget()
     f_dis.place(x=0,y=0,height=2000,width=2000)
     bdis0=Button(f_dis,text="BACK",background="red",height=3,width=20,command=back1)
     bdis0.place(x=20,y=20)
     l51=Label( f_dis,text='l51',background="green",height=2,width=40)
     l51.place(x=100,y=100,height=250,width=250)
     l52=Label( f_dis,text='l52',background="yellow",height=2,width=40)
     l52.place(x=500,y=100,height=250,width=250)
     l53=Label( f_dis,text=rem_amt,background="blue",height=2,width=40)
     l53.place(x=800,y=100,height=250,width=250)
     l54=Label( f_dis,text=rem_amt,background="red",height=2,width=40)
     l54.place(x=100,y=400,height=250,width=250)
     l55=Label( f_dis,text=rem_amt,background="red",height=2,width=40)
     l55.place(x=500,y=400,height=250,width=250)


     #sql table calling
     myCursor.execute("SELECT * FROM INCOME")
     table1=from_db_cursor(myCursor)
     l51.config(text=table1)
     myCursor.execute("SELECT * FROM EXPENDITURE")
     table2=from_db_cursor(myCursor)
     l52.config(text=table2)
     myCursor.execute("SELECT * FROM BUDGET")
     table3=from_db_cursor(myCursor)
     l53.config(text=table3)
     myCursor.execute("SELECT * FROM PERSONAL_DETAILS")
     table4=from_db_cursor(myCursor)
     l54.config(text=table4)
     myCursor.execute("SELECT * FROM VIEW_STATS")
     table5=from_db_cursor(myCursor)
     l55.config(text=table5)


#TKINTER FUNCTIONS CLOSE

    
#MAIN DECLARATIONS OPEN   
root=Tk()
root.config(background="BLUE")
f_home=Frame(root)
f_inc=Frame(root)
f_exp=Frame(root)
f_bud=Frame(root)
f_vis=Frame(root)
f_dis=Frame(root)
home1=PhotoImage(file="PIC_FAMILY.png")
inc1=PhotoImage(file="pic_income.png")
exp1=PhotoImage(file="pic_expenditure.png")
bud1=PhotoImage(file="pic_budget.png")
vis1=PhotoImage(file="pic_stats.png")
f_home.place(x=0,y=0,height=2000,width=2000)
#MAIN DECLARATIONS CLOSE

#HOME SCREEN OPEN
lbhome=Label(f_home,image=home1)
lbhome.place(x=0,y=0)
b1=Button(f_home,text="INCOME",background="red",height=3,width=20,command=bne_inc)
b1.place(x=900,y=150)
b2=Button(f_home,text="EXPENDITURE",background="red",height=3,width=20,command=bne_exp)
b2.place(x=900,y=250)
b3=Button(f_home,text="BUDGET",background="red",height=3,width=20,command=bne_bud)
b3.place(x=900,y=350)
b4=Button(f_home,text="VIEW STATS",background="red",height=3,width=20,command=bne_vis)
b4.place(x=900,y=450)
#bexit=Button(root,text="DONE",background="red",height=3,width=20,command=root.destory)
#bexit.place(x=300,y=500)
#HOME SCREEN CLOSE

root.mainloop()



