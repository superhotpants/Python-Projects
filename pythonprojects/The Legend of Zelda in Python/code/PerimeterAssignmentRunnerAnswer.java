import java.awt.Point;

public class ShapeUtils {

  public static double calculateDistance(Point p1, Point p2) {
    int x1 = p1.x;
    int y1 = p1.y;
    int x2 = p2.x;
    int y2 = p2.y;

    int deltaX = x2 - x1;
    int deltaY = y2 - y1;

    return Math.sqrt(deltaX * deltaX + deltaY * deltaY);
  }

  public static double findLongestSide(Point[] points) {
    double longestSide = 0;

    for (int i = 0; i < points.length - 1; i++) {
      double distance = calculateDistance(points[i], points[i + 1]);
      if (distance > longestSide) {
        longestSide = distance;
      }
    }

    return longestSide;
  }

  public static void main(String[] args) {
    Point[] points = {
        new Point(-3, 9),
        new Point(-8, 7),
        new Point(-12, 4),
        new Point(-6, -2),
        new Point(-4, -6),
        new Point(2, -8),
        new Point(6, -5),
        new Point(10, -3),
        new Point(8, 5),
        new Point(4, 8)
    };

    double longestSide = findLongestSide(points);
    System.out.println("Longest side length: " + longestSide);
  }
}