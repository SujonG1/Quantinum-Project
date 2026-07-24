import pandas as pd

#Reading all the given datasets using pandas
df1 = pd.read_csv("quantium-starter-repo/data/daily_sales_data_0.csv")
df2 = pd.read_csv("quantium-starter-repo/data/daily_sales_data_1.csv")
df3 = pd.read_csv("quantium-starter-repo/data/daily_sales_data_2.csv")

#joining all the datasets to one large data
df = pd.concat([df1, df2, df3], axis=0, ignore_index=True)

#filtering out the necessary value
df = df[df["product"] == "pink morsel"]

df['price'] = df['price'].astype(str).str.replace('$', '', regex=False)

df['price'] = pd.to_numeric(df['price'])

df['quantity'] = pd.to_numeric(df['quantity'])

df["sales"] = df["price"].mul(df["quantity"])

df = df.drop(columns=["price", "quantity"])

df.to_csv('Pink_Morsel_Sales_Data.csv', index=False)