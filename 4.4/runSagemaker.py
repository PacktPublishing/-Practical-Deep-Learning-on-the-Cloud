from sagemaker.estimator import Estimator
import sagemaker as sage

## Uploading data to S3
prefix = 'flower-dataset'
dataset_directory = './flower-dataset'

sess = sage.Session()
data_location = sess.upload_data(dataset_directory, key_prefix=prefix)

## Setting up parameters for training
ecr_image = '339543757547.dkr.ecr.us-east-1.amazonaws.com/sagemakerfinetuning:latest'
role = 'arn:aws:iam::339543757547:role/SageMakerAccessRole'
instance_type = 'ml.p2.xlarge'

hyperparameters = {
    'num_of_epochs': 4
}

metric_definitions = [
    {
        "Name": "epoch",
        "Regex": "Epoch (.*?)/",
    },
    {
        "Name": "loss",
        "Regex": "val_loss: (.*)",
    },
    {
        "Name": "accuracy",
        "Regex": "Accuracy = (.*)",
    }
]

estimator = Estimator(role=role,
                      train_instance_count=1,
                      train_use_spot_instances=True,
                      train_max_wait = 24*3600,
                      train_instance_type=instance_type,
                      image_name=ecr_image,
                      hyperparameters=hyperparameters,
                      metric_definitions=metric_definitions)

## Training the model
estimator.fit(data_location)


## Downloading the model and running it on the example image
import boto3
import tarfile
import tensorflow as tf
import numpy as np

## Downloading the model from S3
model_key = estimator.model_data
model_file_path = 'model.tar.gz'
s3 = boto3.client('s3')
s3.download_file(model_key.split('/')[2], '/'.join(model_key.split('/')[3:]), model_file_path)
tar = tarfile.open(model_file_path, "r:gz")
tar.extractall()
tar.close()

## Running the model on the image
img_file = 'flower.jpg'
label_list = ['Cyclamen','Lotus','Passionflower']
img = tf.keras.preprocessing.image.load_img(img_file, grayscale=False, color_mode='rgb', target_size=None, interpolation='nearest')
img_np = np.expand_dims(np.array(img),axis=0).astype('float16')/255

model = tf.keras.models.load_model('finetunedInceptionModelSagemaker.h5')
prediction = model.predict(img_np)
print(label_list[np.argmax(prediction)])

