#輸入姓名，學號，三科分數，算成績，印出來

char = input("姓名")
integer = input("學號")
sc1 = int(input("國文"))
sc2 = int(input("計算機概論"))
sc3 = int(input("計算機程式設計"))

total = sc1 + sc2 + sc3
avg = total/3
print("Name:" + char)
print("Id:" + integer)
print("Total:" + str(total))
print("Average:" + str(avg))