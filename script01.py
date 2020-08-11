import pandas as pd
import re

dfcsv = pd.read_csv('pokemon_data.csv')  # Read CSV
dfxlsx = pd.read_excel('pokemon_data.xlsx')  # Read Text
dftxt = pd.read_csv('pokemon_data.txt', delimiter="\t")  # Read Text

print("DataFrame csv : ", pd.DataFrame(dfcsv))
dtfrm = pd.DataFrame(dfcsv["Name"][0:5])
print("Name Column DataFrame : ", dtfrm)

print("Show Default Top Rows : ", dfcsv.head())  # default size of head = 5
print("Show Default Bottom Rows : ", dfcsv.tail())  # default size of tail = 5
print("Show 2 Top Rows : ", dfxlsx.head(2))
print("Show 2 Bottom Rows : ", dfxlsx.tail(2))
print(dftxt.head(2))
print(dftxt.tail(2))

print(dfcsv.columns)  # shows all columns
print(dfcsv.columns[0:7])  # Column slicing
print("1st Way to Print : ", dfcsv[["Name", "Attack"]], '\n')  # print name column 1 way
print("2nd Way to Print : ", dfcsv.Name, dfcsv.Attack)  # print name column 2 way
print("Print Single Column : ", dfcsv[["Name"]], '\n')
# When you want to print single Column then "[]" is enough but When you want to print multiple columns
# then you should use "[[]]", even you use "[[]]" that would be ok.
print("Name Column with Slice: \n", dfcsv["Name"][0:5])

print("Integer location to Select Rows 1 to 4(3) : ", dfcsv.iloc[1:4])  # Integer location to Select Rows 1 to 4(3)
print("Integer location to Select All Rows : ", dfcsv.iloc[:])  # Integer location to Select All Rows
print("Integer location to Select Single Row Given Index : ", dfcsv.iloc[3])  # Integer location to Select All Rows
print("Integer location to Select Specific Value 3rd Row & 1st Column : ",
      dfcsv.iloc[3, 1])  # Syntax = [row_number,# column_number]

for index, row in dfcsv.iterrows():
    print("Print Name Column with Index : ", index, row.Name)  # OR row["Name"]
for index, row in dfcsv.iterrows():
    print("Print All Column and All Rows : ", index, row)

print("Print All Rows having value 'Ice' in Column 'Type 1' : ", dfcsv.loc[dfcsv["Type 1"] == "Ice"])
print("Print All Rows having value '711' in Column '#' : ", dfcsv.loc[dfcsv["#"] == 711])

print("Show Math Calculations : ", dfcsv.describe())

print("Sort Values in Default(Ascending) : ", dfcsv.sort_values("#"))  # default ascending = True
print("Sort Values in Descending : ", dfcsv.sort_values("#", ascending=False))
print("Sort Multiple Values in Default(Ascending): ", dfcsv.sort_values(["Type 1", "HP"]))
print("Sort Multiple Values in Descending: ", dfcsv.sort_values(["Type 1", "HP"], ascending=False))
print("Sort Multiple Values in Multiple Order: ", dfcsv.sort_values(["Type 1", "HP"], ascending=[1, 0]))

# [:] = All the rows & All the columns
# [:,4:10] = All the rows & columns 4th to 10th index
# [0:4, :] = All the columns & rows 4th to 10th index
# 1st Way to Add =>
# Below line is to Add new Column to DataFrame
dfcsv["1st) Total from 4th to 10th Column"] = dfcsv.HP + dfcsv.Attack + dfcsv.Defense + dfcsv['Sp. Atk'] + dfcsv[
    'Sp. Def'] + dfcsv['Speed']
print(dfcsv.head(3))  # Check whether new Column Added or Not

# 2nd Way to Add =>
# Below line is to Add new Column to DataFrame
dfcsv["2nd) Total from 4th to 10th Column Horizontal"] = dfcsv.iloc[:, 4:10].sum(axis=1)  # Horizontal
print(dfcsv.head(2))
dfcsv["2nd) Total from 4th to 10th Column Vertical"] = dfcsv.iloc[:, 4:10].sum(axis=0)  # Vertical
print(dfcsv.tail(2))
dfcsv["2nd) Total from 4th to 10th Row Horizontal"] = dfcsv.iloc[0:2, :].sum(axis=1)  # Horizontal
print(dfcsv.head(2))
dfcsv["2nd) Total from 4th to 10th Row Vertical"] = dfcsv.iloc[0:2, :].sum(axis=0)  # Vertical
print(dfcsv.tail(2))

