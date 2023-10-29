#!/usr/bin/env python
# coding: utf-8

import requests

host = "life-expectancy-z1bf.onrender.com"

url = f'http://{host}/predict'

client = {"year": 2004,
         "status": "Developing",
         "adult_mortality": 214.0,
         "infant_deaths": 0,
         "alcohol": 0.48,
         "percentage_expenditure": 10.6242741,
         "hepatitis_b": 67.0,
         "measles": 0,
         "bmi": 71.4,
         "under-five_deaths": 0,
         "polio": 61.0,
         "total_expenditure": 1.39,
         "diphtheria": 62.0,
         "hiv/aids": 0.1,
         "gdp": 113.6286,
         "population": 9542.0,
         "thinness__1-19_years": 0.2,
         "thinness_5-9_years": 0.2,
         "income_composition_of_resources": 0.0,
         "schooling": 12.4
         }

response = requests.post(url, json=client).json()
print(response)
