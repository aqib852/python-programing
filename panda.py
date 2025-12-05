#wes mickney created panda in 2008

#data cleaning , data processing (trends), data manipulation (cleaning , transformation and structuring data data analysis  (finding patterens ))
#sereis: is a 1-D array labeled array that can hold any data type such as integers floasts strings or even python objects. Each element in the series has a unique labeel called an index 
# used to track changes or patterns over time such as daily temperature stock prices or sales revenue.
# that is used for continues data

#Dataframe : is a 2D labelled data data structure or it is the advanced version of series in Pandas , similiar to table in database an excel spreassheet or a SQl table
#it have rows and columns, where 
#rows have indices (labels)
# columns have names(labbels)
#we can create or read exiting file (JSON,CSV)

#series


import pandas as pd





#series
# temp = pd.Series([12,23,45,67,78,34,45],
#                  index = ["mon", "tue", "wed", "thur", "fri", "sat","sun"])
# print(temp["mon"])
# print(temp)
# print(temp.max())
# print(temp.min())
# print(temp.iloc[0:3]) #integer index locator
# print(temp.loc["mon"])
# print(temp.mean())
# print(temp.sort_index())
# print(temp.sort_values())
# print(temp[temp>12]) #we can directly add condition here
# print(dir(max))

#read data from  CSV file into data frame
# df = pd.read_csv("sales_data_sample.csv",encoding= "latin1")  #encoding="utf-8" or = "latin1") ---> encoding is used only  when we get an error while reading the file
# # for large data set we can use in chunks using for loop


# df2 = pd.read_excel("samplesuperstore.xlsx")
# df3 = pd.read_json("sample_Data.json")                 
# print(df)
# print(df2)
# print(df3)


#create own data

# data = {
#     "name": [ "aqib", " jamdi ", "anayat"],
#     "age": [10,20,30],
#     "city":["baramulla", "anantnag","shupain"],
    
# }
# df = pd.DataFrame(data)
# print(df)

# #save this as csv 
# df.to_csv("output.csv", index=False)




#understand rows
# 2 methods head(n) :first n rows  , tail(n):display last n rows print("display 10 rows")print("display 10 rows")
# print("display first 10 rows")
# print(df.head(10)) # by default ist 5 rows 

# print("last 10 rows") # by default last 5 rows

# print(df.tail(10))




#problems
#1-column , rows? no of rows and columns

#2-what type of 
#3missing data
# print("displaying the info of dataset")

# print(df.info())

#describe method most important
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



data = {
    "name":["jam","aqib","anayat","mohit","mehwish","jafar","jd"],
    "age" : [20,24,23,43,32,33,31],
    "salary": [300000,20000,10000,21000,47000,22000,11000],
    "p score": [23,34,56,78,90,88,67]

}
df =pd.DataFrame(data)
print("sample")
print(df)
print("descriptive statistics")
print(df.describe())

