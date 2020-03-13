import boto3
import json
import io
import tflite_runtime.interpreter as tflite
import numpy as np
from PIL import Image
interpreter = None

def handlerMapper(event,context):
  event['image'] = 'images/flower.jpg'
  return event

def loadImage(s3_bucket, s3_key):
  s3 = boto3.client('s3')
  result = s3.get_object(Bucket=s3_bucket, Key=s3_key)
  result_image = Image.open(io.BytesIO(result["Body"].read()))
  input_data = np.expand_dims(np.array(result_image.resize((299,299)),dtype=np.float32)/255, axis=0)
  return input_data

def runInference(interpreter, input_data):
  input_details = interpreter.get_input_details()
  output_details = interpreter.get_output_details()
  interpreter.set_tensor(input_details[0]['index'], input_data)
  interpreter.invoke()
  output_data = interpreter.get_tensor(output_details[0]['index'])
  return output_data

def handlerInferenceNew(event, context):
  label_list = ['Cyclamen','Lotus','Passionflower']
  global interpreter
  if interpreter is None:
    interpreter = tflite.Interpreter(model_path="models/converted_model_quantized.tflite")
    interpreter.allocate_tensors()

  if ('image' in event):
    input_data = loadImage('course-pdl-inference', event['image'])
  else:
    input_details = interpreter.get_input_details()
    input_shape = input_details[0]['shape']
    input_data = np.array(np.random.random_sample(input_shape), dtype=np.float32)
  
  output_data = runInference(interpreter, input_data)
  return {'feature_vector':output_data.tolist(), 'prediction':label_list[np.argmax(output_data)], 'model_type':'NewModel'}

def handlerInferenceOld(event, context):
  label_list = ['Cyclamen','Lotus','Passionflower']
  global interpreter
  if interpreter is None:
    interpreter = tflite.Interpreter(model_path="models/converted_model.tflite")
    interpreter.allocate_tensors()

  if ('image' in event):
    input_data = loadImage('course-pdl-inference', event['image'])
  else:
    input_details = interpreter.get_input_details()
    input_shape = input_details[0]['shape']
    input_data = np.array(np.random.random_sample(input_shape), dtype=np.float32)

  output_data = runInference(interpreter, input_data)
  return {'feature_vector':output_data.tolist(), 'prediction':label_list[np.argmax(output_data)], 'model_type':'OldModel'}

def handlerPublisher(event,context):
  print(event)
  return event