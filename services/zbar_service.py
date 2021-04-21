from typing import List
from pyzbar.pyzbar import decode
from PIL import Image
import ujson
from dataclasses import dataclass, field

@dataclass
class ZbarData:
    data: str = ''
    barcodeType: str = ''
    left: int = 0
    top: int = 0
    width: int = 0
    height: int = 0
    polygon: List = field(default_factory=lambda: [])



@dataclass
class Point:
    x: int = 0
    y: int = 0



class ZbarService:
    
    def detectZbars(self, imgPath: str) -> List:
        img = Image.open(imgPath)
        details = decode(img)
        barcodes = []
        if not details:
            raise Exception('No barcode detected')
        else:
            # print(details)
            for detail in details:
                data = ZbarData(detail.data.decode(), detail.type,
                                detail.rect.left, detail.rect.top, 
                                detail.rect.width, detail.rect.height)
                polygons = detail.polygon
                points = []
                for polygon in polygons:
                    point = Point(polygon.x, polygon.y)
                    points.append(point)
                
                data.polygon = points
                barcodes.append(data)
            return barcodes
                
        