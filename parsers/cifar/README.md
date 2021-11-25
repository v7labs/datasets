# CIFAR-10/100

## Get the Dataset

```
wget https://www.cs.toronto.edu/~kriz/cifar-10-python.tar.gz
wget https://www.cs.toronto.edu/~kriz/cifar-100-python.tar.gz

tar -xf cifar-10-python.tar.gz
tar -xf cifar-100-python.tar.gz

```

## Usage

```python

from parsers.cifar.parser import CIFARParser
from pathlib import Path
import os

parser = CIFARParser(
    images_dir=Path("./images"),
    annotation_dir=Path("./annotations"),
    dataset_name="cifar10",
    path="/train",
)
# parse it
parser.parse(Path("./cifar-10-batches-py"))

parser.upload(os.environ["DARWIN_API_KEY"])

```
