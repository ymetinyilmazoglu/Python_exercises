

##################################################
# Pandas Exercises
##################################################

import numpy as np
import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

#########################################
# Task 1: Identify the Titanic dataset from the Seaborn library.
#########################################
df = sns.load_dataset("titanic")
df.head()
df.shape

#########################################
#Task 2: Find the number of male and female passengers in the Titanic data set described above.
#########################################
df['sex'].value_counts()



#########################################
# Task 3: Find the number of unique values ​​for each column.
#########################################

df.nunique()

#########################################
# Task 4: Find unique values ​​of the pclass variable.
#########################################

df['pclass'].nunique()


#########################################
# Task 5: Find the number of unique values ​​of the pclass and parch variables.
#########################################

df[['pclass','parch']].nunique()

#########################################
# Task 6: Check the type of the embarked variable. Change its type to category. Check the type again.
#########################################

df["embarked"].dtype
str(df["embarked"].dtype)
df["embarked"] = df["embarked"].astype("category")
str(df["embarked"].dtype)
df.info
#########################################
# Task 7: Show all the wisdoms of those with embarked value C.
#########################################

df[df["embarked"]== "C"].head(10)


#########################################
# Task 8: Show all the wisdoms of those whose embarked value is not S.
#########################################

df[df["embarked"]!= "S"].head(10)

#########################################
# Task 9: Show all the information of passengers who are women and under 30 years old.
#########################################

df[(df["age"]< 30) & (df["sex"] == "female")]

#########################################
# Task 10: Show Fare the information of passengers older than 500 or older than 70 years old.
#########################################

df[(df["fare"] > 500) | (df["age"] > 70)]

#########################################
# Task 11: Find the sum of the null values ​​in each variable.
#########################################

df.isnull().sum()


#########################################
# Task 12: Drop the who variable from the dataframe.
#########################################

df.drop("who", axis=1, inplace=True)

df = df.drop("who", axis=1, inplace=True)

#########################################
# Task 13: Fill the empty values ​​in the deck variable with the most repeated value (mode) of the deck variable.
#########################################

type(df["deck"].mode())
df["deck"].mode()[0]
df["deck"].fillna(df["deck"].mode()[0], inplace=True)
df["deck"].isnull().sum()



#########################################
# Task 14: Fill the empty values ​​in the age variable with the median of the age variable.
#########################################

df["age"].fillna(df["age"].median(),inplace=True)
df.isnull().sum()

#########################################
# Task 15: Find the sum, count, mean values ​​of the variable survived in the breakdown of Pclass and Gender variables.
#########################################
df.groupby(["pclass","sex"]).agg({"survived":["sum","count","mean"]})

#########################################
# Task 16: Write a function that will give 1 to those under the age of 30 and 0 to those equal to or above 30.
# Create a variable named age_flag in the titanic data set using the function you wrote. (use apply and lambda structures)
#########################################
def age_30(age):
    if age< 30:
        return 1
    elif age>=30:
        return 0
    
df["age_flag"] = df["age"].apply(lambda x : age_30(x))

df["age_flag"] = df["age"].apply(lambda x: 1 if x<30 else 0)

#########################################
# Task 17: Define the Tips dataset within the Seaborn library.
#########################################

df = sns.load_dataset("tips")
df.head()

#########################################
# Task 18: Find the sum, min, max and average of total_bill values ​​according to the categories (Dinner, Lunch) of the Time variable.
#########################################

df.groupby(df["time"]).agg({"total_bill":["min","max","mean"]})

#########################################
# Task 19: Find the sum, min, max and average of total_bill values ​​according to days and time.
#########################################

df.groupby(["day","time"]).agg({"total_bill":["sum","min","max","mean"]})

#########################################
# Task 20: Find the sum, min, max and average of total_bill and type values ​​of lunch time and female customers according to day.
#########################################

df([df["time"]=="lunch" & df["sex"]=="Female"]).groupby("day").agg({"total_bill":["sum","min","max","mean"],
                                                                   "tip":["sum","min","max","mean"],
                                                                      "Lunch" : lambda x:  x.nunqiue()})
df.head(10)

#########################################
# Task 21: What is the average of orders with size less than 3 and total_bill greater than 10?
#########################################

df.loc[(df["size"]<3) & (df["total_bill"]>10),"total_bill"].mean()

#########################################
# Task 22: Create a new variable named total_bill_tip_sum. Let it give the total bill and tip paid by each customer.
#########################################

df["totall_bill_tip_sum"]=df["total_bill"] + df["tip"]

df.head()
#######################
# Task 23: Find the mean of the total_bill variable separately for men and women.
# Create a new total_bill_flag variable, where the values ​​below the averages you find are assigned 0, and those above or equal to the averages are given a 1.
# Attention !! For females, the average found for women will be taken into account, and for male ones, the average found for men will be taken into account.
# Start by writing a function that takes gender and total_bill as parameters. (Includes if-else conditions)
#######################

# storage of total bill for women and men

f_avg = df[df["sex"]=="Female"]["total_bill"].mean() 
m_avg = df[df["sex"]=="Male"]["total_bill"].mean() 

def func(sex,total_bill):
    if sex=="Female":
        if total_bill < f_avg:
            return 0
        else:
            return 1
    else:
        if total_bill < m_avg:
            return 0
        else:
            return 1

df["total_bill_flag"] = df[["sex","total_bill"]].apply(lambda x: func(x["sex"],x["total_bill"]),axis=1)

#######################
# Task 24: Observe the number of above and below average by gender using the total_bill_flag variable.
#######################

df.groupby(["sex","total_bill_flag"]).agg({"total_bill_flag":"count"})

#######################
# Task 25: Sort from largest to smallest according to the total_bill_tip_sum variable and assign the first 30 people to a new dataframe.
#######################

new_df = df.sort_values("total_bill_tip_sum", ascending=False)[:30]
new_df.shape
