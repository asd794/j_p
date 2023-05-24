import urllib.request as request
import json

# src="https://www.ntu.edu.tw"
# with request.urlopen(src) as response1:
#     data=response1.read().decode("utf-8")
# print(data)

src="https://data.taipei/api/v1/dataset/296acfa2-5d93-4706-ad58-e83cc951863c?scope=resourceAquire"
with request.urlopen(src) as reponseOpenData:
    data=json.load(reponseOpenData)
# print(data)
datajson=data["result"]["results"]
print(datajson)
with open("company.txt",mode="w",encoding="utf+8") as file:
    for i in range(len(datajson)):
    # print(i)
        file.write(datajson[i]["公司名稱"]+" : "+datajson[i]["公司地址"]+"\n")

ttest={1:"123",2:"555",3:{"3-1":"5566"}}
print(ttest[3]["3-1"])