"""
Note about indices and index arrays (sparse arrays):
In detector.py, indices are (y, x). This is for ease of processing.
In detector_result.py, indices are (x, y). This is to follow numpy convention.
The conversion happens in `CalibrationDetectorResult.__init__`.
"""
import logging

import cv2
import numpy as np
from sklearn.cluster import MeanShift

from detector_result import CalibrationDetectorResult


class CalibrationDetector:
	"""Performs template matching and clustering, to find the 4 calibration points.
	
	Attributes:
	    clustering_bandwidth (float): Bandwidth for `MeanShift` clusterer.
	    match_method (int): `cv2.TM_*` constant for template matching. Default `cv2.TM_CCOEFF_NORMED`.
	    match_threshold (float): Threshold for matches to be considered candidates.
	        Ideally, this should be as high as possible while still capturing all calibration points, because the clusterer's runtime increases quadratically with number of points.
	"""
	def __init__(self, params=None, **kwargs):
		# Available parameters:
		self.clustering_bandwidth = 40
		self.match_method = cv2.TM_CCOEFF_NORMED
		self.match_threshold = 0.8

		# Combine params and kwargs -- Use params dict and/or kwargs to seed parameters.
		if params is None:
			params = {}
		params.update(kwargs)

		# For each parameter given in params or kwargs, tries to set the corresponding attribute on self,
		# raising an error if the attribute doesn't exist.
		for name, value in params.items():
			if name in self.__dict__:
				self.__dict__[name] = value # self.__dict__["x"] is like self.x
			else:
				raise AttributeError("Unknown parameter: " + name)

		# Initialize a MeanShift clusterer from sklearn.
		self._clusterer = MeanShift(self.clustering_bandwidth)

	def _bestMatches(self, match_map, candidates, labels):
		"""Finds the highest-scoring point in each cluster."""
		num_matches = len(np.unique(labels))
		min_errors = np.zeros(num_matches, dtype=match_map.dtype)
		best_matches = np.zeros((num_matches, 2), dtype=candidates.dtype)

		for candidate, label in zip(candidates, labels):
			error = match_map[tuple(candidate)]
			if error > min_errors[label]:
				min_errors[label] = error
				best_matches[label] = candidate

		return best_matches

	def detect(self, img, pattern):
		"""Performs template matching and clustering, and returns a CalibrationDetectorResult object encapsulating the results."""
		match_map = cv2.matchTemplate(img, pattern, self.match_method) # Call the cv2 function that does the template matching.
		candidates = np.transpose(np.where(match_map > self.match_threshold)) # Get all the matched points that were above the threshold.

		# If there were no matches, warn and return None.
		if 0 in candidates.shape:
			logging.warning("0 matches detected")
			return

		# Use the MeanShift clusterer to eliminate multiple "matches" for the same object.
		self._clusterer.set_params(bandwidth=self.clustering_bandwidth)
		self._clusterer.fit(candidates)

		# Find the highest-scoring point in each cluster and treat that as the "match".
		labels = self._clusterer.labels_
		matches = self._bestMatches(match_map, candidates, labels)

		# Encapsulate and return.
		return CalibrationDetectorResult(matches, match_map, pattern)