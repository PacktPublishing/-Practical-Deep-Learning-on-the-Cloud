# 7.3 Project - Deep Learning Inference Pipeline for CNN

In this lesson, we will show how to deploy deep learning pipeline using serverless framework.

Used libraries: TFLite, Pillow

Used services: AWS Step Functions, AWS Lambda

Execution graph:

<img width="530" alt="Screen Shot 2020-04-02 at 9 05 40 PM" src="https://user-images.githubusercontent.com/3318397/78323142-76489580-7560-11ea-8406-a9569acdebb9.png">

## Steps

1. Go to lesson folder
2. Create custom bucket using command `aws s3api create-bucket --bucket <bucket_name>`
3. Run command `aws s3 cp images/flower.jpg s3://<bucket_name>/images/flower.jpg`
4. Replace `S3BucketName` parameter in `serverless.yml` with your bucket name
5. Run `serverless deploy`
6. Run `curl <url>` where `<url>` is output from the previous step
7. Check execution graph on AWS Step Function console https://console.aws.amazon.com/states/home