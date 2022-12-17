import base64
import sys
import requests, json
import os
import uvicorn
import cv2
import numpy as np 
import uvicorn
import matplotlib.pyplot as plt

from logbook import Logger
from fastapi import Depends, HTTPException, Request, APIRouter, BackgroundTasks
from fastapi import responses, status
from fastapi.responses import JSONResponse, StreamingResponse, HTMLResponse
from jsonschema import ValidationError
from io import BytesIO
from PIL import Image, ImageDraw
from pathlib import Path
import streamlit as st

from dataset_procesing import load_dataset
from utility import login_function, recognize_function
from class_object import ImagesFromCLients, Respone_type

logger = Logger(__name__)
router = APIRouter()

dataset = load_dataset()

def img_str_to_np_array(img_base64_string):
    img_bytes = base64.b64decode(img_base64_string)
    img_bytesIO = BytesIO(img_bytes)
    img_bytesIO.seek(0)
    image = Image.open(img_bytesIO)
    img_np_arr = np.array(image)
    return img_np_arr


def img_to_base64(img_result):
    img_result = Image.fromarray(img_result)
    img_result_bytes = BytesIO()
    img_result.save(img_result_bytes, format="PNG")
    img_result_bytes = img_result_bytes.getvalue()
    img_result_base64_bytes = base64.b64encode(img_result_bytes)
    img_result_base64_str = img_result_base64_bytes.decode("ascii")
    return img_result_base64_str


@router.post("/start/login_function/", response_model=Respone_type)
def colorization_model1_function(img_upload : ImagesFromCLients):
    img_np_arr = img_str_to_np_array(img_upload.img_data_str)
    name = 'duong'
    messeage = 'login fail'
    login_result = login_function(img_np_arr, name)
    if login_result:
        dataset = load_dataset()
        messeage = "Login success"

    img_result_base64_str = img_to_base64(img_np_arr)
    result_message = {"img_data_str": img_result_base64_str, "messeage": messeage}
    return result_message


@router.post("/start/recognize_function/", response_model=Respone_type)
def colorization_model2_function(img_upload : ImagesFromCLients):
    img_np_arr = img_str_to_np_array(img_upload.img_data_str)

    messeage = 'recognize fail'
    name, confident = recognize_function(img_np_arr, dataset)
    if name is not None:
        messeage = f"recognize success {name} {confident}"

    img_result_base64_str = img_to_base64(img_np_arr)
    result_message = {"img_data_str": img_result_base64_str, "messeage": messeage}
    return result_message
