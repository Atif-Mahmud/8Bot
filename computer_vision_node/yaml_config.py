"""This module deals with loading and using YAML configuration files."""
from yaml import safe_load # See http://pyyaml.org/wiki/PyYAMLDocumentation


class YAMLDict (dict):
	"""A subclass of dict whose values can also be accessed as attributes. That is, `a["b"]["c"]` can instead be written as `a.b.c`."""
	def __init__(self, obj):
		obj = {key: YAMLObject(value) for key, value in obj.items()}
		dict.__init__(self, obj)

	def __getattr__(self, name):
		return dict.__getitem__(self, name)


class YAMLList (list):
	"""A subclass of list which converts dict values to YAMLDict values."""
	def __init__(self, obj):
		obj = [YAMLObject(item) for item in obj]
		list.__init__(self, obj)


def YAMLObject(obj):
	"""Constructs a YAMLDict or a YAMLList if the object is of the corresponding type, otherwise returns the object as-is."""
	if type(obj) is dict:
		return YAMLDict(obj)
	elif type(obj) is list:
		return YAMLList(obj)
	else:
		return obj


def loadYAML(path):
	"""Loads a YAML file at the specified path, and returns it as a YAMLObject.
	
	Args:
	    path (str): Path to the YAML file.
	
	Returns:
	    YAMLDict or YAMLList: The root item in the specified file, as a YAMLObject.
	"""
	with open(path) as file:
		obj = safe_load(file)
	return YAMLObject(obj)