# Contributing to Dataset

Thank you for taking the time to contribute!

We have a set of guidelines that you should follow to ensure cohesion across each dataset

## How to contribute to a new dataset

To contribute with a new dataset you'll have to make a pull request (PR). Each dataset must have its directory inside `parsers`. For example, if I want to create a new parser for `imagenet`, I'll have to create a directory `parsers/imagenet`. The directory **must** have the following files

```
.
├── __init__.py
├── parser.py
└── README.md
```

- `__init__.py` is the classic python `__init__` file used for module definition
- `parser.py` contains the actual parser, a subclass of `parsers.Parser`
- `README.py` explain how to get the dataset and how to run the parser

We highly encourage to use [types](https://docs.python.org/3/library/stdtypes.html)


**Check out [this example](https://github.com/v7labs/datasets/tree/main/parsers/cifar)**
