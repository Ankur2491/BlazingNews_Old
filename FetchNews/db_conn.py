from pymongo import MongoClient
import json
client = MongoClient('localhost:27017')
db = client.admin
collection = db.News
all_file = open("data/all.txt","r")
buss_file = open("data/buss.txt","r")
ent_file = open("data/ent.txt","r")
gen_file = open("data/gen.txt","r")
health_file = open("data/health.txt","r")
sci_file = open("data/sci.txt","r")
spo_file = open("data/spo.txt","r")
tech_file = open("data/tech.txt","r")
all_news = json.loads(all_file.read())
buss_news = json.loads(buss_file.read())
ent_news = json.loads(ent_file.read())
gen_news = json.loads(gen_file.read())
health_news = json.loads(health_file.read())
sci_news = json.loads(sci_file.read())
spo_news = json.loads(spo_file.read())
tech_news = json.loads(tech_file.read())
data = [all_news,gen_news,buss_news,ent_news,health_news,sci_news,spo_news,tech_news]
sample = open("data/sample.txt","w")
sample.write("{\"news\":"+json.dumps(data)+"}")
sample.close()
final_file = open("data/sample.txt","r")
final_data = json.loads(final_file.read())
final_file.close()
all_file.close()
buss_file.close()
ent_file.close()
gen_file.close()
health_file.close()
sci_file.close()
spo_file.close()
tech_file.close()
rec_id = collection.insert_one(final_data)
print("Data Inserted with record id",rec_id)
