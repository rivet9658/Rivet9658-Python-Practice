def stairs(l): #列出巴斯卡三角形，依照幾位數列多少出來
    k=[]
    k.append([1,1,1,1,1,1,1,1,1])
    for i in range(0,l-1):
        kp = [1]
        for j in range(0,8):
            t = kp[j] + k[i][j+1]
            kp.append(t)
        k.append(kp)
    return(k)

def plus(num,sta,l): #先加位數-1的所有階梯數出來，例如輸入為千位數，則加1000以內的結果出來
    total = 0
    if l == 1:
        return(int(num))
    else:
        for i in range(0,l-1):
            total += sum(sta[i])
    return(total)        

def check(num,stairs,l):
    #將輸入的值轉成單獨的int
    c=[]
    cl = l
    for i in range(0,l):
        c.append(int(num[i]))
    
    #加總長度為輸入位數的階梯數出來，如5xxx，則加開頭為5-1至1且位數為4的結果
    totalc = 0
    for i in range(c[0]-1):
        totalc += stairs[l-1][8-i]
    
    #加剩下的
    for i in range(1,l):
        if c[i] > c[i-1]: #目前位數比前一位數大的話，看差多少，加長度為此數的位數且小於此數數字，範圍為此數減差距到此數-1
            for j in range(c[i] - c[i-1]): #例如252，第二位數5大於2，5-2=3，則加長度為2開頭為2,3,4的階梯數
                totalc += stairs[l-i-1][10-c[i]-j]
            cl -= 1
        elif c[i] < c[i-1]:
            break
        elif c[i] == c[i-1]:
            cl -= 1
            pass
    if cl == 1: #自己是階梯數也要加1
        totalc += 1
    return(totalc)

def main():
    num = input()
    l = len(num)
    if l == 1:
        print(plus(num,stairs(l),l))
    else:
        print(plus(num,stairs(l),l)+check(num,stairs(l),l))

main()
