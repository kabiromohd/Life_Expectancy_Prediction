# Midtermproject
## DatatalksClub ML Zoomcamp Mid term project
## Objectives of Midterm Project:
- Find a dataset
- Explore and prepare the data
- Train the best model
- Export the notebook into a script
- Put your model into a web service
- Deploy it locally with Docker
- Deploy to the cloud
### Find a Dataset
The Global Health Observatory (GHO) data repository under World Health Organization (WHO) keeps track of the health status as well as many other related factors for all countries. The datasets are made available to public for the purpose of health data analysis. The dataset related to life expectancy, health factors for 193 countries has been collected from the same WHO data repository website and its corresponding economic data was collected from United Nation website. Among all categories of health-related factors only those critical factors were chosen which are more representative.
Dataset [Link](https://www.kaggle.com/competitions/oht-ibadan-bootcamp-capstone-open-house/data)
### Explore and prepare the data
Exploration of the data was done via train.py script
- Explore data
  - Checked the Data Structure and columns
  - Checked the numbers of features and observation in the data
  - Checked the inconsistency in column names and corrected.
- prepare data
  - Checked for missing values (filled with 0)
  - Checked for outliers
  - Checked for Duplicates
- train data
  - trained model using the random forest regressor after ascertaining it to produce the best model
  - Catergorical variables were encoded using the DictVectorizer
### Put your model into a web service
- model was put in a flask webservice via the predict.py script, see file in github folder for project
  setup are pipenv Virtual Environment, by opening cli on your system and run
  
```
pip install pipenv
```

  and then install the following:
  - Gunicorn
  - flask
  - numpy
  - scikit-learn version "1.3.0"
  - requests
    
```
  pipenv install gunicorn flask numpy scikit-learn="1.3.0" requests
``` 
### Deploy it locally with Docker
You can run the project with Docker. To do so, you need to have Docker installed on your machine. Then, you need to build the image with the following command:

```
docker build -t midtermproj .
```

followed by this docker command

```
docker run -it --rm -p 9690:9690 midtermproj
```

