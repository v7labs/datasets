from dataclasses import dataclass, field, asdict
import dataclasses
from typing import Any, List, Dict, Optional, Union
import re

pattern: re.Pattern = re.compile(r"(?<!^)(?=[A-Z])")

@dataclass
class BaseData:
    width: int
    height: int
    original_filename: str
    filename: str

@dataclass
class Image(BaseData):
    url: Optional[str] = None
    seq: Optional[str] = None
    thumbnail_url: Optional[str] = None
    path: Optional[str] = None
    workview_url: Optional[str] = None


@dataclass
class Video(BaseData):
    frame_count: int
    frame_urls: List[str]
    url: Optional[str] = None
    seq: Optional[str] = None
     

@dataclass
class KeyPoint:
    x: float
    y: float


@dataclass
class BoundingBox:
    h: float
    w: float
    x: float
    y: float


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
    datas: List[AnnotationData] = field(default_factory=List)

    def __getattribute__(self, name: str) -> Any:
        """Little hack to create a dictionary of <AnnotationData name>:Any instead of returning <data>: List[AnnotationData]. Useful because we use `asdict` from `dataclasses` that converts all dataclass to dict and it uses the `getatrr` method se we need to override this one"""
        if name == "datas":
            attr = {
                pattern.sub("_", d.__class__.__name__).lower(): asdict(d)
                for d in super().__getattribute__("datas")
            }
        else:
            attr = super().__getattribute__(name)

        return attr

@dataclass
class ImageAnnotationFile:
    dataset: str
    image: Image
    annotations: List[Annotation]

@dataclass
class VideoAnnotationFile:
    dataset: str
    image: Video
    annotations: List[Annotation]



ann = ImageAnnotationFile(
    dataset='foo',
    image=Image(10, 10, "foo", "foo", "foo"),
    annotations=[Annotation("a", [BoundingBox(10, 10, 10, 10), Tag()])],
)
