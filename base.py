# -*- coding: utf-8 -*-

import json
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

#Ignore SSH Warning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)



class APIKeyError(Exception):
	pass


class Fortify(object):

	BASIC_AUTH = "Basic " # Enter base64 encoded credentials here
	headers = {'Authorization': BASIC_AUTH ,'Content-Type': 'application/json','Accept': 'application/json','Connection': 'close'}
	BASE_PATH=''
	URLS = {}

	def __init__(self):
		self.base_uri = 'https://fortify.target.com/ssc/api'
		self.base_uri += '/{version}'.format(version='v1')

	def _get_path(self,key):
		return self.BASE_PATH+self.URLS[key]

	def _get_id_path(self,key):
		return self._get_path(key)

	def _get_complete_url(self,path):
		return '{base_uri}{path}'.format(base_uri=self.base_uri, path=path)

	def _get_params(self,params):
		api_dict={}
		if params:
			params.update(api_dict)
		else:
			params=api_dict
		return params

	def _request(self,method,path,params=None,payload=None):
		url= self._get_complete_url(path)
		params = self._get_params(params)

		response = requests.request(method,url,params=params,data=json.dumps(payload) if payload else payload, headers=self.headers,verify=False)

		response.raise_for_status()
		response.encoding = 'utf-8'
		return response.json()

	def _GET(self,path,params=None):
		return self._request('GET',path,params=params)

	def _POST(self,path,params=None,payload=None):
		return self._request('POST',path,params=params,payload=payload)

	def _DELETE(self,path,params=None,payload=None):
		return self._request('DELETE',path,params=params,payload=payload)

	def _set_attrs_to_values(self,response={}):
		if isinstance(response,dict):
			for key in response.keys():
				setattr(self,key,response[key])

