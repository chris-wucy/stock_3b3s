data = [9422, 9468, 9512, 9524, 9550, 9450, 9410, 9368]
# data = []
def three_days(data):
	if not data:
		return
	action = []
	count_r = 0
	count_d = 0
	d_last = data[0]
	for d in data:
		if d > d_last:
			count_r += 1
			count_d = 0
		elif d < d_last:
			count_d += 1
			count_r = 0

		if count_r >= 3:
			action.append(1)
		elif count_d >= 3:
			action.append(-1)
		else:
			action.append(0)
		d_last = d
	return action		


def main():
	print(three_days(data))

main()