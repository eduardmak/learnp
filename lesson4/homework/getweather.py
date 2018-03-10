import requests as rq


def get_weather():
	url = 'http://api.data.mos.ru/v1/datasets/2009/rows?api_key='
	api_key = '99addce0a33a70435890e1277d7bbaee'
	r = rq.get(url+api_key)


	
	Cellsz = [i.get("Cells") for i in r.json()]
	Names = [i.get("Name") for i in Cellsz]

	print (Names)

if __name__ == '__main__':
	get_weather()