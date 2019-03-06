## a serverless data pipeline with AWS S3, Lamba and DynamoDB

https://medium.com/the-apps-team/build-a-serverless-data-pipeline-with-aws-s3-lamba-and-dynamodb-5ecb8c3ed23e

This is example of a serverless data pipeline using AWS Lambda Functions, S3 and DynamoDB!

### Prerequisites

- Serverless framework
- Python3.6
- Pandas
- docker

### How this pipeline works

On a daily basis, an external data source exports data of the pervious day in csv format to an S3 bucket. S3 event triggers an AWS Lambda Functions that do ETL process and save the data to DynamoDB.

### Deploying your service

```sls deploy```

### How to test

```$ aws s3 cp sample.csv s3://dev.document.files```
