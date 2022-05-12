import random
def test():
    count=0
    qr=0
    file='C:\\new 1.csv'
    Qf=open(file,"r")
    ques=Qf.readlines()
    random.shuffle(ques)
    question=1
    for i in range(20):
        x=ques[i].strip()
        d=x.split(",")
        q=d[0]
        trueans=d[1]
        print("the question",question)
        print(q)
        answer=input("your answer is:")
        if answer==trueans:
            print("your answer...true")
            count=count+1
            qr=qr+1
            question=question+1
        else:
            print("your answer...false")
            question=question+1
            sume=(count/10)*100
            print("your score :",sume)
test()            
