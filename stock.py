
def read_file(filename):
	prices = []
	with open(filename, 'r', encoding = 'utf-8') as f:
		for line in f:
			price = line.strip().split(',')
			prices.append(price[5])
		return prices


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

def main():
	filename = '2330.csv'
	prices = read_file(filename)
	signals = three_days(prices)
	print(len(prices))
	print(len(signals))
main()