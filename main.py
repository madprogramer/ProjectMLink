import uuid

linkNames = dict()
linkIds = dict()

#print(uuid.uuid4())

testArray=["puppy.com","hash.tag","https://github.com/madprogramer/ProjectMLink/upload/master","b.b","horse.hoof"]

for link in testArray:
	print("New Link: {}\nAttempting to generate uuid...".format(link))
	
	newid=str(uuid.uuid4())
	print(newid)
	while newid in linkIds:
		newid=str(uuid.uuid4())
		print(newid)

	linkNames[newid]=link
	linkIds[link]=newid

	print (linkNames)
	print (linkIds)
