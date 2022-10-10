import pymysql as py
import sys
con=py.connect("localhost","root","","user_detail")
cur=con.cursor()
def new_usr(name,id,mob,occup,bs_salry):
    qry="select max(sr_no) from user"
    cur.execute(qry)
    rec=cur.fetchone()
    #print(rec[0])
    if rec[0]==None:
        sn=1
    else:
        sn=rec[0]+1
    uid=name[0:5]+'_'+str(sn)
    print(" "*20,f"WELCOME {name} YOUR USER ID IS :{uid}")
    pwd=input("please enter your password");
    ep=''
    for i in pwd:
      ep=ep+chr(ord(i)+4)
    #print(ep)
    q="insert into user values (%d,'%s','%s','%s',%d,'%s',%d,'%s')"%(sn,name,uid,id,mob,occup,bs_salry,ep)
    #print(q)
    cur.execute(q)
    con.commit()
    if cur.rowcount>0:
        print("all done...")
    else:
        print("errorr...")

def user_vaild():
    id=input("please enter your user id")
    qry="select user_id from user where user_id='%s'"%(id)
    cur.execute(qry)
    rec=cur.fetchone()
    if id==rec[0]:
       passw=input("please enter password")
       ep=''
       for i in passw:
          ep=ep+chr(ord(i)+4)
       print(ep)
       q="select password from user where password='%s'"%(ep)
       cur.execute(q)
       record=cur.fetchone()
       print(record[0])
       if ep==record[0]:
          print(" "*20,"WELCOME TO HOME SWEET HOME")
       else:
           print(" "*20,"sorry")
    else:
        print("id is invailed \n please enter vailed id")
        user_vaild()

def insert_record(pd_name,size,totalamount,location,status):
    q="select max(sr_no) from product"
    #print(q)
    cur.execute(q)
    rec=cur.fetchone()
    #print(rec[0])
    if rec==None:
        sn=1
    else:
        sn=rec[0]+1
    pd_id=pd_name[0:4]+'_'+str(sn)
    qry="insert into product values (%d,'%s','%s','%s','%s','%s','%s')"%(sn,pd_id,pd_name,size,totalamount,location,status)
    cur.execute(qry)
    con.commit()
    if cur.rowcount>0:
       print("done")
    else:
        print("error")


def display():
    
    print("  "*15,"(^_^) WELCOME (^_^)")
    print("CATEGORY")
    op='y'
    while op=='y' or op=='Y':
      print("1.LAND \n2.PLOT \n3.FLAT")
      ch=int(input("enter your choice"))
         
      if ch==1:    
        qry="select * from product where product_type='LAND'"
        cur.execute(qry)
        rec=cur.fetchall()
        for i in rec:
           print(i,"\n")
      elif ch==2:
        qry="select * from product where product_type='PLOT'and status='FOR SALE'"
        cur.execute(qry)
        rec=cur.fetchall()
        for i in rec:
          print(i,"\n")
      elif ch==3:
        qry="select * from product where product_type='FLAT'"
        cur.execute(qry)
        rec=cur.fetchall()
        for i in rec:
          print(i,"\n")
      op=input(" DO You want to see more property (y/n)")
        
   
