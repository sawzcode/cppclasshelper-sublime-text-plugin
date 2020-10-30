import os, sublime

class Template:

	def __init__(self, name):
		self._template = None
		self._name = name
		self.file = None


	def load(self, filename):
		# load template file
		self.file = open(filename)

		# reading template
		self._template = self.file.read()

		self.file.close()
		 

	def render(self, **values):
		"""
		:values key, value for replacing template vars
		"""
		self._template = self._template.format(**values)



	@property
	def template(self):
		return self._template


		


