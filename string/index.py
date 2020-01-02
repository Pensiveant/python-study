findStr='abcdefg-abcdefg-abcdefg-abcdefg-abcdefg-abcdefg'
print(findStr.find('a')) # 0
print(findStr.find('a',5,9)) # 8
print(findStr.find('z')) # -1

rfindStr='abcdefg-abcdefg-abcdefg-abcdefg-abcdefg-abcdefg'
print(rfindStr.rfind('a')) # 40
print(rfindStr.rfind('a',5,9)) # 8
print(rfindStr.rfind('z')) # -1

indexStr='abcdefg-abcdefg-abcdefg-abcdefg-abcdefg-abcdefg'
print(indexStr.index('a')) # 0
print(indexStr.index('a',5,9)) # 8
print(indexStr.index('z')) # ValueError: substring not found

rindexStr='abcdefg-abcdefg-abcdefg-abcdefg-abcdefg-abcdefg'
print(rindexStr.rindex('a')) # 40
print(rindexStr.rindex('a',5,9)) # 8
print(rindexStr.rindex('z')) # ValueError: substring not found