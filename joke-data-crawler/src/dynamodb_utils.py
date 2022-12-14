import boto3
import os

dynamodb = boto3.resource("dynamodb")

jokes_table_name = os.getenv("JOKES_TABLE_NAME")

jokes_table = dynamodb.Table(jokes_table_name)


def save_joke_to_dynamodb(joke):
    jokes_table.put_item(Item = joke)
