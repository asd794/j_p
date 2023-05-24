class IO:   # 定義類別 ,有兩個屬性 supportedSrcs 和 read
    supportedSrcs=["console","file"]
    def read (src):
        if src not in IO.supportedSrcs:
            print("不支援")
        else:
            print("Read from", src)
 
print(IO.supportedSrcs)
IO.read(input("傳入類型 : "))