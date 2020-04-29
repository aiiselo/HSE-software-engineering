package com.company.Metatags;

import java.util.ArrayList;
import java.util.Collections;

public class Sorter {
    ArrayList<ImageData> images = new ArrayList<>();
    public Sorter(ArrayList<ImageData> images) {
        this.images = images;
    }
    public ArrayList<ImageData> getSortedImagesBySize() {
        Collections.sort(images, ImageData.sizeComparator);
        return images;
    }
    public ArrayList<ImageData> getSortedImagesByDimension() {
        Collections.sort(images, ImageData.dimensionComparator);
        return images;
    }
    public ArrayList<ImageData> getSortedImagesByColors() {
        Collections.sort(images, ImageData.colorsComparator);
        return images;
    }
    public ArrayList<ImageData> getSortedImagesByName() {
        Collections.sort(images, ImageData.nameComparator);
        return images;
    }
}
