#!/usr/bin/python
# -*- coding: utf-8 -*-

#author: github.com/hesoru/

from calendar import c
from cgi import print_environ
from pickle import TRUE

#abbreviate package using "as"

#re: use wildcards!
import re
#numpy: build/read arrays
import numpy as np
#pandas: build/read dataframes (needed to import csv)
import pandas as pd
#matplotlib: visualizing data
import matplotlib.pyplot as plot


################################ table of contents ################################

#numpy arrays
#pandas dataframes
    #create dataframe from dictionary
    #importing csv file as dataframe
    #navigating dataframe

#search function + wildcards
#filter
    #filtering dataframes
        #1. filter() function
        #2. access column directly (like $ operator in R)
        #3. df.query() function

#matplotlib: histograms

###################################################################################


################################ numpy arrays ################################

#numpy package allows you to build arrays 

#arrays vs. lists:
    #arrays can store data very compactly
    #can perform operations on entire array without specifying every value in array
    #cleaning up dataframe

list = list(range(1, 10))
result = [number ** 2 for number in list]
result
#[1, 4, 9, 16, 25, 36, 49, 64, 81]
#vs.
array = np.array(range(1,10))
result_2 = array ** 2
result_2
#array([ 1,  4,  9, 16, 25, 36, 49, 64, 81])

print(type(array))
#<class 'numpy.ndarray'>

height = [1.87,  1.87, 1.82, 1.91, 1.90, 1.85]
weight = [81.65, 97.52, 95.25, 92.98, 86.18, 88.45]

np_height = np.array(height)
np_weight = np.array(weight)

bmi = np_weight/np_height ** 2
bmi
#array([23.34925219, 27.88755755, 28.75558507, 25.48723993, 23.87257618, 25.84368152])

### subsetting arrays ###

bmi[bmi < 25]
#array([23.34925219, 23.87257618])

################################ pandas dataframes ################################

#can create dataframe from dictionary or csv file

# create dataframe from dictionary ----------------------------------------------

countries = {
    "country": ["Brazil", "Russia", "India", "China", "South Africa"],
    "capital": ["Brasilia", "Moscow", "New Delhi", "Beijing", "Pretoria"],
    "area": [8.516, 17.10, 3.286, 9.597, 1.221],
    "population": [200.4, 143.5, 1252, 1357, 52.98]
    }
pd_countries = pd.DataFrame(countries)
pd_countries
#        country    capital    area  population
#0        Brazil   Brasilia   8.516      200.40
#1        Russia     Moscow  17.100      143.50
#2         India  New Delhi   3.286     1252.00
#3         China    Beijing   9.597     1357.00
#4  South Africa   Pretoria   1.221       52.98

#dataframe assigns keys 0-4 for each row

#specify alternative index values (keys)
pd_countries.index = ["BR", "RU", "IN", "CH", "SA"]
pd_countries
#         country    capital    area  population
#BR        Brazil   Brasilia   8.516      200.40
#RU        Russia     Moscow  17.100      143.50
#IN         India  New Delhi   3.286     1252.00
#CH         China    Beijing   9.597     1357.00
#SA  South Africa   Pretoria   1.221       52.98

# importing csv file as dataframe ----------------------------------------------

#first row and first column = 0
enhancers_and_gene_expression = pd.read_csv("C:/Users/Helena/enhancer_status_with_genes_and_expression.tsv", sep='\t', header = 0, index_col = 0)
print(enhancers_and_gene_expression)
#[37914 rows x 30 columns]

# navigating dataframe ----------------------------------------------

#select specific column
enhancers_and_gene_expression["MPP_atac_significant"]
#select multiple columns
enhancers_and_gene_expression[["MPP_ac_significant", "MPP_atac_significant"]]

#select specific rows (prints rows 5 and 6)
enhancers_and_gene_expression[4:6]
#[2 rows x 30 columns]

#use loc (label-based) or iloc (integer index-based) to access row or column [row,column] (: = all)
enhancers_and_gene_expression.loc["ENSMUSG00000007777",:]
enhancers_and_gene_expression.iloc[0,:]

# cleaning up dataframe ----------------------------------------------

#select MPP_TPM column
MPP_TPM = enhancers_and_gene_expression["MPP_TPM"]
MPP_TPM
#[MPP_TPM, Length: 37914, dtype: float64]

#check how many NaNs/inf you have in your TPM data
MPP_TPM.isnull().sum()
#[694]

#use dropna() to remove null values
    #axis: 0 for dropping rows, 1 for columns
    #how: any for dropping any row/column with NA, all for dropping entire row/column
    #inplace: if True, do operation inplace and return None
clean_MPP_TPM = MPP_TPM.dropna(axis=0, how="any", inplace=False)
clean_enhancers_and_gene_expression = enhancers_and_gene_expression.dropna(axis=0, how="any", inplace=False)
#can select specific columns to filter
clean_by_MPP_TPM_enhancers_and_gene_expression = enhancers_and_gene_expression.dropna(subset=["MPP_TPM"], axis=0, how="any", inplace=False)
clean_enhancers_and_gene_expression
#[37220 rows x 30 columns]


#-------------------------------------------------------------------------------------------------------------------------------


################################ search function + wildcards ################################

#use regular expressions (regex) package

# CASE-SENSITIVE

