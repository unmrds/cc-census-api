#!/usr/bin/env python
# coding: utf-8

# # Census APIs
# 
# Request a key at <https://api.census.gov/data/key_signup.html>
# 
# An email will be sent to the addres you provide. The email will include a link to activate the key. It may take a few minutes before the key can be activated.

# In[92]:


import json
import requests
import pandas as pd
import matplotlib as plt


# In[93]:


# Load API key

# Note the file with the API key is not in the GitHub repo.
# Keys need to be read from a local directory
with open("jwCensusApi", "r") as i:
    key = i.read()


# ## Identifying the Data Source
# 
# We are going to use the Census API to retrieve data to reproduce some of the statistics from the Feb 24, 2022, press release and infographic *A Higher Degree.*
# 
# **Press release:** <https://www.census.gov/newsroom/press-releases/2022/educational-attainment.html>
# 
# **Infographic:** <https://www.census.gov/library/visualizations/2022/comm/a-higher-degree.html>
# 
# Below is the infographic. Note that for today's workshop we are using only 2021 data.
# 
# <a class="embeddable-image__embedLink" href="https://www.census.gov/library/visualizations/2022/comm/a-higher-degree.html?cid=higher-degree" target="_blank"><img class="embeddable-image__embedImage" data-src="/library/visualizations/2022/comm/a-higher-degree/_jcr_content/root/responsivegrid/embeddableimage1119.coreimg.jpeg/1645624284211/educational-attainment-2022.jpeg" alt="A Higher Degree" title="A Higher Degree" src="https://www.census.gov/library/visualizations/2022/comm/a-higher-degree/_jcr_content/root/responsivegrid/embeddableimage1119.coreimg.jpeg/1645624284211/educational-attainment-2022.jpeg" width="1080" height="1080"></a>[Source: U.S. Census Bureau]

# According to the press release, the data are from the *2000–2002 March Current Population Survey and 2003–2021 Annual Social and Economic Supplement to the Current Population Survey.*
# 
# ### Q: How to get info on variables via API?
# 
# We can look it up online, but we may also get this info dynamically. 
# 
# #### Steps:
# 
# 1. Go to the *Census Data API Discovery Tool*: <https://www.census.gov/data/developers/updates/new-discovery-tool.html>
# 1. Preview the datasets and available information using the HTML format: <https://api.census.gov/data.html>
# 1. Use HTTPS libraries ("requests") to download the data in JSON format.
# 1. Process the JSON.

# In[94]:


# Request the JSON information about available datasets

datasets_url = "https://api.census.gov/data.json"
datasets_request = requests.get(datasets_url)
datasets_json = datasets_request.json()


# In[95]:


datasets_json


# In[96]:


dataset_list = datasets_json["dataset"]
len(dataset_list)


# In[97]:


# This took a little sleuthing to find the dataset identifier.
# Why is the identifier not included in the press release or infographic?

# Get the titles of the datasets
dataset_list = datasets_json["dataset"]

# title: Current Population Survey Annual Social and Economic Supplement
# c_vintage: 2021
# id: https://api.census.gov/data/id/CPSASEC2021

cpd_asec_mar = [d for d in dataset_list if d["identifier"] == "https://api.census.gov/data/id/CPSASEC2021"]
print(json.dumps(cpd_asec_mar, indent=4)) # long output


# In[98]:


# Get info on variables

dataset_vars_url = cpd_asec_mar[0]["c_variablesLink"]
dataset_vars_request = requests.get(dataset_vars_url)
datasets_vars_json = dataset_vars_request.json()
# print(json.dumps(datasets_vars_json, indent=4)) # long output - many variables

# just print the variable and the label
dataset_vars = datasets_vars_json["variables"]

# sort variable names
sorted_vars = sorted(dataset_vars.keys())

# View the first 10 variable, for example.
for k in sorted_vars[:10]:
    var_info = dataset_vars[k]
    print(k, ":", var_info["label"])


# In[99]:


# Set the API endpoint URL for this dataset

endpoint = cpd_asec_mar[0]["distribution"][0]["accessURL"]
print(endpoint)


# In[100]:


# Get info on a single variable

var = "A_HGA"
var_def_url = endpoint + "/variables/" + var
var_def_request = requests.get(var_def_url)
var_json = var_def_request.json()
print(json.dumps(var_json, indent=4))


# In[101]:


'''
Variables of interest

A_HGA - educational attainment
AGE1 - age
AGI - federal adjusted gross income

NM FIPS ID = 35
'''

vars_list = ["A_HGA", "AGE1", "AGI"]
vars_dict = {}

for v in vars_list:
    var_def_url = endpoint + "/variables/" + v
    var_def_request = requests.get(var_def_url)
    var_json = var_def_request.json()
    vars_dict[v] = var_json


# In[102]:


vars_dict


# ## Tabulating Census Data
# 
# We can download the unweighted data, but that will not produce the same results as the infographic and press release.
# 
# Instead we will download the weighted data, in a "pre-tabulated" format. This means some aggregation has already been done. 

# In[103]:


census_wtd_url = endpoint + "?tabulate=weight(MARSUPWT)&col+A_HGA&row+AGE1&for=state:*"
census_wtd_request = requests.get(census_wtd_url)
census_wtd_json = census_wtd_request.json()
# print(json.dumps(census_wtd_json, indent=4)) # long output


