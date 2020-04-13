package com.company;

public class Matrix {
    private int n;
    private int m;
    private int[][] matrix;

    public Matrix(int n, int m) {
        this.n = n;
        this.m = m;
        this.matrix = new int[n][m];
    }

    public Matrix(int[][] matrixArg) {
        this.n = matrixArg.length;
        this.m = matrixArg[0].length;
        this.matrix = matrixArg;
    }

    public int getN() {
        return this.n;
    }

    public int getM() {
        return this.m;
    }

    public int getElem(int i, int j) {
        return this.matrix[i][j];
    }

    public void setElem(int i, int j, int value) {
        this.matrix[i][j] = value;
    }

    public void PrintMatrix() {
        for (int i = 0; i < this.n; i++) {
            for (int j = 0; j < this.m; j++) {
                System.out.print(this.matrix[i][j] + " ");
            }
            System.out.println();
        }
    }

    public static Matrix add(Matrix x, Matrix y) throws DifferentMatrixSize {
        if (x.getM() != y.getM() || x.getN() != y.getN()) {
            throw new DifferentMatrixSize("Матрицы отличаются размерами");
        } else {
            Matrix res = new Matrix(x.getN(), x.getM());
            for (int i = 0; i < res.getN(); i++) {
                for (int j = 0; j < res.getM(); j++) {
                    res.setElem(i, j, x.getElem(i, j) + y.getElem(i, j));
                }
            }
            return res;
        }
    }

    public static Matrix subtract(Matrix x, Matrix y) throws DifferentMatrixSize {
        if (x.getM() != y.getM() || x.getN() != y.getN()) {
            throw new DifferentMatrixSize("Матрицы отличаются размерами");
        } else {
            Matrix res = new Matrix(x.getN(), x.getM());
            for (int i = 0; i < res.getN(); i++) {
                for (int j = 0; j < res.getM(); j++) {
                    res.setElem(i, j, x.getElem(i, j) - y.getElem(i, j));
                }
            }
            return res;
        }
    }

    public static Matrix multiply(Matrix x, Matrix y) throws DifferentMatrixSize {
        if (x.getM() != y.getN()) {
            throw new DifferentMatrixSize("N != M");
        } else {
            Matrix res = new Matrix(x.getN(), y.getM());
            int current_value = 0;
            for (int i = 0; i < x.getN(); i++) { // идем по строкам первой матрицы
                for (int z = 0; z < y.getM(); z++) { // идем по столбцам второй матрицы
                    current_value = 0;
                    for (int j = 0; j < y.getN(); j++) { // идем по строкам второй матрицы
                        current_value += x.getElem(i, j) * y.getElem(j,z);
                    }
                    res.setElem(i,z,current_value);
                }
            }
            return res;
        }
    }

     public static Matrix transpose(Matrix x) {
        Matrix res = new Matrix(x.getM(), x.getN());
        for (int i = 0; i < x.getN(); i++) {
             for (int j = 0; j < x.getM(); j++) {
                 res.setElem(j, i, x.getElem(i, j));
             }
        }
        return res;
     }

     public static int findDeterminant(Matrix x) throws DifferentMatrixSize {
        if (x.getN() != x.getM()) {
            throw new DifferentMatrixSize("Матрица не квадратная!");
        } else {
            if (x.getM() == 2){
                return x.getElem(0,0)*x.getElem(1,1) - x.getElem(0, 1)*x.getElem(1,0);
            }
            else{
                int res = 0;
                for (int i = 0; i < x.getM(); i++){ // идем по элементам первой строки
                    Matrix matrixNew = new Matrix(x.getN()-1, x.getN()-1); // создаем матрицу из оставшихся чисел
                    int iNew = 0; // координаты новой матрицы
                    int jNew = 0;
                    for (int z = 1; z < x.getM(); z++){ // идем по оставшимся строкам исходной матрицы
                        for (int j = 0; j < x.getM(); j++){ // идем по столбцам
                            if (j != i) {
                                matrixNew.setElem(iNew, jNew, x.getElem(z, j));
                                jNew += 1;
                                if (jNew == x.getN()-1){
                                    iNew+=1;
                                    jNew = 0;
                                }
                            }
                        }
                    }
                    if (i%2 == 0){
                        res += x.getElem(0,i)*findDeterminant(matrixNew);
                    }
                    else {
                        res -= x.getElem(0, i)*findDeterminant(matrixNew);
                    }
                }
                return res;
            }
        }
     }

    public static void main(String[] args) throws DifferentMatrixSize {
        int[][] firstMatrix = {{1, 2, 3}, {4, 5, 6}};
        int[][] secondMatrix = {{1, 2}, {3, 4}, {5, 6}};
        int[][] thirdMatrix = {{1, 2, 3}, {4, 5, 6}};
        int[][] MatrixDeterm = {{1, 2, 3}, {1, 5, 3}, {1, 2, 66}};
        Matrix A = new Matrix(firstMatrix);
        Matrix B = new Matrix(secondMatrix);
        Matrix C = new Matrix(thirdMatrix);
        Matrix Det = new Matrix(MatrixDeterm);

        System.out.println("A :");
        A.PrintMatrix();
        System.out.println("B :");
        B.PrintMatrix();
        System.out.println("C :");
        C.PrintMatrix();

        System.out.println("D = A+C :");
        Matrix.add(A, C).PrintMatrix();

        System.out.println("E = A-C :");
        Matrix.subtract(A, C).PrintMatrix();

        System.out.println("Transpose A :");
        Matrix.transpose(A).PrintMatrix();

        System.out.println("F = A * B :");
        Matrix.multiply(A, B).PrintMatrix();

        System.out.println("Determinant of Det:");
        System.out.println(findDeterminant(Det));

    }

    static class DifferentMatrixSize extends Exception {
        DifferentMatrixSize(String error){
            super(error);
        }
    }
}