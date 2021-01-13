from math import sqrt

nX=nY=8

def writeDistances():
    
        for j in range(1,nY+1):
            for i in range(1,nX+1):
                for j2 in range(1,nY+1):
                    for i2 in range(1,nY+1):
                        if((i2==i)&(j2==j)):
                            continue
                        
                        distance=sqrt((i2-1)**2+(j2-j)**2)
                        print (i,j,"to",i2,j2,"distance",distance)
                        
if __name__ == '__main__':
    
    writeDistances()