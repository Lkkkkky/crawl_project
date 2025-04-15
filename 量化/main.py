import os
import ccxt
import pandas as pd
import pandas_ta as ta
import numpy as np
from datetime import datetime
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

class TradingBot:
    def __init__(self):
        # 初始化交易所API
        self.exchange = ccxt.okx({
            'apiKey': os.getenv('OKX_API_KEY'),
            'secret': os.getenv('OKX_SECRET'),
            'password': os.getenv('OKX_PASSWORD'),
            'enableRateLimit': True
        })
        
        # 交易参数
        self.symbol = 'BTC/USDT'  # 交易对
        self.timeframe = '1h'      # K线周期
        self.position = None       # 当前持仓
        
        # 回测参数
        self.initial_balance = 10000  # 初始资金
        self.balance = self.initial_balance  # 当前资金
        self.trades = []  # 交易记录
        self.position_size = 0  # 持仓数量
        self.trade_amount = 0.001  # 每次交易数量
        self.running = False  # 交易状态  # 每次交易数量
    
    def fetch_ohlcv(self, limit=100):
        """获取K线数据"""
        try:
            ohlcv = self.exchange.fetch_ohlcv(self.symbol, self.timeframe, limit=limit)
            df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
            df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
            return df
        except Exception as e:
            print(f'获取K线数据失败: {e}')
            return None
    
    def calculate_indicators(self, df):
        """计算技术指标"""
        # 使用pandas_ta计算MA
        df['MA5'] = ta.sma(df['close'], length=5)
        df['MA10'] = ta.sma(df['close'], length=10)
        
        # 使用pandas_ta计算RSI
        df['RSI'] = ta.rsi(df['close'], length=14)
        
        return df
    
    def check_signals(self, df):
        """检查交易信号"""
        if len(df) < 10:
            return None
            
        last_row = df.iloc[-1]
        
        # 简单的MA交叉策略
        if last_row['MA5'] > last_row['MA10'] and df.iloc[-2]['MA5'] <= df.iloc[-2]['MA10']:
            return 'buy'
        elif last_row['MA5'] < last_row['MA10'] and df.iloc[-2]['MA5'] >= df.iloc[-2]['MA10']:
            return 'sell'
            
        return None
    
    def execute_trade(self, signal):
        """执行交易（模拟）"""
        try:
            current_price = self.df.iloc[-1]['close']
            timestamp = self.df.iloc[-1]['timestamp']
            
            if signal == 'buy' and self.position != 'long':
                # 模拟买入
                cost = current_price * self.trade_amount
                if cost <= self.balance:
                    self.balance -= cost
                    self.position_size = self.trade_amount
                    self.position = 'long'
                    
                    trade = {
                        'timestamp': timestamp,
                        'type': 'buy',
                        'price': current_price,
                        'amount': self.trade_amount,
                        'cost': cost,
                        'balance': self.balance
                    }
                    self.trades.append(trade)
                    print(f'买入信号执行成功 - {timestamp} - 价格: {current_price} - 余额: {self.balance}')
                
            elif signal == 'sell' and self.position != 'short':
                # 模拟卖出
                if self.position_size > 0:
                    revenue = current_price * self.position_size
                    self.balance += revenue
                    self.position_size = 0
                    self.position = 'short'
                    
                    trade = {
                        'timestamp': timestamp,
                        'type': 'sell',
                        'price': current_price,
                        'amount': self.trade_amount,
                        'revenue': revenue,
                        'balance': self.balance
                    }
                    self.trades.append(trade)
                    print(f'卖出信号执行成功 - {timestamp} - 价格: {current_price} - 余额: {self.balance}')
                
        except Exception as e:
            print(f'交易执行失败: {e}')
    
    def calculate_performance(self):
        """计算回测性能指标"""
        if not self.trades:
            return
            
        # 计算收益率
        total_return = (self.balance - self.initial_balance) / self.initial_balance * 100
        
        # 计算最大回撤
        peak_balance = self.initial_balance
        max_drawdown = 0
        
        for trade in self.trades:
            current_balance = trade['balance']
            if current_balance > peak_balance:
                peak_balance = current_balance
            drawdown = (peak_balance - current_balance) / peak_balance * 100
            max_drawdown = max(max_drawdown, drawdown)
        
        print(f'\n回测结果:')
        print(f'初始资金: {self.initial_balance} USDT')
        print(f'最终资金: {self.balance} USDT')
        print(f'总收益率: {total_return:.2f}%')
        print(f'最大回撤: {max_drawdown:.2f}%')
        print(f'总交易次数: {len(self.trades)}')
    
    def run(self):
        """运行回测"""
        print(f'开始回测 - {datetime.now()}')
        
        # 获取历史数据
        self.df = self.fetch_ohlcv(limit=1000)  # 获取更多历史数据用于回测
        if self.df is None:
            return
            
        # 计算指标
        self.df = self.calculate_indicators(self.df)
        
        # 遍历历史数据进行回测
        for i in range(10, len(self.df)):
            current_data = self.df.iloc[:i+1]
            signal = self.check_signals(current_data)
            
            if signal:
                self.execute_trade(signal)
        
        # 计算并显示回测结果
        self.calculate_performance()
    
    def run(self):
        """运行交易机器人"""
        print(f'开始运行交易机器人 - {datetime.now()}')
        
        while True:
            try:
                # 获取市场数据
                df = self.fetch_ohlcv()
                if df is None:
                    continue
                    
                # 计算指标
                df = self.calculate_indicators(df)
                
                # 检查信号
                signal = self.check_signals(df)
                
                # 执行交易
                if signal:
                    self.execute_trade(signal)
                    
                # 等待一段时间再次检查
                self.exchange.sleep(60)  # 休眠1分钟
                
            except Exception as e:
                print(f'运行出错: {e}')
                self.exchange.sleep(60)

if __name__ == '__main__':
    bot = TradingBot()
    bot.run()