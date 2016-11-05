package com.company;
import com.mongodb.MongoClient;

import java.io.FileNotFoundException;
import java.util.List;

public class Main {

    public static void main(String[] args) throws FileNotFoundException {
	// write your code here
        MongoClient mongoClient = new MongoClient("localhost", 27017);
        TextData TD = new TextData(mongoClient);
        TD.GetDataFromTextfile();
    }
}
