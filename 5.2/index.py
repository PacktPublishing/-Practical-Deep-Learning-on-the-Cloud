def handlerMap(event,context):
    event['tasks'] = [
        {'task_id' : 1},
        {'task_id' : 2},
        {'task_id' : 3}
    ];
    return event

def handlerBranch(event,context):
    return str(event['task_id'])

def handlerReduce(event,context):
    return ['app/exec']+event['map_result']

def handlerPublisher(event,context):
    return event