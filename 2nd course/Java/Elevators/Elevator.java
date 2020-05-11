package com.company.Elevators;
import java.util.ArrayList;

public class Elevator {
    private int id;
    private int floor;
    private int direction = 0;
    private ArrayList<Passenger> passengers = new ArrayList<>();

    Elevator(int id, int floor) {
        setId(id);
        setFloor(floor);
    }

    public void move() {
        setFloor(getFloor() + getDirection());
        getPassengers().removeIf(passenger -> (passenger.getDestinationFloor() == getFloor()));
    }

    /*          Setters           */

    public void setId(int id) {
        this.id = id;
    }

    public void setFloor(int floor) {
        this.floor = floor;
    }

    public void setDirection(int direction) {
        this.direction = direction;
    }

    public void setPassengers(Passenger passenger) {
        this.passengers.add(passenger);
    }

    /*          Getters           */

    public int getId() {
        return id;
    }

    public int getFloor() {
        return floor;
    }

    public int getDirection() {
        return direction;
    }

    public ArrayList<Passenger> getPassengers() {
        return passengers;
    }
}
