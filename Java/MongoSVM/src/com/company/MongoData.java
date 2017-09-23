package com.company;
import com.mongodb.BasicDBObject;
import com.mongodb.DBCollection;
import com.mongodb.MongoClient;

public class MongoData {
    private MongoClient mc;
    private DBCollection c;
}

private MongoData(MongoClient mongoClient) {
    this.mc = mongoClient;
    this.c = this.mc.getDB("testdb").getCollection("mail");
}

private GetCollectionData(String collection) {
    BasicDBObject k = new BasicDBObject();
    BasicDBObject i = new BasicDBObject("_id");
    BasicDBObject o = new BasicDBObject("0");
    BasicDBObject query;
    query = k(i(o));
}