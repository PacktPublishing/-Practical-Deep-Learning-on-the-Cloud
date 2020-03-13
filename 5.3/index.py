import urllib.request
import boto3

def handlerMap(event,context):
	event['tasks'] = [
		{
			'url' : 'http://www.robots.ox.ac.uk/~vgg/data/flowers/102/102flowers.tgz',
			'filename' : '102flowers.tgz',
			's3_key' : 'raw/102flowers.tgz'
		},
		{
			'url' : 'http://www.robots.ox.ac.uk/~vgg/data/flowers/102/imagelabels.mat',
			'filename' : 'imagelabels.mat',
			's3_key' : 'raw/imagelabels.mat'
		}
	]
	return event

def handlerBranch(event,context):
	s3 = boto3.client('s3')
	s3_bucket = 'course-pdl-datapipeline'
	local_file_path = '/tmp/' + event['filename']
	urllib.request.urlretrieve(event['url'], local_file_path)
	with open(local_file_path, 'rb') as data:
		s3.upload_fileobj(data, s3_bucket, event['s3_key'])
	return event['s3_key']

def handlerReduce(event,context):
	return ['app/exec']+event['map_result']

def handlerPublisher(event,context):
	return event