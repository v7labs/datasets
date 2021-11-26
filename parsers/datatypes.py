from __future__ import annotations
import re
from dataclasses import dataclass, make_dataclass
from typing import Any, List, Dict, Optional, Union

# used to convert from CammelCase to underscore_case
pattern: re.Pattern = re.compile(r"(?<!^)(?=[A-Z])")


@dataclass
class Image:
    width: int
    height: int
    original_filename: str
    filename: str
    url: Optional[str] = None
    seq: Optional[str] = None
    thumbnail_url: Optional[str] = None
    path: Optional[str] = "/"
    workview_url: Optional[str] = None


@dataclass
class KeyPoint:
    x: int
    y: int


@dataclass
class BoundingBox(KeyPoint):
    h: int
    w: int


@dataclass
class Cuboid:
    back: BoundingBox
    front: BoundingBox


@dataclass
class DirectionalVector:
    angle: float
    lenght: float


@dataclass
class Line:
    path: List[KeyPoint]


@dataclass
class Polygon(Line):
    pass


@dataclass
class Ellipse:
    angle: float
    center: KeyPoint
    radius: KeyPoint


@dataclass
class SkeletronNode:
    name: str
    occluded: bool
    x: float
    y: float


@dataclass
class Skeletron:
    nodes: List[SkeletronNode]


@dataclass
class Text:
    text: str


@dataclass
class Tag(Dict):
    pass


AnnotationData = Union[
    BoundingBox, Skeletron, Text, Polygon, Tag, Ellipse, Line, Cuboid, KeyPoint
]


@dataclass
class Annotation:
    name: str

    def add_data(self, data: AnnotationData) -> Annotation:
        """Dynamically add a `AnnotationData` to `Annotation` using its converted name to underscore_case as field. To make this work we create a new dataclass each time."""
        attr: str = pattern.sub("_", data.__class__.__name__).lower()
        NewAnnotation = make_dataclass(
            "Annotation", [(attr, AnnotationData)], bases=(self.__class__,)
        )
        new_ann = NewAnnotation(**vars(self), **{attr: data})
        return new_ann


@dataclass
class ImageAnnotationFile:
    dataset: str
    image: Image
    annotations: List[Annotation]
