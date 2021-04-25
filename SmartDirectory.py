import speech_recognition as sr
import pyttsx3

#function to convert text to speech

def TextToSpeech(command):

    #initialise the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()




# importing the module 

import sys 

  
# this function will be the first to run as soon as the main function executes 

def initial_phonebook():

    mytext5= "Please specify initial number of contacts: "

    TextToSpeech(mytext5)

    rows, cols = int(input(mytext5)), 5

    # We are collecting the initial number of contacts the user wants to have in the 

    # phonebook already. User may also enter 0 if he doesn't wish to enter any. 

    phone_book = [] 

    print(phone_book) 

    for i in range(rows): 

        TextToSpeech("\nEnter contact %d details in the following order (ONLY):" % (i+1))
        print("\nEnter contact %d details in the following order (ONLY):" % (i+1))

        print("NOTE: * indicates mandatory fields") 

        print("....................................................................") 

        temp = [] 

        for j in range(cols): 

                      

        # We have taken the conditions for values of j only for the personalized fields 

        # such as name, number, e-mail id, dob, category etc 

            if j == 0:

                TextToSpeech("Enter name. Note: This is a mandatory field.")

                temp.append(str(input("Enter name*: "))) 
                 

                # We need to check if the user has left the name empty as its mentioned that 

                # name & number are mandatory fields. 

                # So implement a condition to check as below. 

                if temp[j] == '' or temp[j] == ' ':

                    TextToSpeech("Name is a mandatory field. Process exiting due to blank field.")

                    sys.exit( 

                        "Name is a mandatory field. Process exiting due to blank field...") 

                    # This will exit the process if a blank field is encountered.                       

            if j == 1:

                TextToSpeech("Enter contact number. Note: This is a mandatory field")

                temp.append(int(input("Enter number*: "))) 

                # We do not need to check if user has entered the number because int automatically 

                # takes care of it. Int value cannot accept a blank as that counts as a string. 

                # So process automatically exits without us using the sys package. 

                  

            if j == 2:

                TextToSpeech("Enter email address")

                temp.append(str(input("Enter e-mail address: "))) 

                # Even if this field is left as blank, None will take the blank's place 

                if temp[j] == '' or temp[j] == ' ': 

                    temp[j] = None

                      

            if j == 3:

                TextToSpeech("Enter date of birth in the format dd-mm-yy")

                temp.append(str(input("Enter date of birth(dd/mm/yy): "))) 

                # Whatever format the user enters dob in, it won't make a difference to the compiler 

                # Only while searching the user will have to enter query exactly the same way as 

                # he entered during the input so as to ensure accurate searches 

                if temp[j] == '' or temp[j] == ' ': 

                                      

                # Even if this field is left as blank, None will take the blank's place 

                    temp[j] = None

            if j == 4:

                TextToSpeech("Enter category: Family/Friends/Work/Others")

                temp.append( 

                    str(input("Enter category(Family/Friends/Work/Others): "))) 

                # Even if this field is left as blank, None will take the blank's place 

                if temp[j] == "" or temp[j] == ' ': 

                    temp[j] = None

                      

        phone_book.append(temp) 

        # By this step we are appending a list temp into a list phone_book 

        # That means phone_book is a 2-D array and temp is a 1-D array 

      

    print(phone_book) 

    return phone_book 

  

def menu(): 

    # We created this simple menu function for 

    # code reusability & also for an interactive console 

    # Menu func will only execute when called 

    print("************************") 

    print("\t\t\tSMARTDIRECTORY", flush=False) 

    print("************************") 

    mytext3 = "\tYou can now perform the following operations on this phonebook\n"

    print(mytext3)

    TextToSpeech(mytext3)

    mytext4 = ("\n 1. Add a new contact \n\n 2. Remove an existing contact \n\n 3. Delete all contacts \n\n 4. Search for a contact \n\n 5. Display all contacts \n\n 6. Exit phonebook")

    print(mytext4)

    TextToSpeech(mytext4)

  

    # Out of the provided 6 choices, user needs to enter any 1 choice among the 6 

    # We return the entered choice to the calling function wiz main in our case

    TextToSpeech("Kindly enter your choice")

    choice = int(

         input("Please enter your choice: ")) 

      

    return choice 

  

def add_contact(pb):

    TextToSpeech("Enter details of the contact you wish to add to the SmartDirectory")

    # Adding a contact is the easiest because all you need to do is: 

    # append another list of details into the already existing list 

    dip = [] 

    for i in range(len(pb[0])): 

        if i == 0:

            TextToSpeech("Enter name. Note: This is a mandatory field")

            dip.append(str(input("Enter name: "))) 

        if i == 1:

            TextToSpeech("Enter number. Note: This is a mandatory field")

            dip.append(int(input("Enter number: "))) 

        if i == 2:

            TextToSpeech("Enter e-mail address")

            dip.append(str(input("Enter e-mail address: "))) 

        if i == 3:

            TextToSpeech("Enter date of birth in the format of dd-mm-yy")

            dip.append(str(input("Enter date of birth(dd/mm/yy): "))) 

        if i == 4:

            TextToSpeech("Enter category: Family/Friends/Work/Others")

            dip.append( 

                str(input("Enter category(Family/Friends/Work/Others): "))) 

    pb.append(dip) 

    # And once you modify the list, you return it to the calling function wiz main, here. 

    return pb 

