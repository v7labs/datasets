# Datasets

A comprehensive collection of parsers for different datasets

## Requirements

You'll need python 3.9 or above, we highly recomand to use [`virtualenv`](https://virtualenv.pypa.io/en/latest/)

```
virtualenv .env --python=3.9
source ./.env/bin/activate
pip install -r requirements.txt
```

## Writing a Parser

We provide several utilities to write sharable parser. The

### Data types

Each parse have to return a darwin-json, to make thing easier we create custom type in `datatypes.py`. You can create an `AnnotationFile` using the pre-definied dataclasses in there. Below we showcase how to create a simple annotation file with one bounding box and one tag

```python

from parsers.datatypes import *

ann = ImageAnnotationFile(
    dataset="foo",
    image=Image(width=100, height=100, original_filename="hey", filename="hey"),
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
