# includes
# none


def get(integer, index):
	mask = 1 << index
	return True if integer & mask else False


def set(integer, index, value):
	mask = 1 << index
	return integer | mask if value else integer & ~mask


def left(integer, shift):
	if shift < 0:
		return integer >> -shift
	return integer << shift


def right(integer, shift):
	if shift < 0:
		return integer << -shift
	return integer >> shift


# highest order bit / most significant bit
def msb(integer):
	shift = -1
	while integer:
		integer >>= 1
		shift += 1
	return 1 << shift if shift != -1 else 0
