# 5.3 Image Data Pipeline Project

In this lesson, we will build data pipeline using AWS Step Functions, with AWS Fargate and AWS Lambda using serverless framework.

Used services: AWS Step Functions, AWS Fargate, AWS Lambda, AWS ECR

Execution graph:

<img width="531" alt="Screen Shot 2020-04-02 at 9 04 12 PM" src="https://user-images.githubusercontent.com/3318397/78323131-6d57c400-7560-11ea-8f97-964b1c036d8d.png">


## Steps

1. Go to `container` folder
2. Run `$(aws ecr get-login --no-include-email --region us-east-1)`
3. Run `aws ecr create-repository --repository-name datapipeline-fargate`
4. Run `docker build -t datapipeline-fargate .`
5. Run `docker tag datapipeline-fargate:latest <accountId>.dkr.ecr.us-east-1.amazonaws.com/datapipeline-fargate:latest` and replace `<accountId>` with your account id
6. Go to lesson folder
7. Create custom bucket using command `aws s3api create-bucket --bucket <bucket_name>`
8. Replace `S3BucketName` parameter in `serverless.yml` with your bucket name
9. Run `serverless deploy`
10. Run `curl <url>` where `<url>` is output from the previous step
11. Check execution graph on AWS Step Function console https://console.aws.amazon.com/states/home and bucket on S3 console https://s3.console.aws.amazon.com/s3/home