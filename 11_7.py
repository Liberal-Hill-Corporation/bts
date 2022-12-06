import os
import cv2
import numpy as np
import pandas as pd
folders=os.listdir('data/')

images=[]
labels= []
for folder in folders:
    files=os.listdir('data/'+folder)
    for file in files:
        img=cv2.imread('data/'+folder+'/'+file,0)
        img=cv2.resize(img,(25,25))
        
        images.append(img)
        labels.append(int(folder))

images = np.array(images)
features = images.reshape(len(images),-1)
