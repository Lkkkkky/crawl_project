import sys
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QTextEdit, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QPalette, QColor
import pyqtgraph as pg
import pandas as pd
from datetime import datetime
from main import TradingBot

class TradingBotGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.bot = TradingBot()
        self.initUI()
        
        # 更新定时器
        self.timer = QTimer()
        self.timer.timeout.connect(self.updateData)
        self.timer.start(60000)  # 每分钟更新一次
        
    def initUI(self):
        self.setWindowTitle('量化交易机器人')
        self.setGeometry(100, 100, 1200, 800)
        
        # 创建主窗口部件和布局
        mainWidget = QWidget()
        self.setCentralWidget(mainWidget)
        layout = QVBoxLayout(mainWidget)
        
        # 创建上部分布局（K线图和交易信息）
        topLayout = QHBoxLayout()
        
        # K线图区域
        self.plotWidget = pg.PlotWidget()
        self.plotWidget.setBackground('w')
        self.plotWidget.setLabel('left', 'Price')
        self.plotWidget.setLabel('bottom', 'Time')
        topLayout.addWidget(self.plotWidget, stretch=2)
        
        # 交易信息区域
        infoWidget = QWidget()
        infoLayout = QVBoxLayout(infoWidget)
        
        # 账户信息
        accountGroup = QWidget()
        accountLayout = QVBoxLayout(accountGroup)
        self.balanceLabel = QLabel(f'账户余额: {self.bot.balance:.2f} USDT')
        self.positionLabel = QLabel(f'当前持仓: {self.bot.position_size}')
        accountLayout.addWidget(self.balanceLabel)
        accountLayout.addWidget(self.positionLabel)
        infoLayout.addWidget(accountGroup)
        
        # 交易按钮
        self.startButton = QPushButton('开始交易')
        self.startButton.clicked.connect(self.startTrading)
        self.stopButton = QPushButton('停止交易')
        self.stopButton.clicked.connect(self.stopTrading)
        self.stopButton.setEnabled(False)
        
        infoLayout.addWidget(self.startButton)
        infoLayout.addWidget(self.stopButton)
        
        # 日志区域
        self.logText = QTextEdit()
        self.logText.setReadOnly(True)
        infoLayout.addWidget(self.logText)
        
        topLayout.addWidget(infoWidget, stretch=1)
        layout.addLayout(topLayout)
        
        # 创建下部分布局（交易历史）
        self.tradeTable = QTableWidget()
        self.tradeTable.setColumnCount(6)
        self.tradeTable.setHorizontalHeaderLabels(['时间', '类型', '价格', '数量', '成本/收益', '余额'])
        layout.addWidget(self.tradeTable)
        
        self.updateData()
        
    def updateData(self):
        try:
            # 获取最新数据
            df = self.bot.fetch_ohlcv()
            if df is not None:
                # 更新K线图
                self.plotWidget.clear()
                self.plotWidget.plot(range(len(df)), df['close'].values, pen='b')
                
                # 添加MA线
                df = self.bot.calculate_indicators(df)
                self.plotWidget.plot(range(len(df)), df['MA5'].values, pen='r')
                self.plotWidget.plot(range(len(df)), df['MA10'].values, pen='g')
                
                # 更新账户信息
                self.balanceLabel.setText(f'账户余额: {self.bot.balance:.2f} USDT')
                self.positionLabel.setText(f'当前持仓: {self.bot.position_size}')
                
                # 更新交易历史
                self.updateTradeHistory()
                
                self.log('数据更新成功')
        except Exception as e:
            self.log(f'更新数据失败: {e}')
    
    def updateTradeHistory(self):
        self.tradeTable.setRowCount(len(self.bot.trades))
        for i, trade in enumerate(self.bot.trades):
            self.tradeTable.setItem(i, 0, QTableWidgetItem(str(trade['timestamp'])))
            self.tradeTable.setItem(i, 1, QTableWidgetItem(trade['type']))
            self.tradeTable.setItem(i, 2, QTableWidgetItem(f"{trade['price']:.2f}"))
            self.tradeTable.setItem(i, 3, QTableWidgetItem(f"{trade['amount']:.3f}"))
            
            if trade['type'] == 'buy':
                self.tradeTable.setItem(i, 4, QTableWidgetItem(f"-{trade['cost']:.2f}"))
            else:
                self.tradeTable.setItem(i, 4, QTableWidgetItem(f"+{trade['revenue']:.2f}"))
                
            self.tradeTable.setItem(i, 5, QTableWidgetItem(f"{trade['balance']:.2f}"))
    
    def startTrading(self):
        self.bot.running = True
        self.startButton.setEnabled(False)
        self.stopButton.setEnabled(True)
        self.log('开始交易')
        
    def stopTrading(self):
        self.bot.running = False
        self.startButton.setEnabled(True)
        self.stopButton.setEnabled(False)
        self.log('停止交易')
    
    def log(self, message):
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        self.logText.append(f'[{timestamp}] {message}')

def main():
    app = QApplication(sys.argv)
    gui = TradingBotGUI()
    gui.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()