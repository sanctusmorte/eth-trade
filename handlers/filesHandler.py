from os import listdir
from os.path import isfile, join
from pathlib import Path


class handler:
	
	files = []
	
	# init функция
	# проверяем сущестовавание директории по пути, который задан в переменной directory_path
	# если такая директория существует, то мы получаем все файлы, которые находятся в этой директории
	def __init__(self, directory_path):
		file = Path(directory_path)
		if not file.exists() or not file.is_dir():
			print('File with Order_book datasets do not exist or it is not directory!')
			exit()
		else:
			self.directory_path = directory_path
			self.files = [f for f in listdir(directory_path) if isfile(join(directory_path, f))]
	
	def get_files_from_directory(self):
		self.set_path_to_files()
		return self.files
	
	# у каждого файла, который мы получили, необходимо изменить название,
	# дописав абсолютный путь (директория + слэш + название файла с расширением)
	def set_path_to_files(self):
		for i in range(0, len(self.files)):
			self.files[i] = self.directory_path + '/' + self.files[i]
