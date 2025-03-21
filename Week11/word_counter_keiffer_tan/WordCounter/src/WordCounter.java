import java.util.Map;
import java.util.Scanner;
import java.util.HashMap;

/**
 * Objective:
 * Develop a Java program that reads a text input from the user and calculates the
 * frequency of each word in the text using a HashMap.
 *
 * @author Keiffer Tan
 * @version 2025-3-21
 *
 */

public class WordCounter {

    public static HashMap<String, Integer> countWordFrequency(String text){
        if (text == null || text.isEmpty()) {
            return new HashMap<>();
        }
        String[] words = text.split("\\s");

        HashMap<String, Integer> wordCount = new HashMap<>();
        for (String word : words) {
            word = word.toLowerCase().strip();
            wordCount.put(word, wordCount.getOrDefault(word, 0) + 1);
        }

        return wordCount;
    }

    public static void displayWordFrequency(HashMap<String, Integer> wordCOunter){
        wordCOunter.entrySet()
                .stream()
                .sorted(Map.Entry.comparingByKey())
                .forEach(entry -> System.out.println(entry.getKey() + ": " + entry.getValue()));
    }


    public static void main(String[] args) {

        System.out.println("Please Enter a Sentence");
        String sentence = new Scanner(System.in).nextLine();
//        System.out.println(sentence);

        HashMap<String, Integer> wordCount = countWordFrequency(sentence);

        displayWordFrequency(wordCount);
    }
}
