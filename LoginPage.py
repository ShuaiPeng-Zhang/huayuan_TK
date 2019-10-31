#coding=utf8

from tkinter import *
from MoudlePage import *
from mysql import *

class Login_Page(object):
    def __init__(self,master=None):
        self.root =master
        self.count = IntVar()
        self.username = StringVar()
        self.password = StringVar()
        self.info = StringVar()
        self.createPage()
        self.name = StringVar()

    def createPage(self):
        self.page = Frame(self.root)
        self.page.pack()
        Label(self.page,text='账号登录',font=('',20),fg='blue',height=10).grid(row=0,columnspan=3,stick=N,pady=20)
        Label(self.page, text='账户: ').grid(row=1, stick=W,pady=10)
        Entry(self.page, textvariable=self.username).grid(row=1, column=1, stick=E)
        self.username.set('贾素玲')
        Label(self.page, text='密码: ').grid(row=2, stick=W, pady=10)
        Entry(self.page, textvariable=self.password, show='*').grid(row=2, column=1, stick=E)
        self.password.set('123456')
        Button(self.page, text='登陆', command=self.loginCheck).grid(row=3, stick=W, pady=10)
        Button(self.page, text='退出', command=self.page.quit).grid(row=3, column=1, stick=E)

        self.count = 0
    def loginCheck(self):
        name = self.username.get()
        Login_Page.name = name
        # print(Login_Page.name)
        secret = self.password.get()

        sql='select * from users'
        result = conn_mysql(sql)
        # print(len(result))
        user_list = []
        for i in range(len(result)):
            user_list.append(result[i][1])
        # print(user_list)

        if name in user_list:
            print('用户名正确')
            #索引用户账户位置
            username_index = user_list.index(name)
            # print(username_index)
            if result[username_index][3] == 0:
                if secret == result[username_index][2]:
                    print('密码验证通过')
                    self.page.destroy()
                    MainPage(self.root)

                else:
                    print('密码验证错误')
                    messagebox.showinfo(title='错误', message='密码错误！')
                    self.count+=1
                    print(self.count)
                    if self.count>=3:
                        sql1 = 'update users set is_lock=1 where username="'+name+'"'
                        conn_mysql(sql1)

            else:
                messagebox.showerror(title='错误', message='账号已锁定！请联系管理员解锁')
        else:
            messagebox.showinfo(title='错误', message='账号错误！')
        return name
