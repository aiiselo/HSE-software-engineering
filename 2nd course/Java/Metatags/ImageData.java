package com.company.Metatags;

import javax.imageio.ImageIO;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.attribute.FileTime;
import java.text.DateFormat;
import java.text.SimpleDateFormat;
import java.util.Comparator;
import java.util.HashSet;

public class ImageData {
    private String path;
    private String name;
    private BufferedImage image;
    private int width;
    private int height;
    private long size; // in bytes
    private String date;
    private int colors;
    private int pixelSize; // глубина кодирования цвета
    private Color averageColor;

    /*          Setters           */

    public void setPath(String path) {
        this.path = path;
    }

    public void setImage() throws IOException {
        try{
            String path = this.getPath();
            this.image = ImageIO.read(new File(path));
        }
        catch (IOException ex) {
            System.out.println("No such file or directory!");
            System.out.println(ex.getMessage());
        }

    }

    public void setHeightWidth() {
        this.width = this.getImage().getWidth();
        this.height = this.getImage().getHeight();
    }

    public void setSize() {
        File file = new File(this.getPath());
        this.size = file.length();
    }

    public void setName() {
        File file = new File(this.getPath());
        this.name = file.getName();
    }

    public void setDate() {
        try {
            Path filePath = Paths.get(this.getPath());
            FileTime creationTime = (FileTime) Files.getAttribute(filePath, "creationTime");
            DateFormat df = new SimpleDateFormat("HH:mm:ss dd/MM/yyyy");
            this.date = df.format(creationTime.toMillis());
        } catch (IOException ex) {
            System.out.println(ex.getMessage());
        }
    }

    public void setAverageColor() {
        long sumr = 0, sumg = 0, sumb = 0;
        for (int x = 0; x < this.getWidth(); x++) {
            for (int y = 0; y < this.getHeight(); y++) {
                Color pixel = new Color(image.getRGB(x, y));
                sumr += pixel.getRed();
                sumg += pixel.getGreen();
                sumb += pixel.getBlue();
            }
        }
        long square = this.getHeight() * this.getWidth();
        this.averageColor = new Color((int)(sumr / square), (int)(sumg / square), (int)(sumb / square));
    }

    public void setColors() {
        HashSet<Integer> colorSet = new HashSet<Integer>();
        for(int y = 0; y < this.getHeight(); y++) {
            for(int x = 0; x < this.getWidth(); x++) {
                int pixel = image.getRGB(x, y);
                colorSet.add(pixel);
            }
        }
        this.colors = colorSet.size();
    }

    public void setPixelSize() {
        this.pixelSize = this.getImage().getColorModel().getPixelSize();
    }

    /*          Getters           */

    public String getPath() {
        return path;
    }

    public BufferedImage getImage() {
        return image;
    }

    public int getWidth() {
        return width;
    }

    public int getHeight() {
        return height;
    }

    public String getName(){
        return name;
    }

    public long getSize() {
        return size;
    }

    public String getDate() {
        return date;
    }

    public int getColors() {
        return colors;
    }

    public Color getAverageColor() {
        return averageColor;
    }

    public int getPixelSize() {
        return pixelSize;
    }

    /*          Comparators           */

    public static Comparator<ImageData> sizeComparator = new Comparator<ImageData>() {
        @Override
        public int compare(ImageData id1, ImageData id2) {
            return (Long.compare(id2.getSize(), id1.getSize()));
        }
    };

    public static Comparator<ImageData> dimensionComparator = new Comparator<ImageData>() {
        @Override
        public int compare(ImageData id1, ImageData id2) {
            return (Long.compare(id2.getWidth()*id2.getHeight(), id1.getWidth()*id1.getHeight()));
        }
    };

    public static Comparator<ImageData> colorsComparator = new Comparator<ImageData>() {
        @Override
        public int compare(ImageData id1, ImageData id2) {
            return (Integer.compare(id2.getColors(), id1.getColors()));
        }
    };

    public static Comparator<ImageData> nameComparator = new Comparator<ImageData>() {
        @Override
        public int compare(ImageData id1, ImageData id2) {
            return (int) (id2.getName().toLowerCase().compareTo(id1.getName().toUpperCase()));
        }
    };

}
