from parsers.cifar.parser import CIFARParser
from pathlib import Path
import os
from parsers.datatypes import *


os.environ["DARWIN_BASE_URL"] = "http://localhost:4242/"

parser = CIFARParser(
    images_dir=Path("./images"),
    annotation_dir=Path("./annotations"),
    dataset_name="cifar10",
    path="/train",
)
# parse it
parser.parse(Path("./cifar-10-batches-py"))

parser.upload_sample(os.environ["DARWIN_API_KEY"], 4)
