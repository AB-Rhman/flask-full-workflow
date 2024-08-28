
# Flask Full Workflow

This project showcases how to apply essential DevOps practices to turn a simple "Hello World" Flask web application into a live production-ready state. It demonstrates the use of CI/CD pipelines for both code and infrastructure deployment using GitHub Actions.

## Project Overview

![workflow](images\workflow.jpg)

The primary goal of this project is to automate the deployment and management of a Flask application on an AWS EKS cluster using best practices. The project is divided into two main components:

1. **CI/CD Pipeline for Code Deployment:**
   - Automatically triggers on code changes.
   - Builds a Docker image.
   - Runs unit tests.
   - Deploys the application to the EKS cluster if tests pass.
   - Sends notifications to a Discord channel if tests fail.

2. **Infrastructure Deployment Pipeline:**
   - Provisions an AWS EKS cluster using Terraform.
   - Installs NGINX Ingress, Prometheus, Grafana, and Loki on the EKS cluster using Helm.
   - Uses HashiCorp Cloud for remote state management.

3. Monitoring and Logging

   - **Prometheus**: Collects real-time metrics.
   
   - **Grafana**: Visualizes the metrics collected by Prometheus and Loki.
   
   - **Loki**: Aggregates and centralizes logs from the application and Kubernetes cluster. 
## Features

- **Automated Infrastructure Provisioning:** The pipeline uses Terraform to provision AWS resources and set up an EKS cluster with the necessary tools and services.
- **CI/CD Pipelines:** The code is built, tested, and deployed using GitHub Actions.
- **Monitoring and Logging:** Prometheus and Grafana are set up for monitoring, while Loki is configured for logging.
- **Discord Notifications:** The pipeline is integrated with Discord to send alerts and notifications.

## Prerequisites

Before you begin, ensure you have the following tools installed and configured on your local machine:

- [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
- [kubectl](https://kubernetes.io/docs/tasks/tools/)
- [Helm](https://helm.sh/docs/intro/install/)
- [Terraform](https://developer.hashicorp.com/terraform/downloads)
- [Docker](https://docs.docker.com/get-docker/)

Additionally, ensure you have the following environment variables configured in your GitHub repository secrets:

- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `DISCORD_WEBHOOK_URL`
- `TF_API_TOKEN`
- `DOCKER_USERNAME`
- `DOCKER_PASSWORD`

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AB-Rhman/flask-full-workflow.git
   cd flask-full-workflow
   ```

2. Set up your AWS CLI and configure it:
   ```bash
   aws configure
   ```

3. Ensure all required dependencies are installed by checking the codebase.

## Usage Instructions

1. **Run the Infrastructure Pipeline:**
   - Trigger the GitHub Actions pipeline to provision the EKS cluster and install NGINX Ingress, Prometheus, Grafana, and Loki.

2. **Connect to Your EKS Cluster:**
   - After the infrastructure is up, connect your local machine to the EKS cluster:
     ```bash
     aws eks update-kubeconfig --region us-east-1 --name demo-eks
     ```

3. **Access Grafana:**
   - Before deploying your application, connect to Grafana to configure Loki as a data source:
     ```bash
     kubectl port-forward --namespace monitoring service/prometheus-grafana 3000:80
     ```
   - Open Grafana in your browser at `http://localhost:3000` and log in.

   - Some dashboards form Grafana

   ![node](images\node.png)

   ![kubelet](images\kubelet.png)

4. **Deploy Your Application:**
   - Once the infrastructure is up and configured, trigger the pipeline to deploy your application to the EKS cluster.

## Technologies Used

- **Flask**: The web framework used to develop the application.
- **GitHub Actions**: CI/CD pipelines.
- **Terraform**: Infrastructure as code for provisioning AWS resources.
- **Helm**: Kubernetes package manager for deploying Prometheus, Grafana, and Loki.
- **Prometheus**: Monitoring system.
- **Grafana**: Dashboard for visualizing metrics and logs.
- **Loki**: Log aggregation system.
- **AWS EKS**: Managed Kubernetes service.
- **HashiCorp Cloud**: Remote state management for Terraform.
- **NGINX Ingress**: Ingress controller for Kubernetes.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements, bug fixes, or additional features.

## Contact

For any inquiries or issues, feel free to open an issue on GitHub or contact the project maintainer.
