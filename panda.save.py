import pandas as pd
data = {
    "name": [ "aqib", " jamdi ", "anayat"],
    "age": [10,20,30],
    "city":["baramulla", "anantnag","shupain"],
    
}
df = pd.DataFrame(data)
print(df)

#save this as csv 
df.to_csv("output.csv", index=False)
