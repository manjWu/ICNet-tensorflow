import os 
import shutil

# 获取文件名，返回txt中路径的名称
def img_file_name(file_dir):
	L=""
	for root,dirs,files in os.walk(file_dir):
		for file in files:
			if file == "img.png":
				L = os.path.join(root,file)
				L2 = imgdir1 + "/" + name[0:-5] + ".png"
				shutil.copy(L,L2)
				print(L)
				# file_name = file[0:-4] #去掉.txt
				# L.append(file_name)
				# L.append(' '+'this is another file\'s name')
	# return L

def label_file_name(file_dir):
	L=""
	L2=""
	for root,dirs,files in os.walk(file_dir):
		for file in files:
			if file == "label.png":
				L = os.path.join(root, file)
				L2 = imgdir2 + "/" + name[0:-5] + ".png"
				shutil.copy(L,L2)
	# return L2

imgdir = "/Users/wumanjia/PycharmProjects/ICNet-tensorflow/clear/Image"
imgdir1 = "/Users/wumanjia/PycharmProjects/ICNet-tensorflow/clear/Image11"
imgdir2 = "/Users/wumanjia/PycharmProjects/ICNet-tensorflow/clear/Image22"

file_dir = "/Users/wumanjia/PycharmProjects/ICNet-tensorflow/clear"
list_txt_file = "/Users/wumanjia/PycharmProjects/ICNet-tensorflow/clear/train2.txt"

docs = os.listdir(imgdir) #列出文件夹下所有文件

for name in docs:
	if name.endswith("_json"): # 找到每个_json文件夹
		print(name)
		label_folder = imgdir+'/'+name
		img_file_name(file_dir)
		label_file_name(file_dir)
		# content = img_file_name(label_folder)+' '+label_file_name(label_folder)+name
		content = "/root/wmj-docker/ICNet-tensorflow/clear/Image1/"+name[0:-5]+ ".png"+" "+"/root/wmj-docker/ICNet-tensorflow/clear/Image2/"+name[0:-5]+ ".png"
		print(content)
		with open(list_txt_file,'a') as f:
			f.write(content+'\n')
		f.close()
