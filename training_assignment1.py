# fclass = "firstpythonclass"
# print(len(fclass))

###################################################################

# string = "google.com"
# freq_string = {}
# for i in string:
#     key = freq_string.keys()
#     if i in key:
#         freq_string[i] += 1
#     else:
#         freq_string[i] = 1

# print(freq_string)

##################################################################

# string = "w3resource"
# if len(string) < 2:
#     print("Empty string")
# else:
#     print(string[:2] + string[-2:])

##################################################################

# string = "restart"
# z = string[0]
# for i in string:
#     string = string.replace(z, "$")

# string = z + string[1:]
    
# print(string)

##################################################################

# def swap(s1, s2):
#     temp = s1
#     s1 = s2
#     s2 = temp
#     temp = s1
#     s1 = s2[0:2] + s1[2]
#     s2 = temp[0:2] + s2[2]

#     print(s1 + " " + s2)


# sample1 = "abc"
# sample2 = "xyz"
# swap(sample1, sample2)

##################################################################

# string = input("enter a string: ")
# if len(string)<3:
#     print("string size should be greater than 3 characters.")
# else:
#     if string.endswith('ing'):
#         string = string + "ly"
#     else:
#         string = string + "ing"

# print(string)

###################################################################

# string = 'the lyrics is not that poor'
# s1 = string.find("not")
# s2 = string.find("poor")

# if s2 > s1:
#     string = string.replace(string[s1:(s2+4)], "good")

# print(string)

###################################################################

# mylist = []
# n = int(input("enter no. of words: "))
# for i in range(n):
#     word = input(f"enter word {i}: ")
#     mylist.append(word)

# lword = 0
# for words in mylist:
#     if len(words) > lword:
#         lword = len(words)
#         long_word = words

# print("longest word: " + long_word)
# print("length of longest word: " + str(lword))

####################################################################

# string = input("Enter a string: ")

# n = len(string)
# string = string[0:n-1]
# print(string)

####################################################################

# string = input("Enter a string: ")

# string = string[-1] + string[1:-1] + string[0]
# print(string)

####################################################################

# st = input("Enter a string: ")
# st = st[:-1:2]
# print(st)

####################################################################

# st = input("Enter a sentence: ")
# word_count = {}
# words = st.split()

# for i in words:
#     if i in word_count:
#         word_count[i] += 1
#     else:
#         word_count[i] = 1

# print(word_count)

####################################################################

# st = input("Enter a text: ")
# print(st.upper())
# print(st.lower())

####################################################################
 
# st = "red, white, black, red, green, black"

# words = st.split(", ")
# words.sort()
# unique = []
# for word in words:
#     if word not in unique:
#         unique.append(word)
#     else:
#         continue

# for word in unique:
#     print(word, end=' ')

####################################################################

# def add_tags(tag, st):
#     return "<%s>%s</%s>" % (tag, st, tag)

# st = input("Enter a string: ")
# tag = input("Enter the tag you want to add: ")
# print(add_tags(tag, st))

####################################################################

# st = input("Enter a string: ")
# st2 = input("Enter a second string in which you want to insert the first string: ")

# st3 = st2[:2] + st + st2[2:]
# print(st3)

####################################################################

# st = input("Enter a string: ")
# a = st[-2:]
# print(a+a+a+a)

####################################################################

# st = input("Enter a string: ")
# if len(st) < 3:
#     print(st)
# else:
#     st = st[:3]
#     print(st)

####################################################################

# st = "https://www.w3resource.com/python-exercises"

# sp_character = input("Enter a character: ")
# for i in st:
#     if i == sp_character:
#         break
#     else:
#         print(i, end='')

####################################################################

# st = input("Enter a string: ")
# n = len(st)

# if n % 4 == 0:
#     st = st[::-1]
#     print(st)
# else:
#     print("The string is not a multiple of 4")

####################################################################

# st = input("Enter a string: ")
# for i in st[:4]:
#     if i == i.upper():
#         st = st.upper()
# print(st)

####################################################################

# print("this is a python program ", end='')
# print("to remove a new line in python")

####################################################################

# st = input("Enter a string: ")
# sp_character = input("Enter a character which you want to check: ")

# if st[0] == sp_character:
#     print("The string starts with the specified character")
# else:
#     print("The string doesn't start with the specified character")

####################################################################