'''
python 学习手册 第8章示例
'''

# table={'1975':'Holy Grail','1979':'Life of Brain','1983':'The Meaning of Life'}

# for year in table:
#     print(year+'\t'+table[year])

table={'Holy Grail':'1975','Life of Brain':'1979','The Meaning of Life':'1983'}

items=list(table.items())
print(items)
test=[title for (title,year) in table.items() if year=='1975']
print(test)