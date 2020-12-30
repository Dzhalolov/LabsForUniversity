from tkinter import *
import pickle
import os


def Login():
    
    menu = Menu()
    menu.title('Login')


    username = Label(rootA, text='Username: ')
    pasword = Label(rootA, text='Password: ')
    username.grid(row=1, sticky=W)
    pasword.grid(row=2, sticky=W)

    name_menu = Entry(menu)
    password_menu = Entry(menu, show='*')
    name_menu.grid(row=1, column=H)
    password_menu.grid(row=2, column=H)

    login = Button(menu, text='Login',
                    command=CheckLogin)
    login.grid(columnspan='auto', sticky='auto')

    menu.mainloop()
    
    
def Sign_up():
    f = open('login.txt', 'rb')
    data = pickle.load(f)
    f.close()
    data[name.get()] = password.get()

    f = open('roles.txt', 'rb')
    list_r = pickle.load(f)
    f.close()
    data[name.get()] = role.get()

    menu.destroy() 


def Show():
    f = open("login.txt", "rb")
    user_pas = pickle.load(f)
    f.close()

    f = open("roles.txt", "rb")
    user_role = pickle.load(f)
    f.close()

    st = ''
    for key in user_pas.keys():
        st = st + key + ' ' + user_role[key] + ' ' + user_pas[key] + '\n'

    r1 = Menu()
    r1.title('D:')
    r1.geometry('150x100')
    text = Label(r1, text='\n {}'.format(st))
    text.pack()
    r1.mainloop()


def Admin():
    
    rootAdm = menu()  # This now makes a new window.
    rootAdm.title('Admin')  # This makes the window title 'login'
    rootAdm.geometry(H*W)


    name = Entry(rootAdm)  # The entry input
    pword = Entry(rootA, show='*')
    name.grid(row=1, column=1)
    pword.grid(row=2, column=1)

    getUserlist = Button(rootAdm, text='Show Users',
                    command=ShowUsers)  # This makes the login button, which will go to the CheckLogin def.
    getUserlist.grid(columnspan=2, sticky=W)

    rmuser = Button(rootAdm, text='Delete User', fg='red',
                    command=DelUser)  # This makes the deluser button. blah go to the deluser def.\
    rmuser.grid(columnspan=2, sticky=W)

    create = Button(rootAdm, text='Create User', fg='green',
                    command=Signup)  # This makes the deluser button. blah go to the deluser def.\
    create.grid(columnspan=2, sticky=W)

    rootAdm.mainloop()


def Read_only(nm):
    global rootAD
    global name
    global nameAD
    name = nm
    rootAD = Tk()  # This now makes a new window.
    rootAD.title('User')  # This makes the window title 'login'
    rootAD.geometry(W*H)

    intruction = Label(rootAD, text='User Page\n')  # More labels to tell us what they do
    intruction.grid(sticky=E)  # Blahdy Blah
    nameAD = Entry(rootAD)  # The entry input
    nameAD.grid(row=1, column=1)
    chPass = Button(rootAD, text='Change Password',
                         command=ChangePass)  # This makes the login button, which will go to the CheckLogin def.
    chPass.grid(columnspan=2, sticky=W)

    rootAD.mainloop()


def Change_Password():
    f = open('login.txt', 'rb')
    list_u = pickle.load(f)
    f.close()
    list_u[name] = nameAD.get()

    f = open('login.txt', 'wb')  # Creates a document using the variable we made at the top.
    pickle.dump(list_u, f)
    f.close()

    rootAD.destroy()
    
    
def Role(user):
    f = open("roles.txt", "rb")
    user_role = pickle.load(f)

    if user_role[user] == 'Admin':
        menu.destroy()
        AdminWindow()
    elif user_role[user] == 'Read_User':
        menu.destroy()
        ReadUserWindow(user)
    else:
        r = menu()
        r.title('D:')
        r.geometry('150x100')
        rlbl = Label(r, text='\n[!] User with no Permissions')
        rlbl.pack()
        r.mainloop()

def Login_check():
    f = open("login.txt", "rb")
    user_pas = pickle.load(f)
    f.close()

    if nameEL.get() in user_pas.keys() and pwordEL.get() == user_pas[nameEL.get()]:  # Checks to see if you entered the correct data.
        CheckRole(nameEL.get())
    else:
        r = Tk()
        r.title('D:')
        r.geometry('150x50')
        rlbl = Label(r, text='\n[!] Invalid Login')
        rlbl.pack()
        r.mainloop()

def Delete_user():


    f = open("login.txt", "rb")
    user_pas = pickle.load(f)
    f.close()

    f = open("roles.txt", "rb")
    user_role = pickle.load(f)
    f.close()

    f1 = open('num', 'w')
    users -= 1
    f1.write(str(users))
    f1.close()


    user_role.pop(menu.get())
    user_pas.pop(menu.get())
    
    menu.destroy()


    rootDL = Tk()  # This now makes a new window.
    rootDL.title('Delete')  # This makes the window title 'login'

    intruction = Label(rootDL, text='Enter user to delete\n')  # More labels to tell us what they do
    intruction.grid(sticky=E)  # Blahdy Blah

    nameL = Label(rootDL, text='Username: ')  # More labels
    nameL.grid(row=1, sticky=W)


    nameDL = Entry(rootDL)  # The entry input
    nameDL.grid(row=1, column=1)


    delB = Button(rootDL, text='Delete',
                    command=del_user)  # This makes the login button, which will go to the CheckLogin def.
    delB.grid(columnspan=2, sticky=W)

    menu.mainloop()


if __name__ == '__main__':
    Login()
