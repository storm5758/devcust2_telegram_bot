from redminelib import Redmine
import requests
import pprint
redmine=Redmine('http://95.213.191.121/',username='admin',password='3ek3o7v1hx')

users = redmine.user.filter(status=3)
lst=list(users)
lst1=list()
for x in lst:
	lst1.append(x.custom_fields[0].value)
for x in lst1:
	print(x)

