dict = {'a':'Aravinth','b':'Aarthi','c':'Gowri','d':'Someone else'}

#print(dict)
#print(dict['b'])

# 1. Adding new elements to Dictionary
dict['e'] = 'Public'
print('# 1. Adding new elements to Dictionary \n dict[''e''] = ''Public'' will result in :',dict,'\n')

# 2. Modify Values
dict['a']='Arvi'
print('# 2. Modify Values by Key \n dict[''a'']=''Arvi'' ',dict,'\n')

# 3. Get Method to get value using key
print('# 3. Get value to access the element \n dict.get(''c'') \n',dict.get('c'),'\n')

# 4. Delete from dictionary

del dict['d']
print('# 4. Deleting elements from Dictioary : \n del dict[''d'']', dict)

# 5 Copy Dictionary
dict2=dict.copy()
print('# 5. Copy Dictionar \n dict2=dict.copy() \n',dict2,'\n')