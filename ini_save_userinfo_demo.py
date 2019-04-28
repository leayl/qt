"""
    配置文件记载用户配置的例子
"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import threading


################################################
#######创建主窗口
################################################
class MainWindow(QMainWindow):
    windowList = []

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('主界面')
        self.showMaximized()

        # 创建菜单栏
        self.createMenus()

    def createMenus(self):
        # 创建动作 注销
        self.printAction1 = QAction(self.tr("注销"), self)
        self.printAction1.triggered.connect(self.on_printAction1_triggered)

        # 创建动作 退出
        self.printAction2 = QAction(self.tr("退出"), self)
        self.printAction2.triggered.connect(self.on_printAction2_triggered)

        # 创建菜单，添加动作
        self.printMenu = self.menuBar().addMenu(self.tr("注销和退出"))
        self.printMenu.addAction(self.printAction1)
        self.printMenu.addAction(self.printAction2)

    # 动作一：注销
    def on_printAction1_triggered(self):
        self.close()
        dialog = logindialog(mode=1)
        if dialog.exec_() == QDialog.Accepted:
            the_window = MainWindow()
            self.windowList.append(the_window)  # 这句一定要写，不然无法重新登录
            the_window.show()

    # 动作二：退出
    def on_printAction2_triggered(self):
        self.close()

    # 关闭界面触发事件
    def closeEvent(self, event):
        print(999999999)
        pass


################################################
#######对话框
################################################
class logindialog(QDialog):
    def __init__(self, mode=0, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.mode = mode
        self.setWindowTitle('登录界面')
        self.resize(200, 200)
        self.setFixedSize(self.width(), self.height())
        self.setWindowFlags(Qt.WindowCloseButtonHint)

        ###### 设置界面控件
        self.frame = QFrame(self)
        self.verticalLayout = QVBoxLayout(self.frame)

        self.list = QListWidget()
        self.list.itemClicked.connect(self.clicked)

        self.pushButton_enter = QPushButton()
        self.pushButton_enter.setText("确定")
        self.pushButton_save = QPushButton()
        self.pushButton_save.setText("保存")
        self.verticalLayout.addWidget(self.pushButton_enter)
        self.verticalLayout.addWidget(self.pushButton_save)
        self.verticalLayout.addWidget(self.list)

        ###### 绑定按钮事件
        self.pushButton_enter.clicked.connect(self.on_pushButton_enter_clicked)
        self.pushButton_save.clicked.connect(self.save_login_info)

        ####初始化登录信息
        self.init_login_info()

        ####自动登录

    # 自动登录
    def goto_autologin(self):
        if self.checkBox_autologin.isChecked() == True and self.mode == 0:
            self.on_pushButton_enter_clicked()

    def on_pushButton_enter_clicked(self):
        # 账号判断
        if self.lineEdit_account.text() == "":
            return

        # 密码判断
        if self.lineEdit_password.text() == "":
            return

        ####### 保存登录信息
        self.save_login_info()

        # 通过验证，关闭对话框并返回1
        self.accept()

    # 保存登录信息
    def save_login_info(self):
        info = {
            "config1": {
                "env1": {"operate": [1, 2, 3], "path": "path1"},
                "env2": {"operate": [1, 2, 3], "path": "path2"},
                "env3": {"operate": [1, 2, 3], "path": "path3"},
            },
            "config2": {
                "env1": {"operate": [1, 2, 3], "path": "path1"},
                "env2": {"operate": [1, 2, 3], "path": "path2"},
            },
        }
        settings = QSettings("config.ini", QSettings.IniFormat)  # 方法1：使用配置文件
        # settings = QSettings("mysoft","myapp")                        #方法2：使用注册表
        settings.setValue("config", info)

    # 初始化登录信息
    def init_login_info(self):
        settings = QSettings("config.ini", QSettings.IniFormat)  # 方法1：使用配置文件
        # settings = QSettings("mysoft","myapp")                        #方法2：使用注册表

        self.config = settings.value("config")
        if self.config:
            list_items = self.config.keys()
            self.list.addItems(list_items)

    def clicked(self, item):
        recent_config_name = item.text()
        QMessageBox.information(self, "ListWidget", "你选择了: " + recent_config_name)
        print(self.config.get(recent_config_name).keys())



################################################
#######程序入门
################################################
if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = logindialog(mode=0)
    if dialog.exec_() == QDialog.Accepted:
        the_window = MainWindow()
        the_window.show()
        sys.exit(app.exec_())
