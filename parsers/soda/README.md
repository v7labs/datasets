# SODA10M Dataset

## Get the Dataset
You can download the labeled dataset from this [link](https://drive.google.com/file/d/1oSJ0rbqNHLmlOOzpmQqXLDraCCQss4Q4/view?usp=sharing). The link contains both training and validation dataset with annotations. 

## Usage

```
from parsers.soda.parser import SODAParser
from pathlib import Path
import os

parser = SODAParser(
    images_dir = 'path_to_image_dir/SSLAD-2d/labelled/train',
    annotation_dir = 'path_to_image_dir/SSLAD-2d/labelled/annotations',
    dataset_name = soda10m,
)

#parse it 
parser_annotation = parser.parse_annotations()

#convert annotations to JSON 
parser.save_to_json(
    path_to_save = 'path',
    dir_name = "annotationFolder"
)

#upload to Darwin 
parser.upload_to_darwin(
    api_key = api_key, 
    image_dir = 'path_to_image_dir/SSLAD-2d/labelled/train', 
    json_dir = 'path/annotationFolder'
)

#get filenames 
print(parser.filename)

#get single annotations 
print(parser.get_annotations(100))

```