# operators
    # [] = a set of characters
    # | = either or

# numbers
    # \d = match decimal digit
    # \D = match non-digits

# strings
    # \w = alphanumeric characters (includes numbers)
    # ^ or \A = starts with
    # $ or \Z = ends with
    # \b = word boundary (put at beginning and/or end of query)
    # \B = !\b (match only in middle of word)

# number of occurrences
    # . = any 1 character
    # + = 1+ occurrences
    # * = 0+ occurrences
    # ? = 0-1 occurrences
    # {} = specified number of occurrences (eg. he{2}o for "hello")

# r'\ ' = slash considered part of string

organisms = ["cat", "bear", "ant", "dog", "elephant", "n/a", "a"]

#challenge: words starting with a

#try *
for aword in organisms:
    if re.findall("a*", aword):
        print(aword, end=" ")
#[cat bear ant dog elephant n/a a]
#returns things with 0 or more a's, not ideal for searching

#find all things that start with a
for aword in organisms:
    if re.findall(r"\ba", aword):
        print(aword, end=" ")
#[ant n/a a]
#want to find words (>1 letter) that starts with a
for aword in organisms:
    #\b (starts with), a+ (>1 letter), \w (words)
    if re.findall(r"\ba+\w", aword):
        print(aword, end=" ")
#[ant]

#alternate method: list comprehension
result = [aword for aword in organisms if aword.startswith("a")]
result
#['ant', 'a']

# 2 functions for search:
    # txt.startswith(x, start, end)
    # txt.contains(x, start, end)

################################ filter ################################

# filter(func, iterable)
def is_A_word(list):
    for aword in list:
        if re.findall(r"\ba+\w", aword):
            return aword
is_A_word(organisms)
A_word = list(filter(is_A_word, organisms))
A_word
#[] didn't work???

# filtering dataframes ----------------------------------------------

#import dataframe
enhancers_and_gene_expression = pd.read_csv("C:/Users/Helena/405_Linux_outputs/Gene_subsets/enhancer_status_with_genes_and_expression.tsv", sep='\t', header = 0, index_col = 0)

### 1. filter() function ###

# filter(func, iterable)
    #doesn't take more than 2 arguments like map()

def over_100(expression):
    return expression > 100
MPP_TPM_over_100 = (filter(over_100, enhancers_and_gene_expression["MPP_TPM"]))
list(MPP_TPM_over_100)
#[returns MPP_TPM column with expression > 100]

#how do we return entire dataset based on filtering 1 column?

### 2. access column directly (like $ operator in R) ###

# df[df.column]
MPP_TPM_over_100 = enhancers_and_gene_expression[enhancers_and_gene_expression.MPP_TPM > 100]
#[1090 rows x 30 columns]

#can use multiple operators: "&", "|"
MPP_ac_TPM_over_100 = enhancers_and_gene_expression[(enhancers_and_gene_expression.MPP_TPM > 100) & (enhancers_and_gene_expression.MPP_ac_significant == 1)]
MPP_ac_TPM_over_100
#[173 rows x 30 columns]

#or

#select MPP_TPM column
MPP_TPM = enhancers_and_gene_expression["MPP_TPM"]
#or
MPP_TPM = enhancers_and_gene_expression.loc[:,"MPP_TPM"]
#select MPP_TPM > 100
MPP_TPM_over_100 = enhancers_and_gene_expression[MPP_TPM > 100]
#[1090 rows x 30 columns]

### 3. df.query() function ###

#filter just closed/ac in MPP
MPP_closed_ac = enhancers_and_gene_expression.query('MPP_ac_significant == 1 & MPP_atac_significant == 0')
print(MPP_closed_ac)
#[338 rows x 30 columns]

#operators for filtering:
    # &
    # |
    # isin()
    # str.startswith("")
    # str.contains("")
    # ~ (not, like !=)
    # nlargest(n, column) or nsmallest(n, column)


#-------------------------------------------------------------------------------------------------------------------------------


################################ matplotlib: histograms ################################

### challenge: create histogram of MPP gene expression ###

#create histogram counts/bins with numpy
counts, bins = np.histogram(enhancers_and_gene_expression["MPP_TPM"])
#ValueError: autodetected range of [nan, nan] is not finite - clean up data
counts, bins = np.histogram(clean_MPP_TPM)
counts
#array([327,   2,   2,   0,   2,   0,   0,   0,   0,   1], dtype=int64)
bins
#array([0,  401.41438396,  802.82876792, 1204.24315188, 1605.65753585, 2007.07191981, 2408.48630377, 2809.90068773, 3211.31507169, 3612.72945565, 4014.14383962])

#plot histogram
MPP_histogram = plot.hist(bins[:-1], bins, weights=counts)

#visualize plot from last line
plot.show()

#can also manually choose number of bins
MPP_histogram = plot.hist(clean_MPP_TPM, bins = 20)
#looks like most counts in 0-10 TPM range

#select TPM range of 1-10 for histogram to increase resolution
MPP_histogram = plot.hist(clean_MPP_TPM, bins = 20, range = [0, 10])
plot.show()

#looks like most genes (>17,500) have ~0 TPM

################################ matplotlib: boxplot ################################

clean_enhancers_and_gene_expression
TPM_data = clean_enhancers_and_gene_expression.columns.str.contains(".+_TPM")
