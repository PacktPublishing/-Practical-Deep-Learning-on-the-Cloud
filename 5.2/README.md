# 5.2 Deploying AWS Step Functions with AWS Fargate Using Serverless Framework

In this lesson, we will learn how to deploy a custom processing pipeline using AWS Step Functions, along with AWS Fargate and AWS Lambda.

Used services: AWS Step Functions, AWS Fargate, AWS Lambda, AWS ECR

Execution graph:

<img width="516" alt="Screen Shot 2020-04-02 at 8 57 00 PM" src="https://user-images.githubusercontent.com/3318397/78322763-30d79880-755f-11ea-987b-212b30f5486e.png">


## Steps

1. Go to `container` folder
2. Run `$(aws ecr get-login --no-include-email --region us-east-1)`
3. Run `aws ecr create-repository --repository-name fargate-example`
4. Run `docker build -t fargate-example .`
5. Run `docker tag fargate-example:latest <accountId>.dkr.ecr.us-east-1.amazonaws.com/fargate-example:latest` and replace `<accountId>` with your account id
6. Go to lesson folder
7. Run `serverless deploy`
8. Run `curl <url>` where `<url>` is output from the previous step
9. Check AWS Step Function console https://console.aws.amazon.com/states/home