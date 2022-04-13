
def levelstress():
    
    string = input("Введіть Ваш рівень стресу?: ")
       
    try:
        numbernum = int(string)
        
        if numbernum > 0:
            
            print("A" * numbernum + "!")
            
        else:
            
            print("Число повинно бути > 0")
        
    except:
        
        print("Це не число. Введіть число!")
    
levelstress()
