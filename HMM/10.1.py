#10.1
#T = 4,O = (红、白、红、白)

import numpy as np

red = 0
white = 1

A=[[0.5,0.2,0.3],
   [0.3,0.5,0.2],
   [0.2,0.3,0.5]]

B=[[0.5,0.5],
   [0.4,0.6],
   [0.7,0.3]]

Pi=[0.2,0.4,0.4]

beta=[[1,1,1]]

a=np.array(A)	
pi=np.array(Pi)
b=np.array(B)

def get_beta( color ):
	global beta
	be=[]
	for i in range(3):
		be.append(np.dot((a[i]*beta[-1]),b[:,color]))
	beta.append(be)

color=[1,0,1]
for i in color:
	get_beta(i)

beta = np.array(beta)
print(beta)

p = np.dot((beta[-1]*pi),b[:,red])

print(p)