# In[104]:


# Convert returned JSON to dataframe

# subset to rows with data (all but the first row, which has column headers)
drop_keys = census_wtd_json[1:]

# column headers - need additional processing
get_keys = census_wtd_json[0]

# read JSON data into a pandas data frame
w_df = pd.read_json(json.dumps(drop_keys), typ = "frame", orient = "values")

# add column headers
cols = []
for k in get_keys:
    if isinstance(k, dict):
        v = [e[:] for e in k.values()]
        cols.append(v[0])
    if isinstance(k, str):
        cols.append(k)
w_df.columns = cols

# create index on AGE1 variable
w_df.set_index("AGE1", inplace = True)

# sort on index (numeric sort)
w_df.sort_index(inplace = True)
print(w_df.info())


# In[105]:


w_df.head()


# In[106]:


w_df = w_df[sorted(w_df.columns)]


# In[107]:


w_df.info()


# In[108]:


w_df.head() # keep in mind our index labels and column names are coded - pandas will work with categorical vars as a dtype


# In[109]:


# AGE1 >= 6 is the population 25 and over
w_df.loc[6:]


# In[110]:


# get the sum of the population >= 25
sum_age_gte25 = w_df[6:].to_numpy().sum()
sum_age_gte25


# Let's match some data points to the press release. Keeping in mind we are only using 2021 data, the press release says:
# 
# >    8.9% had less than a high school diploma or equivalent.  
#     27.9% had high school graduate as their highest level of school completed.   
#     14.9% had completed some college but not a degree.  
#     10.5% had an associate degree as their highest level of school completed.  
#     23.5% had a bachelor’s degree as their highest degree.  
#     14.4% had completed an advanced degree such as a master’s degree, professional degree or doctoral degree.   
# 

# In[111]:


# Start with HS diploma as highest level of education attained (coded as 39 in A_HGA)
# here's the subset:
w_df[6:]["39"]


# In[112]:


# here's the sum of the subset
w_df[6:]["39"].sum()


# In[113]:


# assign that to a variable
hs_diploma = w_df[6:]["39"].sum()


# In[114]:


# Divide by the total pop >= 25 yo to get the percentage. Press release rounds to 1 decimal point
round((hs_diploma/sum_age_gte25) * 100, 1) # This is the correct %


# In[115]:


# some college, no degree (coded as "40" in A_HGA)
some_college = w_df[6:]["40"].sum()
round((some_college/sum_age_gte25) * 100, 1) # also the correct %


# In[116]:


# let's use the same syntax to request multiple columns
# in this case for no HS diploma (codes 31-38 in this case)
no_hs_diploma = w_df[6:][["31", "32", "33", "34", "35", "36", "37", "38"]].to_numpy().sum()
round((no_hs_diploma/sum_age_gte25) * 100, 1) # also correct


# ## Plotting Census Data

# In[117]:


# plot the whole dataset as a stacked bar plot
w_df.plot.bar(stacked = True, legend = False) # ed attainment stacked bar plot (x = age, y = count of pop, colors = A_HGA)


# In[118]:


# we can use the same subsetting syntax as above to limit to population >= 25 yo
# ed attainment stacked bar plot (x = age, y = count of pop, colors = A_HGA)
w_df[6:].plot.bar(stacked = True, legend = False) 


# In[119]:


# The infographic charts bachelors degrees and higher, codes 43-46 in A_HGA
'''
    '43': "Bachelor's degree (BA,AB,BS)",
    '44': "Master's degree (MA,MS,MENG,MED,MSW,MBA)",
    '45': 'Professional school degree (MD,DDS,DVM,L',
    '46': 'Doctorate degree (PHD,EDD)'
'''
w_df[6:][["43", "44", "45", "46"]].plot.bar(stacked = True).legend(loc = "best", bbox_to_anchor = (-0.05, -0.05))


# In[120]:


# the infographic is further aggregated - data are summed per educational attainment level
# across all ages groups
w_df[6:][["43", "44", "45", "46"]].sum().plot.bar(legend = False) # close! - note that the y scale is 10m


# In[121]:


# Create a subset to work with
plot_data = pd.DataFrame(w_df[6:][["43", "44", "45", "46"]].sum())

# Give the new dataframe (a table of summed population per level of ed. attainment) a nice column name
plot_data.columns = ["2021"]

# look at it - the numbers match those in the infographic
plot_data


# In[122]:


# Our version of the infographic
# get sum totals for legend
pop_bd = str(round(plot_data.loc["43"]["2021"]/1000000, 1))
pop_md = str(round(plot_data.loc["44"]["2021"]/1000000, 1))
pop_pd = str(round(plot_data.loc["45"]["2021"]/1000000, 1))
pop_dr = str(round(plot_data.loc["46"]["2021"]/1000000, 1))

# create a list of labels for the legend
# note that we could also have done the math here, but it would be harder to read
l = ["Bachelor's Degree: " + pop_bd + " million", 
     "Master's Degree: " + pop_md + " million", 
     "Professional School Degree: " + pop_pd + " million",
     "Doctorate Degree: " + pop_dr + " million"]

# plot with an intelligble legend
plot_data.T.plot.bar(stacked=True).legend(l, loc = "best", bbox_to_anchor = (-0.05, -0.05))

