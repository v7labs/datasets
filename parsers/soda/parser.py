from ..base import Parser
from pathlib import Path
import pickle
import numpy as np
from ..datatypes import Annotation, Image, ImageAnnotationFile, Tag
from typing import Any, List, Tuple
from PIL import Image as PILImage
from dataclasses import asdict
import json
from tqdm import tqdm
from glob import glob



class SODAParser:
    annotations = {}
    filename = []  
    ALLOWED_PATHS = ["/train", "/test", "/val"]
    

    def __init__(
        self,
        images_dir: Path,
        annotation_dir: Path,
        dataset_name: str,
        path: str = "/train",
    ):
        self.images_dir = images_dir
        self.annotation_dir = annotation_dir
        self.dataset_name = dataset_name

        if path not in self.ALLOWED_PATHS:
            raise ValueError(f"path should be one of {self.ALLOWED_PATHS}")

        self.path = path
        
        
        
    def parse_annotations(self, 
                         data_type='train',
                         save_annotation=True)->ImageAnnotationFile:
        
        files = glob(f'{self.annotation_dir}/*.json')
        
        if data_type=='train':
            json_data = f'{self.annotation_dir}/instance_train.json'
        else:
            json_data=f'{self.annotation_dir}/instance_val.json'
            
        f = open(json_data)
        data = json.load(f)
        
        
        for idx, file in tqdm(enumerate(data['images'], 1), total=5000, desc='parsing'):
            coor = []
            self.filename.append(file['file_name'].split('.')[0])
            for seq, an in enumerate(data["annotations"]):
                if len(an) != 0:
                    if an["image_id"] == idx:
                        
                        coor.append(Annotation(name=data['categories'][an['category_id']-1]['name'])
                        .add_data(
                            BoundingBox(
                                x=int(an['bbox'][0]),
                                y=int(an['bbox'][1]),
                                w=int(an['bbox'][2]),
                                h=int(an['bbox'][3]))))
                        ann = ImageAnnotationFile(
                        dataset=self.dataset_name,
                        image=Image(
                            width=int(file['width']),
                            height=int(file['height']),
                            original_filename=file['file_name'],
                            filename=file['file_name'],
                            path=self.path), 
                        annotations=coor)
            if save_annotation:
                self.annotations[file['file_name'].split('.')[0]] = ann
        
            
    def get_annotations(self, idx:int):
        ann = self.annotations[self.filename[idx]]
        return ann
    
    def save_to_json(self, path_to_save='', dir_name='annotationFolder'):
        path = f'{path_to_save}/{dir_name}'
        try:
            if not os.path.exists(path):
                os.mkdir(path)
                for idx in tqdm(range(5000), desc="Creating JSON file"):
                    ann = self.get_annotations(idx)
                    filename = self.filename[idx]
                    json_object = json.dumps(asdict(ann), indent=4)
                    with open(f"{path}/{filename}.json", "w") as outfile:
                        outfile.write(json_object)
        except:
            print('path exist')
            
    
    def upload_to_darwin(self, 
                         api_key:str, 
                         image_dir: Path,  
                         json_dir: Path):
        
        images = glob(f'{image_dir}/*.jpg')
        annotations = glob(f'{json_dir}/*.json')
        client = Client.from_api_key(api_key)
        dataset_identifier = f"{client.default_team}/{self.dataset_name}"
        try:
            dataset = client.create_dataset(self.dataset_name)
        except darwin.exceptions.NameTaken:
            dataset = client.get_remote_dataset(dataset_identifier)
        dataset.push(images, path=self.path)
        importer.import_annotations(
            dataset,
            formats.darwin.parse_file,
            annotations,
            append=True,
        )
    
        
    
        
        
        

    
        
        
        