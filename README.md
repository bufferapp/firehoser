# K3

Simple Lambda function to archive Kinesis raw stream records to S3. K3 uses Firehose to save the records.

## Usage

1. Inside [AWS Lambda Console](https://console.aws.amazon.com/lambda), create a new Python 3.6 blank function and paste the content of [`lambda_function.py`](functions/k3/lambda_function.py) file. Alternatively you can use Apex to deply and manage it. Tweak the `function.json` file and run `apex deploy k3`.
    - Add a Kinesis stream as a trigger with a batch size smaller than 500.
1. Create a Firehose Stream with your desired configuration.
1. Set a new environment variable named `FIREHOSE_STREAM_NAME` with the stream name.

### Testing

#### Locally
Is it possible to test the lambda function locally. Install Docker and `jq`. You'll also need an `.env` file in the folder containing some AWS variables (`AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_DEFAULT_REGION`) besides your `FIREHOSE_STREAM_NAME`.

```
docker run \
    -v ${PWD}:/var/task \
    --env-file .env \
    lambci/lambda:python3.6 \
    lambda_function.lambda_handler `jq . events.json -c`
```

#### Remote

Sometimes is useful to test the function in AWS Lambda. You can do it by running `apex invoke k3 < events.json`.

## Contributing

All kinds of contributions are welcome!
