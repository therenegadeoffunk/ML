package com.company;
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Arrays;
import com.mongodb.DBCollection;
import com.mongodb.MongoClient;
import com.mongodb.BasicDBObject;

import java.util.List;
import java.util.Scanner;

public class TextData {
    private MongoClient mc;
    private DBCollection c;

    private TextData(MongoClient mongoClient) {
        this.mc = mongoClient;
        this.c = this.mc.getDB("testdb").getCollection("mail");
    }

    private void InsertLinesAsDocs(String PATH) throws FileNotFoundException {
        Scanner s = new Scanner(new File(PATH));
        while (s.hasNextLine()) {
            List<String> f;
            f = Arrays.asList(s.nextLine().split(","));
            InsertLineAsDoc(f);
        }
        s.close();
    }

    private void InsertLineAsDoc(List LINE) {
        BasicDBObject obj = new BasicDBObject("x", LINE.get(0))
                .append("y", LINE.get(1));
        this.c.insert(obj);
    }

    private void GetDataFromTextfile() throws FileNotFoundException {
        String PATH;
        PATH = "Data/svm_data_1.txt";
        InsertLinesAsDocs(PATH);
    }
}
