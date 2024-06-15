# End-to-End Deployment of Machine Learning Models using Google Cloud Platform, Flask, Docker and Kubernetes.

![ml_deploy](https://github.com/MNCEDISIMNCWABE/loan-approval-prediction-GCP/assets/67195600/cfdd666c-af1a-4795-84af-23659ac4b19c)


### An Easy-to-Follow Guide to Train and Deploy a Loan Approval Prediction Machine Learning Model on GCP, Docker and Kubernetes.

In this repo we explore how we can build a comprehensive end-to-end machine learning model to predict loan approvals and deploy the model using GCP (Google Cloud Platform), Docker, Kubernetes and Flask. In order to correctly identify people who have a high chance of having their loans approved, this model will be trained on applicant's financial historical data such as their income, credit rating, employment status, and other relevant attributes. The model can be used to help financial institutions to evaluate loan candidates and decide which loans to approve or reject. 

# Steps to deploy the model on GCP 

#### Prerequisites
- Google Cloud Platform account
  - Create a google cloud account. Google cloud offers a $300 credit that you can use to access all GCP features for 3 months. Install the Google could SDK from [here](https://cloud.google.com/sdk/docs/install).
- Docker: Install from [here](https://docs.docker.com/engine/install/).
- kubectl installed:
  - The Kubernetes command-line tool, kubectl, allows you to run commands against Kubernetes clusters. You can use kubectl to deploy applications, inspect and manage cluster resources, and view logs. View more [here](https://kubernetes.io/docs/tasks/tools/).
- GitHub repository with your project

## Steps to Deploy the Model on GCP
### 1. Clone the Repository
- First, clone your GitHub repository using the google cloud shell terminal:
- Once you have your your google cloud account up and running, activate the cloud shell terminal as shown in the image below:
  
![image](https://github.com/MNCEDISIMNCWABE/loan-approval-prediction-GCP/assets/67195600/c56155a1-4231-4478-b5af-482d9cc63e54)


#### Clone the Github repositry where you saved your model and deployment files using the command below
   - git clone https://github.com/your-username/loan-approval-prediction.git

  - Check the files cloned using this command: ls 

<img width="1418" alt="image" src="https://github.com/MNCEDISIMNCWABE/loan-approval-prediction-GCP/assets/67195600/2608e8eb-e54d-4e21-b29b-8acd09cb0424">


### 2: Build the Docker Image
#### Navigate to your project directory
- cd loan-approval-prediction
##### Build the docker image
- docker build -t gcr.io/YOUR-GCP-PROJECT-ID/loan-approval:v1 .

### 3: Push the Docker Image to Google Container Registry / Artifact Registry
##### First Authenticate Docker with Google Cloud
- gcloud auth configure-docker
  
##### Push the Docker image to Google Container Registry:
- docker push gcr.io/YOUR-GCP-PROJECT-ID/loan-approval:v1

  <img width="1418" alt="image" src="https://github.com/MNCEDISIMNCWABE/loan-approval-prediction-GCP/assets/67195600/ae594947-35a3-4554-8850-2738e8e08a57">

### 4: Create a Kubernetes Cluster
- gcloud container clusters create loan-approval-cluster --num-nodes=2

#### Get authentication credentials for the cluster
- gcloud container clusters get-credentials loan-approval-cluster

### 5: Deploy the Application to Kubernetes
Use the command below to deploy the appication to kubernetes
- kubectl apply -f deployment.yaml

### 6: Expose the Deployment as a Service
- kubectl apply -f service.yaml

### 7: Verify the Deployment
- kubectl get services

From here you should see an external IP address assigned to your loan-approval-service. Access your application at this IP address by typing it on your web browser. The external IP address can be shared with end-users to interact with and use the model to predict the loan application outcome for new applicants.

<img width="1418" alt="image" src="https://github.com/MNCEDISIMNCWABE/loan-approval-prediction-GCP/assets/67195600/9559e0f3-fd97-42c2-b41f-5303e894ac4d">

<img width="1402" alt="image" src="https://github.com/MNCEDISIMNCWABE/loan-approval-prediction-GCP/assets/67195600/694fb140-fa54-4d00-a8a5-2db58d582048">












