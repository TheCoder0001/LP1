public class MathOperations {
    static {
        System.loadLibrary("MathOps"); 
    }

    public native double power(double base, double exp);
    public native long factorial(int n);
    public native double squareroot(double x);

    public static void main(String[] args) {
        MathOperations mo = new MathOperations();

        System.out.println("Power(2, 10) = " + mo.power(2, 10));
        System.out.println("Factorial(5) = " + mo.factorial(5));
        System.out.println("SquareRoot(25) = " + mo.squareroot(25));
        System.out.println("SquareRoot(-9) = " + mo.squareroot(-9));
        System.out.println("Factorial(0) = " + mo.factorial(0));
    }
}

///# 1. Compile Java
//javac MathOperations.java

//# 2. Generate header
//javac -h . MathOperations.java

//# 3. Compile C++ into .so
//g++ -fPIC -shared -I"$JAVA_HOME/include" -I"$JAVA_HOME/include/linux" MathOps.cpp -o libMathOps.so

//# 4. Run
//java -Djava.library.path=. MathOperations