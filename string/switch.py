# 全部转为大写
upperStr='abcdefg-HIJKLMN-opq-RST-uvw-XYZ'
print(upperStr.upper()) # ABCDEFG-HIJKLMN-OPQ-RST-UVW-XYZ
print(upperStr) # abcdefg-HIJKLMN-opq-RST-uvw-XYZ

# 全部转为小写
lowerStr='abcdefg-HIJKLMN-opq-RST-uvw-XYZ'
print(lowerStr.lower()) # abcdefg-hijklmn-opq-rst-uvw-xyz
print(lowerStr) # abcdefg-HIJKLMN-opq-RST-uvw-XYZ

# 首字母大写，其他字母小写
capitalizeStr='abcdefg-HIJKLMN-opq-RST-uvw-XYZ'
print(capitalizeStr.capitalize()) # Abcdefg-hijklmn-opq-rst-uvw-xyz
print(capitalizeStr) # abcdefg-HIJKLMN-opq-RST-uvw-XYZ

# 首字母大写，其他字母小写
swapcaseStr='abcdefg-HIJKLMN-opq-RST-uvw-XYZ'
print(swapcaseStr.swapcase()) # ABCDEFG-hijklmn-OPQ-rst-UVW-xyz
print(swapcaseStr) # abcdefg-HIJKLMN-opq-RST-uvw-XYZ

# 
titleStr='my name is pensiveant'
print(titleStr.title()) # My Name Is Pensiveant
print(titleStr) # my name is pensiveant