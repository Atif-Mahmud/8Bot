"""This module includes a function and the class which it returns, which wrap opencv's perspective (non-affine) transformation modules."""
import cv2
import numpy as np

class PerspectiveTransform:
	"""Encapsulates a 3x3 transform matrix calculated by `cv2.getPerspectiveTransform`, and provides convenience methods that wrap `cv2.warpPerspective` and `cv2.perspectiveTransform`."""
	def __init__(self, matrix, image_shape):
		self.matrix = matrix
		self.image_shape = image_shape

	def transformImage(self, img):
		"""Wrapper around `cv2.warpPerspective`, which takes an image and outputs a transformed image."""
		return cv2.warpPerspective(img, self.matrix, self.image_shape)

	def transformPoints(self, points):
		"""Wrapper around `cv2.perspectiveTransform`, which takes an array of points (sparse array) and transforms each point."""
		return cv2.perspectiveTransform(points, self.matrix)

	def __call__(self, array):
		"""Convenience method. Automatically determines whether it's called on a points (sparse) array or an array representing an image, and transforms it accordingly.
		
		Args:
		    array (numpy.ndarray): If it's a points (sparse) array, uses `cv2.perspectiveTransform`. If it's an image array, uses `cv2.warpPerspective`.
		
		Returns:
		    numpy.ndarray: The points array or image array, transformed.
		"""
		if array.shape[1] == 2 and array.ndim == 2:
			return self.transformPoints(array)
		elif array.ndim == 2 or array.ndim == 3:
			return self.transformImage(array)
		else:
			raise TypeError("Argument not recognized as an image array or points (sparse) array.")

	def __repr__(self):
		return repr(self.matrix)

	def __str__(self):
		return str(self.matrix)