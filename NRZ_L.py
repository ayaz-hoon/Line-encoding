# AUTHOR: AIYAZ AHMED N.HANSBHANVI
#( 201104003, BE-ETC Engineering, SEM-7,2023-24,GEC )
import numpy as np
import matplotlib.pyplot as plt
bit_seq = input("enter the bit sequence: ")
font1 ={"color":"black", "size":18}
font2 ={"color":"black", "size":20}
fs = 1000
bits=[]
for i in range(0,len(bit_seq)) :
    bit = int(bit_seq[i])
    bits.append(bit)

num_bits = len(bits)  
samples = int(fs/num_bits)
out = []
for i in bits:
    if (i == 1):
        out.append(-1)
    else:
        out.append(1)
        
input1 =[]
for i in bits:
    input1.extend([i]*samples)

output =[]
for i in out:
    output.extend([i]*samples)

t = np.linspace(0, num_bits,len(output))  

plt.subplot(3,1,1)
plt.plot(t,input1)
plt.grid()
plt.xlabel("Time in seconds",fontdict=font1)
plt.ylabel("Amplitude in volts",fontdict=font1)
plt.title("input bits",fontdict=font2)

plt.subplot(3,1,3)
plt.plot(t,output)
plt.grid()
plt.xlabel("Time in seconds",fontdict=font1)
plt.ylabel("Amplitude in volts",fontdict=font1)
plt.title("NRZ-L Encoding",fontdict=font2)
plt.show()
