# 6.2 Deploying AWS Step Functions with AWS Batch Using Serverless Framework

This lesson will show to use it to deploy AWS Step Functions, AWS Batch, and AWS Lambda.

Used libraries: Tensorflow, Keras

Used services: AWS Step Functions, AWS Batch, AWS Lambda, AWS ECR

Execution graph:

<img width="532" alt="Screen Shot 2020-04-02 at 9 04 37 PM" src="https://user-images.githubusercontent.com/3318397/78323136-72b50e80-7560-11ea-8cb6-3a1fabb3dbaa.png">

## Steps

1. Go to `container` folder
2. Run `$(aws ecr get-login --no-include-email --region us-east-1)`
3. Run `aws ecr create-repository --repository-name stepfunction-batch-example`
4. Run `docker build -t stepfunction-batch-example .`
5. Run `docker tag stepfunction-batch-example:latest <accountId>.dkr.ecr.us-east-1.amazonaws.com/stepfunction-batch-example:latest` and replace `<accountId>` with your account id
6. Go to lesson folder
7. Create custom bucket using command `aws s3api create-bucket --bucket <bucket_name>`
8. Replace `S3BucketName` parameter in `serverless.yml` with your bucket name
9. Run `serverless deploy`
10. Run `curl <url>` where `<url>` is output from the previous step
11. Check execution graph on AWS Step Function console https://console.aws.amazon.com/states/home and bucket on S3 console https://s3.console.aws.amazon.com/s3/home