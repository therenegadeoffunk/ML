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
        Student student = new Student();
        BasicDBObject obj = new BasicDBObject("name", student.name)
                .append("sat", student.sat)
                .append("iq", student.iq)
                .append("gpa", student.gpa)
                .append("admit", student.admit);
        collection.insert(obj);
    }
}
