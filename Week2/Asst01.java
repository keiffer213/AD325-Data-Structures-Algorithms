
public class Asst01{
  public static void main(String[] args) {
    int[] testArr = {1, 2, 3, 4, 5, 6};
    printPairs(testArr);
    
    }
    
    static void printPairs(int[] array) {
    for (int i = 0; i < array.length; i++) {
        for (int j = i + 1; j < array.length; j++) {
            System.out.println(array[i] + ", " + array[j]);
        }
    }
  }

}



