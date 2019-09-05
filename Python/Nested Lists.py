marksheet=[]
scorelist=[]
if __name__ == '__main__':
    #no of input
    for _ in range(int(input())):
        name = input()
        score = float(input())
        marksheet+=[[name,score]]
        scorelist+=[score]
    #removing duplicates and taking second smallest no
    b=sorted(list(set(scorelist)))[1] 
    #(name,score)
    for a,c in sorted(marksheet):
            #(score==second smallest score)
            if c==b:
                print(a)