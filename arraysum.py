import time

def solution(A,count,sum):
    j=1
    P=[]
    blank=[]
    if(count==1 and concat_sum(A)==sum):
        j=len(A)
        return concat_arr(A)
    if(count==1 and concat_sum(A)!=sum):
        return concat_arr1(['a','b'])
    
        
    while j<len(A):
        P=[]
        if(count==len(A) and array_sum(A)==sum ):
            o=0
            while(o<len(A)):
                
                
                P.append(A[o])
                o+=1
                
           
            j=len(A)
        
        
              
        else:
            P=[]
            i=0
            while(i<len(A[:j])):
                
                i=i+1
            i=0
            while(i<len(A[j:])):
                      
                i=i+1
            P.append(concat_sum(A[:j]))
            L=solution(A[j:],count-1,sum-concat_sum(A[:j]))
            if 'ab' in L:
                L.remove('ab')
            m=0
            while(m < len(L)):
                P.append(L[m])
                m+=1
            j+=1
            if(array_sum(P)==sum):
                j=len(A)
              
    #print("j,len(A),array_sum(P),sum,len(P),count",j,len(A),array_sum(P),sum,len(P),count)        
    if((j==len(A) and array_sum(P)!=sum) or len(P)!=count ):
        return blank  
    else:
        return P
  

            
        


def array_sum(A):
    i=0
    sum=0
    while i < len(A):
        sum+=A[i]
        i+=1
    return sum

def concat_arr(A):
    i=1
    str1=A[0]
    arr=[]
    while(i<len(A)):
        str1=str(str1)+str(A[i])
        i+=1
    arr.append(int(str1))
    return arr
def concat_sum(A):
    i=1
    str1=A[0]
    while(i<len(A)):
        str1=str(str1)+str(A[i])
        i+=1
    return int(str1)
def concat_arr1(A):
    i=1
    str1=A[0]
    arr=[]
    while(i<len(A)):
        str1=str(str1)+str(A[i])
        i+=1
    arr.append(str1)
    return arr
