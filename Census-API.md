---
title: 'US Census Data and Application Programming Interfaces (APIs)'
author: "Robert Rhatigan"
date: "3/18/2022"
output:
  pdf_document: default
  html_document: default
---

```{r setup, include=FALSE}
knitr::opts_chunk$set(echo = TRUE)
```
# **Census Data Products**


The US Census Bureau ([www.census.gov](www.census.gov)) conducts 130+ surveys each year

**[data.census.gov](data.census.gov)** is the primary Census Bureau data portal (formerly FactFinder).

Many surveys are conducted on behalf of other federal agencies with their own data portals and/or APIs e.g 

- Bureau of Labor Statistics [www.bls.gov/developers/](www.bls.gov/developers/)

- Bureau Economic Analysis [apps.bea.gov/API/signup/index.cfm](https://apps.bea.gov/API/signup/index.cfm)

- National Center for Health Statistics
 [www.cdc.gov/nchs/index.htm](https://www.cdc.gov/nchs/index.htm)

- National Center for Education Statistics [nces.ed.gov/datatools/](https://nces.ed.gov/datatools/)





## **Census APIs**

www.census.gov/data/developers/data-sets.html

### *Decennial Census*

www.census.gov/programs-surveys/decennial-census/data.html

Foundation of all official demographic data in the US.

Decennial Census is mandated in the US Constitution Article 1, Section 2

The first thing the US Constitution directs the new government to do is *Go Gather Data*

For most data users, the decennial census has limited *direct* usability because it is updated only once a decade and because it contains few variables i.e.

- Population by Age/Sex/Race/Ethnicity 

- Relationship to head of household

- Housing Tenure (Own/Mortgage/Rent) 
	
Primary use cases:

- Congressional Apportionment
	
- Redistricting - P.L94-171 data
	
Census smallest Geography - census block 

Hierarchy of Census Geography - [www2.census.gov/geo/pdfs/reference/geodiagram.pdf](https://www2.census.gov/geo/pdfs/reference/geodiagram.pdf)


[data.census.gov](data.census.gov) quick demo on geography
 
### *American Community Survey*

www.census.gov/programs-surveys/acs

Sample survey of approximately two million households each year (~1.6%)

Began in 2005 replacing the census long form

1-year data for Counties and Places with population > 65,000

5-year data for populations < 65,000

Questions/Variables:	

~50 questions for each person at the residence
	
~24 questions on the housing unit
	
Key data:

	Selected Social Characteristics - DP02
		Educational Attainment, Languages spoken, Disability status
		
	Selected Economic Characteristics - DP03
		Income and Earning, Poverty Status, Health Insurance Coverage, Commuting
		
	Selected Housing Characteristics - DP04
		Own/Rent, Persons per Household, Broadband Access, Heating Fuel Type
		
	Demographic and Housing Estimates - DP05
		Age/Sex, Race, Ethnicity, Group Quarters Populations, CVAP
		
ACS Smallest Geography - Block Group

### *Population Estimates and Projections*

#### Estimates

Annually updated population estimates by Age/Sex/Race/Ethnicity

Population Estimates = Census + Births - Deaths + Net Migration

[www.census.gov/programs-surveys/popest.html](https://www.census.gov/programs-surveys/popest.html
)


Primary uses:

- Federal funding distribution

- Survey control totals

Estimates smallest geography = County and Place

#### Projections

Biennual population projections by Age/Sex/Race/Ethnicity

Based on current trends in fertility, mortality and net international migration

www.census.gov/programs-surveys/popproj.html



Projections smallest geography = Nation

### *Planning Database*

Select demographic and socio-economic variables from ACS + operational metrics such as response rates

Planning database smallest geography = Block Group

### *Census Microdata API*

Allows for custom tabulations based on a sample of responses

All other census datasets and APIs are aggregated data i.e. summaries and cross-tabulations 

Census microdata smallest geography = Public Use Microdata Areas (PUMA) - at least 100,000 people contained in one state

### *Health Insurance Statistics*

From various sample surveys

- American Community Survey (ACS)

- Current Population Survey (CPS)

CPS smallest geography = state

- Survey of Income and Program Participation (SIPP)
Longitudinal study - same respondents up to four years

SIPP smallest geography is region 

### *Small Area Health Insurance Estimates (SAHIE)*

2006-2017 only

Modeling that combines survey data with administrative records

SAHIE smallest geography = county

### *Poverty Statistics*

From various sample surveys:

- American Community Survey (ACS)

- Current Population Survey (CPS)

- Small Area Income and Poverty Estimates (SAIPE)

Official vs Supplemental Poverty Measures:

www.census.gov/newsroom/blogs/random-samplings/2021/09/difference-between-supplemental-and-official-poverty-measures.html

#### *International Database*

Demographic data for over 2000 countries since 1960

## **Economic data APIs**

### *Economic Census*

Data include:

- Establishments

- Employees

- Payroll

- Sales and Receipts 

Data gathered in years ending in 2 and 7

Economic Census smallest geography = County

### *Sample Surveys*

- Annual Business Survey

- Annual Survey of Manufactures

- Annual Survey of Entrepreneurs

- Survey of Business Owners

- Economic Indicators

- International Trade Program

- Longitudinal Employer-Household Dynamics (LEHD)

## **Public Sector Statistics - Government of Surveys**

New Mexico e.g.

- 138 general purpose governments (33 counties + 105 municipal)

- 875 special purpose governments such as School Districts, Water Authorities, Acequias, etc. 

## IPUMS - Integrated Public Use Microdata Series

Great alternative sources of census data


World's largest population database

API https://developer.ipums.org/docs/apiprogram/

# **Census Geography**

Census Geography Division - www.census.gov/programs-surveys/geography/geographies.html

## Census Hierarchy

https://www2.census.gov/geo/pdfs/reference/geodiagram.pdf

Political geography (defined by statute) vs. Statistical geography (defined by Census Bureau with community input)

Geographies evolve through annexations, incorporation, redistricting, decennial updates. Beware if doing time series analysis 

## Shapefiles and Geodatabases

Shapefiles: https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-line-file.html

Geodatabases:https://www.census.gov/geographies/mapping-files/time-series/geo/tiger-geodatabase-file.html

## Geocoding 

Identifying x, y coordinates from an address (or addresses from x,y)

Census geocoding service - https://geocoding.geo.census.gov/

Alternative geocoding services:

https://geoservices.tamu.edu/Services/Geocode/OtherGeocoders/	

https://www.geocod.io/compare/

## Census TIGERweb GeoServices REST API

https://www.census.gov/data/developers/data-sets/TIGERweb-map-service.html

## Zip Codes and ZCTAS

## Also see
National Historic Geographic Information System

https://www.nhgis.org/

Affilatied with IPUMS

API - https://developer.ipums.org/docs/apiprogram/

# data.census.gov

Demo on income and educational attainment

https://www.census.gov/newsroom/press-releases/2022/educational-attainment.html

https://www.census.gov/library/visualizations/2022/comm/a-higher-degree.html

