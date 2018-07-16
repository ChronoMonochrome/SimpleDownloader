import minidb

class Downloads(minidb.Model):
	url = str
	filename = str
	status = str
	size = int
	description = str

db = minidb.Store("downloads.db")
db.register(Downloads)
d = Downloads(url='Hello World', filename='minidb@example.com', status="Paused", size = 2048, description = "")
d.save(db)
db.close()
