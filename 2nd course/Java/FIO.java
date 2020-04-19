package com.company;

import java.io.FileNotFoundException;
import java.time.*;
import java.util.Scanner;

public class FIO {
    public static int calculateAge(LocalDate birthDate) {
        LocalDate currentDate = LocalDate.now();
        return Period.between(birthDate, currentDate).getYears();
    }

    public static void main(String[] args) throws ArrayIndexOutOfBoundsException {
        try {
            Scanner in = new Scanner(System.in);
            System.out.print("Введите фамилию, имя и отчетство через пробел:  \n");
            String[] FIO = in.nextLine().trim().split(" ");
            System.out.print("Введите дату рождения в формате дд.мм.гггг : \n");
            String[] inputDate = in.nextLine().trim().split("\\.");
            LocalDate birthDay = LocalDate.of(Integer.parseInt(inputDate[2]), Integer.parseInt(inputDate[1]), Integer.parseInt(inputDate[0]));
            System.out.println("Фамилия: " + FIO[0].substring(0, 1).toUpperCase() + FIO[0].substring(1));
            System.out.println("Инициалы: " + FIO[0].toUpperCase().charAt(0) + "." + FIO[1].toUpperCase().charAt(0) + "." + FIO[2].toUpperCase().charAt(0));
            if (FIO[2].substring(FIO[2].length() - 1).equals("а")) {
                System.out.println("Пол: женский");
            } else {
                System.out.println("Пол: мужской");
            }
            System.out.println("Возраст: " + calculateAge(birthDay));
        }
        catch (ArrayIndexOutOfBoundsException ex){
            System.out.println(ex.getMessage());
        }
    }
}
