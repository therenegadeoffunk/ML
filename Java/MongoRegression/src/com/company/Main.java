package com.company;
import com.mongodb.DB;
import com.mongodb.DBCollection;
import com.mongodb.MongoClient;
import java.util.List;

public class Main {

    public static void main(String[] args) {

        // Lets see if we can't just connect and run a simple query
        String output;
        MongoClient mongoClient = new MongoClient("localhost", 27017);
        DB db = mongoClient.getDB("students");
        DBCollection collection = db.getCollection("academics");
        StudentGenerator g = new StudentGenerator(mongoClient);
        List<Student> students = g.GenerateStudents(100);
        g.InsertStudents(students);
        output = collection.findOne().toString();
        System.out.println(output);
        mongoClient.close();
        return;
    }
}
