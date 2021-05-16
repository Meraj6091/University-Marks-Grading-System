#i declare that my work contains no examples of misconduct,such as plagiarism,or collusion
#Any code taken from others sources is referenced within my code solution
#Student ID: 2017026
#Date:11/29/2019

list=[]
for i in range(0,121,20):
    list.append(i)



def output():
    print("Trailing 2: **")
    print("Progress 1: *")
    print("Retriever 3: ***")
    print("Excluded 4: ****")
    print("10 outcomes in total.")

    
def credits1():
    print("Student no:1\n")
    print("Pass credits:",list[6])
    print("Defer credits:",list[0])
    print("Fail credits:",list[0])
    print("Progress\n")
    
def credits2():
    print("Student no:2\n")
    print("Pass credits:",list[0])
    print("Defer credits:",list[0])
    print("Fail credits:",list[6])
    print("Excluded\n")
    
def credits3():
    print("Student no:3\n")
    print("Pass credits:",list[1])
    print("Defer credits:",list[1])
    print("Fail credits:",list[4])
    print("Excluded\n")

def credits4():
    print("Student no:4\n")
    print("Pass credits:",list[0])
    print("Defer credits:",list[1])
    print("Fail credits:",list[5])
    print("Excluded\n")

def credits5():
    print("Student no:5\n")
    print("Pass credits:",list[0])
    print("Defer credits:",list[2])
    print("Fail credits:",list[4])
    print("Excluded\n")

def credits6():
    print("Student no:6\n")
    print("Pass credits:",list[0])
    print("Defer credits:",list[6])
    print("Fail credits:",list[0])
    print("Do not progress-module retriever\n")

def credits7():
    print("Student no:7\n")
    print("Pass credits:",list[0])
    print("Defer credits:",list[5])
    print("Fail credits:",list[1])
    print("Do not progress-module retriever\n")

def credits8():
    print("Student no:8\n")
    print("Pass credits:",list[0])
    print("Defer credits:",list[4])
    print("Fail credits:",list[2])
    print("Do not progress-module retriever\n")

def credits9():
    print("Student no:9\n")
    print("Pass credits:",list[5])
    print("Defer credits:",list[1])
    print("Fail credits:",list[0])
    print("Progress-module trailer\n")

def credits10():
    print("Student no:10\n")
    print("Pass credits:",list[5])
    print("Defer credits:",list[0])
    print("Fail credits:",list[1])
    print("Progress-module trailer\n")

   
credits1()
credits2()
credits3()
credits4()
credits5()
credits6()
credits7()
credits8()
credits9()
credits10()
output()

