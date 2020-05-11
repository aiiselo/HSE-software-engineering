package com.company.Elevators;

public class Passenger {
    private int currentFloor;
    private int destinationFloor;

    Passenger(int currentFloor, int destinationFloor){
        setCurrentFloor(currentFloor);
        setDestinationFloor(destinationFloor);
    }

    /*          Setters           */

    public void setCurrentFloor(int currentFloor) {
        this.currentFloor = currentFloor;
    }

    public void setDestinationFloor(int destinationFloor) {
        this.destinationFloor = destinationFloor;
    }

    /*          Getters           */

    public int getCurrentFloor() {
        return currentFloor;
    }

    public int getDestinationFloor() {
        return destinationFloor;
    }
}
