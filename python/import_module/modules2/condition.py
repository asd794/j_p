# x=int(input("請輸入數字:"))
# if x>=0:
#     print("正整數")
# else:
#     print("負整數")

n1=int(input("請輸入第一個數字: "))
n2=int(input("請輸入第二個數字: "))
op=input("請輸入運算方式 ,+ ,- ,* , /: ")
print(op)
if op=="+":
    print(n1+n2)
elif op=="-":
    print(n1-n2)
elif op=="*":
    print(n1*n2)
elif op=="/":
    print(n1/n2)
else:
    print("錯誤,請輸入正確的運算方式")