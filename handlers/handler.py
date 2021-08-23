import datasetHandler
import numpy as np

MAIN_PATH = 'E:/Jupyter_notebook/trading/data/4/ETHUSDT'

save_paths = {
	'/Order_Book': 'order_book_dataset_4.csv',
	'/Kdata': 'k_data_dataset_1.csv',
	'/Trades': 'trades_dataset_4.csv',
}

paths = [
	#'/Order_Book',
	'/Kdata',
	#'/Trades'
]

for i in range(0, len(paths)):
	df = datasetHandler.handler(MAIN_PATH + paths[i]).get_dataset()
	column_to_sort = 'time'
	if paths[i] == '/Kdata':
		df = df[df['Volume'].notna()]
		#column_to_sort = 'Open time'
	df.drop_duplicates(subset=column_to_sort, keep='first', inplace=True)
	df.sort_values(column_to_sort, inplace=True)
	df.to_csv('E:/Jupyter_notebook/trading/data_handled/' + save_paths[paths[i]], index=False)