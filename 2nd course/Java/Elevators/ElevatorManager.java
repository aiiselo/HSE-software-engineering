package com.company.Elevators;

import java.util.ArrayList;

public class ElevatorManager implements Runnable {
    private int space;
    private int floors;
    private int elevatorsNumber;
    private ArrayList<Elevator> elevators = new ArrayList<>();
    private ArrayList<Passenger> passengers = new ArrayList<>();

    ElevatorManager (int space, int floors, int elevators) {
        setSpace(space);
        setFloors(floors);
        for (int i = 0; i < elevators; i++) {
            Elevator elevator = new Elevator(i, 0);
            setElevators(elevator);
        }
    }

    @Override
    public void run() {
        int iteration = 0;
        System.out.println(": = = = = = = = = = = = = = = = Log history = = = = = = = = = = = = = = = :");
        while (true) {
            iteration++;
            int elevatorsEnvolved = 0;
            System.out.println("______________________________Iteration #"+iteration+"______________________________");
            for (Elevator elevator: getElevators()) {
                elevator.move();
                int currentFloor = elevator.getFloor();
                if (getSpace() - elevator.getPassengers().size() > 0) {
                    ArrayList<Passenger> upstairsStart = new ArrayList<>();
                    ArrayList<Passenger> downstairsStart = new ArrayList<>();
                    ArrayList<Passenger> upstairsDestination = new ArrayList<>();
                    ArrayList<Passenger> downstairsDestination = new ArrayList<>();
                    for (Passenger passenger : getPassengers()) {
                        int passengerStartFloor = passenger.getCurrentFloor();
                        int passengerDirection = passengerStartFloor - passenger.getDestinationFloor();
                        if (passengerStartFloor > currentFloor)
                            upstairsStart.add(passenger);
                        else if (passengerStartFloor < currentFloor)
                            downstairsStart.add(passenger);
                        if (passengerStartFloor == elevator.getFloor() && passengerDirection < 0) {
                            upstairsDestination.add(passenger);
                        }
                        else if (passengerStartFloor == elevator.getFloor() && passengerDirection > 0) {
                            downstairsDestination.add(passenger);
                        }
                    }
                    if (elevator.getPassengers().size() == 0 || currentFloor == getFloors() - 1) {
                        if (elevator.getDirection() == 1 && (upstairsStart.size() < elevatorsEnvolved * getSpace()
                                || downstairsStart.size() < elevatorsEnvolved * getSpace())) {
                            elevator.setDirection(0);
                        }
                        else if (downstairsStart.size() > elevatorsEnvolved * getSpace() || currentFloor == getFloors() - 1){
                            elevator.setDirection(-1);
                        }
                    }
                    else if (currentFloor == 0) {
                        if (upstairsStart.size() > elevatorsEnvolved * getSpace()) {
                            elevator.setDirection(1);
                        }
                        else {
                            elevator.setDirection(0);
                        }
                    }
                    else {
                        elevator.setDirection(1);
                    }
                    if (elevator.getDirection() == 0) {
                        if (upstairsDestination.size() > downstairsDestination.size() && upstairsStart.size() > elevatorsEnvolved * getSpace())                         {
                            elevator.setDirection(1);
                        }
                        else if (upstairsDestination.size() <= downstairsDestination.size()
                                && downstairsStart.size() > elevatorsEnvolved * getSpace()) {
                            elevator.setDirection(-1);
                        }
                    }
                    if (currentFloor == getFloors() - 1) {
                        elevator.setDirection(-1);
                    }
                    if (currentFloor == 0) {
                        elevator.setDirection(1);
                    }
                    ArrayList<Passenger> priorityPassengers = new ArrayList<>();
                    if (elevator.getDirection() == -1) {
                        priorityPassengers = upstairsDestination;
                    }
                    else if (elevator.getDirection() == 1) {
                        priorityPassengers = downstairsDestination;
                    }
                    while (priorityPassengers.size() != 0 && elevator.getPassengers().size() < getSpace()) {
                        elevator.setPassengers(priorityPassengers.get(0));
                        getPassengers().remove(priorityPassengers.get(0));
                        priorityPassengers.remove(0);
                    }
                }
                else {
                    if (currentFloor == getFloors() - 1) {
                        elevator.setDirection(-1);
                    }
                    if (currentFloor == 0) {
                        elevator.setDirection(1);
                    }
                }
                String direction = "";
                elevatorsEnvolved++;
                switch (elevator.getDirection()) {
                    case -1:
                        direction = "down";
                        break;
                    case 1:
                        direction = "up";
                        break;
                    default:
                        direction = "stopped";
                        break;
                }
                System.out.println("Elevator id: " + elevator.getId() + "; Current floor: " + elevator.getFloor() +
                        "; Direction: " + direction + "; Passenger number: " + elevator.getPassengers().size());
            }
            try {
                Thread.sleep(2000);
            } catch (InterruptedException ex) {
                System.out.println(ex.getMessage());
            }
        }
    }

    /*          Setters           */

    public void setSpace(int space) {
        this.space = space;
    }

    public void setFloors(int floors) {
        this.floors = floors;
    }

    public void setElevators(Elevator elevator) {
        this.elevators.add(elevator);
    }

    public void setPassengers(Passenger passenger) {
        this.passengers.add(passenger);
    }

    public void setElevatorsNumber(int elevatorsNumber) {
        this.elevatorsNumber = elevatorsNumber;
    }

    /*          Getters           */

    public int getSpace() {
        return space;
    }

    public int getFloors() {
        return floors;
    }

    public ArrayList<Passenger> getPassengers() {
        return passengers;
    }

    public ArrayList<Elevator> getElevators() {
        return elevators;
    }

    public int getElevatorsNumber() {
        return elevatorsNumber;
    }
}
