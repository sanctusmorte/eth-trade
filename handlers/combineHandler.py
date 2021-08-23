import pandas as pd


class handler:
	
	files = []
	frames = []
	
	def __init__(self, files):
		self.files = files
	
	def combine_all_datasets(self):
		for i in range(0, len(self.files)):
			self.frames.append(self.get_one_df(self.files[i]))
		return pd.concat(self.frames)
		
	def get_one_df(self, df_path):
		return pd.read_csv(df_path)