package com.company;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.stream.Stream;

public class TextData {
    public TextData() {
    }

    public void GetDataFromTextfile() {
        String PATH;
        PATH = "Data/svm_data_1.txt";
        try (Stream<String> stream = Files.lines(Paths.get(PATH))) {
            stream.forEach(System.out::println);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
