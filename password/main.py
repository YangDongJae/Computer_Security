member_text_db = {
    'admin':'1234',
    'user1':'asdf1234',
    'user2':'qwer1234',
    'user3':'iloveyou'
}

login_count = 3

def login_text(id, password):
    if member_text_db[id] == password:
        return True
    else:
        return False

def print_member(member):
    for id in member:
        print(id, member[id], sep = ": ")

if __name__ == "__main__":
    print("Welcom to the login system!")
    
    print_member(member_text_db)
    
    id = input("ID: ")
    
    while True:
        if id in member_text_db:
            while login_count >= 0:
                password = input("Password: ")
                login_result = login_text(id, password)
                
                if login_result:
                    print("Welcom!")
                    break
            
                else:
                    print("Wrong Password. Try again")
                    login_count -= 1
                    continue 
                
            if login_count == 0:
                break
            
            break
        else:
            print("Wrong ID. Try again.")
            id = input("ID : ")
            continue