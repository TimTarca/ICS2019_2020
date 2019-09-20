import java.util.Scanner;

public class Program{
	public static Turtle bob = new Turtle();
	
	
	public static void main(String[] args){
		int userNum, angleMea;
		Scanner input = new Scanner(System.in);
		System.out.println("Shape Drawer\nEnter a whole number of sides to draw a shape: ");
		userNum = input.nextInt();
		angleMea = 360 / userNum;
		shapeDrawer(userNum, angleMea);
	}
	
	public static void shapeDrawer(int numOfSides, int angleMea){
		bob.speed(100);
		if(0 < numOfSides){
			bob.forward(100);
			bob.left(angleMea);
			numOfSides = numOfSides - 1;
			shapeDrawer(numOfSides, angleMea);
		}
	}
	
	
	
}
