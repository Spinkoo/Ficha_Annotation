import json
import numpy as np
import matplotlib.pyplot as plt
data = json.load(open('6_classes2.json'))


dic = {}
catgs = data['categories']



for d in data['annotations'] :
	clas = d['category_id']
	categ = catgs[clas - 1]['supercategory']
	if categ in dic :
		dic[categ] +=1
	else:
		dic[categ] = 1
print(dic)

keys = dic.keys()
values = dic.values()

plt.bar(keys, values)
plt.xticks(rotation='vertical')

plt.show()