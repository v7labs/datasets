# Datasets

A comprehensive collection of parsers for different datasets

## Requirements

You'll need python 3.9 or above, we highly recommend to use [`virtualenv`](https://virtualenv.pypa.io/en/latest/)

```
virtualenv .env --python=3.9
source ./.env/bin/activate
pip install -r requirements.txt
```

## Writing a Parser

We provide several utilities to write a sharable parser. **You'll have to subclass parses.Parser`. An example is provided at `parsers.cifar10`. Before contributing please read the [contributing guide](CONTRIBUTING.md)**.

A custom parser is a subclass of `parsers.Parser`. You must implement the following two methods

```python


class MyParser(Parser):

    def parse_annotation(self, *args: Any, **kwargs: Any) -> ImageAnnotationFile:
        # your logic here

    def parse(self, root: Path):
        # your logic here

```

```python
my_parser = MyParser(
        images_dir=Path("./images"),
        annotation_dir=Path("./annotations"),
        dataset_name="foo",
        path="/train",
)
# parse it
parser.parse(root=Path("./foo"))
parser.upload(os.environ["DARWIN_API_KEY"])
parser.upload_sample(os.environ["DARWIN_API_KEY"], n_samples=5)

```

`Parser` comes with special methods to upload the images, \*\*due to a slow import problem on our hand you can test the correctness of your parser by using `.upload_sample`

For each dataset, you are expected to submit a PR that will be reviewed by us :)

### Data types

Each parse has to return a darwin-json, to make thing easier we create a custom type in `datatypes.py`. You can create an `AnnotationFile` using the pre-defined data classes in there. Below we showcase how to create a simple annotation file with one bounding box and one tag

```python

from parsers.datatypes import *

ann = ImageAnnotationFile(
    dataset="foo",
    image=Image(
        width=100,
        height=100,
        original_filename="hey",
        filename="hey"),
    annotations=[
        Annotation(name="a")
        .add_data(BoundingBox(x=1, y=2, h=10, w=10))
        .add_data(Tag())
    ],
)

```

Annotations can be easily converted to json using the `dataclasses.asdict` utility

```python
from dataclasses import asdict
from pprint import pprint

pprint(asdict(ann))

```

```
{'annotations': [{'bounding_box': {'h': 10, 'w': 10, 'x': 1, 'y': 2},
                            'tag': {}},
                  'name': 'a'}],
 'dataset': 'foo',
 'image': {'filename': 'hey',
           'height': 100,
           'original_filename': 'hey',
           'path': None,
           'seq': None,
           'thumbnail_url': None,
           'url': None,
           'width': 100,
           'workview_url': None}}

```

To correctly specify a dataset split, e.g. 'train', you need to pass the `path` parameter to the `Image` type.

```python

from parsers.datatypes import *

ann = ImageAnnotationFile(
    dataset="foo",
    image=Image(
        width=100,
        height=100,
        original_filename="hey",
        filename="hey",
        path="/train"), # <------ HERE!
    annotations=[
        Annotation(name="a")
        .add_data(BoundingBox(x=1, y=2, h=10, w=10))
        .add_data(Tag())
    ],
)

```
