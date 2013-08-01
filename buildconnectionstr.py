def BuildConnectionString(params):
	'''build a connection string from a dictionary of parameters
	
	Returns string'''
	return ";".join(["%s=%s"%(k,v) for k,v in params.items()])

if __name__ == "__main__":
	myParams = {"server":"mpligrim",\
					"database":"master",\
					"uid":"sa",\
					"pwd":"secret"\
					}
	print BuildConnectionString(myParams)
	