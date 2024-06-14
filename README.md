# End-to-End Deployment of Machine Learning Models on Google Cloud Platform: From Development to Production with Flask, Docker, and Kubernetes.

### An Easy-to-Follow Guide to Train and Deploy a Loan Approval Prediction Machine Learning Model on GCP, Docker and Kubernetes.

In this repo we explore how we can build a comprehensive machine learning model to predict loan approvals and deploy the model using GCP (Google Cloud Platform), Docker, Kubernetes and Flask. In order to correctly identify people who have a high chance of having their loans approved, this model will be trained on applicant's financial historical data. The model can be used to help financial institutions to evaluate loan candidates and decide which loans to approve or reject. 

## Steps to deplot the model on GCP 

#### Prerequisites
- Google Cloud Platform account
  - Create a google cloud account. Google cloud offers a $300 credit that you can use to access all GCP features for 3 months. Install the Google could SDK from [here](https://cloud.google.com/sdk/docs/install).
- Docker: Install from [here](https://docs.docker.com/engine/install/).
- kubectl installed:
  - The Kubernetes command-line tool, kubectl, allows you to run commands against Kubernetes clusters. You can use kubectl to deploy applications, inspect and manage cluster resources, and view logs. View more [here](https://kubernetes.io/docs/tasks/tools/).
- GitHub repository with your project

### Steps to Deploy the Model on GCP
#### 1. Clone the Repository
- First, clone your GitHub repository to a google cloud shell terminal:
- Once you have your your google cloud account up and running, activate the cloud shell terminal as shown in the image below:
  
![image](https://github.com/MNCEDISIMNCWABE/loan-approval-prediction-GCP/assets/67195600/c56155a1-4231-4478-b5af-482d9cc63e54)


#### 2. Clone the Github repositry where you saved your model and deployment files using the command below
   - git clone https://github.com/your-username/loan-approval-prediction.git
#### 3: Build the Docker Image

##### Navigate to your project directory
- cd loan-approval-prediction
###### Build the docker image
- docker build -t gcr.io/YOUR-GCP-PROJECT-ID/loan-approval:v1 .

#### 3: Push the Docker Image to Google Container Registry
##### First Authenticate Docker with Google Cloud
- gcloud auth configure-docker





