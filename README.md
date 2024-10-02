                   AWS BMI Calculator – Serverless Architecture for Scalable Health Data Computation
Project Overview
This project implements a fully serverless, cloud-native Body Mass Index (BMI) calculator using AWS services. The system accepts user inputs (height and weight), performs real-time BMI computations, and persists the calculated results in an AWS DynamoDB table for further analysis and retrieval. It leverages AWS Lambda as the compute engine, with API Gateway handling HTTP requests and Amplify for front-end hosting. This setup allows seamless scalability, minimal maintenance, and cost-efficient operation due to the serverless nature of AWS Lambda.

Key Features
1. Serverless BMI Computation
AWS Lambda provides the computational backend without requiring server management. The Lambda function calculates the BMI based on user-provided height and weight and can scale dynamically to meet demand.
2. RESTful API Integration
An AWS API Gateway is deployed to expose the Lambda function as a REST API, allowing users to send HTTP requests for BMI computation. The API ensures stateless interaction with the backend, improving scalability and fault tolerance.
3. NoSQL Data Persistence
Amazon DynamoDB, a fully managed NoSQL database service, stores computed BMI results alongside the user’s height and weight. DynamoDB’s auto-scaling and low-latency performance ensure that large volumes of data can be handled efficiently.
4. Highly Scalable Front-End Hosting
The front-end interface is deployed using AWS Amplify, which provides fast and secure hosting of static web applications. Amplify simplifies continuous integration and deployment, automatically reflecting updates made to the code repository.
5. Role-Based Access Control
AWS IAM (Identity and Access Management) is configured to provide secure role-based access control (RBAC) for different AWS services. The Lambda function has precise write permissions to DynamoDB, governed by tightly scoped IAM policies, ensuring a least-privilege security model.
6. Event-Driven Architecture
The system operates on an event-driven architecture, where user-triggered HTTP requests via API Gateway invoke the BMI calculation Lambda function. Results are persisted asynchronously in DynamoDB, supporting a highly decoupled and reactive system.
7. Real-Time Feedback
The front-end fetches and displays the BMI calculation result immediately after the computation, enhancing the user experience. The API integration enables fast response times and immediate storage of results for future analysis.
8. Fully Managed Infrastructure
AWS manages all underlying infrastructure components, ensuring high availability, reliability, and scalability without requiring manual intervention. AWS Lambda and DynamoDB both come with built-in fault tolerance, automatic scaling, and monitoring.
High-Level Architecture
The following components constitute the architecture:

AWS Amplify: Hosts the front-end web interface where users submit their height and weight. The interface communicates with the backend via API Gateway.
AWS API Gateway: Exposes a RESTful API for BMI calculations. It routes user input data (height, weight) to the Lambda function for processing.
AWS Lambda: The compute layer that handles the BMI calculation logic. The Python function runs serverless and returns the calculated BMI.
Amazon DynamoDB: Stores user input (height, weight) along with the computed BMI. This NoSQL database ensures low-latency data storage and retrieval.
AWS IAM: Manages role-based permissions and security policies to restrict access to critical AWS resources.

![architecure diagram](https://github.com/user-attachments/assets/b8f0f3d7-db72-4f5b-9739-c6132a66e1b3)
 
