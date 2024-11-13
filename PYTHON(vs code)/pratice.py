
dic={'dinga':1234,'dingi':4567}

# user_name_password={'dinga':1234,'dingi':4567}
# user_name_amount={'dinga':1000,'dingi':500}
# user_name_pin={'dinga':1111,'dingi':2222}


print('\t\t\t\t\t\t\t\t\t\t\t\t\t\tWelcome To Bank' )
print('\t\tChoose the option')
print('\t\t\t\t\t\t1.Account already exists')
print('\t\t\t\t\t\t2.Create a new account')
option=int(input('Enter the given options:'))
if option==1:
    user_name=input('User_name:')
    password=int(input('Password:'))
    if user_name in dic:
        if dic[user_name]==password:
            print('\t\t\tDone')
        else:
            if dic[user_name] != password:
                print('Incorrect username and password')
                print('1.Back to sign up')
c=int(input('Enter:'))
if option==1:
   