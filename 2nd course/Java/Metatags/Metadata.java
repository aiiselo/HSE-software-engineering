package com.company.Metatags;

import java.awt.*;
import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.HashSet;
import java.util.Scanner;

public class Metadata {
    public static void printMenu(){
        System.out.println("\nMenu:\n");
        System.out.println("[1] - Enter new image path");
        System.out.println("[2] - See info about all images");
        System.out.println("[3] - See info by file name");
        System.out.println("[4] - Find the most similar image for current one");
        System.out.println("[5] - Find two most similar images among all images");
        System.out.println("[6] - Sort images by ...");
        System.out.println("[0] - Exit\n");
    }

    static ImageData setMetadata(String path) throws IOException {
        ImageData pic = new ImageData();
        pic.setPath(path);
        pic.setImage();
        pic.setHeightWidth();
        pic.setSize();
        pic.setName();
        pic.setDate();
        pic.setAverageColor();
        pic.setColors();
        pic.setPixelSize();
        return pic;
    }

    static void watchInfo(ImageData image){
        System.out.println("\nName: "+image.getName());
        System.out.println("Path: "+image.getPath());
        System.out.println("Dimension: "+image.getWidth()+"x"+image.getHeight());
        System.out.println("Size: "+image.getSize()+" bytes");
        System.out.println("Date: "+image.getDate());
        System.out.println("Colors: "+image.getColors());
        System.out.println("Color encoding depth: "+image.getPixelSize());
        System.out.println("Average color: (r = "+image.getAverageColor().getRed()+
                ", g = "+image.getAverageColor().getGreen()+", b = "+image.getAverageColor().getBlue()+")");
    }

    static void watchInfoByName(ArrayList<ImageData> images, String name){
        for (ImageData image : images){
            if (image.getName().equals(name)){
                watchInfo(image);
                break;
            }
        }
    }

    static String enterNewPath() {
        while (true) {
            Scanner in = new Scanner(System.in);
            System.out.print("Enter an absolute path to .jpg/.jpeg/.png image >> ");
            String path = in.nextLine();
            File tmpDir = new File(path);
            boolean exists = tmpDir.exists();
            if (exists) {
                return path;
            } else {
                System.out.println("Absolute path is incorrect. Try again");
            }
        }
    }

    static int findS(Color c1, Color c2){
        return (int)(Math.sqrt(Math.pow((c2.getRed() - c1.getRed()), 2) + Math.pow((c2.getBlue() - c1.getBlue()), 2)
                + Math.pow((c2.getGreen() - c1.getGreen()), 2)));
    }

    static void findSimilar(ImageData image, ArrayList<ImageData> images){
        int minS = Integer.MAX_VALUE;
        ImageData imageSim = null;
        for (ImageData otherImage: images) {
            int currentS = findS(image.getAverageColor(), otherImage.getAverageColor());
            if ((currentS < minS) && (!image.getName().equals(otherImage.getName()))){
                minS = currentS;
                imageSim = otherImage;
            }
        }
        if (imageSim == null) {
            System.out.println("Comparison is unavailable. You entered only one image! ");
        }
        else {
            System.out.println("The most similar image to "+image.getName()+" is "+imageSim.getName());
            System.out.println("Average color of original image: (r = "+image.getAverageColor().getRed()
                    +", g = "+image.getAverageColor().getGreen()+", b = "+image.getAverageColor().getBlue()+")");
            System.out.println("Average color of similar image: (r = "+imageSim.getAverageColor().getRed()
                    +", g = "+imageSim.getAverageColor().getGreen()+", b = "+imageSim.getAverageColor().getBlue()+")");
            System.out.println("Distance: "+minS);
        }
    }

    static void findSimilarOverall(ArrayList<ImageData> images){
        int minS = Integer.MAX_VALUE;
        ImageData imageFirst = null;
        ImageData imageSecond = null;
        for (int i=0; i<images.size()-1; i++){
            for (int j=i+1; j<images.size(); j++){
                int currentMin = findS(images.get(i).getAverageColor(), images.get(j).getAverageColor());
                if (minS > currentMin) {
                    minS = currentMin;
                    imageFirst = images.get(i);
                    imageSecond = images.get(j);
                }
            }
        }
        if (imageFirst != null && imageSecond != null){
            System.out.println("The most similar images: "+imageFirst.getName()+" is "+imageSecond.getName());
            System.out.println("Average color of the first image: (r = "+imageFirst.getAverageColor().getRed()
                    +", g = "+imageFirst.getAverageColor().getGreen()+", b = "+imageFirst.getAverageColor().getBlue()+")");
            System.out.println("Average color of the second image: (r = "+imageSecond.getAverageColor().getRed()
                    +", g = "+imageSecond.getAverageColor().getGreen()+", b = "+imageSecond.getAverageColor().getBlue()+")");
            System.out.println("Distance: "+minS);
        }
        else {
            System.out.println("Comparison is unavailable. You entered less than 2 images!");
        }
    }

