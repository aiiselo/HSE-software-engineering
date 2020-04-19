package com.company;
import java.io.*;
import java.util.*;

public class CountLetters {
    public static <str> void main(String[] args) throws IOException, FileNotFoundException {
        String pathName = "/Users/olesyamartinyuk/Downloads/inputfile.txt";
        try {
            FileInputStream directory = new FileInputStream(pathName);
            Map<Character, Integer> dict = new HashMap<Character, Integer>();
            int i = -1;
            while ((i = directory.read()) != -1) {
                if ((char) i >= 'A' && (char) i <= 'Z' | (char) i >= 'a' && (char) i <= 'z') {
                    if (dict.get(Character.toUpperCase((char) i)) == null) {
                        dict.put(Character.toUpperCase((char) i), 1);
                    } else {
                        int newValue = (int) dict.get(Character.toUpperCase((char) i)) + 1;
                        dict.put(Character.toUpperCase((char) i), newValue);
                    }
                }
            }
            FileWriter writer = new FileWriter("/Users/olesyamartinyuk/Downloads/outputfile.txt", false);
            try {
                for (Map.Entry<Character, Integer> item : dict.entrySet()) {
                    writer.write(item.getKey() + " " + item.getValue() + "\n");
                }
                writer.flush();
            } catch (IOException ex) {
                System.out.println(ex.getMessage());
            }
        }
        catch (FileNotFoundException ex){
            System.out.println(ex.getMessage());
        }
    }
}
