#i declare that my work contains no examples of misconduct,such as plagiarism,or collusion
#Any code taken from others sources is referenced within my code solution
#Student ID: 2017026
#Date:11/8/2019

list=[]
for i in range(0,121,20):
    list.append(i)
while True:
    while True:
            Pass=input("Enter Pass Credits:")
            if not(Pass.isdigit()):
                print("Integers required")
            elif int(Pass) in list:
                
                break
            else:
                print("Range error")
                
    while True:
            Defer=input("Enter Defer Credits:")
            if not(Defer.isdigit()):
                print("Integers required")
            elif int(Defer) in list:
                
                break
            else:
                print("Range error")
                
    while True:
            Fail=input("Enter Fail Credits:")
            if not(Fail.isdigit()):
                print("Integers required")
            elif int(Fail) in list:
                
                break
            else:
                print("Range error")
                

    while True:
        if (int(Fail)+int(Defer)+int(Pass))!=120:
            print("Total Incorrect")
            break
        elif (int(Pass)==list[5]) and (int(Fail)==list[1]):
            print("Progress-module trailer")
            break
        
        elif int(Pass)==list[6]:
            print("Progress")
            break
        elif (int(Pass)==list[2]) and (int(Fail)==list[4]):
            print("Exclude")
            break
        elif (int(Pass)==list[0]) and (int(Defer)==list[2]):
            print("Exclude")
            break
        elif (int(Pass)==list[0]) and (int(Defer)==list[1]):
            print("Exclude")
            break
        elif (int(Pass)==list[0]) and (int(Defer)==list[0]):
            print("Exclude")
            break
        elif (int(Pass)==list[1]) and (int(Defer)==list[1]):
            print("Exclude")
            break
        elif (int(Pass)==list[1]) and (int(Defer)==list[0]):
            print("Exclude")
            break
        
        elif int(Pass)==list[5]:
            print("Progress-module trailer")
            break
        elif int(Pass)==list[4]:
            print("Do not Progress-module retriever")
            break
        elif int(Pass)==list[2]:
            print("Do not Progress-module retriever")
            break

            
        elif int(Pass)==list[1]:
            print("Do not Progress-module retriever")
            break
        elif int(Pass)==list[0]:
            print("Do not Progress-module retriever")
            break
        
            
    
    
    

    

