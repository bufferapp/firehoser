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

    batch_data = list(map(lambda x: {'Data': json.dumps(x)}, batch))

    try:
        response = firehose_client.put_record_batch(
            DeliveryStreamName=firehose_stream_name,
            Records=batch_data)

        failed_put_count = response.get('FailedPutCount')

        # Handle failed records
        if failed_put_count > 0:
            logger.error('{} failed records put!'.format(failed_put_count))

            failed_records = []
            for i, record in enumerate(response['Records']):
                if record.get('ErrorCode') == 'ProvisionedThroughputExceededException':
                        failed_records.append(batch_data[i])

            send_batch(failed_records)

    except Exception as e:
        logger.error('Exception: {}'.format(e))


def lambda_handler(event, context):
    """ Main lambda handler.

    The handler grabs events from Kinesis and forwards their content to
    Firehose.

    Parameters
    ----------
    event: dict
        Contains Records grabbed from the Kinesis stream
    """

    if event['Records']:
        send_batch(event['Records'])
