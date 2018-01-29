from time import time

def functime(views):
	def ctime(request):
		start = time()
		views(request)
		end = time()
		print(end-start)
		return views(request)
	return ctime
