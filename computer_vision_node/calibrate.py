"""In theory, all other python modules in this package (other than the `main` files of course) are general enough to be useful for any CV project.
This module steps down one level of generalization, and provides functions that each perform one step of the specific task of finding sensors on a calibrated tray."""
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())
import os

import logging

import cv2
import numpy as np

from cvutils import scaleImage
from cvutils import adaptiveThreshold

from detector import CalibrationDetector

from transform import getPerspectiveTransform

def loadImage(path, scale=1, color=True):
	"""Loads an image by path at a specified scale."""
	mode = cv2.IMREAD_COLOR if color else cv2.IMREAD_GRAYSCALE
	img = cv2.imread(path, mode)
	if img is None:
		raise FileNotFoundError("No such file: " + path)
	img = scaleImage(img, scale)
	return img

def calibrate(img, params):
	"""Given an uncalibrated image (with 4 calibration points visible), finds the 4 calibration points and transforms the image into a calibrated image.
	
	Args:
	    img (numpy.ndarray): Image to be transformed.
	    params (yaml_config.YAMLDict): Data loaded from `parameters.yml`.
	    tray (tray.TrayDefinition): `TrayDefinition` object which determines the height/width of the output image.
	
	Returns:
	    numpy.ndarray: Transformed image, of the shape (tray.height, tray.width, 3) for color images, or (tray.height, tray.width) for grayscale images.
	"""
	pattern = loadImage(**params.calibration_detector.pattern)

	# First, pass both the image and the pattern through an adaptiveThreshold filter.
	detector_img = adaptiveThreshold(img, **params.calibration_detector.preprocessing)
	pattern = adaptiveThreshold(pattern, **params.calibration_detector.preprocessing)

	# Detect calibration points.
	detector = CalibrationDetector(**params.calibration_detector.detector)
	result = detector.detect(detector_img, pattern)

	# Assuming at least 4 calibration points found...
	if len(result) < 4:
		logging.error("Only found %d out of 4 required calibration points." %(len(result)))
		return

	# PerspectiveTransform the image and return.
	transform = getPerspectiveTransform(img, result[:4], (int(os.getenv("HEIGHT")), int(os.getenv("WIDTH"))))
	
	return transform