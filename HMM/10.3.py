#10.3
#T = 4, O = (红白红白)

import numpy as np

A=[[0.5,0.2,0.3],
   [0.3,0.5,0.2],
   [0.2,0.3,0.5]]

B=[[0.5,0.5],
   [0.4,0.6],
   [0.7,0.3]]

Pi=[0.2,0.4,0.4]

a=np.array(A)	
pi=np.array(Pi)
b=np.array(B)

red=np.array(b[:,0])
white=np.array(b[:,1])
pos=[]

def init(color):
	return color*pi
def process(sigema,color):
	global a
	a=a.T
	c=[]
	for i in a:
		c.append(sigema*i)
	d=[]
	pos=[]
	for i in c:
		temp=i.tolist()

		pos.append(temp.index(i.max()))
		d.append(i.max())
	d=np.array(d)

	return d*color,pos


s0=init(red)
print(s0,)
s1,pos1=process(s0,white)
print(s1,"\n",pos1)
s2,pos2=process(s1,red)
print(s2,"\n",pos2)
s3,pos3=process(s2,white)
print(s3,"\n",pos3)
