# Firehoser

Command line tool that automates the setup of a lambda function that fowards records from Kinesis to Firehose.

## Installation

To install Firehoser, simply:

```
pip install git+https://github.com/bufferapp/firehoser
```

## Usage

```bash
firehoser link [kinesis-stream-name] [firehose-stream-name]
firehoser unlink [kinesis-stream-name] [firehose-stream-name]
```

## Contributing

Feel free to open issues or submit pull requests with bug fixes or changes. All kind of contributions welcome!
