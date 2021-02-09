Python 3.8.4 (tags/v3.8.4:dfa645a, Jul 13 2020, 16:30:28) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> mylist = []
>>> mylist.append(1)
>>> mylist.append(2)
>>> mylist.append(3)
>>> for x in mylist:
	print(x)

	
1
2
3
>>> # use of index
>>> print(mylist[2])
3
>>> # Exercise - create a list of numbers and strings using the append list method and use index
>>> numbers = []
>>> strings = []
>>> names = ["John", "Eric", "Jessica"]
>>> # get the second name in the names list
>>> second_name = names[1]
>>> print(second_name)
Eric
>>> numbers.append(1)
>>> numbers.append(2)
>>> numbers.append(3)
>>> numbers.append(4)
>>> print(numbers)
[1, 2, 3, 4]
>>> strings.append('hello')
>>> strings.append('world')
>>> print(strings)
['hello', 'world']
>>> 