try:
    from tkinter import ttk
    from tkinter import messagebox
    from tkinter.filedialog import *
except :
    import os
    os.system('pip install tkinter')
    from tkinter import ttk
    from tkinter import messagebox
    from tkinter.filedialog import *
from mysql import *
try:
    import requests
except :
    import os
    os.system('pip install requests')
    import requests
try:
    import time
except :
    import os
    os.system('pip install time')
    import time
try:
    import pandas as pd
except :
    import os
    os.system('pip install pandas')
    import pandas as pd
try:
    import numpy as np
except :
    import os
    os.system('pip install numpy')
    import numpy as np
try:
    import xlrd
except :
    import os
    os.system('pip install xlrd')
    import xlrd
import LoginPage

class index(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.path = StringVar()
        self.createPage()

    def createPage(self):
        # Button(self.root,text='用户名:'+name+'').grid(row=0,column=2,stick=W)
        # Button(self.root, text='SIP:'+secret+'').grid(row=0,column=3,stick=E)
        Label(self,text='欢迎使用后端小程序',font=('',20),fg='blue',height=30).grid(row=0,column=0,columnspan=1,stick=S)

        Button(self,text='导入案件',fg='red',command=self.import_case).grid(row=1,column=1,columnspan=5,stick=E)
    def import_case(self):
        top = Toplevel()
        top.title('new path!')
        top.geometry('300x60+650+450')
        top.attributes("-topmost", 1)

        Label(top, text="目标路径:",font=('',15)).grid(row=0,column=0)
        Entry(top, textvariable=self.path).grid(row=0, column=1)
        Button(top, text="路径选择", command=self.selectPath).grid(row=0, column=2)
        Button(top,text='导入案件',command=self.daoruanjian).grid(row=1,column=1)

    def daoruanjian(self):
        file_path = self.path.get()
        # print(file_path)
        df = pd.read_excel(file_path)
        df.fillna(value=0)
        row = df.shape[0]
        ser_info_frame = df.loc[df['姓名']!=None,['姓名','号码']]
        ser_info_list = np.array(ser_info_frame).tolist()
        # print(ser_info_list)

        for i in range(row):
            ser_name = ser_info_list[i][0]
            ser_tel = ser_info_list[i][1]
            ser_tel = int(ser_tel)
            sql = "insert into ser_info(sername,sertel) values('%s',%d)"%(ser_name,ser_tel)
            # print(sql)
            conn_mysql(sql)
        messagebox.showinfo('提示','导入成功!')
        self.path.set('')

    def selectPath(self):
        filename = askopenfilename()
        if filename != '':
            self.path.set(filename)
            time.sleep(3)
        else:
            self.path.set("您没有选择任何文件")

class shujuchaxun(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root

        self.username = StringVar()
        self.usertel = StringVar()
        self.usernum = StringVar()

        self.sername = str()
        self.sertel = str()
        self.serNum = str()

        self.zhaiwuren = StringVar()
        self.tel = StringVar()
        self.num = StringVar()
        self.states = StringVar()

        self.createPage()

    def chaxunname(self):
        name = self.username.get()
        sql = 'select * from ser_info where sername = "%s"'%name
        result = conn_mysql(sql)
        self.sername = result[0][1]
        self.sertel = result[0][2]
        self.serstates = result[0][3]
        # print(self.sername,self.sertel,self.serNum)

        Label(self,text='债务人:').grid(row=5,column=0,pady=10)
        Entry(self,textvariable=self.zhaiwuren).grid(row=5, column=1)
        self.zhaiwuren.set(self.sername)
        Label(self, text='电话:').grid(row=6, column=0,pady=10)
        Entry(self,textvariable=self.tel).grid(row=6, column=1)
        self.tel.set(self.sertel)
        Label(self, text='案件状态:').grid(row=7, column=0,pady=10)
        Entry(self,textvariable=self.states).grid(row=7, column=1)
        if self.serstates == 0:
            self.states.set('未联系')
        elif self.serstates == 1:
            self.states.set('未接通')
        elif self.serstates == 2:
            self.states.set('停机')
        elif self.serstates == 3:
            self.states.set('已加微信')
        elif self.serstates == 4:
            self.states.set('已下载app')
        elif self.serstates == 5:
            self.states.set('空号')
        elif self.serstates == 6:
            self.states.set('不需要')
        elif self.serstates == 7:
            self.states.set('挂断')
        else:
            self.states.set('error')

    def chaxuntel(self):
        tel = self.usertel.get()
        # print(name)
        sql = 'select * from ser_info where sertel = "%s"'%tel
        result = conn_mysql(sql)
        self.sername = result[0][1]
        self.sertel = result[0][2]
        self.serNum = result[0][3]
        self.serstates = result[0][4]
        # print(self.sername,self.sertel,self.serNum)

        Label(self,text='债务人:').grid(row=5,column=0,pady=10)
        Entry(self,textvariable=self.zhaiwuren).grid(row=5, column=1)
        self.zhaiwuren.set(self.sername)
        Label(self, text='电话:').grid(row=6, column=0,pady=10)
        Entry(self,textvariable=self.tel).grid(row=6, column=1)
        self.tel.set(self.sertel)
        Label(self, text='案件状态:').grid(row=7, column=0,pady=10)
        Entry(self,textvariable=self.states).grid(row=7, column=1)
        if self.serstates == 0:
            self.states.set('未联系')
        elif self.serstates == 1:
            self.states.set('未接通')
        elif self.serstates == 2:
            self.states.set('停机')
        elif self.serstates == 3:
            self.states.set('已加微信')
        elif self.serstates == 4:
            self.states.set('已下载app')
        elif self.serstates == 5:
            self.states.set('空号')
        elif self.serstates == 6:
            self.states.set('不需要')
        elif self.serstates == 7:
            self.states.set('挂断')
        else:
            self.states.set('error')

    def createPage(self):
        Label(self, text='查询界面',font=('',20),height=5).grid(row=0,columnspan=3,stick=N)

        Label(self, text='姓名:',font=('',10)).grid(row=1,column=0,stick=W,pady=10)
        Entry(self,textvariable=self.username).grid(row=1,column=1)
        # self.username.set('')
        Button(self,text='查询',font=('',10),command=self.chaxunname).grid(row=1,column=2,stick=E)

        Label(self, text='电话:',font=('',10)).grid(row=2,column=0,stick=W,pady=10)
        Entry(self,textvariable=self.usertel).grid(row=2,column=1)
        Button(self,text='查询',font=('',10),command=self.chaxuntel).grid(row=2,column=2,stick=E)


        Label(self,text='案件人信息',pady=10,font=('',20),fg='blue',height=5).grid(row=3,columnspan=3,stick=N,pady=5)

class wodeanjian(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root

        self.name_1 = StringVar()
        self.tel_1 = StringVar()
        self.state_1 = StringVar()

        self.name_2 = StringVar()
        self.tel_2 = StringVar()
        self.state_2 = StringVar()

        self.name_3 = StringVar()
        self.tel_3 = StringVar()
        self.state_3 = StringVar()

        self.name_4 = StringVar()
        self.tel_4 = StringVar()
        self.state_4 = StringVar()

        self.name_5 = StringVar()
        self.tel_5 = StringVar()
        self.state_5 = StringVar()

        self.name_6 = StringVar()
        self.tel_6 = StringVar()
        self.state_6 = StringVar()

        self.name_7 = StringVar()
        self.tel_7 = StringVar()
        self.state_7 = StringVar()

        self.name_8 = StringVar()
        self.tel_8 = StringVar()
        self.state_8 = StringVar()

        self.name_9 = StringVar()
        self.tel_9 = StringVar()
        self.state_9 = StringVar()

        self.name_10 = StringVar()
        self.tel_10 = StringVar()
        self.state_10 = StringVar()

        self.name_11 = StringVar()
        self.tel_11 = StringVar()
        self.state_11 = StringVar()

        self.name_12 = StringVar()
        self.tel_12 = StringVar()
        self.state_12 = StringVar()

        self.name_13 = StringVar()
        self.tel_13 = StringVar()
        self.state_13 = StringVar()

        self.name_14 = StringVar()
        self.tel_14 = StringVar()
        self.state_14 = StringVar()

        self.name_15 = StringVar()
        self.tel_15 = StringVar()
        self.state_15 = StringVar()

        self.name_16 = StringVar()
        self.tel_16 = StringVar()
        self.state_16 = StringVar()

        self.name_17 = StringVar()
        self.tel_17 = StringVar()
        self.state_17 = StringVar()

        self.name_18 = StringVar()
        self.tel_18 = StringVar()
        self.state_18 = StringVar()
        #计算页码
        self.page=IntVar()
        #正在使用的sip号码
        self.sipnum = StringVar()
        self.chaxun_name = StringVar()

        self.createPage()
    #按键拨号
    def call_sip(self,num):
        tel_list = []
        name = LoginPage.Login_Page.name
        # print(name)
        sip = self.sipnum.get()
        if sip != "":
            page = self.page.get()
            # print("这是第"+str(page)+"页")
            index = (page-1)*18+num-1
            sql = 'select sertel from ser_info where vest_in = "'+name+'"'
            result_tel = conn_mysql(sql)
            for i in range(len(result_tel)):
                tel = result_tel[i][0]
                tel_list.append(tel)
            tel = tel_list[index]
            print(index,tel)
            tel = str(tel)
            url='http://192.168.2.9:5000/makecall?' \
                'callernum='+sip+'&callednum='+tel+'&fsip=192.168.108.27:5060'
            print(url)
            try:
                response = requests.get(url)
                print('status_code:%d'%(response.status_code))
                if response.status_code == 200:
                    print(response.json())
                    return response.json()
            except:
                messagebox.showerror('error','url请求失败')
        else:
            messagebox.showinfo('提示', '请输入分机号')
    #提交状态
    def submit_state(self,num,state_):
        name_list = []
        name = LoginPage.Login_Page.name
        # print(name)
        page = self.page.get()
        print("当前页面为第"+str(page)+"页")
        index = (page-1)*18+num-1
        state = state_.get()
        # print(index,state)
        sql = 'select sername from ser_info where vest_in = "' + name + '"'
        result_name = conn_mysql(sql)
        for i in range(len(result_name)):
            name_ = result_name[i][0]
            name_list.append(name_)
        name_index = name_list[index]
        print(index, name_index)
        if state == '未联系':
            state=0
            sql1 = 'update ser_info set state=%d where sername="%s"' % (state, name_index)
            conn_mysql(sql1)
            messagebox.showinfo('提示','已提交')
        elif state == '未接通':
            state=1
            sql1 = 'update ser_info set state=%d where sername="%s"' % (state, name_index)
            conn_mysql(sql1)
            messagebox.showinfo('提示', '已提交')
        elif state == '停机':
            state=2
            sql1 = 'update ser_info set state=%d where sername="%s"' % (state, name_index)
            conn_mysql(sql1)
            messagebox.showinfo('提示', '已提交')
        elif state == '已加微信':
            state=3
            sql1 = 'update ser_info set state=%d where sername="%s"' % (state, name_index)
            conn_mysql(sql1)
            messagebox.showinfo('提示', '已提交')
        elif state == '已下载app':
            state=4
            sql1 = 'update ser_info set state=%d where sername="%s"' % (state, name_index)
            conn_mysql(sql1)
            messagebox.showinfo('提示', '已提交')
        elif state == '空号':
            state=5
            sql1 = 'update ser_info set state=%d where sername="%s"' % (state, name_index)
            conn_mysql(sql1)
            messagebox.showinfo('提示', '已提交')
        elif state == '不需要':
            state=6
            sql1 = 'update ser_info set state=%d where sername="%s"' % (state, name_index)
            conn_mysql(sql1)
            messagebox.showinfo('提示', '已提交')
        elif state == '挂断':
            state=7
            sql1 = 'update ser_info set state=%d where sername="%s"' % (state, name_index)
            conn_mysql(sql1)
            messagebox.showinfo('提示', '已提交')
        else:
            messagebox.showinfo('提示','状态码错误')
    #计算总页数
    def sum_page(self):
        name = LoginPage.Login_Page.name
        # print(name)
        sql = 'select * from ser_info where vest_in = "'+name+'"'
        result = conn_mysql(sql)
        # print(len(result))
        div = len(result) // 18
        yu = len(result) % 18
        # print(div,yu)
        if div<=1:
            div = 1
            return div
        else:
            div=div+1
            return div
    #左翻页
    def left_page(self):
        name = LoginPage.Login_Page.name
        # print(name)
        div = self.sum_page()
        name_list = []
        tel_list = []
        state_list = []
        # 限制总页码
        page = self.page.get()-1
        if page>=1:
            self.page.set(page)
            start = (page-1)*18
            end = page*18
            print(start,end)
            sql = 'select * from ser_info where vest_in = "'+name+'"'
            result = conn_mysql(sql)
            for i in range(start + 2, end + 2):
                name = result[i - 2][1]
                tel = result[i - 2][2]
                state = result[i - 2][3]
                name_list.append(name)
                tel_list.append(tel)
                state_list.append(state)

                if i%18==2:
                    self.chuanzhi(i-2,self.name_1,self.tel_1,self.state_1,
                                  name_list,tel_list,state_list,2)
                elif i%18==3:
                    self.chuanzhi(i-2,self.name_2,self.tel_2,self.state_2,
                                  name_list,tel_list,state_list,3)
                elif i%18==4:
                    self.chuanzhi(i-2,self.name_3,self.tel_3,self.state_3,
                                  name_list,tel_list,state_list,4)
                elif i%18==5:
                    self.chuanzhi(i-2,self.name_4,self.tel_4,self.state_4,
                                  name_list,tel_list,state_list,5)
                elif i%18==6:
                    self.chuanzhi(i-2,self.name_5,self.tel_5,self.state_5,
                                  name_list,tel_list,state_list,6)
                elif i%18==7:
                    self.chuanzhi(i-2,self.name_6,self.tel_6,self.state_6,
                                  name_list,tel_list,state_list,7)
                elif i%18==8:
                    self.chuanzhi(i-2,self.name_7,self.tel_7,self.state_7,
                                  name_list,tel_list,state_list,8)
                elif i%18==9:
                    self.chuanzhi(i-2,self.name_8,self.tel_8,self.state_8,
                                  name_list,tel_list,state_list,9)
                elif i%18==10:
                    self.chuanzhi(i-2,self.name_9,self.tel_9,self.state_9,
                                  name_list,tel_list,state_list,10)
                elif i%18==11:
                    self.chuanzhi(i-2,self.name_10,self.tel_10,self.state_10,
                                  name_list,tel_list,state_list,11)
                elif i%18==12:
                    self.chuanzhi(i-2,self.name_11,self.tel_11,self.state_11,
                                  name_list,tel_list,state_list,12)
                elif i%18==13:
                    self.chuanzhi(i-2,self.name_12,self.tel_12,self.state_12,
                                  name_list,tel_list,state_list,13)
                elif i%18==14:
                    self.chuanzhi(i-2,self.name_13,self.tel_13,self.state_13,
                                  name_list,tel_list,state_list,14)
                elif i%18==15:
                    self.chuanzhi(i-2,self.name_14,self.tel_14,self.state_14,
                                  name_list,tel_list,state_list,15)
                elif i%18==16:
                    self.chuanzhi(i-2,self.name_15,self.tel_15,self.state_15,
                                  name_list,tel_list,state_list,16)
                elif i%18==17:
                    self.chuanzhi(i-2,self.name_16,self.tel_16,self.state_16,
                                  name_list,tel_list,state_list,17)
                elif i%18==0:
                    self.chuanzhi(i-2,self.name_17,self.tel_17,self.state_17,
                                  name_list,tel_list,state_list,18)
                elif i % 18 == 1:
                    self.chuanzhi(i-2,self.name_18, self.tel_18, self.state_18,
                                  name_list,tel_list,state_list,19)
        else:
            self.page.set('1')
    #右翻页
    def right_page(self):
        name = LoginPage.Login_Page.name
        # print(name)
        div = self.sum_page()
        name_list = []
        tel_list = []
        state_list = []
        #限制总页码
        page = self.page.get() + 1
        if page <= div:
            self.page.set(page)
            start = (page - 1) * 18
            end = page * 18
            print(start, end)
            sql = 'select * from ser_info where vest_in = "'+name+'"'
            result = conn_mysql(sql)
            for i in range(start+2,end+2):
                name = result[i-2][1]
                tel = result[i-2][2]
                state = result[i-2][3]
                name_list.append(name)
                tel_list.append(tel)
                state_list.append(state)

                if i%18==2:
                    self.chuanzhi(i-2,self.name_1,self.tel_1,self.state_1,
                                  name_list,tel_list,state_list,2)
                elif i%18==3:
                    self.chuanzhi(i-2,self.name_2,self.tel_2,self.state_2,
                                  name_list,tel_list,state_list,3)
                elif i%18==4:
                    self.chuanzhi(i-2,self.name_3,self.tel_3,self.state_3,
                                  name_list,tel_list,state_list,4)
                elif i%18==5:
                    self.chuanzhi(i-2,self.name_4,self.tel_4,self.state_4,
                                  name_list,tel_list,state_list,5)
                elif i%18==6:
                    self.chuanzhi(i-2,self.name_5,self.tel_5,self.state_5,
                                  name_list,tel_list,state_list,6)
                elif i%18==7:
                    self.chuanzhi(i-2,self.name_6,self.tel_6,self.state_6,
                                  name_list,tel_list,state_list,7)
                elif i%18==8:
                    self.chuanzhi(i-2,self.name_7,self.tel_7,self.state_7,
                                  name_list,tel_list,state_list,8)
                elif i%18==9:
                    self.chuanzhi(i-2,self.name_8,self.tel_8,self.state_8,
                                  name_list,tel_list,state_list,9)
                elif i%18==10:
                    self.chuanzhi(i-2,self.name_9,self.tel_9,self.state_9,
                                  name_list,tel_list,state_list,10)
                elif i%18==11:
                    self.chuanzhi(i-2,self.name_10,self.tel_10,self.state_10,
                                  name_list,tel_list,state_list,11)
                elif i%18==12:
                    self.chuanzhi(i-2,self.name_11,self.tel_11,self.state_11,
                                  name_list,tel_list,state_list,12)
                elif i%18==13:
                    self.chuanzhi(i-2,self.name_12,self.tel_12,self.state_12,
                                  name_list,tel_list,state_list,13)
                elif i%18==14:
                    self.chuanzhi(i-2,self.name_13,self.tel_13,self.state_13,
                                  name_list,tel_list,state_list,14)
                elif i%18==15:
                    self.chuanzhi(i-2,self.name_14,self.tel_14,self.state_14,
                                  name_list,tel_list,state_list,15)
                elif i%18==16:
                    self.chuanzhi(i-2,self.name_15,self.tel_15,self.state_15,
                                  name_list,tel_list,state_list,16)
                elif i%18==17:
                    self.chuanzhi(i-2,self.name_16,self.tel_16,self.state_16,
                                  name_list,tel_list,state_list,17)
                elif i%18==0:
                    self.chuanzhi(i-2,self.name_17,self.tel_17,self.state_17,
                                  name_list,tel_list,state_list,18)
                elif i % 18 == 1:
                    self.chuanzhi(i-2,self.name_18, self.tel_18, self.state_18,
                                  name_list,tel_list,state_list,19)
        else:
            self.page.set(page-1)

    def chuanzhi(self,id,name,tel,state,name_list,tel_list,state_list,i):
        curr_state_list = ['未联系', '未接通', '停机', '已加微信', '已下载app', '空号', '不需要',
                           '挂断']
        Label(self, text=id, width=13).grid(row=i)
        Entry(self, textvariable=name, width=13).grid(row=i, column=1)
        name.set(name_list[i - 2])
        tel_ = str(tel_list[i - 2])
        cutout_tel = tel_[0:3]+'*'*8
        # print(cutout_tel)
        Entry(self, textvariable=tel, width=15).grid(row=i, column=2)
        tel.set(cutout_tel)

        comboxlist = ttk.Combobox(self, textvariable=state)
        comboxlist['value'] = curr_state_list
        comboxlist.current(0)
        comboxlist.grid(row=i, column=4)
        if state_list[i - 2] == 0:
            state.set('未联系')
        elif state_list[i - 2] == 1:
            state.set('未接通')
        elif state_list[i - 2] == 2:
            state.set('停机')
        elif state_list[i - 2] == 3:
            state.set('已加微信')
        elif state_list[i - 2] == 4:
            state.set('已下载app')
        elif state_list[i - 2] == 5:
            state.set('空号')
        elif state_list[i - 2] == 6:
            state.set('不需要')
        elif state_list[i - 2] == 7:
            state.set('挂断')
        else:
            state.set('error')

    def chaxun_name_page(self):
        print_name = self.chaxun_name.get()
        name = LoginPage.Login_Page.name
        # print(name)
        chaxun_name_list = []
        sql = 'select * from ser_info where vest_in = "'+name+'"'
        result = conn_mysql(sql)
        # print(len(result))
        for n in range(len(result)):
            result_name = result[n][1]
            chaxun_name_list.append(result_name)
        print_name_index = chaxun_name_list.index(print_name)
        # print(print_name_index)

        if print_name_index <=17:
            page = 1
            self.page.set(page - 1)
            self.right_page()
        else:
            page = print_name_index // 18
            yu = print_name_index % 18
            # print(page,yu)
            if yu == 0:
                # print(page)
                self.page.set(page-1)
                self.right_page()
            else:
                page=page+1
                self.page.set(page-1)
                self.right_page()

    def createPage(self):
        name = LoginPage.Login_Page.name
        # print(name)
        Label(self, text='案件列表',font=('',20),fg='blue',height=2).grid(row=0,columnspan=7)

        Label(self, text='输入分机号:',fg='blue').grid(row=0,column=5,stick=E)
        Entry(self,textvariable=self.sipnum).grid(row=0,column=6,stick=W)

        sql = 'select * from ser_info where vest_in = "'+name+'"'
        result = conn_mysql(sql)
        # print(sql)
        name_list = []
        tel_list = []
        state_list = []
        for n in range(len(result)):
            name = result[n][1]
            tel = result[n][2]
            state = result[n][3]
            name_list.append(name)
            tel_list.append(tel)
            state_list.append(state)

        header_list = ['序号','姓名','电话','分机呼叫','当前状态','提交许可']
        for j in range(6):
            Label(self,text=header_list[j],padx=50,fg='red',font=('',10)).grid(row=1,column=j)
        for i in range(2,20):
            if i-2<len(name_list):
                if i%18==2:
                    self.chuanzhi(i-2,self.name_1,self.tel_1,self.state_1,
                                  name_list,tel_list,state_list,i)
                elif i%18==3:
                    self.chuanzhi(i-2,self.name_2,self.tel_2,self.state_2,
                                  name_list,tel_list,state_list,i)
                elif i%18==4:
                    self.chuanzhi(i-2,self.name_3,self.tel_3,self.state_3,
                                  name_list,tel_list,state_list,i)
                elif i%18==5:
                    self.chuanzhi(i-2,self.name_4,self.tel_4,self.state_4,
                                  name_list,tel_list,state_list,i)
                elif i%18==6:
                    self.chuanzhi(i-2,self.name_5,self.tel_5,self.state_5,
                                  name_list,tel_list,state_list,i)
                elif i%18==7:
                    self.chuanzhi(i-2,self.name_6,self.tel_6,self.state_6,
                                  name_list,tel_list,state_list,i)
                elif i%18==8:
                    self.chuanzhi(i-2,self.name_7,self.tel_7,self.state_7,
                                  name_list,tel_list,state_list,i)
                elif i%18==9:
                    self.chuanzhi(i-2,self.name_8,self.tel_8,self.state_8,
                                  name_list,tel_list,state_list,i)
                elif i%18==10:
                    self.chuanzhi(i-2,self.name_9,self.tel_9,self.state_9,
                                  name_list,tel_list,state_list,i)
                elif i%18==11:
                    self.chuanzhi(i-2,self.name_10,self.tel_10,self.state_10,
                                  name_list,tel_list,state_list,i)
                elif i%18==12:
                    self.chuanzhi(i-2,self.name_11,self.tel_11,self.state_11,
                                  name_list,tel_list,state_list,i)
                elif i%18==13:
                    self.chuanzhi(i-2,self.name_12,self.tel_12,self.state_12,
                                  name_list,tel_list,state_list,i)
                elif i%18==14:
                    self.chuanzhi(i-2,self.name_13,self.tel_13,self.state_13,
                                  name_list,tel_list,state_list,i)
                elif i%18==15:
                    self.chuanzhi(i-2,self.name_14,self.tel_14,self.state_14,
                                  name_list,tel_list,state_list,i)
                elif i%18==16:
                    self.chuanzhi(i-2,self.name_15,self.tel_15,self.state_15,
                                  name_list,tel_list,state_list,i)
                elif i%18==17:
                    self.chuanzhi(i-2,self.name_16,self.tel_16,self.state_16,
                                  name_list,tel_list,state_list,i)
                elif i%18==0:
                    self.chuanzhi(i-2,self.name_17,self.tel_17,self.state_17,
                                  name_list,tel_list,state_list,i)
                elif i % 18 == 1:
                    self.chuanzhi(i-2,self.name_18, self.tel_18, self.state_18,
                                  name_list,tel_list,state_list,i)
            else:
                Label(self, text='').grid(row=i)

        Button(self, text='呼叫', command=lambda: self.call_sip(1)).grid(row=2, column=3, pady=5)
        Button(self, text='提交', command=lambda: self.submit_state(1,self.state_1)).grid(row=2, column=5)

        Button(self, text='呼叫', command=lambda: self.call_sip(2)).grid(row=3, column=3, pady=5)
        Button(self, text='提交', command=lambda: self.submit_state(2,self.state_2)).grid(row=3, column=5)

        Button(self, text='呼叫', command=lambda: self.call_sip(3)).grid(row=4, column=3, pady=5)
        Button(self, text='提交', command=lambda: self.submit_state(3,self.state_3)).grid(row=4, column=5)

        Button(self, text='呼叫', command=lambda: self.call_sip(4)).grid(row=5, column=3, pady=5)
        Button(self, text='提交', command=lambda: self.submit_state(4,self.state_4)).grid(row=5, column=5)

        Button(self, text='呼叫', command=lambda: self.call_sip(5)).grid(row=6, column=3, pady=5)
        Button(self, text='提交', command=lambda: self.submit_state(5,self.state_5)).grid(row=6, column=5)

        Button(self, text='呼叫', command=lambda: self.call_sip(6)).grid(row=7, column=3, pady=5)
        Button(self, text='提交', command=lambda: self.submit_state(6,self.state_6)).grid(row=7, column=5)

        Button(self, text='呼叫', command=lambda: self.call_sip(7)).grid(row=8, column=3, pady=5)
        Button(self, text='提交', command=lambda: self.submit_state(7,self.state_7)).grid(row=8, column=5)

        Button(self, text='呼叫', command=lambda: self.call_sip(8)).grid(row=9, column=3, pady=5)
        Button(self, text='提交', command=lambda: self.submit_state(8,self.state_8)).grid(row=9, column=5)

        Button(self, text='呼叫', command=lambda: self.call_sip(9)).grid(row=10, column=3, pady=5)
        Button(self, text='提交', command=lambda: self.submit_state(9, self.state_9)).grid(row=10, column=5)

        Button(self, text='呼叫', command=lambda: self.call_sip(10)).grid(row=11, column=3, pady=5)
        Button(self, text='提交', command=lambda: self.submit_state(10, self.state_10)).grid(row=11, column=5)

        Button(self, text='呼叫', command=lambda: self.call_sip(11)).grid(row=12, column=3, pady=5)
        Button(self, text='提交', command=lambda: self.submit_state(11, self.state_11)).grid(row=12, column=5)

        Button(self, text='呼叫', command=lambda: self.call_sip(12)).grid(row=13, column=3, pady=5)
        Button(self, text='提交', command=lambda: self.submit_state(12, self.state_12)).grid(row=13, column=5)

        Button(self, text='呼叫', command=lambda: self.call_sip(13)).grid(row=14, column=3, pady=5)
        Button(self, text='提交', command=lambda: self.submit_state(13, self.state_13)).grid(row=14, column=5)

        Button(self, text='呼叫', command=lambda: self.call_sip(14)).grid(row=15, column=3, pady=5)
        Button(self, text='提交', command=lambda: self.submit_state(14, self.state_14)).grid(row=15, column=5)

        Button(self, text='呼叫', command=lambda: self.call_sip(15)).grid(row=16, column=3, pady=5)
        Button(self, text='提交', command=lambda: self.submit_state(15, self.state_15)).grid(row=16, column=5)

        Button(self, text='呼叫', command=lambda: self.call_sip(16)).grid(row=17, column=3, pady=5)
        Button(self, text='提交', command=lambda: self.submit_state(16, self.state_16)).grid(row=17, column=5)

        Button(self, text='呼叫', command=lambda: self.call_sip(17)).grid(row=18, column=3, pady=5)
        Button(self, text='提交', command=lambda: self.submit_state(17, self.state_17)).grid(row=18, column=5)

        Button(self, text='呼叫', command=lambda: self.call_sip(18)).grid(row=19, column=3, pady=5)
        Button(self, text='提交', command=lambda: self.submit_state(18, self.state_18)).grid(row=19, column=5)

        Entry(self,textvariable = self.page,width=5).grid(row=20,pady=20,columnspan=6,stick=S)
        self.page.set('1')
        Button(self,text='上一页',font=('',10),command=self.left_page).grid(row=20,columnspan=6,stick=W)
        Button(self,text='下一页',font=('',10),command=self.right_page).grid(row=20,columnspan=6,stick=E)

        Label(self, text='姓名:',fg='blue').grid(row=0,column=0,stick=E)
        Entry(self,textvariable=self.chaxun_name).grid(row=0,column=1,stick=W)
        Button(self, text='翻页', font=('', 10), command=self.chaxun_name_page).grid(row=0,column=2,stick=W)

class yuangongguanli(Frame):  # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.username = StringVar()
        self.passwd = StringVar()
        self.sip = StringVar()
        self.team_name = StringVar()
        self.team_leader = StringVar()
        self.fenzu = StringVar()
        self.fenzu_name = StringVar()
        self.fenzu_group = StringVar()
        self.updata_group = StringVar()
        self.fenan_username = StringVar()
        self.fenan_passwd = StringVar()
        self.fenan_fenpei = StringVar()
        self.fenan_baifenbi = StringVar()

        self.createPage()

    def createPage(self):

        Label(self,text='员工管理',font=('',20),fg='blue',height=5).grid(row=0,columnspan=3,stick=N)

        Button(self,text='添加员工',font=('',10),command=self.create_user).grid(row=1,column=1,stick=W)
        Button(self, text='创建分组', font=('', 10), command=self.create_group).grid(row=1, column=2, stick=E)

        Label(self, text='员工查询', font=('', 20),fg='blue',height=5).grid(row=2,columnspan=3,stick=N)

        Label(self, text='姓名',height=3).grid(row=3, column=0)
        Entry(self, textvariable=self.fenzu).grid(row=3, column=1)
        Button(self, text='查询', width=10, command=self.chaxun_group).grid(row=3, column=2)

        Label(self, text='分组').grid(row=4, column=0)
        Entry(self, textvariable=self.fenzu_name).grid(row=4, column=1)
        Entry(self, textvariable=self.fenzu_group).grid(row=4, column=2)

        Label(self, text='分案管理', font=('', 20),fg='blue',height=5).grid(row=5,columnspan=3,stick=N)

        Label(self, text='用户名',height=3).grid(row=6, column=0)
        Entry(self, textvariable=self.fenan_username).grid(row=6, column=1)
        self.fenan_username.set('祝庆国')
        Button(self, text='查询案件', width=10, command=self.chaxun_fenan).grid(row=6, column=2)
        Label(self, text='密码', height=3).grid(row=7, column=0)
        Entry(self, textvariable=self.fenan_passwd,show='*').grid(row=7, column=1)
        self.fenan_passwd.set('123456')

    def chaxun_fenan(self):
        name = self.fenan_username.get()
        secret = self.fenan_passwd.get()

        sql='select * from users'
        result = conn_mysql(sql)
        user_list = []
        for i in range(len(result)):
            user_list.append(result[i][1])
        # print(user_list)

        if name in user_list:
            print('用户名正确')
            # 索引用户账户位置
            username_index = user_list.index(name)
            # print(username_index)
            if result[username_index][3] == 0:
                if secret == result[username_index][2]:
                    print('密码验证通过')

                    sql1 = 'select author from users where username = "'+name+'"'
                    result = conn_mysql(sql1)[0][0]
                    if result == 1:
                        sql2 = 'select username from users where author = 2'
                        # print(sql2)
                        result_sql2 = conn_mysql(sql2)
                        # print(result_sql2)
                        sql2_list = []
                        for i in range(len(result_sql2)):
                            sql2_list.append(result_sql2[i][0])
                        # print(sql2_list)
                        top = Toplevel()
                        top.title('分配界面')
                        top.geometry('300x80+650+450')
                        top.attributes("-topmost", 1)

                        Label(top, text='分配给:').grid(row=0, column=0)
                        comboxlist = ttk.Combobox(top,textvariable = self.fenan_fenpei)
                        comboxlist['value'] = sql2_list
                        comboxlist.current(0)
                        comboxlist.grid(row=0, column=1)

                        Button(top, text='提交', width=10, command=self.submit_fenpei).grid(row=0, column=2)
                        Label(top, text='百分比:').grid(row=1, column=0)
                        Entry(top, textvariable=self.fenan_baifenbi).grid(row=1, column=1)

                    elif result == 2:
                        sql2 = 'select username from users where author = 3'
                        result_sql2 = conn_mysql(sql2)
                        sql2_list = []
                        for i in range(len(result_sql2)):
                            sql2_list.append(result_sql2[i][0])
                        # print(sql2_list)
                        top = Toplevel()
                        top.title('分配界面')
                        top.geometry('300x80+650+450')
                        top.attributes("-topmost", 1)

                        Label(top, text='分配给:').grid(row=0, column=0)
                        comboxlist = ttk.Combobox(top, textvariable=self.fenan_fenpei)
                        comboxlist['value'] = sql2_list
                        comboxlist.current(0)
                        comboxlist.grid(row=0, column=1)

                        Button(top, text='提交', width=10, command=self.submit_fenpei).grid(row=0, column=2)
                        Label(top, text='百分比:').grid(row=1, column=0)
                        Entry(top, textvariable=self.fenan_baifenbi).grid(row=1, column=1)
                    else:
                        messagebox.showinfo('提示','您的账号没有权限')

                else:
                    print('密码验证错误')
                    messagebox.showinfo(title='错误', message='密码错误！')
            else:
                messagebox.showerror(title='错误', message='账号已锁定！请联系管理员解锁')
        else:
            messagebox.showinfo(title='错误', message='账号错误！')


    def submit_fenpei(self):
        if self.fenan_username.get() == '祝庆国':
            fenpeiren = self.fenan_fenpei.get()
            print(fenpeiren)
            baifenbi = self.fenan_baifenbi.get()
            baifenbi = int(baifenbi)
            # print(fenpeiren,baifenbi)
            if 0<=baifenbi<=100:
                sql4 = 'UPDATE ser_info AS A INNER JOIN (select id from ser_info where vest_in is NULL) AS B ON A.id=B.id SET A.vest_in="'+fenpeiren+'"'
                # print(sql4)
                conn_mysql(sql4)
                messagebox.showinfo('提示','案件分配成功!')
            else:
                messagebox.showerror('error','百分比错误!')
        else:
            fenpeiren = self.fenan_fenpei.get()
            print(fenpeiren)
            baifenbi = self.fenan_baifenbi.get()
            baifenbi = int(baifenbi)
            # print(fenpeiren,baifenbi)
            if 0<=baifenbi<=100:
                fenan_username = self.fenan_username.get()
                sql3 = 'select vest_in from ser_info where vest_in = "'+fenan_username+'"'
                result_vest_in = conn_mysql(sql3)
                count = len(result_vest_in)
                curr_count = count * baifenbi // 100
                # print(curr_count)
                curr_count = str(curr_count)
                sql4 = 'update ser_info set vest_in="'+fenpeiren+'" ORDER BY vest_in DESC LIMIT '+curr_count+''
                # print(sql4)
                conn_mysql(sql4)
                messagebox.showinfo('提示','案件分配成功!')
            else:
                messagebox.showerror('error','百分比错误!')


    def create_user(self):
        top = Toplevel()
        top.title('创建用户')
        top.geometry('300x80+650+450')
        top.attributes("-topmost", 1)

        Label(top,text='姓名').grid(row=0,column=0)
        Entry(top,textvariable=self.username).grid(row=0, column=1)
        Label(top,text='密码').grid(row=1,column=0)
        Entry(top,textvariable=self.passwd).grid(row=1, column=1)
        Button(top,text='提交',width=10,command=self.submit_user).grid(row=1,column=2)

    def create_group(self):
        top = Toplevel()
        top.title('创建分组')
        top.geometry('300x80+650+450')
        top.attributes("-topmost", 1)

        Label(top, text='组名').grid(row=0, column=0)
        Entry(top, textvariable=self.team_name).grid(row=0, column=1)
        Label(top, text='组长').grid(row=1, column=0)
        Entry(top, textvariable=self.team_leader).grid(row=1, column=1)
        Button(top, text='提交', width=10, command=self.submit_group).grid(row=1, column=2)

    def submit_user(self):
        username = self.username.get()
        passwd = self.passwd.get()
        print(username,passwd)
        if username == '' or passwd == '':
            messagebox.showinfo('提示', '信息不能为空')
        else:
            sql = 'insert into users(username,passwd) values("%s","%s")'%(username,passwd)
            conn_mysql(sql)
            messagebox.showinfo('提示', '提交成功,关闭窗口即可')
            self.username.set('')
            self.passwd.set('')

    def submit_group(self):
        team_name = self.team_name.get()
        team_leader = self.team_leader.get()
        if team_name == '' or team_leader == '':
            messagebox.showinfo('提示', '信息不能为空')
        else:
            sql = 'insert into cui_group(team,team_leader) values("%s","%s")'%(team_name,team_leader)
            # print(sql)
            conn_mysql(sql)
            messagebox.showinfo('提示', '提交成功,关闭窗口即可')
            self.team_name.set('')
            self.team_leader.set('')

    def chaxun_group(self):
        self.fenzu_name.set('')
        self.fenzu_group.set('')
        name = self.fenzu.get()
        sql = 'select team from users where username = "'+name+'"'
        try:
            result = conn_mysql(sql)[0][0]
            self.fenzu_name.set(name)
            self.fenzu_group.set(result)
            Button(self, text='更换分组', font=('', 10), command=self.click_group).grid(row=4, column=3, stick=E)

        except:
            self.fenzu_name.set(name)
            self.fenzu_group.set('未分组')
            Button(self, text='点击分组', font=('', 10), command=self.click_group).grid(row=4, column=3, stick=E)

    def click_group(self):
        name = self.fenzu.get()

        sql = 'select username from users'
        result = conn_mysql(sql)
        count = len(result)
        name_list = []
        for i in range(count):
            team = result[i][0]
            name_list.append(team)
        # print(name_list)
        if name in name_list:
            top = Toplevel()
            top.title('分组')
            top.geometry('300x80+650+450')
            top.attributes("-topmost", 1)

            Label(top,text='输入组名').grid(row=0,column=0)
            Entry(top,textvariable=self.updata_group).grid(row=0, column=1)
            Button(top,text='提交',width=10,command=self.submite_updata_group).grid(row=0,column=2)
        else:
            messagebox.showinfo('提示','不存在此员工')

    def submite_updata_group(self):
        name = self.fenzu_name.get()
        update_group = self.updata_group.get()
        # print(update_group)
        sql = 'select team from cui_group'
        result = conn_mysql(sql)
        count = len(result)
        group_list = []
        for i in range(count):
            team = result[i][0]
            group_list.append(team)
        # print(group_list)
        if  update_group in group_list:
            sql1 = 'update users set team="'+update_group+'" where username = "'+name+'"'
            try:
                conn_mysql(sql1)
                messagebox.showinfo('提示','更改成功')
            except:
                messagebox.showinfo('提示','更改失败')
        else:
            messagebox.showinfo('提示','不存在此分组')

class about(Frame):
    def __init__(self,master=None):
        Frame.__init__(self, master)
        self.root = master  # 定义内部变量root
        self.createPage()

    def createPage(self):
        Label(self, text='关于',height=5,font=('',30),fg='blue').pack()
        T = Text(self)
        T.insert(END,'感谢您使用这款软件，该软件由郑州华塬商业管理有限公司倾情赞助完成。 \n'
                     '由于作者水平有限，软件有诸多不足之处请多多海涵，该软件仅供用于学习、 \n'
                     '参考、技术研究使用。严禁用于其他用途，如产生任何法律纠纷概于作者 \n'
                     '和任何组织无关。 \n'
                     '\n'
                     '\n'
                     '感谢您的使用!')
        T.pack()
