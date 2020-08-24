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
            
   
def HDL_driver():
    #get input
    HDL = get_input()
    #check if HDL is normal
    HDL_level = check_HDL(HDL)
    #output
    return_level(HDL, HDL_level)

def get_input():
    HDL = input("Enter your HDL level: ")
    return int(HDL)

def check_HDL(HDL):
    if HDL >=60:
         HDL_level = "your HDL is normal"
    elif 40 <=HDL<60:
         HDL_level = "your HDL is borderline low"
    else:
         HDL_level = "your HDL is low"
    return HDL_level

def return_level(HDL, HDL_level):
    print("The HDL result is {}".format(HDL))
    print("That is {}".format(HDL_level))
    
interface()
