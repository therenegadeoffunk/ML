package com.company;
import com.mongodb.DB;
import com.mongodb.DBCollection;
import com.mongodb.MongoClient;
import com.mongodb.BasicDBObject;

public class StudentGenerator {
    private MongoClient mc;

    public StudentGenerator(MongoClient mongoClient){
        this.mc = mongoClient;
    }

    public void InsertStudents() {
        DB db = this.mc.getDB("students");
        DBCollection collection = db.getCollection("academics");
        BasicDBObject obj = new BasicDBObject("name", "dude")
                .append("sat", 1800)
                .append("iq", 105)
                .append("gpa", 3.0)
                .append("admit", 0);
        collection.insert(obj);
    }
}
