                  Cloud-Based BMI Calculator with API Integration and Scalable Data Management on AWS
Project Overview:
This project implements a fully cloud-native and serverless Body Mass Index (BMI) calculator using AWS. The system allows users to input their height and weight, performs real-time BMI calculations using a Lambda function, and stores the results in DynamoDB for scalable data management. By leveraging API Gateway for request handling and Amplify for front-end hosting, this solution ensures a highly available and resilient infrastructure that requires minimal operational maintenance.

Key Features
1. Serverless BMI Calculation
Powered by AWS Lambda, the BMI computation logic is managed without the need for server infrastructure. Lambda scales automatically with incoming requests, ensuring high availability.

3. API-Driven Architecture
AWS API Gateway serves as the RESTful API interface, enabling users to submit height and weight data via HTTP requests. It provides a secure, scalable endpoint that integrates seamlessly with AWS Lambda.

5. Persistent Data Storage in DynamoDB
Amazon DynamoDB is used to store user input and BMI results in a NoSQL format. DynamoDB is fully managed, scalable, and optimized for low-latency performance, ensuring that large-scale data sets are handled efficiently.

7. Front-End Deployment with AWS Amplify
The user interface, where users input their height and weight, is hosted on AWS Amplify, a service that provides scalable hosting for static web applications and continuous integration/deployment workflows.

9. Secure Role-Based Access Control (RBAC)
AWS IAM (Identity and Access Management) ensures that the Lambda function has the appropriate roles and permissions for interacting with DynamoDB. The IAM policies follow the principle of least privilege for enhanced security.

11. Real-Time API Responses
The system delivers real-time responses to user inputs, instantly computing and returning the BMI value while persisting the result in DynamoDB for future reference.

12. Scalable and Managed Infrastructure
By utilizing AWS-managed services like Lambda, API Gateway, and DynamoDB, this project is designed to scale automatically based on demand while reducing operational overhead.

Architecture
Components:
AWS Amplify: Hosts the front-end interface where users provide height and weight.
AWS API Gateway: Exposes a RESTful API to receive user inputs and route them to Lambda.
AWS Lambda: Executes the BMI calculation logic.
Amazon DynamoDB: Stores the user inputs and BMI calculation results for future retrieval.
AWS IAM: Manages permissions and roles for secure access between AWS services.
Architecture Diagram


![architecure diagram](https://github.com/user-attachments/assets/b8f0f3d7-db72-4f5b-9739-c6132a66e1b3)
 
