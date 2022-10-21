from pymongo import MongoClient
from gridfs import GridFS
client = MongoClient(host="",port=8080)
print("connected to database")
db = client.gridfs
fs = GridFS(db)
grid_out = fs.find({"filename": "prakash.mp4"})
print(grid_out)
data = grid_out['_id'].read()
out = open('prakash.mp4', 'wb')
out.write(data)
out.close()
print("download complete")