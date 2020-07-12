#import requests and json for retrieving and parsing temparature


import requests,json
#URL for Current Weather
api_url="https://api.openweathermap.org/data/2.5/weather"

api_key="paste your api key here,this APIkey in code will change"

def get_query_params(city_name):

	params=dict()
	params["q"]=city_name
	params["appid"]=api_key

	return params

def get_weather(params):

	try:

		response=requests.get(url=api_url,params=params)
		return response

	except:

		print("Unable to retrive Data from the API Server")

	

def parse_response(response):

	if response==None:
		return None

	content_type='application/json; charset=utf-8'
	
	if response.headers["Content-Type"]!=content_type:

		print("Error in retrieving the temparature")
		return

	data=json.loads(response.text)
	
	if data['cod']==200:


		print(data["name"])
		print(data["main"]["temp"],data["weather"][0]["main"],data["weather"][0]["description"])
		try:

			country=data["sys"]["country"]
		except:
			country=""
		
		details_temp=[data["name"],country,round(data["main"]["temp"]-270,2),data["weather"][0]["main"],data["weather"][0]["description"]]
		details=details_temp.copy()
		del details_temp
		return details


	elif data["cod"]==401:

		return 401

		print("Invalid API key")

	elif data["cod"]=="404":

		return 404

		print("City not found")

	else:

		return -1

		print("Error in retrieving the data")

def call_api(city):
	params=get_query_params(city)
	response=get_weather(params)
	return parse_response(response)

def return_temp_to_excel(cities):
	city_temp=list()
	for city in cities:
		resp=call_api(city)
		try:
			if len(resp)==5:
				city_temp.append(resp[2])
		except:
			city_temp.append("None")

	temp_list=city_temp.copy()
	del city_temp
	return temp_list





