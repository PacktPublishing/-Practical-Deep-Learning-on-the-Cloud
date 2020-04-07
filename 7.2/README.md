# 7.2 Deploying AWS Step Functions with AWS Lambda Using Serverless Framework

In production, one of the best ways to deploy serverless infrastructure is to use serverless framework. This lesson will show how to use it to deploy AWS Step Functions and AWS Lambda.

Used libraries: TFLite, Pillow

Used services: AWS Step Functions, AWS Lambda

Execution graph:

<img width="531" alt="Screen Shot 2020-04-02 at 9 05 21 PM" src="https://user-images.githubusercontent.com/3318397/78323140-75176880-7560-11ea-9d51-e88f5b691a7b.png">

## Steps

1. Go to lesson folder
2. Create custom bucket using command `aws s3api create-bucket --bucket <bucket_name>`
3. Run command `aws s3 cp images/flower.jpg s3://<bucket_name>/images/flower.jpg`
4. Replace `S3BucketName` parameter in `serverless.yml` with your bucket name
5. Run `serverless deploy`
6. Run `curl <url>` where `<url>` is output from the previous step
7. Check execution graph on AWS Step Function console https://console.aws.amazon.com/states/home