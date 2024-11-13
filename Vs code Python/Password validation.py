password=input('Enter the password :')
if len(password)>8:
    u_count=0
    l_count=0
    n_count=0
    sp_count=0
    for i in password:
        if i.isupper():
            u_count+=1
        elif i.islower():
            l_count+=1
        elif i.isdigit():
            n_count+=1
        else:
            sp_count+=1
    if u_count>=2 and l_count>=2 and n_count>=1 and sp_count>=1:
        print('Password Accepted......')
    else:
        print('Password Not Accepted... \n Must be contain 2 uppercase,2 lowercase, 1 number, 1 special character')    
else:
    print (f'Invalid Password.......Must be contain 2 uppercase,2 lowercase, 1 number, 1 special character ')