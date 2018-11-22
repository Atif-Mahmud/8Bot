from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import os

import logging

import cv2
import numpy as np

from transform import getPerspectiveTransform
from center_of_shape import get_points

def calibrate(img):
    return getPerspectiveTransform(img, get_points(img), (int(os.getenv("HEIGHT")), int(os.getenv("WIDTH"))))