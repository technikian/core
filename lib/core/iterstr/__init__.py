
def partition(src_str, sep):
	r = []
	# first partition
	parted = src_str.partition(sep)
	# middle partitions
	while parted[1] != '':
		if parted[0] == '':
			r.append(parted[1])
		else:
			r.extend(parted[:2])
		src_str = parted[2]
		parted = src_str.partition(sep)
	# last partition
	if parted[0] != '':
		r.append(parted[0])
	return r


def join(*iterables):
	i = iter(iterables)
	r = None
	try:
		r = next(i)
		while True:
			r = r + next(i)
	except StopIteration:
		return r
