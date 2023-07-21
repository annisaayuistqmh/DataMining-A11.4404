x1 = [1,1,1]
x2 = [-1,-1,-1]

bias = [1,1]
target = [1,-1]

w1_delta=[]
w2_delta=[]
b_delta=[]

w1_baru=[]
w2_baru=[]
b_baru=[]

net=[]
f_net=[]

#Inisialisasi
w1_awal=0
w2_awal=0
b_awal=0

net1 = 0
net2 = 0
temp = 0
temp1=int(w1_awal)
temp2=int(w2_awal)
temp5=int(b_awal)

#while(target!=f_net):
#for j in range(0,2):
for i in range (0,3):
    w1_delta.append(x1[i]*target[0])
    w1_baru.append(temp1+w1_delta[i])
    temp1=0
    
    w2_delta.append(x2[i]*target[1])
    temp2=w1_baru[i]
    w2_baru.append(temp2+w2_delta[i])
       
  
for i in range (0,2):
    b_delta.append(bias[i]*target[i])
    b_baru.append(temp5+b_delta[i])
    temp5=b_baru[i]

  
for i in range (0,3):
    net1 = x1[i]*w1_awal+net1
    net2 = x2[i]*w1_baru[i]+net2

net.append(net1+temp)
net.append(net2+b_baru[0])


for i in range (0,2):
    if(net[i]>0.5):
        f_net.append(1)
    elif(net[i]<-0.5):
        f_net.append(-1)
    else:
        f_net.append(0)
        

print('epoch ke-1')
print('x awal')
print(x1)
print(x2)
print('\n net')
print(net)
print('\n target')
print(target)
print('\n f(net)')
print(f_net)

if(target == f_net):
    print('\n Jaringan mengenali pola')
else:
     print('\n Jaringan tidak mengenali pola')

w_temp=0
b_temp=0

def fnet(n):
    if(n>0.5):
        h=1
    elif(n<-0.5):
        h=-1
    else:
        h=0
    return h

while(target!=f_net):
    e = 1
    print('epoch ke-',e+1)
    net1=0
    net2=0
    
    w_temp=w2_baru
    b_temp=b_baru
    
    net[0]=x1[0]*w_temp[0]+x1[1]*w_temp[1]+x1[2]*w_temp[2]+b_temp[1]
    f_net[0]=fnet(net[0])
    

    for i in range(0,2):
        if(target[i]==f_net[i] and i==0):
            for j in range(0,3):
                w1_delta[j]=0
        elif(target[i]==f_net[i] and i==1):
            for j in range(0,3):
                w2_delta[j]=0
                
    for i in range(0,3):
        w1_baru[i]=w1_delta[i]+w_temp[i]
        w2_baru[i]=w2_delta[i]+w1_baru[i]
                
    net[1]=x2[0]*w_temp[0]+x2[1]*w_temp[1]+x2[2]*w_temp[2]+b_temp[1]
        
    print('x awal')
    print(x1)
    print(x2)
    print('\n net')
    print(net)
    print('\n target')
    print(target)
    print('\n f(net)')
    print(f_net)

    if(target == f_net):
        print('\n Jaringan mengenali pola')
    else:
        print('\n Jaringan tidak mengenali pola')
    