print("****Welcome to Orabelle Hotel And Resort****")


def customer_data():
  Name=input("Enter your name:")
  Phone=int(input("Enter your phone number:"))
  City=input("Enter your City:")
  Aadhar=int(input("Enter your Aadhar number:"))
  Check_In=input("Enter check-in date:")
  Check_Out=input("Enter check-out date:")
  import mysql.connector as sqltor
  mycon=sqltor.connect(host="localhost",user="root",passwd="root",database="Hotel")
  cursor=mycon.cursor()
  st="insert into Records(NAME,PHONE,CITY,AADHAR,CHECK_IN,CHECK_OUT) values('{}','{}','{}','{}','{}','{}')".format(Name,Phone,City,Aadhar,Check_In,Check_Out)
  cursor.execute(st)
  mycon.commit()
  mycon.close()
  print() 
  print("Details inputed successfully...")
  print("You can avail the services now...")
  print("----------------------")
  return

while True:
    ab=int(input("Main Menu\n1.New customer:\n2.Complaints or queries:\n3.About us:\n4.Show my bill:\n5.Exit the site:\n-------------------------\nEnter your choice:"))    
    
    if ab==1:
        customer_data()
        print("We have the following services for you...")
        while True:
          cd=int(input("1.Rooms\n2.Restaurant\n3.Spa\n4.Sports activities\n5.Laundry services\n6.Back:\n-------------------------\nEnter your choice:")) 
          print("----------------------")
        
          if cd==1:
              print() 
              print("Welcome to Orabelle Hotel.")
              print() 
              print("We have the following rooms for you...\n1.Deluxe-1500rs.\n2.Super-Deluxe-3000rs.\n3.Luxurious Suite-6000rs.\n4.Hall-9000rs.\n5.Back:")
              ef=int(input("Enter your choice:")) 
              gh=int(input("Enter no. of quantities of room required:"))
              ij=int(input("Enter no. of days:"))
              print("----------------------")
              if ef==1:
                  room=1500*gh*ij                  
              elif ef==2:
                  room=3000*gh*ij
              elif ef==3:
                  room=6000*gh*ij
              elif ef==4 :
                  room=9000*gh*ij
              elif ef==5:
                  break
              else:
                 print("Please enter a valid choice...")
          elif cd==2:     
           print()
           print("Welcome to Orabelle restaurant...")
           print()
           print("We have the following items for you...\n1.Breakfast combo:100rs.\n2.Lunch combo:200rs.\n3.Dinner combo:300rs.\n4.Snacks combo:50rs.\n5.Coldrinks and hot beverages:25rs.\n6.Packaged drinking water:10rs.\n7.Back:")
           kl=int(input("Enter your choice:"))
           mn=int(input("Enter no. of items:"))
           print("----------------------")
           if kl==1:
               food=100*mn              
           elif kl==2:
               food=200*mn              
           elif kl==3:
               food=300*mn              
           elif kl==4:
               food=50*mn               
           elif kl==5:
               food=25*mn               
           elif kl==6:
               food=10*mn
           elif kl==7:
                break
           else:
               print("Please enter a valid choice...")
          elif cd==3:
               print()
               print("Welcome to Orabelle spa...")
               print()
               print("We have the following massages for you...\n1.Silver-1000rs.\n2.Gold-1500rs.\n3.Platinum-2000rs.\n4.Diamond:2500rs.\n5.Royale:3000rs.\n6.Back:")
               op=int(input("Enter your choice:"))
               qr=int(input("Enter no. of person(s):"))
               print("----------------------")
               if op==1:
                   spa=1000*qr                   
               elif op==2:
                   spa=1500*qr
               elif op==3:
                   spa=2000*qr
               elif op==4:
                   spa=2500*qr
               elif op==5:
                   spa=3000*qr
               elif op==6:
                    break
               else:
                   print("Please enter a valid choice.")
          elif cd==4:
              print()
              print("Welcome to Orabelle sports activities...")
              print()
              print("We have the following activities for you...\n1.Swimming:100rs./hr.\n2.Cricket:150rs./hr.\n3.Football:200rs./hr.\n4.Volleyball:250rs./hr.\n5.Trekking:500rs./person\n6.Rides:500rs./hr.\n7.Back:")
              st=int(input("Enter your choice:"))
              uv=int(input("Enter no. of hours:"))
              wx=int(input("Enter no. of person(s):"))
              print("----------------------")
              if st==1:
                  Sports=100*uv*wx                 
              elif st==2:
                  Sports=150*uv*wx                 
              elif st==3:
                  Sports=200*uv*wx                 
              elif st==4:
                  Sports=250*uv*wx
              elif st==5:
                  Sports=500*uv*wx
              elif st==6:
                  Sports=500*uv*wx                 
              elif st==7:
                  break
                
              else:
                  print("Please enter a valid choice...")
          elif cd==5:
              print()
              print("Welcome to Orabelle laundry services...")
              print()
              print("Please choose among the following:\n1.Shirt:5rs.\n2.Trousers:5rs.\n3.Girls suit:15rs.\n4.Shorts:3rs.\n5. Blazers:30rs.\n6.Back:")
              yz=int(input("Enter your choice:"))
              za=int(input("Enter no. of quantity:"))
              print("----------------------")
              if yz==1:
                  Clothes=5*za
              elif yz==2:
                  Clothes=5*za
              elif yz==3:
                  Clothes=15*za
              elif yz==4:
                  Clothes=3*za
              elif yz==5:
                  Clothes=30*za
              elif yz==6:
                    break
              else:
                  print("Please enter a valid choice...")
          elif(cd==6):
              break
                  
    
    elif ab==2:
       while True:
         print("We have following choices for you:\n1.Complaints:\n2.Queries:\n3.Back:")
         print("----------------------")
         bc=int(input("Enter your choice:"))
         print("----------------------")
         if bc==1:
           print("We are sorry to hear that you have complaints for us...")
           de=input("Enter your complaint:")
           print("Complaint registered successfully...")
           print("----------------------")
           import mysql.connector as sqltor
           mycon=sqltor.connect(host="localhost",user="root",passwd="root",database="Hotel")
           cursor=mycon.cursor()
           st="insert into COMPLAINTS(COMPLAINTS) values('{}')".format(de)
           cursor.execute(st)
           mycon.commit()
           mycon.close()
         elif bc==2:
            fg=input("Please enter your query:")
            print("We will soon solve your query. Thank you...")
            print("----------------------")
            import mysql.connector as sqltor
            mycon=sqltor.connect(host="localhost",user="root",passwd="root",database="Hotel")
            cursor=mycon.cursor()
            st="insert into QUERIES(QUERIES) values('{}')".format(fg)
            cursor.execute(st)
            mycon.commit()
            mycon.close()
         elif bc==3:
            break
         else:
            print("Please enter a valid choice...")
        
    elif ab==3:
       print("WE care FOR PEOPLE SO THEY CAN BE THEIR best.\nAs we continue to grow, we don’t lose sight of what’s most important—people.\n Orabelle is a company that was built by family. It’s a workplace where coworkers become friends.\n Every day we care for our guests. Care is at the heart of our business, and it’s this distinct guest experience that makes Hyatt one of the world’s best hospitality brands.") 
       print("FIND your place AT Orabelle.\nBe a part of something bigger. Enjoy life every day. Make a difference in the lives of those around you.\n Love where you work. Join a company that values respect, integrity, humility, empathy, creativity, and fun.\n With careers spanning the globe, your perfect opportunity awaits. Discover why Orabelle is consistently ranked one of the world’s best places to work.")
    elif ab==4:
        print("Your room bill is", room ,"rs.")
        print("Your restaurant bill is", food ,"rs.")
        print("Your spa bill is", spa , "rs.")
        print("Your sport activities bill is", Sports , "rs.")
        print("Your laundry bill is", Clothes ,"rs.")
        total=room+food+spa+Sports+Clothes
        print("Your total bill is",total,"rs.")
        import mysql.connector as sqltor
        mycon=sqltor.connect(host="localhost",user="root",passwd="root",database="Hotel")
        cursor=mycon.cursor()
        st="insert into Bills(Bill) values('{}')".format(total)
        cursor.execute(st)
        mycon.commit()
        mycon.close()
        
    elif ab==5:
        print("Have a nice day.")
        break
    else:
        print("Please enter a valid choice...")