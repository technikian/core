#
# logical implementation
#


#
# get/set/shift
#

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


#
# order
#

def hob(integer):
	"""highest order bit / most significant bit"""
	shift = -1
	while integer:
		integer >>= 1
		shift += 1
	return 1 << shift if shift != -1 else 0


def lob(integer):
	"""lowest order bit / most significant bit"""
	raise NotImplementedError


#
# reverse
#

def reverse(source: int, length: int):
	"""logical reverse: reverse bit order"""
	r = 0
	for i in reversed(range(length)):
		r |= (source & 1) << i
		source >>= 1
	return r

# def logical_reverse(x):  # more efficient way to reverse bits?
#     x = ((x & 0x55555555) << 1) | ((x & 0xAAAAAAAA) >> 1)
#     x = ((x & 0x33333333) << 2) | ((x & 0xCCCCCCCC) >> 2)
#     x = ((x & 0x0F0F0F0F) << 4) | ((x & 0xF0F0F0F0) >> 4)
#     x = ((x & 0x00FF00FF) << 8) | ((x & 0xFF00FF00) >> 8)
#     x = ((x & 0x0000FFFF) << 16) | ((x & 0xFFFF0000) >> 16)
#     return x
