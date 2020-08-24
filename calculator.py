def interface():
    print("My Program")
    while True:
        print("Options:")
        print("1 - HDL")
        print("9 - Quit")
        choice = input("Enter your choice: ")
        if choice=='9':
            return
        elif choice =='1':
            HDL_driver()
            
   
def HDl_driver():
    #get input
    HDL = get_input()
    #check if HDL is normal
    HDL_level = check_HDL()
    #output

def get_input():
    HDL = input("Enter your HDL level: ")
    return int(HDL)

def check_HDL(HDL):
    if HDL >=60:
        return HDL_level = "your HDL is normal"
    elif HDL<60 && HDL>40:
        return HDL_level = ("your HDL is borderline low"
    else:
        return HDL_level = "your HDL is low"

def return_level():
    
    
interface()
