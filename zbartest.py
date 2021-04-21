from pyzbar.pyzbar import decode
import os
import sys
from PIL import Image
from dataclasses import dataclass
from services.zbar_service import ZbarService



file = sys.argv[1]

service = ZbarService()
data = service.detectZbars(file)
print(data)