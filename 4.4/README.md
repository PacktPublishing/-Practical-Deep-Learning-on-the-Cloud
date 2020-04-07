# 4.4 Using AWS SageMaker to Train Deep Learning CNN Models

In this lesson, we will learn how to easily go from running the training locally to running the same training code on the cloud.

Used libraries: Tensorflow, Keras

Used services: AWS SageMaker, AWS ECR

## Steps

1. Go to `container` folder
2. Run `$(aws ecr get-login --no-include-email --region us-east-1)`
3. Run `aws ecr create-repository --repository-name sagemakerexample`
4. Run `docker build -t sagemakerexample`
5. Run `docker tag sagemakerexample:latest <accountId>.dkr.ecr.us-east-1.amazonaws.com/sagemakerexample:latest` and replace `<accountId>` with your account id
6. Go to lesson folder
7. Run `python3 runSagemaker.py`
8. Check output files and produced metrics (https://console.aws.amazon.com/cloudwatch/home)