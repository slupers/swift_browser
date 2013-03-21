import swiftclient as SWIFT
import getpass

# get URL and token to use for requests
auth_info = SWIFT.get_auth('http://192.168.52.2:8080/auth/v1.0/','test:tester','testing')
swift_url = auth_info[0]
auth_token = auth_info[1]

user = getpass.getuser()
container_name = 'testdir'
obj_name = 'testobj'
contents = 'test content of testobj'
element_id = 23


# delete an object
#rv = SWIFT.delete_object(swift_url, auth_token, container_name, obj_name+str(13))
#print rv

# delete a container
#rv = SWIFT.delete_object(swift_url, auth_token, container='testdir')
#print rv

# create a container
"""
element_id += 1
container_meta = {'X-Container-Meta-ID' : element_id, 'X-Container-Meta-Creator' : user}
rv = SWIFT.put_container(swift_url, auth_token, container_name, headers=container_meta )
print 'put_container:', rv
"""

# get container info
stats = SWIFT.head_container(swift_url, auth_token, container_name)
print 'stats for testdir:', stats

# store 10 objects

for x in xrange(10):
	# create an object
	element_id += 1
	object_meta = {'X-Object-Meta-ID' : element_id, 'X-Object-Meta-Creator' : user}
	obj_etag = SWIFT.put_object(swift_url, auth_token, container=container_name, name=obj_name+str(element_id), contents=contents, headers=object_meta )
	print 'put_object:', obj_etag


"""
# get container info and list objects in container
objs = SWIFT.get_container(swift_url, auth_token, container_name, marker='testobj10')
print 'dir size:', objs[0]['x-container-bytes-used']
for obj in objs[1]:
	print obj['name']
"""

