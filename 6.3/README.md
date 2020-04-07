# 6.3 Project – Deep Learning Training Pipeline for the CNN

In this lesson, we will show how to deploy the deep learning pipeline.

Used libraries: Tensorflow, Keras, TFLite

Used services: AWS Step Functions, AWS Batch, AWS Lambda, AWS ECR

Execution graph:

<img width="533" alt="Screen Shot 2020-04-02 at 9 05 00 PM" src="https://user-images.githubusercontent.com/3318397/78323118-68931000-7560-11ea-802f-a2fc7b415b6c.png">

## Steps

1. Go to `container` folder
2. Run `$(aws ecr get-login --no-include-email --region us-east-1)`
3. Run `aws ecr create-repository --repository-name deep-learning-training-batch`
4. Run `docker build -t deep-learning-training-batch`
5. Run `docker tag deep-learning-training-batch:latest <accountId>.dkr.ecr.us-east-1.amazonaws.com/deep-learning-training-batch:latest` and replace `<accountId>` with your account id
6. Go to lesson folder
7. Create custom bucket using command `aws s3api create-bucket --bucket <bucket_name>`
8. Replace `S3BucketName` parameter in `serverless.yml` with your bucket name
9. Run `serverless deploy`
10. Run `curl <url>` where `<url>` is output from the previous step
11. Check execution graph on AWS Step Function console https://console.aws.amazon.com/states/home and bucket on S3 console https://s3.console.aws.amazon.com/s3/home