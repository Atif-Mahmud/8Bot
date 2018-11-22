"""A collection of convenience wrappers around useful `cv2` functions."""
import logging

import cv2


def scaleImage(img, scale, interpolation=None):
	"""Scales the image up or down. 
	
	Args:
	    img (numpy.ndarray): Image to be scaled.
	    scale (float): Factor by which to scale the image.
	    interpolation (int, optional): `cv2.INTER_*` constant. If not provided, automatically selecting the best interpolation method
	        (`cv2.INTER_AREA` for downscaling and `cv2.INTER_CUBIC` for upscaling).
	
	Returns:
	    numpy.ndarray: Scaled image.
	"""
	if interpolation is None:
		if scale < 1: # Pick the right interpolation method for scaling up or down
			interpolation = cv2.INTER_AREA
		else:
			interpolation = cv2.INTER_CUBIC

	new_size = (int(img.shape[1]*scale), int(img.shape[0]*scale))
	output = cv2.resize(img, new_size, interpolation=interpolation)
	return output

def getHsv(img):
	"""Converts the image from BGR to HSV mode."""
	img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	channels = cv2.split(img_hsv)
	return channels

def getHue(img):
	"""Returns a single-channel image representing the hue channel in HSV mode."""
	return getHsv(img)[0]

def getSat(img):
	"""Returns a single-channel image representing the saturation channel in HSV mode."""
	return getHsv(img)[1]

def getVal(img):
	"""Returns a single-channel image representing the value channel in HSV mode."""
	return getHsv(img)[2]

def blur(img, kernel_size=5):
	"""Performs `cv2.GaussianBlur`."""
	return cv2.GaussianBlur(img, (kernel_size, kernel_size))

def canny(img, threshold_low, threshold_ratio=3, gaussian_kernel_size=5, sobel_kernel_size=3):
	"""Performs Canny edge detection, with the gaussian blur step."""
	img = blur(img, gaussian_kernel_size)
	img = cv2.Canny(img, threshold_low, threshold_low*threshold_ratio, sobel_kernel_size)
	return img

def isColorImage(img):
	"""Returns True if the image array is of the shape (y, x, 3), implying that it's probably a BGR image; False otherwise."""
	return (img.ndim == 3 and img.shape[2] == 3)

def grayscale(img):
	"""Converts a BGR image to grayscale."""
	return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

def adaptiveThreshold(img, block_radius=5, c=7):
	"""Performs `cv2.adaptiveThreshold`, converting image to grayscale if it isn't already.
	
	Args:
	    img (numpy.ndarray): Image to perform thresholding on. If color image, will be converted to grayscale.
	    block_radius (int, optional): Radius of the `block_size` parameter passed to `cv2.adaptiveThreshold`.
	    c (int, optional): `c` parameter passed to `cv2.adaptiveThreshold`.
	
	Returns:
	    numpy.ndarray: Thresholded image.
	"""
	if isColorImage(img):
		img = grayscale(img)
	img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, block_radius*2+1, c)
	return img