def update_rec():
    print(" "*20,"1.UPDATE USER DETAIL")
    print(" "*20,"2.UPDATE PRODUCT DETAIL")
    choice=int(input("enter your choice"))
    if choice==1:
       ur_id=input("enter user id")
       qry="select * from user where user_id='%s'"%(ur_id)
       cur.execute(qry)
       rec=cur.fetchall()
       print("your privious data is")
       for i in rec:
          print(rec)
       print("1.UPDATE EMAIL ID")
       print("2.UPDATE MOBILE NUMBER")
       choi=int(input("enter your choice"))
       if choi==1:
           eid=input("input email id for update")
           qry="update user SET email_id='%s' where user_id='%s'"%(eid,ur_id)
           cur.execute(qry)
           con.commit()
           if cur.rowcount>0:
              print("done")
           else:
              print("error")
       elif choi==2:
           mob_no=int(input("input mob_no for update"))
           qry="update user SET mobile_no=%d where user_id='%s'"%(mob_no,ur_id)
           cur.execute(qry)
           con.commit()
           if cur.rowcount>0:
               print("done")
           else:
               print("error")
    elif choice==2:
         print(" "*20,"1.UPDATE PRODUCT AMOUNT")
         print(" "*20,"2.UPDATE STATUS")
         ch=int(input("enter your choice"))
         if ch==1:
            p_id=input("enter product id")
            qry="select * from product where product_id='%s'"%(p_id)
            cur.execute(qry)
            rec=cur.fetchall()
            print(" "*20,"YOUR PRIVIOUS RECORD IS:")
            for i in rec:
              print(i,"\n")
            x=input("do you want to update informatio y/n")
            if x=='y' or x=='Y':
                app=input("enter update amount")
                qry="update product SET amount='%s' where product_id='%s'"%(app,p_id)
                print(qry)
                cur.execute(qry)
                if cur.rowcount>0:
                    print("done....")
                else:
                    print("error...")
            
         elif ch==2:
              pd_id=input("enter product id")
              st=input("please input status")
              qry="update product SET status='%s' where product_id='%s'"%(st,pd_id)
              #print(qry)
              cur.execute(qry)
              con.commit()
              if cur.rowcount>0:
                 print("done")
              else:
                 print("error")


def delete_rec():
    print(" "*20,"1.DELETE USER RECORD")
    print(" "*20,"2.DELETE PRODUCT RECORD")
    ch=int(input("enter your choice"))
    if ch==1:
       u_id=input("enter user id")
       qry="delete from user where user_id='%s'"%(u_id)
       cur.execute(qry)
       con.commit()
       if cur.rowcount>0:
          print("done...")
       else:
           print("error")
    elif ch==2:
         pd_id=input("enter product id")
         q="delete from product where product_id='%s'"%(pd_id)
         cur.execute(q)
         con.commit()
         if rowcount>0:
             print("done....")
         else:
             print("error...")
             
def booking_detail():
  op=input("do you want to book anything(y/n)")
  while True:
     if op=='y' or op=='Y':
        genrate()           #genrating request id
        break
     else:
        print(" "*20,"THANK YOU (^_^)")
        break

def genrate():
    u_nm=input("please enter name")
    pd_id=input("please enter product id")
    cur_mobno=int(input("enter current mobile number"))
    email_id=input("enter your EMAIL ID")
    appo_date=input("enter date when you want to see location of flat/land/plot")
    appo_time=input("enter time when you have time to see location of flat/land/plot")
    qry="select max(sr_no) from book_table"
    cur.execute(qry)
    rec=cur.fetchone()
    print(rec)
    if rec[0]==None:
        sn=1
        #print(sn)
    else:
        sn=rec[0]+1
        #print(sn)
    req_id=u_nm[0:5]+'_'+pd_id
    print(" "*20,f"WELCOME {u_nm} YOUR REQUEST ID IS :{req_id}")
    q="insert into book_table values (%d,'%s','%s','%s',%d,'%s','%s','%s')"%(sn,req_id,pd_id,u_nm,cur_mobno,email_id,appo_date,appo_time)
    cur.execute(q)
    con.commit()
    if cur.rowcount>0:
        print("all done...")
        print("  "*20,"(^_^) THANKYOU FOR BOOKING (^_^) \nWE HOPE WE MEET VERY SOON")
    else:
        print("errorr...")

def disp_Reqrecord():
    qry="select * from book_table"
    cur.execute(qry)
    rec=cur.fetchall()
    for i in rec:
        print(i,"\n")

def disp_Urecord():
    qry="select * from user"
    cur.execute(qry)
    rec=cur.fetchall()
    for i in rec:
        print(i,"\n")
def admin():
    use_id=input("please enter your user id")
    q="select user_id from user"
    cur.execute(q)
    record=cur.fetchall()
    for row in record:
      if use_id in row[0]:
        qry="select user_id from user where user_id='%s'"%(use_id)
        cur.execute(qry)
        rec=cur.fetchone()
        if use_id==rec[0]:
           pwd=input("please enter password")
           ep=''
           for i in pwd:
              ep=ep+chr(ord(i)+4)
           if ep=='efgh':
              print("%20s"%"WELCOME ADMIN")
           else:
              print("%20s"%"YOU ARE NOT ADMIN")
              sys.exit()
    
    else:
        print("enter correct user id")

    
    
