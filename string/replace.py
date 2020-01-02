# 
replaceStr='My name is pensiveant,My name is pensiveant'
print(replaceStr.replace('My','my'))
print(replaceStr.replace('My','my',2))


expandtabsStr='My\tname\tis\tpensiveant\t00'
print(expandtabsStr.expandtabs()) # My      name    is      pensiveant
print(expandtabsStr.expandtabs(2)) # My  name  is  pensiveant
print(expandtabsStr.expandtabs(4)) # My  name    is  pensiveant