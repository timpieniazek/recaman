
n = 50

seq = [0]

for x in range(1,n):
	if ((seq[x-1] - x > 0) and (seq[x-1] - x not in seq)):
		seq.append(seq[x-1] - x)
	else:
		seq.append(seq[x-1] + x)

for num in seq:
	print(num)