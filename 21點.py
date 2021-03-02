import random
def card():
    rd=random.choice(["A","1","2","3","4","5","6","7","8","9","10","J","Q","K"])
    return rd

def your_point():
    global your_card
    global your_total
    global i
    
    if your_card[i]=="A":
        your_total+=1
    elif your_card[i]=="J" or your_card[i]=="Q" or your_card[i]=="K":
        your_total+=0.5
    else:
        your_total+=int(your_card[i])
        
    if your_total>10.5:
        your_total=0
        print("你的點數超過了")
    else:
        i+=1
        print("目前點數:",your_total)

def pc_point():
    global pc_card
    global pc_total
    global j
    
    if pc_card[j]=="A":
        pc_total+=1
    elif pc_card[j]=="J" or pc_card[j]=="Q" or pc_card[j]=="K":
        pc_total+=0.5
    else:
        pc_total+=int(pc_card[j])
    
def pc():
    global pc_card
    global pc_total
    global j
     
    if pc_total>6.5:
        pass
    else:
        pc_card.append(card())
        j+=1
        pc_point()
    
    if pc_total>10.5:
        pc_total=0
        print("電腦點數超過了")
        
def main():
    global your_card
    global pc_card
    your_card.append(card())
    print("你的卡牌:",your_card)
    your_point()
    pc_card.append(card())
    pc_point()
    print("拿牌輸入1，不拿牌輸入0")
    while True:
        check=int(input())
        if check==1:
            your_card.append(card())
            print("你的卡牌",your_card)
            your_point()
            if your_total==0:
                break
            if your_total!=0:
                pc()
                if pc_total==0:
                    break
            print("拿牌輸入1，不拿牌輸入0")
        elif check==0:
            break
            
    while pc_total<6.5 and your_total!=0:   
        if pc_total==0:
            break
        else:
            pc()
    
    print("你的卡牌:",your_card)
    print("你的分數:",your_total)
    print("電腦卡牌:",pc_card)
    print("電腦分數:",pc_total)
    if your_total>pc_total:
        print("你贏了")
    elif pc_total>your_total:
        print("電腦贏了")
    else:
        print("雙方平手")
    
your_card=[]
your_total=0
i=0
pc_card=[]
pc_total=0
j=0
main()
