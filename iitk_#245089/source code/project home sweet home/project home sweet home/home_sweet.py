import sweet_home_modul as home
option='y'
while option=='y' or option=='Y':
      print(" "*24,"WELCOME")
      print(" "*20,"HOME SWEET HOME")
      print("press 1 you want to login as user ")
      print("press 2 you want to login as admin")
      choice=int(input("enter your choice"))
      if choice==1:
         print("press 1 for new user")
         print("press 2 for you have already account")
         ch=int(input("enter your choice"))
         if ch==1:
           Uname=input("enter your name")
           ID=input("enter your email id")
           mob_no=int(input("enter your mobile number"))
           occup=input("enter your occupation")
           bs_sal=int(input("enter your basic salary"))
           home.new_usr(Uname,ID,mob_no,occup,bs_sal)
           
         elif ch==2:
             home.user_vaild()
             home.display()
             home.booking_detail()
            
      elif choice==2:
           print(" "*20,"WELCOME ADMIN")
           home.admin()
           print("1.INSERT PRODUCT DETAIL \n2.UPDATE PRODUCT DETAIL \n3.DELETE PRODUCT DETAIL \n4.DISPLAY USER DETAIL \n5.DISPLAY REQUEST")
           ch=int(input("\n ENTER YOUR CHOICE"))
           if ch==1:
               print(" "*20,"INSERT PRODUCT RECORD")
               pd_type=input("enter product type")
               size=input(f"enter {pd_type} size")
               amount=input(f"enter prize of {pd_type}:")
               location=input(f"enter location of {pd_type}")
               status=input(f"what is the status of this {pd_type}")
               home.insert_record(pd_type,size,amount,location,status)  #insert record function
           elif ch==2:
                 home.update_rec()
           elif ch==3:
                 home.delete_rec()
           elif ch==4:
                home.disp_Urecord()
           elif ch==5:
                home.disp_Reqrecord()
                
      option=input("do you want to continue(Y/N)")
