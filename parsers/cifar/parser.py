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


class CIFARParser(Parser):
    def parse_annotation(
        self, idx: int, img: np.array, file_name: str, labels: List[str]
    ) -> ImageAnnotationFile:

        ann = ImageAnnotationFile(
            dataset=self.dataset_name,
            image=Image(
                width=img.shape[0],
                height=img.shape[1],
                original_filename=file_name.decode(),
                filename=file_name.decode(),
                path=self.path,
            ),
            annotations=[Annotation(name=labels[idx]).add_data(Tag())],
        )
        return ann

    def parse_image(self, img: np.array) -> PILImage.Image:
        return PILImage.fromarray(img)

    def parse_batch(self, batch_path: Path, labels: List[str]):
        with (batch_path).open("rb") as f:
            data = pickle.load(f, encoding="bytes")
            labels_ids = data[b"labels"]
            images = data[b"data"].reshape((-1, 3, 32, 32)).transpose((0, 2, 3, 1))
            file_names = data[b"filenames"]

            ann_stage = map(
                lambda x: self.parse_annotation(*x, labels),
                zip(labels_ids, images, file_names),
            )
            images_stage = map(self.parse_image, images)

            for file_name, ann, img in tqdm(zip(file_names, ann_stage, images_stage)):
                file_name = Path(file_name.decode()).stem
                ann_file = Path(self.annotation_dir / f"{file_name}.json")
                img_file = Path(self.images_dir / f"{file_name}.png")

                with ann_file.open("w") as f:
                    json.dump(asdict(ann), f, indent=4)

                img.save(str(img_file))

    def parse(self, root: Path):
        with (root / "batches.meta").open("rb") as f:
            meta = pickle.load(f)
            labels = meta["label_names"]
        if self.path == "/train":
            batches_files = root.glob("data_batch_*")
        else:
            batches_files = [root / "test_batch"]
        list(map(lambda x: self.parse_batch(x, labels), batches_files))
