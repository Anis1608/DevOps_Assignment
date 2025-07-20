def gradeChecker(marks):
    if (marks >= 90):
        return ("A")
    elif(marks >=80 and marks <=89):
        return("B")
    elif(marks >=70 and marks <=79):
        return("C")
    elif(marks >=60 and marks <=69):
        return("D")
    else:
        return("F")
    
print("Welocome To Grade Checker...")
while(True):
    try:
        user_input = int(input("Enter Your Marks : "))
        if(user_input > 100):
            print("Marks Cannot be Greater than 100.")
        elif (user_input >= 60):
            print("Hey.. Congraulation Your Grade is : ",gradeChecker(user_input))
        else:
            print("Sorry... You Failed in these Exams Your Grade is : ",gradeChecker(user_input))
        continue_input = input("Do You Want to Continue Checking Others Grade ( Y / N ): ")
        if(continue_input in ("yes" , "YES", "Yes" , "Y" , "y")):
            continue
        else:
            break
    except:
        print("Input Error : Enter Valid Input")

        
