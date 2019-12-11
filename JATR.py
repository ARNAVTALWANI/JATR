#How the AI is supposed to work, found in comment code below:

#from SimpleCV import Camera
#cam = Camera()
#while True:
    #img = cam.getImage()

    #Machine learning code...

    #%reload_ext autoreload
    #%autoreload 2
    #%matplotlib inline

    #%config InlineBackend.figure_format = 'retina'
    #from fastai.vision import *
    #from fastai.metrics import error_rate
    #from pathlib import Path
    #from glob2 import glob
    #from sklearn.metrics import confusion_matrix

    #import pandas as pd
    #import numpy as np
    #import os
    #import zipfile as zf
    #import shutil
    #import re
    #import seaborn as sns
    #files = zf.ZipFile("dataset-resized.zip",'r')
    #files.extractall()
    #files.close()
    #os.listdir(os.path.join(os.getcwd(),"dataset-resized"))

    #def split_indices(folder,seed1,seed2):    
        #n = len(os.listdir(folder))
        #full_set = list(range(1,n+1))

        #random.seed(seed1)
        #train = random.sample(list(range(1,n+1)),int(.5*n))

        #remain = list(set(full_set)-set(train))

        #random.seed(seed2)
        #valid = random.sample(remain,int(.5*len(remain)))
        #test = list(set(remain)-set(valid))
    
        #return(train,valid,test)

    #def get_names(waste_type,indices):
        #file_names = [waste_type+str(i)+".jpg" for i in indices]
        #return(file_names)    

    #def move_files(source_files,destination_folder):
        #for file in source_files:
            #shutil.move(file,destination_folder)
    #subsets = ['train','valid']
    #waste_types = ['cardboard','glass','metal','paper','plastic','trash']

    #for subset in subsets:
        #for waste_type in waste_types:
            #folder = os.path.join('data',subset,waste_type)
            #if not os.path.exists(folder):
                #os.makedirs(folder)
            
    #if not os.path.exists(os.path.join('data','test')):
        #os.makedirs(os.path.join('data','test'))
            
    #for waste_type in waste_types:
        #source_folder = os.path.join('dataset-resized',waste_type)
        #train_ind, valid_ind, test_ind = split_indices(source_folder,1,1)
    
        #train_names = get_names(waste_type,train_ind)
        #train_source_files = [os.path.join(source_folder,name) for name in train_names]
        #train_dest = "data/train/"+waste_type
        #move_files(train_source_files,train_dest)
    
        #valid_names = get_names(waste_type,valid_ind)
        #valid_source_files = [os.path.join(source_folder,name) for name in valid_names]
        #valid_dest = "data/valid/"+waste_type
        #move_files(valid_source_files,valid_dest)
    
        #test_names = get_names(waste_type,test_ind)
        #test_source_files = [os.path.join(source_folder,name) for name in test_names]
        #move_files(test_source_files,"data/test")
    #path = Path(os.getcwd())/"data"
    #path
    #tfms = get_transforms(do_flip=True,flip_vert=True)
    #data = ImageDataBunch.from_folder(path,test="test",ds_tfms=tfms,bs=16)
    #print(data.classes)
    #data.show_batch(rows=4,figsize=(10,8))
    #learn = create_cnn(data,models.resnet34,metrics=error_rate)
    #learn.model

    #Based on result...

    #if m == garbage
        #img.drawText("Garbage")
    #elif m == recycle
        #img.drawText("Recycle")
    #Show the image using...
    #img.show()

#Actual code for demo
print("Welcome to JATR: Garbage Sort System 0.1")
print("/nWe sort it all, so you don't have to!")
print("/nMade by Arnav Talwani, Sam Assareymuriyil, Vinay Reddy, and Jarukson Jeevakumar")
print("/nSend us an email at arnavtalwani@outlook.com if you have any questions or feedback!")
material = input(/n"Please type the name of the material you wish to enter: ")

if material == "cardboard":
    print("This material belongs in the recycling bin. Save our planet!")
elif material == "banana peel":
    print("This material belongs in the garbage can. Save our planet!")
else
    print("Unfortunately this material has not been added to our database. Send us an email if you want it added!")
