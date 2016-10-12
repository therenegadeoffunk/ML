package com.company;
import com.mongodb.DBCollection;
import com.mongodb.MongoClient;
import com.mongodb.BasicDBObject;
import java.util.List;
import java.util.ArrayList;

public class StudentGenerator {
    private MongoClient mc;
    private DBCollection c;

    public StudentGenerator(MongoClient mongoClient){
        this.mc = mongoClient;
        this.c = this.mc.getDB("students").getCollection("academics");
    }

    public List<Student> GenerateStudents(Integer numStudents){
        List<Student> students = new ArrayList<Student>();
        Integer i;
        for (i = 1; i < numStudents; i++) {
            Student s = new Student();
            students.add(s);
        }
        return students;
    }

    public void InsertStudents(List<Student> students) {
        for (Student s : students ) {
            InsertStudent(s);
        }
    }

    public void InsertStudent(Student student) {
        BasicDBObject obj = new BasicDBObject("name", student.name)
                .append("sat", student.sat)
                .append("iq", student.iq)
                .append("gpa", student.gpa)
                .append("admit", student.admit);
        this.c.insert(obj);
    }
}
