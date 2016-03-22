'''
Multiple algorithms for determining whether a given string is a 
palindrome.
Each function receives a string and returns a boolean.
(str -> bool)
'''
def reverse(s):
	'''
	This is a helper function that we may use in our following 
	three functions.
	reverse: str -> str
	>> receives a string and returns a reversed string
	'''
	reversed_str = ''
	for character in s:
		reversed_str = character + reversed_str
	return reversed_str


def is_palindrome1(s):
	'''
	is_palindrome1 simply compares the given str with its reversed form
	to determine whether it is a palindrome
	'''
	return s == reverse(s)

def is_palindrome2(s):
	'''
	is_palindrome2 cuts the string in half and compares the first half
	with the reversed second half to see if they are the same.
	If the length of the string is odd then we exclude the middle index and 
	only compare the remaining two halves.
	'''
	strlen = len(s)
	'''
	We take advantage of the fact that integers get floored when they are divided.
	Case 1: 'kayak' has a len of 5. We compare string[:2] to reverse(string[5 - 2:])
			So we end up comparing 'ka' with 'ka' which is True
	Case 2: 'toot' has an even length of 4. We compare string[:2] to reverse(string[4-2:])
			So we end up comparing 'to' with 'to' which is True
	Case 3: 'hello': Compares 'he' with 'ol' which yields False		
	'''
	return s[:strlen / 2] == reverse(s[strlen - strlen / 2:])

def is_palindrome3(s):
	'''
	is_palindrome3 is basically like is_palindrome2 but it uses cases of
	even and odd instead of one generalized formula.
	'''
	# midpoint index of string
	midpoint = len(s) / 2
	# index the second half must start on
	index = midpoint

	# if string has an odd length skip the middle index of the string
	if len(s) % 2 != 0:
		index = index + 1
	return s[:midpoint] == reverse(s[index:])
	
def is_palindrome4(s):
	'''
	is_palindrome4 iteratively compares the first and last character of the 
	string. 
	For example, given 'noon', we compare 'n' to 'n' then 'o' to 'o'
		- Given 'rotator':
						Compare 'r' to 'r' -> 'o' to 'o' -> 't' to 't' then stop
						when there is only one character left
	'''
	# i : first index 
	# j : last index
	i = 0
	j = len(s) - 1

	# We keep the process going as long as the first index is less than the
	# last index and their values are equal
		# if j is ever greater than or equal to i, we know that the two indices
		# have met, so we stop the loop
		# if i does not equal j, we stop the loop
	while i < j and s[i] == s[j]:
		# move both i and j closer to the middle of the string
		i = i + 1
		j = j - 1
	# This will return True when the string is a palindrome because if the string
	# a palindrome it will continue until i and j are equal (since it will not
	# satisfy the i < j condition anymore)
	return i >= j


