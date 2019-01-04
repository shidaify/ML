#10.1
#T = 8 , O = (红、白、红、红、白、红、白、白)
import numpy as np
A=[[0.5,0.1,0.4],
   [0.3,0.5,0.2],
   [0.2,0.2,0.6]]
B=[[0.5,0.5],
   [0.4,0.6],
   [0.7,0.3]]
Pi=[0.2,0.3,0.5]


red = 0
white = 1
a=np.array(A)	
pi=np.array(Pi)
b=np.array(B)

def get_beta( color ):
	global beta
	be=[]
	for i in range(3):
		be.append(np.dot((a[i]*beta[-1]),b[:,color]))
	beta.append(be)
###后向
color = [white,white,red,white,red,red,white,red]
beta = [[1,1,1]]
for i in color[:len(color)-1]:
	get_beta(i)
beta = np.array(beta)
print(beta)

###前向
color2 = [white,red,red,white,red,white,white]
afa = []

afa.append(b[:,red]*pi)

def get_afa( color ):
	global afa
	afa.append((np.dot(afa[-1],a))*b[:,color])

for i in color2:
	get_afa(i)
afa=np.array(afa)
print(afa)

p=afa[3,2]*beta[4,2]/(sum(afa[3]*beta[4]))
print(p)
