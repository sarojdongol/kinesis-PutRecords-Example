import boto3
import random
import json


###Dynamodb Connection
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('hashkeylookup')

def GenerateData():
    data = { "id" : random.randint(100,90000), "street" : random.randrange(0,100000)}
    jsonsets = json.dumps(data)
    return(jsonsets)

def QueryDB():
    response = table.get_item(Key={"shardid" :"shardId-000000000001"},ProjectionExpression='endinghaskkey')
    return(response['Item']['endinghaskkey'])



def IngestRecords(streamResource):
    client = boto3.client('kinesis')
    kinesisrecords = [];
    for i in range(100):
        callgeneratedata = {'Data' : GenerateData(),'PartitionKey':'saroj','ExplicitHashKey' : QueryDB()}
        kinesisrecords.append(callgeneratedata)
        i +=1;
        if(i == 10):
            response = client.put_records(Records=kinesisrecords,StreamName=streamResource)
            kinesisrecords=[];

            print(response)

IngestRecords('santosh-kinesis')



