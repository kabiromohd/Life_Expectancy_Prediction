# Mid-Term Project
## DatatalksClub ML Zoomcamp Mid term project
## Objectives of Midterm Project:
- Find a dataset
- Explore and prepare the data
- Train the best model
- Export the notebook into a script
- Put model into a web service
- Deploy model locally with Docker
- Deploy to the cloud
  
### Find a Dataset
The Global Health Observatory (GHO) data repository under World Health Organization (WHO) keeps track of the health status as well as many other related factors for all countries. The datasets are made available to public for the purpose of health data analysis. The dataset related to life expectancy, health factors for 193 countries has been collected from the same WHO data repository website and its corresponding economic data was collected from United Nation website. Among all categories of health-related factors only those critical factors were chosen which are more representative.
Dataset [Link](https://www.kaggle.com/competitions/oht-ibadan-bootcamp-capstone-open-house/data)

### Explore and prepare the data
Exploration of the data was done via *Life_expectancy_EDA.ipynb* jupyter notebook file
- Explore data
  - Checked the Data Structure and columns
  - Checked the numbers of features and observations in the data
  - Checked the inconsistency in column names and corrected.
- prepare data
  - Checked for missing values (filled with 0)
  - Checked for outliers
  - Checked for Duplicates
- train data
  - Catergorical variables were encoded using the DictVectorizer
  - trained best model using the random forest regressor after ascertaining it to produce the best model with obtained parameters via *Train_model.py* script using the hyper parameter gotten while turning.
    
### Model deployment to web services
- Model Web services via flask via *predict.py* script, see file in github folder for project
- Setup Pipenv Virtual Environment, by opening cli on your system and run
  
```
pip install pipenv
```

- install the following:
  - Gunicorn
  - flask
  - numpy
  - scikit-learn version "1.3.0"
  - requests
    
```
pipenv install gunicorn flask numpy scikit-learn==1.3.0 requests
```
- Copy the following files from the github repo to created virtual environment
  - predict.py
  - Dockerfile
  - pipfile.lock
  - pipfile
  - predict-test.py
  - predict-test_render.py
  - model_dv.pkl
  - model_rf_1.pkl
  
### Deploy model locally with Docker
You can run the project with Docker. To do so, you need to have Docker installed on your machine, then you build the image with the following command:
NOTE: Docker must be running before your run the following commands:

```
pipenv shell
```

Create docker image by running the following:

```
docker build -t midtermproj .
```

followed by this docker command which runs the docker image created

```
docker run -it --rm -p 9690:9690 midtermproj
```
![Docker Deployment Screenshot](https://github.com/kabiromohd/Midtermproject/assets/121871052/05d1babe-0150-4ec3-b082-be8ee14a9b7a)

if all the above command run successfully, open another cli and run below command to see prediction via local Docker deployment:

```
pipenv shell
```

Run below command. *predict-test.py* has already prepared data point to test the model:

```
python predict-test.py
```

This ends the local deployment to docker.

### Deploy docker image to the cloud
For cloud deployment [Render](render.com) was used.

- Create a Render Account.
- Docker repository was created to enable getting URL for the midtermproj image.
  
![Docker Repository ScreenShot](https://github.com/kabiromohd/Midtermproject/assets/121871052/da00eda3-1bdd-43ef-9921-0d0ff1dd7d35)

- copy the docker image URL on to render.
  
![Render ScreenShot](https://github.com/kabiromohd/Midtermproject/assets/121871052/9766ac9a-d7e3-4929-b3df-b53e4e2d6d59)

- deploy docker image to render cloud service
  
![Render Deployment Screenshot](https://github.com/kabiromohd/Midtermproject/assets/121871052/1a77dce5-a7e8-404f-8443-a92d0d376907)
  
### To use the docker image deployed to cloud via render
- copy the render deployment link and place in the *predict.test_render.py* script as "host"
- run the following:

  ```
  pipenv shell
  ```

  followed by:
  
  ```
  python predict-test_render.py
  ```

  You see the prediction via the cloud service
