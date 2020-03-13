import boto3
import json
import io

def handlerMap(event,context):
	tasks_parameters = [
		{
			's3_key_inp' : 'tasks_input/task_1.json',
			's3_key_out' : 'tasks_output/task_1.json',
			'hyperparamters' : {
				'parameter1' : 1,
				'parameter2' : 'test1',
				'parameter3' : True
			}
		},
		{
			's3_key_inp' : 'tasks_input/task_2.json',
			's3_key_out' : 'tasks_output/task_2.json',
			'hyperparamters' : {
				'parameter1' : 2,
				'parameter2' : 'test2',
				'parameter3' : False
			}
		},
		{
			's3_key_inp' : 'tasks_input/task_3.json',
			's3_key_out' : 'tasks_output/task_3.json',
			'hyperparamters' : {
				'parameter1' : 3,
				'parameter2' : 'test3',
				'parameter3' : False
			}
		}
	];

	s3 = boto3.client('s3')
	s3_bucket = 'course-pdl-batch-example'
	event['tasks'] = []

	for task_parameters in tasks_parameters:
		s3.upload_fileobj(
			io.BytesIO(
				json.dumps(
					task_parameters['hyperparamters']
				).encode('utf-8')),
			s3_bucket,
			task_parameters['s3_key_inp']
		)
		event['tasks'].append(
			{
				'task_command' : [
					'/app/exec',
					task_parameters['s3_key_inp'],
					task_parameters['s3_key_out']
				],
				'task_output' : task_parameters['s3_key_out']
			}
		)
	return event

def handlerReduce(event,context):
	s3 = boto3.client('s3')
	s3_bucket = 'course-pdl-batch-example'
	tasks_result = []
	for task in event['tasks']:
		result = s3.get_object(Bucket=s3_bucket, Key=task['task_output'])
		parameters = json.loads(result["Body"].read().decode())
		tasks_result.append(parameters)
	return tasks_result

def handlerPublisher(event,context):
	print(event)
	return event