import swiftclient as SWIFT
import getpass


class Swift(object):
	def __init__(self):
		# get URL and token to use for requests
		self.auth_info = SWIFT.get_auth('http://192.168.52.2:8080/auth/v1.0/','test:tester','testing')
		self.swift_url = self.auth_info[0]
		self.auth_token = self.auth_info[1]

		self.user = getpass.getuser()
		self.container_name = 'testdir'
	
	def get_acct(self):
		acct_data = SWIFT.get_account(self.swift_url, self.auth_token)
		return acct_data
		
	def get_cont(self, container_name):
		'''Get container info and list objects in container'''
		cont_data = SWIFT.get_container(self.swift_url, self.auth_token, container_name)
		return cont_data
		
	def get_obj(self, container_name, obj_name):
		obj_data = SWIFT.get_object(self.swift_url, self.auth_token, container_name, obj_name)
		return obj_data
		