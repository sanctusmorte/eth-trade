import filesHandler
import combineHandler
import pandas as pd

class handler:
	
	files = []
	
	def __init__(self, directory_path):
		self.files = filesHandler.handler(directory_path).get_files_from_directory()
	
	# возвращает объединенный датасет order_book
	def get_dataset(self):
		return combineHandler.handler(self.files).combine_all_datasets()