# Below line is to Remove Column of DataFrame
dfcsv = dfcsv.drop(columns=["2nd) Total from 4th to 10th Row Vertical"])
print("After Deletion : ", dfcsv.head(3))  # Check whether Column deleted or Not

dftxt["Total"] = dftxt.iloc[:, 4:10].sum(axis=1)
print("Print Newly Added Column Total : ", dftxt.tail(2))

print("Print Selective columns: ", dftxt[["Total", "HP", "Defense"]].tail(2))

cols = list(dftxt.columns)
print("Print List of Columns : ", cols)
print("Change List of Columns : ", dftxt[cols[0:4] + [cols[-1]] + cols[4:12]].head(2))

# Create CSV
dftxt.to_csv("new_modified.csv")  # Default index will be Added
dftxt.to_csv("new_modified.csv", index=False)  # index will not be added

# Create Excel
dftxt.to_excel("new_modified.xlsx", index=False)  # index will not be added

# Create Text
dftxt.to_csv("new_modified.txt", index=False, sep="\t")  # index will not be added

### Filtering the Data
print("Filtered Data with == , >= , <= : ", dftxt.loc[(dftxt['HP'] <= 100)])
# In Above we can use : == , >= , > , <= , < , !=

### boolean filtering : & = and , | = or
print("Filtered Data with AND(&) : ", dftxt.loc[(dftxt['Type 1'] == 'Grass') & (dftxt['Type 2'] == 'Poison')])
print("Filtered Data with OR( | ) : ", dftxt.loc[(dftxt['Type 1'] == 'Grass') | (dftxt['Type 2'] == 'Poison')])
# In Above line Index comes in default sequence, if we want to reset it from 0 to so on, then use "reset_index".
print("Filtered Data with reset_index : ",
      dftxt.loc[(dftxt['Type 1'] == 'Grass') | (dftxt['Type 2'] == 'Poison')].reset_index())
# In Above line Index comes in default sequence, if we want to reset it from 0 to so on,
# then we used "reset_index" but it still saves old index as well, so avoid it use drop=True
print("Filtered Data with reset_index : ",
      dftxt.loc[(dftxt['Type 1'] == 'Grass') | (dftxt['Type 2'] == 'Poison')].reset_index(drop=True))
# Above line will remove Index Column


new_dftxt = dftxt.loc[(dftxt['Type 1'] == 'Grass') | (dftxt['Type 2'] == 'Poison')].reset_index(drop=True)
print("Filtered Data with reset_index & Drop Old Index Column : ", new_dftxt)

dftxt.loc[(dftxt['Type 1'] == 'Grass') | (dftxt['Type 2'] == 'Poison')].reset_index(drop=True, inplace=True)
print("Filtered Data with reset_index & Drop Old Index Column & inplace : ", dftxt)
# inplace=True saves memory i.e. if you want to store changes in existing DataFrame the use this inplace.

# Below line is : LIKE operation in SQL
like_operation = dftxt.loc[dftxt['Name'].str.contains("co")]
print("like_operation : ", like_operation)  # Total Count is 10

# Below line is : NOT LIKE operation in SQL
not_like_operation = dftxt.loc[~dftxt['Name'].str.contains("co")]
print("not_like_operation : ", not_like_operation)  # Total Count is 790

# Below line is : IN operation in SQL
in_operation = dftxt.loc[dftxt['Type 1'].str.contains("Dark|Fairy")]
print("in_operation : ", in_operation)  # Total Count is 48

# Below line is : NOT IN operation in SQL
notin_operation = dftxt.loc[~dftxt['Type 1'].str.contains("Dark|Fairy")]
print("notin_operation : ", notin_operation)  # Total Count is 752

