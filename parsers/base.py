from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any
from abc import ABC 
from .datatypes import ImageAnnotationFile
import darwin
import darwin.importer as importer
from darwin.client import Client
from darwin.importer import formats

class Parser(ABC):

    def __init__(self, images_dir: Path, annotation_dir: Path, dataset_name: str):
        self.images_dir = images_dir
        self.annotation_dir = annotation_dir
        self.dataset_name = dataset_name

    @abstractmethod
    def parse_annotation(self, *args: Any, **kwargs: Any) -> ImageAnnotationFile:
        """Parse one single annotation and return a darwin annotation file
        """
    @abstractmethod
    def parse(self, root: Path):
        """Parse all the files contained in root"""

    def upload(self, api_key: str):
        """Handy function to upload images and annotations to darwin in one go

        Args:
            api_key (str): A valid API KEY
            dataset_name (str): The dataset name
            images_dir (Path): The images' directory
            annotation_dir (Path): The annnotations' directory
        """
        client = Client.from_api_key(api_key)
        dataset_identifier = f"{client.default_team}/{self.dataset_name}"
        try:
            dataset = client.create_dataset(self.dataset_name)
        except darwin.exceptions.NameTaken:
            dataset = client.get_remote_dataset(dataset_identifier)
        # dataset.push(list(self.images_dir.glob("*")))
        importer.import_annotations(
            dataset,
            formats.darwin.parse_file,
            list(self.annotation_dir.glob("*.json")),
            append=True,
        )

