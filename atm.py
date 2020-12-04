#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Create Database using Dict

database={
    'ram':{
        'name':'Ram',
        'age':22,
        'email':'ramzzz@gmail.com',
        'password':'ram@123',
        'amount': 20000,
    },
     'prad':{
        'name':'Prad',
        'age':26,
        'email':'pradzzz@gmail.com',
        'password':'prad@123',
        'amount': 60000,
        },
     'prithi':{
        'name':'Prithi',
        'age':22,
        'email':'prizzz@gmail.com',
        'password':'pri@123',
        'amount': 10000,
        
    },
 
}


# In[59]:


def main():
    print('Welcome to ATM\n')
    while True:
        print('Enter your choice\n')
        print('1. Sign in\n')
        print('2. Sign up\n')
        print('3. Exit \n')

        option = int(input('What Would you like to choose?'))

        if option==1:
            #print('Sign in')
            username= input('Enter your username: ')
            password= input('Enter your password: ')
            if username not in database:
                print('User does not Exist')
            elif password!= database[username]['password']:
                print('Password Error')

            else:
                print('Welcome ',database[username]['name'])
                while True:
                    print('Enter your choice\n')
                    print('1. Check Balance\n')
                    print('2. Deposit Balance\n')
                    print('3. Withdrawal \n')
                    print('4. Logout \n')

                    signin_option = int(input())
                    if signin_option==1:
                        print('Balance= ',database[username]['amount'])

                    elif signin_option==2:
                        balance= int(input('Enter your deposit amount:'))
                        database[username]['amount']=database[username]['amount']+balance
                    elif signin_option==3:
                        balance= int(input('Enter your withdrawal amount:'))
                        database[username]['amount']=database[username]['amount']-balance
                    else:
                        print('Logging out')
                        break




        elif option==2:


            #print('Sign up')
            username= input('Enter your username: ')
            name= input('Enter your name: ')
            password= input('Enter your password: ')
            balance= int(input('Enter your balance: '))
            mail_ID= input('Enter your mail ID : ')
            database[username]={'name':name, 'password':password, 'email': mail_ID, 'amount': balance}
            print('Username Successfully Created')


        elif option==3:

            print('Exit')
            break
main()
    


# In[ ]:




