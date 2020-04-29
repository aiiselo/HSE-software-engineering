package com.company.Metatags;

import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

public class UploadDefaultImages {
    public String upload(String filename) throws IOException {
        String workingDirectory= System.getProperty("user.dir");
        workingDirectory = workingDirectory+"/src/com/company/Metatags/"+filename;
        if (System.getProperty("os.name").toLowerCase().contains("win")) {
            workingDirectory.replace("/", "\\");
        }
        return workingDirectory;
    }
}