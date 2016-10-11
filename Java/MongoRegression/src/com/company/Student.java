package com.company;
import java.util.Random;

public class Student {
    public String name;
    public Integer sat;
    public Integer iq;
    public double gpa;
    public Integer admit;
    public Student() {
        this.iq = InitIQ();
        this.sat = InitSAT(this.iq);
        this.gpa = InitGPA(this.iq);
        this.admit = InitAdmit(this.sat, this.gpa);
        this.name = InitName();
    }
    private Integer InitIQ(){
        Integer IQ;
        Random random = new Random();
        IQ = random.nextInt(80) + 80;
        return IQ;
    }

    private Integer InitSAT(Integer IQ) {
        /*
        For now we will very naively assume
        that SAT score is a simple function
        of IQ
        */
        Integer SAT = IQ * 12;
        if (SAT > 1600) {
            SAT = 1600;
        }
        return SAT;
    }

    private double InitGPA(Integer IQ) {
        // Same assumption as above
        double GPA = (float) IQ / 32.0;
        return GPA;
    }

    private Integer InitAdmit(Integer sat, double gpa){
        Integer Admit;
        if ((gpa > 3.6 ) && (sat > 1400)) {
            Admit = 1;
        }
        else {
            Admit = 0;
        }
        return Admit;
    }

    private String InitName() {
        // TODO: Make this less dumb
        Random random = new Random();
        String Name = "Muh name" + Integer.toString(random.nextInt(1000));
        return Name;
    }
}
