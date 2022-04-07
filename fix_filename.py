import json
import numpy as np
import matplotlib.pyplot as plt



def fix_name(data, output_path = 'fixed_data.json'):

	dic = {}
	catgs = data['categories']

	l = []
	for d in data['images'] :
		fname = d['file_name']
		fname = '/content/drive/MyDrive/j/data/'+fname.split('/')[-1]
		print(fname)
		d['file_name'] = fname


	with open(output_path, 'w') as f:
	    json.dump(data, f)


def remove_label(data, label = 'Dumpster'):

	annos = []
	catgs = data['categories']

	for d in data['annotations'] :
		clas = d['category_id']
		categ = catgs[clas - 1]['supercategory']
		if categ != label :
			annos.append(d)
	data['annotations'] = annos
	categs = []
	i = 1
	old_new = []
	for c in data['categories'] :
		if c['supercategory'] != label:
			old_new.append((c['id'], i))
			categs.append({'supercategory' : c['supercategory'], 'id' : i, 'name' : c['name']})
			i+=1
	data['categories'] = categs
	for d in data['annotations'] :
		clas = d['category_id']
		for o, n in old_new :
			if clas == o :
				d['category_id'] = n
				break
	return data

def save_json(data, output_path):
	with open(output_path, 'w') as f:
	    json.dump(data, f)

def interchange_labels(data, labels = None, num_classes = 6):
	assert len(labels) > 1 is not None, 'Tuple of label needed'

	x, y = labels
	categs = []
	i = 1
	old_new = []
	n = get_category_idx(data, y)
	o = get_category_idx(data, x)

	for c in data['categories'] :
		if c['id'] == o:
			old_new.append((c['id'], n))
			old_new.append((n, c['id']))
			break

	temp = data['categories'].copy()
	for  i, c in enumerate(temp)  :
		id_c = c['id']
		for o, n in old_new:
			if id_c == o:
				data['categories'][i]['id'] = n
				break
			if id_c == n:
				data['categories'][i]['id'] = o
				break
	temps = [1] * num_classes
	for idx, item in enumerate(data['categories']):
		for j in data['categories']:
			if j['id'] == idx+1:

				temps[idx] = j
				break
	data['categories'] = temps
	print(temps)
	temp = data['annotations'].copy()
	for i, d in enumerate(temp) :
		clas = d['category_id']
		for o, n in old_new :
			if clas == o :
				data['annotations'][i]['category_id'] = n
				break
			if clas == n :
				data['annotations'][i]['category_id'] = o
				break
	return data


def get_category_idx(data, label):
	for i, c in enumerate(data['categories']) :
		if c['supercategory'] == label:
			return c['id']
def fusion_classes(data, to_save_label, to_remove_label):
	for d in data['annotations'] :
		idxto_save = get_category_idx(data, to_save_label)
		idxto_remove = get_category_idx(data, to_remove_label)
		clas = d['category_id']
		
		if clas == idxto_remove :	
					
			d['category_id'] = idxto_save
			print(idxto_save)

	data = remove_label(data, to_remove_label)
	return data
	

if __name__ == '__main__':


	rem = ['Recycle waste']

	path = '6_classes2.json'
	data = json.load(open(path))

	#data = interchange_labels(data, ( 'Bulky', 'Garbage Bag' ))
	'''for r in rem :
		data = fusion_classes(data,'Recycle Waste', r)
	'''
	#save_json(data, '6_classes2.json')


	fix_name(data, path)