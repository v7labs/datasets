# Stanford Dogs Dataset

## Get the Dataset

```
Download the dataset from http://vision.stanford.edu/aditya86/ImageNetDogs/
```

## Extract the annotations from .tar file

```
Run annotations.py to get the annotations from the tar file

Run the following command in the annotations folder to convert the annotations to .xml format  
find . -type f -exec mv '{}' '{}'.xml \;

```

## Make the annotations compatible to the corresponding images

```

Run upload.py to make the annotations of bounding box compatable to upload. It includes pre-processing of folder/filenames of the annotations matching as the images.

```