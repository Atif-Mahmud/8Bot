"""Object returned by `detector.CalibrationDetector.detect`.
Note about indices and index arrays (sparse arrays):
In detector.py, indices are (y, x). This is for ease of processing.
In detector_result.py, indices are (x, y). This is to follow numpy convention.
The conversion happens in `CalibrationDetectorResult.__init__`.
"""
import numpy as np
from matplotlib.patches import Circle, Rectangle


"""Given a float value in [0..1], returns a RGB or BGR 3-tuple mapping the input to a color between 0=red and 1=green"""
_color_gradient_bgr = lambda val: (0, val*2*255, 255) if val < 0.5 else (0, 255, (1-val)*2*255) # Currently unused; useful for working with cv2 draw functions
_color_gradient_rgb = lambda val: (1, val*2, 0) if val < 0.5 else ((1-val)*2, 1, 0)


class CalibrationDetectorResult:
	"""Result of `CalibrationDetector.detect`.
	
	Attributes:
	    centers (numpy.ndarray): Center point of each matched object.
	    scores (numpy.ndarray): The quality of match ([0..1]).
	Args:
	    Passed from CalibrationDetector.
	"""

	def __getitem__(self, key):
		return self.centers[key]

	def __iter__(self):
		return iter(self.centers)

	def __len__(self):
		return len(self.centers)

	def __repr__(self):
		return repr(self.centers)

	def __str__(self):
		return str(self.centers)

	def __init__(self, matches, match_map, pattern):
		self._positions = np.flip(matches, axis=1)

		self.scores = match_map[tuple(np.transpose(matches))]

		self._pattern_shape = np.array(pattern.shape[:2])

		centers = matches + self._pattern_shape // 2
		self.centers = np.flip(centers, axis=1)

	def axPaint(self, ax):
		"""Display the matches' locations on the given `ax` using matplotlib patches.
		
		Args:
		    ax (matplotlib.axes.Axes): The `Axes` to paint onto.
		"""
		pattern_h, pattern_w = self._pattern_shape

		for pos, score, center in zip(self._positions, self.scores, self.centers):
			color = _color_gradient_rgb(score)

			rect = Rectangle(pos, pattern_w, pattern_h, alpha=1, fill=False, color=color)
			point = Circle(center, radius=2, color=color)

			ax.add_patch(rect)
			ax.add_patch(point)