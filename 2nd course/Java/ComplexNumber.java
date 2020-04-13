package com.company;
import java.lang.Math;

public class ComplexNumber {
    private double rn; // действительное число
    private double iu; // мнимая единица

    public ComplexNumber(double rn, double iu) {
        this.rn = rn;
        this.iu = iu;
    }

    public double GetRn() {
        return rn;
    }

    public double GetIu() {
        return iu;
    }

    public static ComplexNumber sum(ComplexNumber firstNum, ComplexNumber secondNum) {
        return new ComplexNumber(firstNum.GetRn() + secondNum.GetRn(), firstNum.GetIu() + secondNum.GetIu());
    }

    public static ComplexNumber multy(ComplexNumber firstNum, ComplexNumber secondNum) {
        return new ComplexNumber(firstNum.GetRn() * secondNum.GetRn() - firstNum.GetIu() * secondNum.GetIu(), firstNum.GetRn() * secondNum.GetIu() + firstNum.GetIu() * secondNum.GetRn());
    }

    public static double GetModule(ComplexNumber num) {
        double a_pow = Math.pow(num.GetRn(), 2);
        double b_pow = Math.pow(num.GetIu(), 2);
        return Math.sqrt(a_pow + b_pow);
    }

    public static double GetPhi(ComplexNumber num) {
        double arg = num.GetIu() / num.GetRn();
        return Math.atan(arg);
    }

    public static void ToTrigonometry(ComplexNumber num) {
        System.out.println(num.GetRn() + "+" + num.GetIu() + "i = " + GetModule(num) + "*(cos" + GetPhi(num) + " + i*sin" + GetPhi(num) + ")");
    }

    public static void main(String[] args) {
        ComplexNumber x = new ComplexNumber(2, 4);
        ComplexNumber y = new ComplexNumber(3, 5);
        System.out.println("X = " + x.rn + " " + x.iu);
        System.out.println("Y = " + y.rn + " " + y.iu);
        ComplexNumber z;
        z = ComplexNumber.sum(x, y);
        System.out.println("x + y = " + z.rn + " " + z.iu);
        z = ComplexNumber.multy(x, y);
        System.out.println("x - y = " + z.rn + " " + z.iu);
        System.out.println("Module of X = " + ComplexNumber.GetModule(x));
        System.out.println("Phi of X = " + ComplexNumber.GetPhi(x));
        System.out.println("X to Trigonometry:");
        ToTrigonometry(x);
    }
}
