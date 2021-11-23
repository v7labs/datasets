from parsers.cifar.parser import CIFARParser
from pathlib import Path
import os
from parsers.datatypes import *
from dataclasses import asdict, fields

# ann = ImageAnnotationFile(
#     dataset="foo",
#     image=Image(width=100, height=100, original_filename="hey", filename="hey"),
#     annotations=[
#         Annotation(name="a").add_data(BoundingBox(x=1, y=2, h=10, w=10)).add_data(Tag())
#     ],
# )


# print(asdict(ann))





os.environ["DARWIN_BASE_URL"] = "http://localhost:4242/"

parser = CIFARParser(images_dir = Path('./images'), annotation_dir= Path('./annotations'), dataset_name='cifar10_train')

parser.parse(Path('./cifar-10-batches-py'))

parser.upload("MhgBYfX.P6j-VDDW30Kil7SGuJdmZ2pI388VEeBe")