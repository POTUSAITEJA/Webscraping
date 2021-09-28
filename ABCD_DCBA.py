y = []
for i in range(1,10):
    for j in range(10):
        for k in range(10):
            for l in range(1,10):
                if (i!=j and i!=k and i!=l and j!=k and j!=l and k!=l):
                    #print(i,",",j,",",k,",",l)
                    x = str(i)+str(j)+str(k)+str(l)
                    if 4*int(x) == int(str(l)+str(k)+str(j)+str(i)):
                        print(i,",",j,",",k,",",l)
                #
                # if 4*(i*1000+j*100+k*10+l*1) == (l*1000+k*100+j*10+i*1):
                        
                        #y.append(x)
                
#print(4*x)
#print(y)
#print(i,",",j,",",k,",",l)          
