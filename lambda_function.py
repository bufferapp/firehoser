import boto3
import os
import logging
import json

# Standard logger
logger = logging.getLogger()

# Configure Firehose
firehose_client = boto3.client('firehose')
firehose_stream_name = os.getenv('FIREHOSE_STREAM_NAME')


def send_batch(batch):
    """ Send a batch of records to Kinesis Firehose.

    Parameters
    ----------
    batch: array
        Array of records. Each records should be a dictionary with a Data key
    """

    try:
        response = firehose_client.put_record_batch(
            DeliveryStreamName=firehose_stream_name,
            Records=batch)
    except Exception as e:
        logger.error('Exception: {}'.format(e))

    if response['FailedPutCount'] > 0:
        logger.error('{} failed records!'.format(response['FailedPutCount']))

    # TODO: Handle FailedPut errors


def lambda_handler(event, context):
    """ Main lambda handler.

    The handler grabs the events from Kinesis and forwards the content to
    Firehose.

    Parameters
    ----------
    event: dict
        Contains the Records grabbed from the Kinesis stream
    """
    batch = []

    for record in event['Records']:
        batch.append({'Data': json.dumps(record)})

        # If we hit 500 records, flush them to the stream
        if len(batch) > 499:
            send_batch(batch)
            batch = []

    # Flush remaining messages
    if batch:
        send_batch(batch)
