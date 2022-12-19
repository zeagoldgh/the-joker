# TheJoker
Virtual mentorship for teens, anxiety, and depression people in need

sns_notifier.py has to be run with (Dynamodb update) template event. Example:

{
  "Records": [
    {
      "eventID": "c4ca4238a0b923820dcc509a6f75849b",
      "eventName": "INSERT",
      "eventVersion": "1.1",
      "eventSource": "aws:dynamodb",
      "awsRegion": "us-east-1",
      "dynamodb": {
        "Keys": {
          "Id": {
            "N": "101"
          }
        },
        "NewImage": {
          "value": {
            "S": "New item!"
          },
          "id": {
            "S": "101"
          }
        },
        "ApproximateCreationDateTime": 1428537600,
        "SequenceNumber": "4421584500000000017450439091",
        "SizeBytes": 26,
        "StreamViewType": "NEW_AND_OLD_IMAGES"
      },
      "eventSourceARN": "arn:aws:dynamodb:us-east-1:123456789012:table/ExampleTableWithStream/stream/2015-06-27T00:48:05.899"
    }
  ]
}