    public static void main(String[] args) throws IOException {
        ArrayList<ImageData> images = new ArrayList<ImageData>();
        HashSet<String> imagesNames = new HashSet<>();
        Scanner in = new Scanner(System.in);

//        // раскомментируйте, чтобы не добавлять изображения вручную
//        ArrayList<String> defaultImages = new ArrayList<>();
//        defaultImages.add("6-pbhLBHBJo.jpg");
//        defaultImages.add("8EDqXnO10Dc.jpg");
//        defaultImages.add("aw3iSSZXKa4.jpg");
//        defaultImages.add("photo_2020-03-03 21.09.44.jpeg");
//        defaultImages.add("uotDTjixkmI.jpg");
//        UploadDefaultImages uploader = new UploadDefaultImages();
//        for (String path: defaultImages) {
//            String absolutePath = uploader.upload(path);
//            ImageData defaultImage = setMetadata(absolutePath);
//            images.add(defaultImage);
//            imagesNames.add(defaultImage.getName());
//        }

        String choice = "100";
        System.out.print("To start: Enter an absolute path to .jpg/.jpeg/.png image >> ");
        String path = in.nextLine();
        File tmpDir = new File(path);
        boolean exists = tmpDir.exists();
        if (exists) {
            ImageData newImage = setMetadata(path);
            images.add(newImage);
            imagesNames.add(newImage.getName());
            System.out.print("The image has been added. Do you want to see info about it? Y/N >> ");
            if (in.nextLine().equals("Y")) {
                watchInfo(newImage);
            } else {
                System.out.print("Okay, let's return to the menu!");
            }
        }
        else {
            System.out.println("Absolute path is incorrect. You have been returned to the menu.");
        }
        while (!choice.equals("0")) {
            printMenu();
            System.out.print("Enter command number >> ");
            choice = in.nextLine();
            switch (choice) {
                case ("1"):
                    ImageData newImage = setMetadata(enterNewPath());
                    if (!imagesNames.contains(newImage.getName())) {
                        images.add(newImage);
                        imagesNames.add(newImage.getName());
                        System.out.print("The image has been added. Do you want to see info about it? Y/N >> ");
                        if (in.nextLine().equals("Y")) {
                            watchInfo(newImage);
                        }
                        else {
                            System.out.print("Okay, let's return to the menu!");
                        }
                    }
                    else {
                        System.out.print("This file has already been added. Do you want to see info about it? Y/N >> ");
                        if (in.nextLine().equals("Y")) {
                            watchInfoByName(images, newImage.getName());
                        }
                        else {
                            System.out.print("Okay, let's return to the menu!");
                        }
                    }
                    break;
                case ("2"):
                    for (ImageData image: images) {
                        watchInfo(image);
                    }
                    break;
                case ("3"):
                    System.out.print("Enter image name >> ");
                    String name = in.nextLine();
                    if (imagesNames.contains(name)) {
                        watchInfoByName(images, name);
                    }
                    else {
                        System.out.print("Sorry, you have not enter path to the image with name "+name+".");
                        System.out.print("Do you want to enter it? Y/N >> ");
                        if (in.nextLine().equals("Y")) {
                            enterNewPath();
                        }
                        else {
                            System.out.print("Okay, let's return to the menu!");
                        }
                    }
                    break;
                case ("4"):
                    System.out.print("Enter image name >> ");
                    name = in.nextLine();
                    for (ImageData image : images){
                        if (image.getName().equals(name)){
                            findSimilar(image, images);
                            break;
                        }
                    }
                    break;
                case("5"):
                    findSimilarOverall(images);
                    break;
                case("6"):
                    Sorter imageSorter = new Sorter(images);
                    System.out.println("How do you want to sort images?");
                    System.out.println("[1] - Sort by name");
                    System.out.println("[2] - Sort by size");
                    System.out.println("[3] - Sort by colors amount");
                    System.out.println("[4] - Sort by dimension");
                    System.out.println("Enter command number >> ");
                    switch (in.nextLine()){
                        case ("1"):
                            System.out.println("Sorting by name . . . ");
                            images = imageSorter.getSortedImagesByName();
                            Collections.reverse(images);
                            for (ImageData image : images) {
                                watchInfo(image);
                            }
                            break;
                        case ("2"):
                            System.out.println("Sorting by size . . . ");
                            images = imageSorter.getSortedImagesBySize();
                            Collections.reverse(images);
                            for (ImageData image : images) {
                                watchInfo(image);
                            }
                            break;
                        case ("3"):
                            System.out.println("Sorting by colors amount . . . ");
                            images = imageSorter.getSortedImagesByColors();
                            Collections.reverse(images);
                            for (ImageData image : images) {
                                watchInfo(image);
                            }
                            break;
                        case ("4"):
                            System.out.println("Sorting by dimension . . . ");
                            images = imageSorter.getSortedImagesByDimension();
                            Collections.reverse(images);
                            for (ImageData image : images) {
                                watchInfo(image);
                            }
                            break;
                        default:
                            System.out.print("There is no such command. Please try again");
                            break;
                    }
                    break;
                case ("0"):
                    System.out.print("Goodbye!");
                    break;
                default:
                    System.out.print("There is no such command. Please try again");
                    break;
            }
        }
    }
}
