# Coffee & Code Workshop - US Census Data and their Application Programming Interfaces (APIs)

This workshop is focused on US census data and use of their application programing interaces (APIs). Through [their APIs](https://www.census.gov/data/developers/data-sets.html) the US census Bureau provides a wealth of socioeconomic data for the United States including the [Decennial Census, American Commuity Survey, and a wide variety of more specialized surveys](https://www.census.gov/data/developers/data-sets.html). Developed in collaboration with [Robert Rhatigan](https://gps.unm.edu/staff/robert-rhatigan) from UNM's [Geospatial and Population Studies Program](https://gps.unm.edu) this workshop will provide:

* An introduction to US Census data products and working with the [data.census.gov](https://data.census.gov/cedsci/) web interface. 
* An introduction to APIs and their use
* A brief review of python programming concepts used in support of working with published APIs
* Hands-on experience working with US Census APIs to retrieve, analyze and visualize selected data using some key python packages:
  * `requests` for interacting with the US Census APIs - [https://docs.python-requests.org/en/latest/](https://docs.python-requests.org/en/latest/)
  * `json` for reading the data provided by the API calls - [https://docs.python.org/3/library/json.html](https://docs.python.org/3/library/json.html)
  * `numpy` and `pandas` for managing the returned tabular data and performing basic statistics - [https://numpy.org](https://numpy.org),  [https://pandas.pydata.org](https://pandas.pydata.org)
  * `matplotlib` for data visualization - [https://matplotlib.org](https://matplotlib.org)

## Pre-workshop setup

To be able to follow along with the hands-on practice using the listed tools you will need an operational python programming environment. We will be demonstrating the programming tools using Jupyter notebooks which have loaded the above listed packages. In preparation for the workshp we recommend installing the Anaconda individual edition ([https://www.anaconda.com/products/individual](https://www.anaconda.com/products/individual)) on your computer. We will run through the installation and use of the needed packages as part of the hands-on exercise. 

You should also [request an API key](https://api.census.gov/data/key_signup.html) from the US Census bureau, as this needs to be used when you submit requests to their system for data through their API. 
