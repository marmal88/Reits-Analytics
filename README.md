# REITs Analytics

Real Estate Investment Trusts are a popular investment choice amongst the retail investors in Singapore. Ascendas Reit (SGX: A17U) is the oldest listed reit on the SGX.

Ascendas Reit is unique as an industrial reit, as it has an extensive range of industrial properties (business parks to flatted factories) both within Singapore and across the world.

In this project, I would like to showcase the 




---
## Table of Contents
- [REITs Analytics](#reits-analytics)
  - [Table of Contents](#table-of-contents)
  - [1. General Instructions](#1-general-instructions)
    - [1.1 API keys](#11-api-keys)
    - [1.2 Folder Structure](#12-folder-structure)
  - [2. Data Ingestion Pipeline](#2-data-ingestion-pipeline)
  - [3. Navigation](#3-navigation)


---
## 1. General Instructions

Create virtual environment and download necessary packages using:

```bash
conda create --name reits-analytics python=3.11
conda activate reit-analytics
pip install -r requirements.txt
```

To view dashboard, please follow the instructions under [API Keys](#api-keys) before keying in the following commands:

```bash
python -m src.main
```
---
### 1.1 API keys

This project makes use of API's from google and mapbox

Please see the documentation to obtain the correct API keys.
- [Mapbox api](https://docs.mapbox.com/help/getting-started/access-tokens/)
- [Google developer api](https://support.google.com/googleapi/answer/6158862?hl=en)

Please note that you should never expose your API key online. 
Make use of .env and .gitignore to hide your keys. 

Please also read this article if you are new to API keys:  
- [Best practice for keeping secrets](https://jonathansoma.com/lede/foundations-2019/classes/apis/keeping-api-keys-secret/)
  
Both API's used in this projects have a rate use limit and the credit card component is to prevent abuse of the API endpoint.


---
### 1.2 Folder Structure

This is the folder structure for this project: 

```bash
.
├── data
│   ├── Ascendas-Reit-Annual-Report-2021.pdf
│   └── output.csv
├── README.md
├── # place .env file here
├── requirements.txt
└── src
    ├── app_func
    │   ├── api.py
    │   ├── dbs_fx.py
    │   └── pdf.py
    ├── main.py
    └── test.ipynb
```
---
## 2. Data Ingestion Pipeline

The baseline data is taken from the Ascendas Reit's Annual Report 2021. 
With data augmented using:
- DBS's forex website [link](https://www.dbs.com/in/treasures/rates-online/foreign-currency-foreign-exchange.page)
- Google maps for longitude and lattitude data
- Mapbox for stylistic changes to plots



```mermaid
graph LR;
 A([PDF Scraper</br>Scrap annual report for information])-->D
 B([Web Scraper</br>Scrap website for exchange])-->D
 D([Preliminary dataframe])-->F
 E([Google API</br>Get Longitude and Lattitude data])-->F
 F([Plotting dataframe])-->G
 G([Frontend</br>Plotly.js])

 H([Mapbox API</br>Stylistic changes to plot])-->G
```
 
---
## 3. Navigation

![Image](/home/oem/Documents/coding/personal/Reits-Analytics/assets/geojson.png "Sketchup of graph plot")