def remove_existing(pb): 

    # This function is to remove a contact's details from existing phonebook

    mytext6 = "Please enter the name of the contact you wish to remove: "

    TextToSpeech(mytext6)

    query = str( 

        input(mytext6)) 

    # We'll collect name of the contact and search if it exists in our phonebook 

      

    temp = 0

    # temp is a checking variable here. We assigned a value 0 to temp. 

      

    for i in range(len(pb)): 

        if query == pb[i][0]: 

            temp += 1

            # Temp will be incremented & it won't be 0 anymore in this function's scope 

              

            print(pb.pop(i)) 

            # The pop function removes entry at index i 

            mytext7="This query has now been removed"

            TextToSpeech(mytext7)

            print(mytext7) 

            # printing a confirmation message after removal. 

            # This ensures that removal was successful. 

            # After removal we will return the modified phonebook to the calling function 

            # which is main in our program 

              

            return pb 

    if temp == 0: 

        # Now if at all any case matches temp shoul've incremented but if otherwise, 

        # temp will remain 0 and that means the query does not exist in this phonebook

        TextToSpeech("Sorry. You have entered an invalid entry. Kindly check again and try later. The process is exiting.")

        print("Sorry, you have entered an invalid query. \n Please recheck and try again later.") 

          

        return pb 

  

def delete_all(pb): 

    # This function will simply delete all the entries in the phonebook pb 

    # It will return an empty phonebook after clearing 

    return pb.clear() 

  

def search_existing(pb): 

    # This function searches for an existing contact and displays the result

    TextToSpeech("Enter search criteria\n\n\n 1. Name\n 2. Number\n 3. Email-id\n 4. DOB\n 5. Category(Family/Friends/Work/Others)\n\n Please enter: ")

    choice = int(

         input("Please enter search criteria\n\n\n 1. Name\n 2. Number\n 3. Email-id\n 4. DOB\n 5. Category(Family/Friends/Work/Others)\n\n  "))

    # We're doing so just to ensure that the user experiences a customized search result 

      

    temp = [] 

    check = -1

      

    if choice == 1: 

    # This will execute for searches based on contact name

        TextToSpeech("Please enter the name of the contact you wish to search")

        query = str( 

            input("Please enter the name of the contact you wish to search: ")) 

        for i in range(len(pb)): 

            if query == pb[i][0]: 

                check = i 

                temp.append(pb[i]) 

                  

    elif choice == 2: 

    # This will execute for searches based on contact number

        TextToSpeech("Please enter the phone number of the contact you wish to search")

        query = int( 

            input("Please enter the number of the contact you wish to search: ")) 

        for i in range(len(pb)): 

            if query == pb[i][1]: 

                check = i 

                temp.append(pb[i]) 

                  

    elif choice == 3: 

    # This will execute for searches based on contact's e-mail address 

        query = str(input("Please enter the e-mail ID of the contact you wish to search: ")) 

        for i in range(len(pb)): 

            if query == pb[i][2]: 

                check = i 

                temp.append(pb[i]) 

                  

    elif choice == 4: 

    # This will execute for searches based on contact''s date of birth

        TextToSpeech("Please enter the DOB (in dd/mm/yyyy format ONLY) of the contact you wish to search: ")

        query = str(input("Please enter the DOB (in dd/mm/yyyy format ONLY) of the contact you wish to search: ")) 

        for i in range(len(pb)): 

            if query == pb[i][3]: 

                check = i 

                temp.append(pb[i]) 

                  

    elif choice == 5: 

    # This will execute for searches based on contact category

        TextToSpeech=("Please enter the category of the contact you wish to search: ")

        query = str( 

            input("Please enter the category of the contact you wish to search: ")) 

        for i in range(len(pb)): 

            if query == pb[i][4]: 

                check = i 

                temp.append(pb[i]) 

        # All contacts under query category will be shown using this feature

          

    else: 

    # If the user enters any other choice then the search will be unsuccessful

        TextToSpeech("Invalid search criteria. Search unsuccessful.")

        print("Invalid search criteria") 

        return -1

    # returning -1 indicates that the search was unsuccessful 

      

    # all the searches are stored in temp and all the results will be displayed with 

    # the help of display function 

      

    if check == -1:

        mytext9= "Query does not exist in the directory"

        TextToSpeech(mytext9)

        print(mytext9)

        return -1

        # returning -1 indicates that the query did not exist in the directory 

    else: 

        display_all(temp) 

        return check 

        # we're just returning a index value wiz not -1 to calling function just to notify 

        # that the search worked successfully 

  
# this function displays all content of phonebook pb 

def display_all(pb): 

    if not pb: 

    # if display function is called after deleting all contacts then the len will be 0 

    # And then without this condition it will throw an error

        TextToSpeech("List is empty")

        print("List is empty: []") 

    else: 
        
        for i in range(len(pb)): 

            print(pb[i]) 


def thanks(): 
# A simple gesture of courtesy towards the user to enhance user experience 

    print("************************")

    mytext11= "Thank you for using our SmartDirectory system. \n\n Please visit again!"

    print(mytext11)

    TextToSpeech(mytext11)

    print("************************")

    mytext12= "Goodbye, have a nice day ahead!"

    TextToSpeech(mytext12)

    sys.exit(mytext12) 

  
# Main function code 

print("....................................................................") 

mytext= "Hello dear user, welcome to our SmartDirectory system"

print(mytext)

TextToSpeech(mytext)

mytext2= "You may now proceed to explore this directory"

print(mytext2)

TextToSpeech(mytext2)

print("....................................................................") 

ch = 1

pb = initial_phonebook() 

while ch in (1, 2, 3, 4, 5): 

    ch = menu() 

    if ch == 1: 

        pb = add_contact(pb) 

    elif ch == 2: 

        pb = remove_existing(pb) 

    elif ch == 3: 

        pb = delete_all(pb) 

    elif ch == 4: 

        d = search_existing(pb) 

        if d == -1:

            mytext13= "The contact does not exist. Please try again"

            TextToSpeech(mytext13)

            print(mytext13) 

    elif ch == 5: 

        display_all(pb) 

    else: 

        thanks()
