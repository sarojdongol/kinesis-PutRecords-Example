import boto3

dynamodb = boto3.resource('dynamodb')
dynamodbTable = dynamodb.Table('hashkeylookup')

def DescribeResource(streamResource):
    client = boto3.client('kinesis')
    response = client.describe_stream(StreamName=streamResource)
    ShardsInfo = response['StreamDescription']['Shards']
    i = 0
    while i < len(ShardsInfo):
        dynamodbTable.put_item(
            Item = {
            'shardid' : ShardsInfo[i]['ShardId'],
            'endinghaskkey' : ShardsInfo[i]['HashKeyRange']['EndingHashKey'],
            'startinghashkey' : ShardsInfo[i]['HashKeyRange']['StartingHashKey']
            }
        )
        i +=1;



response = DescribeResource('santosh-kinesis')
