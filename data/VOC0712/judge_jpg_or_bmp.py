#! /usr/bin/env python

import os

dirname = r"VOCdevkit/"
savename = r"trainval.txt"
txt_dir = "trainval_backup.txt"

alist = []
with open(txt_dir) as f:
    for iline in f:
        img_name = iline.strip().split(" ")[0]
	if os.path.exists(dirname+img_name):
	    alist.append(iline.strip())
	else:
	    if len(iline.strip().split(" ")) == 2:
		astring = img_name[:-4]+".bmp"+ " "+iline.strip().split(" ")[1]
		alist.append(astring)
	    else:
		print "wrong:",len(iline.strip().split(" "))
print alist
with open(savename,"a") as ff:
    for ii in alist:
        ff.write(ii+"\n")
print "do all!"
