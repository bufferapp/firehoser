# K3

Simple Lambda function to archive Kinesis raw stream records to S3. K3 uses Firehose to save the records.

## Usage

1. Inside [AWS Lambda Console](https://console.aws.amazon.com/lambda), create a new Python 3.6 blank function and paste the content of [`lambda_function.py`](lambda_function.py) file.
1. Set a new environment variable named `FIREHOSE_STREAM_NAME` with the stream name.

## Contributing

All kinds of contributions are welcome!
