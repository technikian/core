from ._impl_ import left as shift_left


# the $300 function
# took 12 hours to write...
# ... and 1 hour later I've already forgotten how it works ...
# ... nor do I want to know.

# src = byte array source
# src_bit = bit index of source
# tgt = byte array target
# tgt_bit = bit index of target
# bit_len = number of bits to copy
# lim = size of target (in bytes), for safety
def copy(src, src_bit, tgt, tgt_bit, bit_len, lim=0):

	# find minimum required limit
	req_lim = (tgt_bit + bit_len + 7) // 8  # find the required limit of target to complete operation

	# auto generate limit if it is not provided
	if lim == 0:
		lim = len(tgt)  # find the current limit of target
		if lim < req_lim:  # if target length is insufficient...
			tgt.extend(bytearray(req_lim - lim))  # extend it by the difference, you retard
			lim = len(tgt)

	# check limit
	if lim < req_lim:
		return

	# setup constants
	shift = (tgt_bit % 8) - (src_bit % 8)
	end_msk = 0xff >> ((8 - (tgt_bit + bit_len)) % 8)
	src_lim = (src_bit + bit_len + 7) // 8
	tgt_lim = (tgt_bit + bit_len + 7) // 8

	# setup dynamics
	src_idx = src_bit // 8
	tgt_idx = tgt_bit // 8
	src_msk = 0  # must be 32 bit
	tgt_msk = 0xff << (tgt_bit % 8)  # mask which bytes in current idx of target may be changed

	# first case
	if src_idx != src_lim:
		src_msk |= shift_left(src[src_idx] << 8, shift)
		src_idx += 1

	# copy whole bytes
	while tgt_idx != tgt_lim:
		src_msk >>= 8

		# copy from source
		if src_idx != src_lim:
			src_msk |= shift_left(src[src_idx] << 8, shift)
			src_idx += 1

		# end case
		if tgt_idx + 1 == tgt_lim:
			tgt_msk &= end_msk

		# copy into target
		tgt[tgt_idx] &= 0xff & ~tgt_msk
		tgt[tgt_idx] |= 0xff & src_msk & tgt_msk
		tgt_msk = 0xff
		tgt_idx += 1

	return
