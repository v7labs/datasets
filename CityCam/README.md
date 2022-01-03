# CityCam-CMU

## Get the Dataset

```
gdown --id 1e3NtzpwBcUeakcfiYo_gB2IgxxFIGkVe
tar -xf CityCam.tar.gz
```

## Pre-processing for upload

Move all files and annotations from corresponding sub-folders to the root folder
```
python3 gather.py
```

Convert annotations to pascal_voc 

```
python3 process_annotations.py
```