# Below line is : Advance Like Operation in SQL
advance_like_operation = dftxt.loc[dftxt['Type 1'].str.contains("dark|fairy", flags=re.I)]  # , regex= True)]
print("advance_like_operation : ", advance_like_operation)  # Total Count is 48, here CaseSensative taken care of

# Below line is : Advance Like Operation in SQL
advance_notlike_operation = dftxt.loc[~dftxt['Type 1'].str.contains("dark|fairy", flags=re.I)]  # , regex= True)]
print("advance_notlike_operation : ", advance_notlike_operation)  # Total Count is 752, here CaseSensative taken care of

# Below line is : Start with in SQL
starwith_operation = dftxt.loc[dftxt['Name'].str.contains("^bu[a-z]*", flags=re.I)].reset_index(drop=True) # Here it also work with : "^Bu[A-Z]*"
print("starwith_operation : ", starwith_operation)
# Total Count is 7, This shows the Name Started with Bu or bu, here CaseSensative taken care of Bu & bu.

# Change Value of records in Column
dftxt.loc[dftxt['Type 1'] == 'Grass' ,'Type 1'] = "Omkar"
print("Change Value of records in Column : ",dftxt.head(20))
print("Type 1 = Omkar : ",dftxt.loc[dftxt['Type 1'] == 'Omkar']) # Total 70 Records changed to Omkar from Grass

# Change Value of records in Column
dftxt.loc[dftxt['Type 1'] == 'Omkar' ,'Type 1'] = "Grass"
print("Change Value of records in Column : ",dftxt.head(20))
print("Type 1 = Grass : ", dftxt.loc[dftxt['Type 1'] == 'Grass']) # Total 70 Records changed to Omkar from Grass

# Change Value of records in Column
dftxt.loc[dftxt['Type 1'] == 'Grass' ,'Legendary'] = "True"
print("Change Value of records in Column : ",dftxt.head(20))
print(dftxt.loc[(dftxt['Type 1'] == 'Grass') & (dftxt['Legendary'] == "True")].iloc[:,:4]) # Total 70 Records changed to Omkar from Grass

# Change Value of records in Column : Update with &, here you can use or i.e. "|" as well
dftxt.loc[(dftxt['Type 1'] == "Grass") & (dftxt['Type 2'] == "Omkar") , "Type 2"] = "Poison"

# Change Value of records in 2 Columns at same time
dftxt.loc[dftxt["Total"] > 500, ['Generation','Legendary']] = "UpdateBothAtSameTime"
print("Update 2 Columns at same time same value : ",dftxt)

# Change Value of records in 2 Columns at same time
dftxt.loc[dftxt["Total"] > 500, ['Generation','Legendary']] = ["UpdateBothAtSameTimeValue1","UpdateBothAtSameTimeValue2"]
print("Update 2 Columns at same time different value : ",dftxt.iloc[:,10:])

# Aggregation
dfxlsx = pd.read_excel('pokemon_data.xlsx')  # Read excel
print("groupby : ",dfxlsx.groupby(["Type 1"]).mean().sort_values("Defense", ascending = False))
print("groupby + Sum : ",dfxlsx.groupby(["Type 1"]).sum())
print("groupby + Count : ",dfxlsx.groupby(["Type 1"]).count())

# Make Count more easy
dfxlsx["count"] = 1
print("groupby + Count and Type1 Columns : ",dfxlsx.groupby(["Type 1"]).count()["count"])
print("groupby + Count and Type1 and Type2 Columns : ",dfxlsx.groupby(["Type 1","Type 2"]).count()["count"])

# For loop & Concatination with DataFrame
new_df = pd.DataFrame(columns=dftxt.columns)
for rcds in pd.read_csv('pokemon_data.txt', delimiter="\t", chunksize=5):  # Read Text
    result = dftxt.groupby(['Type 1']).count()
    print(result)
    new_df = pd.concat([new_df, result],sort=False)
    print("Records read in chunksize : ", new_df)

# Simple Read Limited Records at time from File
for rcds in pd.read_csv('pokemon_data.txt', delimiter="\t", chunksize=5):  # Read Text
    print("Records read in chunksize : ", rcds)