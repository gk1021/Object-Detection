import sqlite3
import json
conn = sqlite3.connect('TEST2.db')
with open('imagenet_class_index.json') as f:
    data=json.load(f)
classes=[]
i=0
while i<len(data):
    classes.append(data[str(i)])
    conn.execute('''CREATE TABLE ''' + classes[i][1] + '''
         (VIDEO     TEXT , FRAME        TEXT);''')
    print("table created:",classes[i][1])
    print(i)

    i+=1


""" table=["one","two"]
conn.execute('''DROP TABLE two''')
conn.execute('''CREATE TABLE ''' + table[1] + '''
         (LABLE           TEXT   ,
         L1     TEXT,
         L2     TEXT,
         L3     TEXT);''')
conn.execute("INSERT INTO two (LABLE,L1,L2,L3) VALUES ('hey','hi','pikachu','raichu')")
cur=conn.execute("select * from two")
 for row in cur:
   print("frame = ", row[0])
   print ("l1 = ", row[1])
   print ("l2 = ", row[2])
   print ("l3 = ", row[3]) """

conn.commit()
conn.close()
