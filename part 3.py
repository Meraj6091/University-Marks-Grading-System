#i declare that my work contains no examples of misconduct,such as plagiarism,or collusion
#Any code taken from others sources is referenced within my code solution
#Student ID: 2017026
#Date:11/29/2019

list=[]
for i in range(0,121,20):
    list.append(i)
k=0#no of progress
m=0#no of Do not progress-module retriever
c=0#no of Exclude
d=0#no of Progress-module trailer
  
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
            d+=1
            tot=(k+m+c+d)
            break
        elif int(Pass)==list[6]:
            print("Progress")
            k+=1
            tot=(k+m+c+d)
            break
                
        elif (int(Pass)==list[2]) and (int(Fail)==list[4]):
            print("Exclude")
            c+=1
            tot=(k+m+c+d)
            break
                
                
        elif (int(Pass)==list[0]) and (int(Defer)==list[2]):
            print("Exclude")
            c+=1
            tot=(k+m+c+d)
            break
                
                
        elif (int(Pass)==list[0]) and (int(Defer)==list[1]):
            print("Exclude")
            c+=1
            tot=(k+m+c+d)
            break
                
                
        elif (int(Pass)==list[0]) and (int(Defer)==list[0]):
            print("Exclude")
            c+=1
            tot=(k+m+c+d)
            break
                
                
        elif (int(Pass)==list[1]) and (int(Defer)==list[1]):
            print("Exclude")
            c+=1
            tot=(k+m+c+d)
            break
                
                
        elif (int(Pass)==list[1]) and (int(Defer)==list[0]):
            print("Exclude")
            c+=1
            tot=(k+m+c+d)
            break
       
               
        elif int(Pass)==list[5]:
            print("Progress-module trailer")
            d+=1
            tot=(k+m+c+d)
            break
               
            
        elif int(Pass)==list[4]:
            print("Do not Progress-module retriever")
            m+=1
            tot=(k+m+c+d)
            break
    
                
        elif int(Pass)==list[2]:
            print("Do not Progress-module retriever")
            m+=1
            tot=(k+m+c+d)
            break
                
                

                
        elif int(Pass)==list[1]:
            print("Do not Progress-module retriever")
            m+=1
            tot=(k+m+c+d)
            break
                
                
        elif int(Pass)==list[0]:
            print("Do not Progress-module retriever")
            m+=1
            tot=(k+m+c+d)
            break
        
         
    x=input("press q to exit or press Any key to continue:")
    quit='q'
    if x==quit:  
        print("Program is now Exited.\n")
        kk = k
        mm = m
        cc = c
        dd = d
    
    
        xx = ["Progress" , "Retriever", "Excluded", "Trailing"]                              #https://stackoverflow.com/questions/53285446/how-do-i-make-print-vertically-on-python-loops  
        print(' '.join(xx))
        for m in range(max(kk, mm, cc, dd)):
            print("  {0}        {1}         {2}       {3}  ".format( '*' if m < kk else " ",
                   '*' if m < mm else " ",'*' if m < cc else " ",'*' if m < dd else " "))
   
                 
        break

    
               
                


        
        



                 
              
         
    

