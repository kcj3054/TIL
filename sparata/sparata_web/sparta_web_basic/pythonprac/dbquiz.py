from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta


movie = db.movies.find_one({'title':'매트릭스'})
tartgetSatr = movie['star']

tartget_movies = list(db.movies.find({'star':tartgetSatr},{'_id':False}))

for movie in tartget_movies:
    db.movies.update_one({'title': '매트릭스'}, {'$set': {'star': '0'}})
    print(movie['title'])



# 저장 - 예시
doc = {'name':'bobby','age':21}
db.users.insert_one(doc)

# 한 개 찾기 - 예시
user = db.users.find_one({'name':'bobby'})

# 여러개 찾기 - 예시 ( _id 값은 제외하고 출력)
same_ages = list(db.users.find({'age':21},{'_id':False}))

# 바꾸기 - 예시
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# 지우기 - 예시
db.users.delete_one({'name':'bobby'})