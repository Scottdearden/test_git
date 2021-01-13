def setcolours(j):
    
    if((j%2)==1):
        oddsquare="black"
        evensquare="white"
    else:
        oddsquare="white"
        evensquare="black"
    return(oddsquare,evensquare)
    
def writechesscolour():
    
    nX=nY=8
    for j in range(1,nY+1):
        
        oddsquare,evensquare=setcolours(j)
        
        for i in range(1,nX+1):
            if((i%2)==1):
                colour=oddsquare
            
        else:
            colour=evensquare
            print(i,j,colour)
            
if __name__ == '__main__':
    
    writechesscolour()