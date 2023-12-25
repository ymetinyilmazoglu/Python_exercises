
#######################
# Potential Customer Yield Calculation with Rule-Based Classification
#######################

#######################
# Business Problem
#######################
# New level-based customer definitions (personas) using some characteristics of a game company's customers
# create segments according to these new customer definitions and identify new customers who may come to the company according to these segments.
# wants to estimate how much money it can earn on average.


# For example: It is desired to determine how much money a 25-year-old male user from Turkey, who is an IOS user, can earn on average.

#######################
# Dataset Story
#######################
# Persona.csv data set shows the prices of the products sold by an international game company and some of the users who purchased these products.
# contains demographic information. The data set consists of records created in each sales transaction. This means table
# is not deduplicated. In other words, a user with certain demographic characteristics may have made more than one purchase.

# Price: Customer's spending amount
# Source: The type of device the customer is connected to
# Sex: Customer's gender
# Country: Customer's country
# Age: Customer's age


################## Before Application #######################

#    PRICE   SOURCE   SEX COUNTRY  AGE
# 0     39  android  male     bra   17
# 1     39  android  male     bra   17
# 2     49  android  male     bra   17
# 3     29  android  male     tur   17
# 4     49  android  male     tur   17


################## Post Application #######################

#       customers_level_based        PRICE SEGMENT
# 0   BRA_ANDROID_FEMALE_0_18  1139.800000       A
# 1  BRA_ANDROID_FEMALE_19_23  1070.600000       A
# 2  BRA_ANDROID_FEMALE_24_30   508.142857       A
# 3  BRA_ANDROID_FEMALE_31_40   233.166667       C
# 4  BRA_ANDROID_FEMALE_41_66   236.666667       C


#######################
# PROJECT TASKS
#######################

#######################
# TASK 1: Answer the following questions.
#######################
import pandas as pd

# Question 1: Read the persona.csv file and show general information about the data set.
df = pd.read_csv("datasets/persona.csv")
df.head()
df.shape
df.info()
df.describe().T
df.isnull().sum()

# Question 2: How many unique SOURCE are there? What are their frequencies?
df["SOURCE"].unique()
#FREKANSI
df["SOURCE"].value_counts()

# Question 3: How many unique PRICEs are there?
df["PRICE"].unique()

# Question 4: How many sales were made from which PRICE?
df["PRICE"].value_counts()

# Question 5: How many sales were made from which country?
df["COUNTRY"].value_counts()
df.groupby("COUNTRY")["PRICE"].count()
 
df.pivot_table(values="PRICE",index="COUNTRY",aggfunc="count")
# Question 6: How much was earned from sales in total by country?
df.groupby("COUNTRY")["PRICE"].sum()
df.groupby("COUNTRY").agg({"PRICE":"sum"})

df.pivot_table(values="PRICE",index="COUNTRY",aggfunc="sum")


# Question 7: What are the sales numbers according to SOURCE types?

df["SOURCE"].value_counts()

# Question 8: What are the PRICE averages by country?

df.groupby("COUNTRY").agg({"PRICE":"mean"})

# Question 9: What are the PRICE averages according to SOURCEs?

df.groupby("SOURCE").agg({"PRICE":"mean"})

# Question 10: What are the PRICE averages in the COUNTRY-SOURCE breakdown?
df.groupby(["COUNTRY","SOURCE"]).agg({"PRICE":"mean"})

#######################
# TASK 2: What are the average earnings in the COUNTRY, SOURCE, SEX, AGE breakdown?
#######################

df.groupby(["COUNTRY","SOURCE","SEX","AGE"]).agg({"PRICE": "mean"}).head()

#############################################
# TASK 3: Sort the output by PRICE.
#######################
# To better see the output in the previous question, apply the sort_values ​​method to PRICE in decreasing order.
# Save the output as agg_df

agg_df = df.groupby(["COUNTRY","SOURCE","SEX","AGE"]).agg({"PRICE": "mean"}).sort_values("PRICE",ascending = False )
agg_df.head(10)

#######################
# TASK 4: Convert the names in the index into variable names.
#######################
# All variables except PRICE in the output of the third question are index names.
# Convert these names to variable names.
#Hint: reset_index()
# agg_df.reset_index(inplace=True)

agg_df = agg_df.reset_index()
agg_df.head(10)

#######################
# TASK 5: Convert the AGE variable to a categorical variable and add it to agg_df.
#######################
# Convert the numeric variable Age to a categorical variable.
# Create the intervals in a way that you think will be convincing.
# For example: '0_18', '19_23', '24_30', '31_40', '41_70'

bins = [0,18, 23, 30, 40,agg_df["AGE"].max()]

mylabels = ["0_18","19_23","24_30","31_40","41_"+ str(agg_df["AGE"].max())]

agg_df["age_cut"]= pd.cut(agg_df["AGE"],bins, mylabels)

agg_df.head()


#######################
# TASK 6: Define new level based customers and add them to the data set as a variable.
#######################
# Define a variable called customers_level_based and add this variable to the data set.
# Attention!
# After creating customers_level_based values ​​with list comp, these values ​​need to be deduplicated.
# For example, there may be more than one of: USA_ANDROID_MALE_0_18
# It is necessary to take these to groupby and get the price averages.

agg_df['age_cut'] = agg_df['age_cut'].astype(str)

agg_df['customers_level_based'] = agg_df[['COUNTRY', 'SOURCE', 'SEX', 'age_cut']].agg(lambda x: '_'.join(x).upper(), axis=1)

#######################
# TASK 7: Segment new customers (USA_ANDROID_MALE_0_18).
#######################
# Segment by PRICE,
# add the segments to agg_df with the name "SEGMENT",
# describe the segments,

agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"],4,labels = ["D","C","B","A"])

agg_df.groupby("SEGMENT").agg({"PRICE":"mean"})
agg_df.head(10)
agg_df.groupby("SEGMENT").agg({"PRICE": "mean"})

#######################
# TASK 8: Classify new customers and estimate how much income they can bring.
#######################
# To which segment does a 33-year-old Turkish woman using ANDROID belong and how much income is she expected to earn on average?

new_user = "TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]


# In which segment and how much income on average is a 35-year-old French woman using IOS expected to earn?
new_user = "FRA_IOS_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]