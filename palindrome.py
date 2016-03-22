'''
Three algorithms for determining whether a given string is a 
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

