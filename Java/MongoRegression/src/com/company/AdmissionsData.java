package com.company;
import com.mongodb.DBCollection;
import com.mongodb.DBCursor;
import com.mongodb.MongoClient;
/**
 * Created by themaster on 16/10/12.
 */
public class AdmissionsData {
    private MongoClient mc;
    private DBCollection db;
    public AdmissionsData(MongoClient mc){
        this.mc = mc;
        this.db = mc.getDB("students").getCollection("academics");
    }

    public DBCursor GetDocuments() {
        DBCursor cur = this.db.find();
        return cur;
    }
}
