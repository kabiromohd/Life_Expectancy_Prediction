# LIFE EXPECTANCY PREDICTION
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
The Global Health Observatory (GHO) data repository under World Health Organization (WHO) keeps track of the health status as well as many other related factors for all countries. 

The datasets are made available to public for the purpose of health data analysis. The dataset is related to life expectancy, health factors for 193 countries has been collected from the same WHO data repository website and its corresponding economic data was collected from United Nation website. 

Among all categories of health-related factors only those critical factors were chosen which are more representative.

 [Dataset Link](https://www.kaggle.com/competitions/oht-ibadan-bootcamp-capstone-open-house/data)

The aim of this project is to build a model that can predict life expectancy given certain criteria.

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
  - Catergorical variables were encoded using the DictVectorizer library.
  - trained best model using the random forest regressor after ascertaining it to produce the best model with hyper parameters via *Train_model.py* script.
    
### Model deployment to web services
- flask was used for web deployment via *predict.py* script.
- Setup Pipenv Virtual Environment, by opening Cli on your system and run
  
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
- Get copies of the project and dependencies, you can clone the repo.
- The files should be placed in the virtual environment folder after being cloned via below command.

```
git clone https://github.com/kabiromohd/Life_Expectancy_Prediction.git
```

### Deploy model locally with Docker
You can deploy the model on Docker locally by following these steps.
To do so, you need to have Docker installed on your machine, then you build the image with the following command:

NOTE: Docker must be running before your run the following commands on Cli:

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

if all the above command run successfully, open another Cli and run below command to see prediction via local Docker deployment:

```
pipenv shell
```

Note: *predict-test.py* has already prepared with data point to test the model deployed locally on docker

Run below command. 

```
python predict-test.py
```

This ends the local deployment to docker.

### Deploy docker image to the cloud
For cloud deployment [Render](render.com) was used.

- Create a Docker Account 
- Creating an account on Docker enables setting up of Docker repository which can be used to push the docker image created locally.
- The docker repo is create on the docker web login
- Docker repo created for the purpose of this project is *"kabiromohd/data_science"*
- Docker repository was created to enable getting URL for the midtermproj image.
 
![Docker Repository ScreenShot](https://github.com/kabiromohd/Midtermproject/assets/121871052/da00eda3-1bdd-43ef-9921-0d0ff1dd7d35)

To deploy the docker image to cloud, open a Cli and run the following commands:

```
pipenv shell
```

```
docker build -t kabiromohd/data_science:midtermproj .
```

Push the docker image created above to the repo created with the following command:

```
docker push kabiromohd/data_science:midtermproj
```

- copy the docker image URL on to render from the docker repo
  
![Render ScreenShot](https://github.com/kabiromohd/Midtermproject/assets/121871052/9766ac9a-d7e3-4929-b3df-b53e4e2d6d59)

- deploy docker image to render cloud service.
  
![Render Deployment Screenshot](https://github.com/kabiromohd/Midtermproject/assets/121871052/1a77dce5-a7e8-404f-8443-a92d0d376907)
  
### To interact with the docker image deployed to cloud via render
- copy the render deployment link and place in the *predict-test_render.py* script as "host".
- *predict-test_render.py* has already prepared data point to be used to test the model deployed to cloud.
- for this project, the deployment link has already been provided in the .py script. It can be executed as illustrated below:
  
- open a Cli and run the following: 

  ```
  pipenv shell
  ```

  followed by:
  
  ```
  python predict-test_render.py
  ```

You see the prediction via the cloud service.
See illustration video below

https://github.com/kabiromohd/Life_Expectancy_Prediction/assets/121871052/eaae542b-a5e4-404f-8a19-9d9a4c787539



