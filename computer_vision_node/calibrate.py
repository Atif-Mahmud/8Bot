"""In theory, all other python modules in this package (other than the `main` files of course) are general enough to be useful for any CV project.
This module steps down one level of generalization, and provides functions that each perform one step of the specific task of finding sensors on a calibrated tray."""
import logging

import cv2
import numpy as np

from cvutils import scaleImage

def loadImage(path, scale=1, color=True):
	"""Loads an image by path at a specified scale."""
	mode = cv2.IMREAD_COLOR if color else cv2.IMREAD_GRAYSCALE
	img = cv2.imread(path, mode)
	if img is None:
		raise FileNotFoundError("No such file: " + path)
	img = scaleImage(img, scale)
	return img