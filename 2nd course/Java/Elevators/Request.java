package com.company.Elevators;
import java.util.Random;

public class Request implements Runnable {
    private int floors;
    private int maxPeopleOnFloor;
    private ElevatorManager manager;

    Request (int floors, int maxPeopleOnFloor, ElevatorManager manager) {
        setFloors(floors);
        setMaxPeopleOnFloor(maxPeopleOnFloor);
        setManager(manager);
    }

    public void run() {
        while(true) {
            Random random = new Random();
            int startFloor = random.nextInt(floors + 1);
            int peopleAmount = random.nextInt(maxPeopleOnFloor + 1);
            for (int i = 0; i < peopleAmount; i++) {
                int destinationFloor = random.nextInt(floors + 1);
                while (destinationFloor == startFloor) {
                    destinationFloor = random.nextInt(floors + 1);
                }
                Passenger passenger = new Passenger(startFloor, destinationFloor);
                getManager().setPassengers(passenger);
            }
            try {
                Thread.sleep(2000);
            } catch (InterruptedException ex) {
                System.out.println(ex.getMessage());
            }
        }
    }

    /*          Setters           */

    public void setFloors(int floors) {
        this.floors = floors;
    }

    private void setMaxPeopleOnFloor(int maxPeopleOnFloor) {
        this.maxPeopleOnFloor = maxPeopleOnFloor;
    }

    public void setManager(ElevatorManager manager) {
        this.manager = manager;
    }

    /*          Getters           */

    public int getFloors() {
        return floors;
    }

    public int getMaxPeopleOnFloor() {
        return maxPeopleOnFloor;
    }

    public ElevatorManager getManager() {
        return manager;
    }
}
