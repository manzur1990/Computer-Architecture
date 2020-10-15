def ripple_carry_add(a, b):
	"""
	8-bit ripple carry adder.
​
	Adds two 8-bit numbers for an 8-bit result.
​
	Returns tuple (result, carry)
​
	If the result overflows 8 bits, the carry flag is set to 1.
	"""
​
	# Get individual bits of the numbers
​
	a0 = (a >> 0) & 1
	a1 = (a >> 1) & 1
	a2 = (a >> 2) & 1
	a3 = (a >> 3) & 1
	a4 = (a >> 4) & 1
	a5 = (a >> 5) & 1
	a6 = (a >> 6) & 1
	a7 = (a >> 7) & 1
​
	b0 = (b >> 0) & 1
	b1 = (b >> 1) & 1
	b2 = (b >> 2) & 1
	b3 = (b >> 3) & 1
	b4 = (b >> 4) & 1
	b5 = (b >> 5) & 1
	b6 = (b >> 6) & 1
	b7 = (b >> 7) & 1
​
	result = 0
​
	c = 0  # Initial carry in
​
	# Add bit 0
	s = a0 ^ b0 ^ c
	c = (a0 & b0) | (c & (a0 ^ b0))
	result |= s << 0
​
	# Add bit 1
	s = a1 ^ b1 ^ c
	c = (a1 & b1) | (c & (a1 ^ b1))
	result |= s << 1
​
	# Add bit 2
	s = a2 ^ b2 ^ c
	c = (a2 & b2) | (c & (a2 ^ b2))
	result |= s << 2
​
	# Add bit 3
	s = a3 ^ b3 ^ c
	c = (a3 & b3) | (c & (a3 ^ b3))
	result |= s << 3
​
	# Add bit 4
	s = a4 ^ b4 ^ c
	c = (a4 & b4) | (c & (a4 ^ b4))
	result |= s << 4
​
	# Add bit 5
	s = a5 ^ b5 ^ c
	c = (a5 & b5) | (c & (a5 ^ b5))
	result |= s << 5
​
	# Add bit 6
	s = a6 ^ b6 ^ c
	c = (a6 & b6) | (c & (a6 ^ b6))
	result |= s << 6
​
	# Add bit 7
	s = a7 ^ b7 ^ c
	c = (a7 & b7) | (c & (a7 ^ b7))
	result |= s << 7
​
	return (result, c)
​
if __name__ == "__main__":
	# Test adding all combinations of numbers from 0-255:
	for a in range(0, 256):
		for b in range(0, 256):
			r, c = ripple_carry_add(a, b)
			assert(r + c * 256 == a + b)