import pandas as pd

titanic = pd.read_csv("data/titanic.csv")

# Print data types
print(titanic.dtypes)

# Convert to excel sheet
titanic.to_excel("data/titanic.xlsx", sheet_name="passengers", index=False)
titanic = pd.read_excel("data/titanic.xlsx", sheet_name="passengers")

# Select all ages
ages = titanic["Age"]
print(ages.head())

# Each column is a Series
print(type(titanic["Age"]))

# .shape -> number of rows and columns
print(titanic["Age"].shape)

# Filter -> passengers age and sex
age_sex = titanic[["Age", "Sex"]]
print(age_sex.head())

# Filter -> passengers above 35
above_age_35 = titanic[titanic["Age"] > 35]
print(above_age_35.head())

# Filter -> passenger from class 2 or 3
#class_23 = titanic[(titanic["Pclass"] == 2) | (titanic["Pclass"] == 3)]
class_23 = titanic[titanic["Pclass"].isin([2,3])]
print(class_23)

# Filter -> passenger with age is non-missing (not null)
age_no_na = titanic[titanic["Age"].notna()]
print(age_no_na)

# Filter -> passenger older than 35 but retrieve only their names
adult_names = titanic.loc[titanic["Age"] > 35, "Name"]

# Filter -> male passengers older than 18, but retrive only their names 
adult_males = titanic.loc[(titanic["Age"] > 18) & (titanic["Sex"] == "male"), "Name"]
print(adult_males.head())

