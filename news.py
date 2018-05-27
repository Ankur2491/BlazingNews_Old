from pymongo import MongoClient
import requests
import json
import time
client = MongoClient('localhost:27017')
db = client.admin
collection = db.News
while True:
    all_news = open("./FetchNews/data/all.txt","w")
    buss_news = open("./FetchNews/data/buss.txt","w")
    ent_news = open("./FetchNews/data/ent.txt","w")
    gen_news = open("./FetchNews/data/gen.txt","w")
    health_news = open("./FetchNews/data/health.txt","w")
    sci_news = open("./FetchNews/data/sci.txt","w")
    spo_news = open("./FetchNews/data/spo.txt","w")
    tech_news = open("./FetchNews/data/tech.txt","w")
    all_url = ('https://newsapi.org/v2/top-headlines?'
       'sources=bbc-news,business-insider,buzzfeed,cnn,cnbc,reuters,the-hindu,the-times-of-india&'
       'language=en&'
       'pageSize=100&'
       'apiKey=')
    buss_url = ('https://newsapi.org/v2/top-headlines?'
       'country=in&'
       'language=en&'
       'pageSize=100&'
       'category=business&'
       'apiKey=')
    ent_url = ('https://newsapi.org/v2/top-headlines?'
       'country=in&'
       'language=en&'
       'pageSize=100&'
       'category=entertainment&'
       'apiKey=')
    gen_url = ('https://newsapi.org/v2/top-headlines?'
       'country=in&'
       'language=en&'
       'pageSize=100&'
       'category=general&'
       'apiKey=')
    health_url = ('https://newsapi.org/v2/top-headlines?'
       'country=in&'
       'language=en&'
       'pageSize=100&'
       'category=health&'
       'apiKey=')
    sci_url = ('https://newsapi.org/v2/top-headlines?'
       'country=in&'
       'language=en&'
       'pageSize=100&'
       'category=science&'
       'apiKey=')
    spo_url = ('https://newsapi.org/v2/top-headlines?'
       'country=in&'
       'language=en&'
       'pageSize=100&'
       'category=sports&'
       'apiKey=')
    tech_url = ('https://newsapi.org/v2/top-headlines?'
       'country=in&'
       'language=en&'
       'pageSize=100&'
       'category=technology&'
       'apiKey=')
    response = requests.get(all_url)
    json_response = response.content
    parsed_response = json.loads(json_response)
    str_response = json.dumps(parsed_response)
    all_news.write(str_response)
    all_news.close()

    response = requests.get(buss_url)
    json_response = response.content
    parsed_response = json.loads(json_response)
    str_response = json.dumps(parsed_response)
    buss_news.write(str_response)
    buss_news.close()

    response = requests.get(ent_url)
    json_response = response.content
    parsed_response = json.loads(json_response)
    str_response = json.dumps(parsed_response)
    ent_news.write(str_response)
    ent_news.close()

    response = requests.get(gen_url)
    json_response = response.content
    parsed_response = json.loads(json_response)
    str_response = json.dumps(parsed_response)
    gen_news.write(str_response)
    gen_news.close()

    response = requests.get(health_url)
    json_response = response.content
    parsed_response = json.loads(json_response)
    str_response = json.dumps(parsed_response)
    health_news.write(str_response)
    health_news.close()

    response = requests.get(sci_url)
    json_response = response.content
    parsed_response = json.loads(json_response)
    str_response = json.dumps(parsed_response)
    sci_news.write(str_response)
    sci_news.close()

    response = requests.get(spo_url)
    json_response = response.content
    parsed_response = json.loads(json_response)
    str_response = json.dumps(parsed_response)
    spo_news.write(str_response)
    spo_news.close()

    response = requests.get(tech_url)
    json_response = response.content
    parsed_response = json.loads(json_response)
    str_response = json.dumps(parsed_response)
    tech_news.write(str_response)
    tech_news.close()
    all_file = open("./FetchNews/data/all.txt","r")
    buss_file = open("./FetchNews/data/buss.txt","r")
    ent_file = open("./FetchNews/data/ent.txt","r")
    gen_file = open("./FetchNews/data/gen.txt","r")
    health_file = open("./FetchNews/data/health.txt","r")
    sci_file = open("./FetchNews/data/sci.txt","r")
    spo_file = open("./FetchNews/data/spo.txt","r")
    tech_file = open("./FetchNews/data/tech.txt","r")
    all_news = json.loads(all_file.read())
    buss_news = json.loads(buss_file.read())
    ent_news = json.loads(ent_file.read())
    gen_news = json.loads(gen_file.read())
    health_news = json.loads(health_file.read())
    sci_news = json.loads(sci_file.read())
    spo_news = json.loads(spo_file.read())
    tech_news = json.loads(tech_file.read())
    data = [all_news,gen_news,buss_news,ent_news,health_news,sci_news,spo_news,tech_news]
    sample = open("./FetchNews/data/sample.txt","w")
    sample.write("{\"news\":"+json.dumps(data)+"}")
    sample.close()
    final_file = open("./FetchNews/data/sample.txt","r")
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
    time.sleep(600)
