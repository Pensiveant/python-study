# str检查相关方法示例
# @autor:pensiveant
#

emptyStr='A'
rawStr=r"c:\new\test.spm"
escapeStr='s\tp\nam'
byteStr=b'sp\x01am'
unicodeStr=u'eggs\u0020spam'


# isdecimal()
# print(emptyStr.isdecimal()) # False
# print('Ⅳ'.isdecimal()) # False
# print('12334'.isdecimal()) # True
# print(u'0000'.isdecimal()) # True

# isdigit()
print('isdigit---')
print(emptyStr.isdigit()) # False
print('FOUR'.isdigit()) # False
print('四'.isdigit()) # False
print('Ⅳ'.isdigit()) # False
print('13289702049'.isdigit()) # True
print('①'.isdigit()) # True
print(u'0000'.isdigit()) # True


# # isnumeric()
# print('isnumeric---')
# print(emptyStr.isnumeric()) # False
# print('THREE'.isnumeric()) # False
# print('3+4j'.isnumeric()) # False
# print('3.14e-10'.isnumeric()) # False
# print('0x9ff'.isnumeric()) # False
# print('13289702049'.isnumeric()) # True
# print('u+2155'.isnumeric()) # 
# print('四'.isnumeric()) # True
# print('Ⅳ'.isnumeric()) # True




# # isascii()
# name='pensiveant'
# print('isascii----')
# print(name.isascii())
# print(emptyStr.isascii())
# print(rawStr.isascii())
# print(escapeStr.isascii())
# print(byteStr.isascii())
# print(unicodeStr.isascii())

# # isidentifier()
# identifier='pensive_001'
# print(identifier.isidentifier())
# print(emptyStr.isidentifier())


# isalpha()

# islower()
print('islower----')
print(emptyStr.islower()) # False
print('123'.islower()) # False
print('abd'.islower()) # True

# isupper()

# istitle()



# isspace()

# isalnum()

# isprintable()

# startswith(prefix[, start[, end]])

#  endswith(suffix[, start[, end]])