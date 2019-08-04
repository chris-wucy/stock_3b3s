
# def read_file(filename):
# 	prices = []
# 	with open(filename, 'r', encoding = 'utf-8') as f:
# 		for line in f:
# 			if 'Adj Close' in line:
# 				continue
# 			price = line.strip().split(',')
# 			prices.append(price[5])
# 	return prices

import pandas as pd

def read_csv(file):
    # converters 那邊是告訴它Adj Close那欄 我要讀取成float，否則他預設會是字串。
    df = pd.read_csv(file, converters={'Adj Close': float}) 
    df = df['Adj Close'] # 我只要Adj Close那欄的資料
    return df.tolist() # 轉換回python內建的list物件


def three_days(data):
    output = []
    for i in range(len(data)):
        if i < 3:
            output.append(0)
        elif data[i] > data[i-1] > data[i-2] > data[i-3]:
            output.append(1)
        elif data[i] < data[i-1] < data[i-2] < data[i-3]:
            output.append(-1)
        else:
            output.append(0)
    return output


def calc_profit(data, signal):
    pos = 0 # 持有方向
    entry = 0 # 進場價
    total  = 0 # 總共賺的錢
    for i in range(len(data)):
        if signal[i] == 1:
            if pos == 0: # 表示目前沒有持股
                entry = data[i] # 那就只是單純進場，紀錄成本價就好
            elif pos == -1: # 原本持有空單，現在遇到買進訊號
                # 因為要把空單出場，換成多單
                # 要先計算 此筆單出場的獲利
                profit = entry - data[i] # 空單的獲利是 成本價 - 現在價格
                total += profit
                entry = data[i]
            pos = 1 # 把持有方向 設為 1
        elif signal[i] == -1:
            if pos == 0: # 表示目前沒有持股
                entry = data[i] # 那就只是單純進場，紀錄成本價就好
            elif pos == 1: # 原本持有多單，現在遇到賣出訊號
                # 因為要把多單出場，換成空單
                # 要先計算 此筆單出場的獲利
                profit = data[i] - entry  # 空單的獲利是 成本價 - 現在價格
                total += profit
                entry = data[i]
            pos = -1 # 把持有方向 設為 1

    return total * 1000 # 放大一千倍因為每次交易都是一張(1000股)





def main():
	filename = '2330.csv'
	prices = read_csv(filename)
	signals = three_days(prices)
	print(calc_profit(prices, signals))

main()