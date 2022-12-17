from typing import Union,Dict
from pydantic import BaseModel
import pydantic

class ImagesFromCLients(BaseModel):
    img_data_str : str = None
    class Config: 
        schema_extra = {
                'example': {
                    'image': ('iVBORw0KGgoAAAANSUhEUgAAAAoAAAAKCAIAAAACUFjqAAAACXBIWXMAAC4jAAAuIwF4pT92AAAA'
                                'B3RJTUUH5AwZAyMzqt+uDgAAABVJREFUGNNj/P//PwNuwMSAF4xUaQCl4wMR/9A5uQAAAABJRU5E'
                                'rkJggg==')
                }
            }

class Respone_type(BaseModel):
    img_data_str : str = None
    messeage : str = None  