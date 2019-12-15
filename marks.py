school = {'ClassA':{'aki':{'English':80,'Maths':90,'Tamil':99},
        'muthu':{'English':89,'Maths':90,'Tamil':100},
        'loki':{'English':87,'Maths':100,'Tamil':66},
        },
        'ClassB':{'gowthi':{'English':80,'Maths':90,'Tamil':100},
        'deenu':{'English':80,'Maths':88,'Tamil':66},
        'ashwin':{'English':80,'Maths':100,'Tamil':77},
        },
        }

ch=0
while(ch!=4):
    print("\nSelct an option\n"
          "1) Display the students list \n"
          "2) Display the school topper \n"
          "3) Display The class toppers \n"
          "4) Exit")
    ch=int(input("Enter your choice"))
    if(ch==1):
        a={ck:{nk:nv.values() for nk,nv in cv.items()} for ck,cv in school.items()}
        #print(a)
       
        print("The students list are:")
        for k,v in a.items():
            for key,values in v.items():
                print("{}".format(key))
        option="yes"
        while(option!="no"):
            option=input("Do you need to see the marks of the student? yes/no \n")
            if(option=="yes"):
                name=input("Enter student name:")
                d= {nk: nv for ck, cv in school.items() for nk, nv in cv.items() for sk, sv in nv.items() }
                stud = d[name]
                l = []
                print("\n{:<10} {:>8}".format("Subject", "Marks"))

                for k, v in stud.items():
                    print("{:<10} {:>5}".format(k, v))
                    l.append(v)

                avg = (sum(l)//len(l))

                print("\nTotal of {} is {} \n".format(name, sum(l)))
                l = []
                print("Average of {} is {} \n".format(name, avg))
            else:
                print("main menu")
                break
        
            
    
        
              

    if(ch==2):
        a={nk:sum(nv.values())  for ck,cv in school.items() for nk,nv in cv.items()}
        #print(a)
        b=max(a.items(),key=lambda x:x[1])
        #print(b)
        print("School topper is")
        print("Student name: {}" .format(b[0]))
        print("Student mark: {}".format(b[1]))
        

          
    if(ch==3):
        a = {ck:{nk:sum(nv.values()) for nk,nv in cv.items()} for ck,cv in school.items()}
        b = {ck:max(cv.items(),key = lambda k:k[1]) for ck,cv in a.items()}   
        for k,v in b.items():
                print('{:<10}{:<10}{:<10}'.format(k,v[0],v[1]))


    if(ch==4):
        exit()
                
    
        
      
