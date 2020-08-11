import pandas as pd

##### Loading Data ==>
dfcsv = pd.read_csv('pokemon_data.csv')  # Read CSV
# ----------------------------------------------------------------------

##### Viewing and Inspecting Data ==>
print("Describe shows count, mean, std min, 25%,50%,75%,max : ", dfcsv.describe())
print("Returns the mean of all columns : ", dfcsv.mean())
# Above mean => If any column has TRUE & FALSE then also it finds mean for that column with value TRUE = 1 and FALSE = 0
print("Returns the correlation between columns in a data frame : ", dfcsv.corr())
print("Returns the highest value in each column : ", dfcsv.max())
print("Returns the lowest value in each column : ", dfcsv.min())
print("Returns the median of each column : ", dfcsv.median())
print("Returns the standard deviation of each column : ", dfcsv.std())
print("Returns the number of non-null values in each data frame column : ", dfcsv.count())
print("Returns the number of rows and columns : ", dfcsv.shape)
print("Returns the index, datatype and memory information : ", dfcsv.info)
print("Returns the count of unique values of given columns with Nan : ", dfcsv["Type 2"].value_counts(dropna=False))
# Above : This will show "NaN"
print("Returns the count of unique values of given columns without Nan : ", dfcsv["Type 2"].value_counts(dropna=True))
# Above : This will not show "NaN"
print("Total Unique values of Dataframe and their counts : ", pd.value_counts(dfcsv.values.flatten()))
# ----------------------------------------------------------------------

##### Selection of Data ==>
print("Select Singl column : ", dfcsv["Name"])
print("Select Multiple column : ", dfcsv[["Name", "HP"]])
print("Select column's particular record : ", dfcsv[["Name"]].iloc[5])
print("Select the first row : ", dfcsv.iloc[1:1])
# Above [:] ...means All rows and All columns
# Above [0:] or [1:] ...means Start index(here 0 or 1) of row to end of file
# Above [1:3 : ] => 2nd and 3rd rows
# Above [1:3, 4:6] => 2nd and 3rd rows & 4th and 5th columns
# Above [4,5] => Value of 4th row and 5th column
# Above [1:3, : 4] => 2nd and 3rd rows & 1st to 4th Column only
# Above [1:3, 4] => 2nd and 3rd rows & 4th Column only
# Above [1,:] => Only one row : 1st index row
# ----------------------------------------------------------------------

##### Filter, Sort and Groupby ==>
print("Filtered Data with == , >= , <= : ", dfcsv.loc[(dfcsv['HP'] > 100)])
# In Above we can use : == , >= , > , <= , < , !=
### Below is boolean filtering : & = and , | = or
print("Filtered Data with AND(&) : ", dfcsv.loc[(dfcsv['Type 1'] == 'Grass') & (dfcsv['Type 2'] == 'Poison')])
### Below is Sorting =>
print("Sort Values in Default(Ascending) : ", dfcsv.sort_values("#"))  # default ascending = True
print("Sort Values in Descending : ", dfcsv.sort_values("#", ascending=False))
print("Sort multiple columns Values in Both Asc & Desc : ", dfcsv.sort_values(["Type 1","Type 2"], ascending=[True,False]))
### Below is Groupby =>
print("Groupby columns Values : ", dfcsv.groupby(["Type 1","Type 2"]).count())
print("Groupby columns Values : ", dfcsv.groupby(["Type 1"]).count())
# ----------------------------------------------------------------------

##### Data Cleaning ==>
print("Check where blank value is isnull : ",dfcsv.isnull().iloc[0:8,:])
# Above => shows true for missing values and false for non-missing values

print("Check where blank value is isnull with sum : ",dfcsv.isnull().sum())
# Above => shows count of null values for each column

print("Check where blank value is notnull : ",dfcsv.notnull())
# Above => shows False for missing values and True for non-missing values : Exactly opposite of isnull()

print("Check where blank value is isnull with sum : ",dfcsv.notnull().sum())
# Above => shows count of notnull values for each column : Exactly opposite of isnull()

print("Drop Rows which has blank values with dropna : ",dfcsv.dropna())
# Above => It dropped rows which are having null value in anywhere

print("Drop Columns which has blank values with dropna : ",dfcsv.dropna(axis=1))
# Above => It dropped columns which are having null value in anywhere

print("Fill value in blank values with fillna : ",dfcsv.fillna("Omkar").iloc[0:8,0:7])
# Above => Fill the value as Omkar in which it is blank/null with fillna

print("Fill mean value in blank values with fillna : ",dfcsv.fillna(dfcsv["HP"].mean()).iloc[0:8,0:7])
# Above => Fill the Mean value to replace all null values, mean should be of Numeric Columns only :P

print("Single Replace Value : ",dfcsv.replace("Grass","Omkar").iloc[0:8,0:7])
# Above => Fill the Mean value to replace all null values, mean should be of Numeric Columns only :P

print("Multiple Replace Value : ",dfcsv.replace(["Grass","Fire"],["Omkar","Karan"]).iloc[0:8,0:7])
# Above => Fill the Mean value to replace all null values, mean should be of Numeric Columns only :P

print("Rename the column name : ",dfcsv.rename(columns = {"Type 1":"Type_1"}).iloc[0:8,0:7])
# Above => Fill the Mean value to replace all null values, mean should be of Numeric Columns only :P
# ----------------------------------------------------------------------

##### Join/Combine ==>
# df1.append(df2) —> add the rows in df1 to the end of df2 (columns should be identical)
# df.concat([df1, df2],axis=1) —> add the columns in df1 to the end of df2 (rows should be identical)
# df1.join(df2,on=col1,how='inner') —> SQL-style join the columns in df1 with the columns on df2 where the rows for colhave identical values.
    # In Above "how" can be equal to one of: 'left', 'right', 'outer', 'inner'
dfxlsx = pd.read_excel('pokemon_data.xlsx')  # Read Text
dfcsv.append(dfxlsx)
print(dfcsv)

# ----------------------------------------------------------------------