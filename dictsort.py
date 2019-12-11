dict={'abc':{'Age':12,'marks':100},
       'abe':{'Age':22,'marks':95},
       'ybz':{'Age':15,'marks':90}}
print(sorted(dict.items(), key = lambda x: x[1]['Age']))
