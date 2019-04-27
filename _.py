import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
                             QHBoxLayout, QVBoxLayout, QApplication, QTableWidget, QTableWidgetItem, QComboBox)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()
        self.init_table_data()

    def initUI(self):
        self.table = QTableWidget()
        self.table.setColumnCount(6)

        column_name = [
            'ETH/BIC',
            'column1',
            'column2',
            'column3',
            'column4',
            'column5',
        ]
        self.table.setHorizontalHeaderLabels(column_name)  # 设置列名称
        self.table.verticalHeader().hide()
        okButton = QPushButton("添加")
        cancelButton = QPushButton("删除")
        okButton.clicked.connect(self.del_item)

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(self.table)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 520, 300)
        self.setWindowTitle('Buttons')
        self.show()
    def init_table_data(self):
        '''
            建议的tue任务配置数据结构：
            {
            环境名1:{"operate":[操作1,操作2,...],"dir":输入路径}，
            环境名2:{"operate":[操作1,操作2,...],"dir":输入路径}，
            }
        '''
        items = {}
        item_data = [1,2,3,4]
        for i in range(1,6):
            items[i]={'data':item_data,'dir':'dir%s' % i,'len_data':len(item_data)}
        item_row = 0 # 每一个对象的初始行数
        for j in items:
            item = items[j]
            item['start_row'] = item_row
            rows=item['len_data']
            self.table.setRowCount(item_row+rows)
            self.table.setSpan(item_row,0,rows,1)
            self.table.setItem(item_row, 0, QTableWidgetItem(str(j)))
            # 将这里一列变成按钮
            self.table.setSpan(item_row,5,rows,1)
            self.table.setItem(item_row, 5, QTableWidgetItem(str(item['dir'])))

            for row in range(item_row,item_row+rows):
                for col in range(1,5):
                    self.table.setItem(row, col, QTableWidgetItem(str(item["data"][col - 1])))
            item_row += rows
        print(items)
        # for i in range(5):
        #     for j in range(5):
        #         # 1)直接在表格中添加数据
        #         self.table.setItem(i, j, QTableWidgetItem(str(i) + str(j)))
    def del_item(self):
        pass





if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())