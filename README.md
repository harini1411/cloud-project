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


Here's the revised setup instructions based on using the **AWS Management Console** for deploying your **Cloud-Based BMI Calculator with API Integration and Scalable Data Management on AWS**.

---

Procedure
   ```

### **1. Set Up AWS Lambda Function**
1. **Login to AWS Management Console** and navigate to the **Lambda** service.

2. Click on **Create function**.

   - Choose **Author from scratch**.

   - Name the function (e.g., `BMI_Calculator_Function`).

   - Choose **Python** as the runtime.

   - Set **Execution Role** to create a new role with basic Lambda permissions.

3. Once the function is created, in the function editor, upload the provided `bmi_calculator.py` code file by:

   - Clicking on the **Code** tab.

   - Deleting the default code and pasting your BMI calculation logic or uploading the `.zip` file containing the script.

4. Set the **timeout** to a reasonable limit (e.g., 10 seconds).

5. Click **Deploy** to save the function.

2. Set Up API Gateway

1. In the AWS Management Console, navigate to **API Gateway** and click on Create API\

   - Select **REST API**.

   - Choose **New API** and give it a name (e.g., `BMI_API`).

2. Click **Create Resource** and define an endpoint (e.g., `/calculate-bmi`).

3. Under the `/calculate-bmi` resource, create a **Method**:

   - Choose `POST` and click the checkmark.

   - Set the integration type to **Lambda Function**.

   - Select the Lambda function created earlier (`BMI_Calculator_Function`).

4. After saving, click **Actions** > **Deploy API**.

   - Select a deployment stage (e.g., `prod`).

5. Once deployed, copy the **Invoke URL**—this is the endpoint you’ll use to test the API.


### **3. Create DynamoDB Table

1. Go to the **DynamoDB** service in the AWS Console.

2. Click on **Create table**.

   - Name the table (e.g., `BMI_Calculations`).

   - Set a Primary Key (e.g., `UserID` as a string).

3. Define additional attributes such as `height`, `weight`, and `bmi`.

4. Leave other options at default and click Create Table.

4. Connect Lambda to DynamoDB

1. Go back to your Lambda function in the AWS Console.

2. Under the Permissions tab, click the role name to open the **IAM Console**.

3. Add a DynamoDB Full Access policy to the Lambda role so that the function can read/write to the DynamoDB table.

4. Modify your Lambda function to use the boto3 library to write data to DynamoDB after calculating the BMI. Ensure the table name is referenced correctly.

5. Testing the API

1. Use a tool like Postman or curl to send a `POST` request to your API Gateway's Invoke URL.

   - Example request:

     ```http
     POST {API-Invoke-URL}/calculate-bmi
     Content-Type: application/json

     {
       "height": 170,
       "weight": 65
     }

     ```
2. The API will trigger your Lambda function, calculate the BMI, and store the results in DynamoDB. You should receive a response containing the calculated BMI.

6. Deploy Front-End with Amplify (Optional)

1. Navigate to AWS Amplify in the Console.

2. Click **Get Started** under Deploy.

3. Connect your GitHub repository and choose the branch to deploy.

4. Amplify will automatically build and deploy the front-end application to a hosted URL.

7. Monitor and Maintain

1. You can monitor the execution of Lambda via **AWS CloudWatch** to view logs, trace requests, and performance metrics.

2. Use **API Gateway Logs** to view traffic and performance insights for your REST API.

3. Regularly check the **DynamoDB Table** for the calculated BMI entries.



 
