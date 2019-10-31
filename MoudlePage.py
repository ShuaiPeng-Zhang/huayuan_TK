from view import *  # 菜单栏对应的各个子页面


class MainPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        # self.root.geometry('%dx%d' % (600, 400))  # 设置窗口大小
        self.createPage()

    def createPage(self):
        self.indexPage = index(self.root)  # 创建不同Frame
        self.shujuchaxunPage = shujuchaxun(self.root)
        self.wodeanjianPage = wodeanjian(self.root)
        self.yuangongguanliPage = yuangongguanli(self.root)
        self.aboutPage = about(self.root)
        self.indexPage.pack()  # 默认显示数据录入界面

        menubar = Menu(self.root)
        menubar.add_command(label='首页', command=self.index)
        menubar.add_command(label='数据查询', command=self.shujuchaxun)
        menubar.add_command(label='我的案件', command=self.wodeanjian)
        menubar.add_command(label='员工管理', command=self.yuangongguanli)
        menubar.add_command(label='关于',command=self.about)
        self.root['menu'] = menubar  # 设置菜单栏

    def index(self):
        self.indexPage.pack()
        self.shujuchaxunPage.pack_forget()
        self.wodeanjianPage.pack_forget()
        self.yuangongguanliPage.pack_forget()
        self.aboutPage.pack_forget()

    def shujuchaxun(self):
        self.indexPage.pack_forget()
        self.shujuchaxunPage.pack()
        self.wodeanjianPage.pack_forget()
        self.yuangongguanliPage.pack_forget()
        self.aboutPage.pack_forget()

    def wodeanjian(self):
        self.indexPage.pack_forget()
        self.shujuchaxunPage.pack_forget()
        self.wodeanjianPage.pack()
        self.yuangongguanliPage.pack_forget()
        self.aboutPage.pack_forget()

    def yuangongguanli(self):
        self.indexPage.pack_forget()
        self.shujuchaxunPage.pack_forget()
        self.wodeanjianPage.pack_forget()
        self.yuangongguanliPage.pack()
        self.aboutPage.pack_forget()

    def about(self):
        self.indexPage.pack_forget()
        self.shujuchaxunPage.pack_forget()
        self.wodeanjianPage.pack_forget()
        self.yuangongguanliPage.pack_forget()
        self.aboutPage.pack()