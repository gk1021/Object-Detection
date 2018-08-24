#import sys
#sys.path.append('/usr/local/lib/python2.7/site-packages/cv2')
#sys.path.append('/usr/local/lib/python2.7/site-packages/')
#import cv2
from keras.applications.xception import Xception
from keras.applications.inception_v3 import InceptionV3
from keras.applications.inception_v3 import preprocess_input
from keras.applications.inception_v3 import decode_predictions
from keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt
import os
import sqlite3
import json
from pprint import pprint
""" with open('imagenet_class_index.json') as f:
    data=json.load(f) """
conn = sqlite3.connect('TEST2.db')
file = open("data.txt", 'w').close()

import time
#cap = cv2.VideoCapture('1.mp4')
#video_length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) - 1
#print "Number of frames: ", video_length
count = 0
print ("Loading..\n")
path = "/home/kunal/doc/p3/data2/"
videos=os.listdir(path)
for n in videos:
    p=path
    path=path+"/"+n+"/"
    images = os.listdir(path)
    print(images)
    c=1
    """ classes_n=[]
    z=0
    while z<len(data):
        classes_n.append(data[str(z)])
        
        z+=1
    """
    for i in images:

        #img = cv2.imread(path + image)
        #print img.shape
        im = path+i
        print(i)
        model = InceptionV3(weights='imagenet', include_top=True, classes=1000)
        img = image.load_img(im, target_size=(299, 299))
        print(img.size)
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        features = model.predict(x)
        predict = decode_predictions(features, top=3)

        print(decode_predictions(features, top=3))
        file = open("data.txt", 'a')

        file.write("{} {}\n".format( i,predict))
        
        l1=predict[0][0][1]
        l2=predict[0][1][1]
        l3=predict[0][2][1]
        index=0
        if "-" in l1:
            l1=l1.replace("-","_",3)
        if "-" in l2:
            l2=l2.replace("-","_",3)
        if "-" in l3:
            l3=l3.replace("-","_",3)
        if "'" in l1:
            l1=l1.replace("'","",3)
        if "'" in l2:
            l2=l2.replace("'","",3)
        if "'" in l3:
            l3=l3.replace("'","",3)
        
        
        #conn.execute("INSERT INTO TEST2 (FRAME,L1,L2,L3) VALUES (?,?,?,?)",(i,l1,l2,l3))
        #cv2.imwrite("frame" + str(count) + ".jpg" , frame)
        conn.execute('''INSERT INTO '''+l1+''' VALUES (?,?)''',(n,i))
        conn.execute('''INSERT INTO '''+l2+''' VALUES (?,?)''',(n,i))
        conn.execute('''INSERT INTO '''+l3+''' VALUES (?,?)''',(n,i))
        
        count = count + 1
        c=c+1
    path=p
query=input("Enter your query here : ")

print(query)
q=query.split(" ")
n=len(q)
list1=[]
for ob in q:
    list1.append(conn.execute("select distinct * from "+ob+""))
print(list1)


""" cur=conn.execute("select distinct * from "+q[0]+"")
cur1=conn.execute("select distinct * from "+q[1]+"")
for row in cur:
   for row1 in cur1:
       if(row==row1):
           print("videos",row[0])
           print("frame",row[1])
 """
conn.commit()
conn.close()
file.close()
