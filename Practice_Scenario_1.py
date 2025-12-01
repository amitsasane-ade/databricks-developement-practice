# Databricks notebook source
import pandas as pd
import numpy as np

# COMMAND ----------

array_4 = np.random.randint(10,100,size=(8,8))
print(array_4)

# COMMAND ----------

DF4 = pd.DataFrame(array_4,columns=list("ABCDEFGH"))
DF4

# COMMAND ----------

DF1.display()
DF2.display()
DF3.display()
DF4.display()

# COMMAND ----------

List = [DF1, DF2, DF3, DF4]
List

# COMMAND ----------

#Data from all the dataframes for those specific identical columns will append one by one
List2 = ["A", "B", "C", "D"]

zeros = np.zeros((0,4),dtype="int")
same_fields_df = pd.DataFrame(zeros,columns=DF1.columns[:4])

for i in List:
    zeros = np.zeros((0,4),dtype="int")
    temp_df = pd.DataFrame(zeros,columns=DF1.columns[:4])
    for k in i.columns:
        for j in List2:
            if k==j:
                temp_df[f"{k}"] = i[f"{k}"]
#                 print(temp_df)
    same_fields_df = pd.concat([same_fields_df,temp_df],ignore_index=True)                     
print(same_fields_df)  

# COMMAND ----------

# MAGIC %md
# MAGIC ####Columns from all dataframes having different field names will extend one by one

# COMMAND ----------

#Columns from all dataframes having different field names will extend one by one
List2 = ["A", "B", "C", "D"]

diff_fields_df = pd.DataFrame([])
for i in List:
    for k in i.columns:
        for j in List2:
            if k!=j:
                diff_fields_df[f"{k}"] = i[f"{k}"]
diff_fields_df.drop(columns=List2,axis=1,inplace=True)                  
print(diff_fields_df)  
