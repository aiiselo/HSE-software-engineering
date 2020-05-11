package com.company.Elevators;

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        System.out.print("Enter how many elevators are in the building >> ");
        int elevatorsNumber = Integer.parseInt(in.nextLine());
        System.out.print("Enter how many people can be in elevator at the same moment >> ");
        int capacity = Integer.parseInt(in.nextLine());
        System.out.print("Enter how many floors are in the building >> ");
        int floors = Integer.parseInt(in.nextLine());
        System.out.print("Enter how many people can be on the floor at the same moment >> ");
        int maxPeopleOnFloor = Integer.parseInt(in.nextLine());
        if (floors * capacity * elevatorsNumber * maxPeopleOnFloor > 0) {
            ElevatorManager manager = new ElevatorManager(capacity, floors, elevatorsNumber);
            Request request = new Request(floors,maxPeopleOnFloor, manager);
            Thread requestsThread = new Thread(request);
            Thread elevatorsThread = new Thread(manager);
            requestsThread.start();
            elevatorsThread.start();
        }
        else {
            System.out.print("Enter only positive numbers! Re-run program and try again.");
        }
    }
}
