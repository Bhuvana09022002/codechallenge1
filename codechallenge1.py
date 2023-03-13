import pandas as pd
df = pd.read_csv("C:/Users/3108p/code_challenge/vendors.csv")

inp = pd.DataFrame()
n = int(input("Enter n: "))
pur = []
item = []
quan = []
for i in range(n):
    read = list(input().split(" "))
    pur.append(read[0])
    item.append(read[1])
    quan.append(read[2])
    
inp["Purchase ID"] = pur
inp["Item"] = item
inp["Req. Quantity"] = quan

Pur = []
Item = []
req_quan = []
IsAvail = []
Vendor_ID = []
Total = []
Time = []

for i in range(inp.shape[0]):
    
    cost = 100000
    mintime = 1000
    isavail = "false"
    vendor = " "
    total = 0
    time = 0
    
    for j in range(df.shape[0]):
        
        if inp["Item"][i] == df["Item"][j]:
            
            if df["Cost Per KG"][j]<cost:
                
                cost = df["Cost Per KG"][j]
                mintime = df["Time to Deliver"][j]
                isavail = "true"
                vendor = df["Vendor"][j]
                total = int(df["Cost Per KG"][j])*int(inp["Req. Quantity"][i])
                time = mintime
                
            elif df["Cost Per KG"][j] == cost:
                
                if df["Time to Deliver"][j] < mintime:
                    
                    mintime = df["Time to Deliver"][j]
                    isavail = "true"
                    vendor = df["Vendor"][j]
                    total = int(df["Cost Per KG"][j])*int(inp["Req. Quantity"][i])
                    time = mintime
                    
    IsAvail.append(isavail)
    Vendor_ID.append(vendor)
    Total.append(total)
    Time.append(time)
    Pur.append(inp["Purchase ID"][i])
    Item.append(inp["Item"][i])
    req_quan.append(inp["Req. Quantity"][i])
    
out = pd.DataFrame(list(zip(Pur,Item,req_quan,IsAvail,Vendor_ID,Total,Time)),columns=["Purchase Id","Item","Quantity","IsAvail","Vendor","Total cost","Time"])
print(out) 