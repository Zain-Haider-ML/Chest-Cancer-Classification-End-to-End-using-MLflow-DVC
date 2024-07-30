# Chest-Cancer-Classification-End-to-End-using-MLflow-DVC


##Workflows

Update config.yaml
Update secrets.yaml [Optional]
Update params.yaml
Update the entity
Update the configuration manager in src config
Update the components
Update the pipeline
Update the main.py
Update the dvc.yaml



# AZURE-CICD-Deployment-with-Github-Actions

## Save pass:

C8Us2DnLvBeXCP6axRXWHJC4eSwpFtnDbdPC0byXyH+ACRDvK8i3


## Run from terminal:

docker build -t chestcancerclassificationapp.azurecr.io/mltest:latest .

docker login chestcancerclassificationapp.azurecr.io

docker push chestcancerclassificationapp.azurecr.io/mltest:latest


## Deployment Steps:

1. Build the Docker image of the Source Code
2. Push the Docker image to Container Registry
3. Launch the Web App Server in Azure 
4. Pull the Docker image from the container registry to Web App server and run 