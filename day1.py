S = "test 5a a0A1 pass0071 ?xy1"
def solution(S):
    lengths=[]
    for n in (S.lower()).split(" "):    
        if n.isalnum():
            alpha = 0
            digit = 0
            for i in list(n):
                if i.isalpha():
                    alpha=alpha+1
                elif i.isdigit(): 
                   digit=digit+1    
            if alpha%2 == 0 and digit%2==1:
                lengths.append(len(n))        
    if len(lengths)== 0:
        print(-1)
    else:
        print(max(lengths))
                         
solution(S)
