import java.util.HashMap;
//import java.util.Map;
import java.util.Scanner;

/**
 *  SimpleWordFrequencyCounter class to count the frequency of words from a user input
 *
 * @author Keiffer Tan
 * @version 2025-3-19
 */


public class SimpleWordFrequencyCounter {

    /**
     * Processes a given text and returns a HashMap containing word frequency.
     * @param text The input text to process.
     * @return A HashMap containing word frequency counts.
     */
    public static HashMap<String, Integer> countWordFrequency(String text) {
        if (text == null || text.isEmpty()) {
            return new HashMap<>();
        }

        String[] words = text.split("\\s+"); // Split by whitespace
        HashMap<String, Integer> wordMap = new HashMap<>();

        for (String word : words) {
            // Normalize: Remove punctuation and convert to lowercase
            word = word.replaceAll("[^a-zA-Z0-9]", "").toLowerCase().strip();

            if (!word.isEmpty()) { // Ignore empty words
                wordMap.put(word, wordMap.getOrDefault(word, 0) + 1);
            }
        }
        return wordMap;
    }

    public static void main(String[] args) {

        /* Easier Method */
        System.out.println("Please enter a sentence: ");
        String sentence = new java.util.Scanner(System.in).nextLine();
        String[] words = sentence.split(" ");
        //End of easy method

        Scanner scanner = new Scanner(System.in);
        System.out.println("Enter text (type 'exit' to finish):");

        StringBuilder inputText = new StringBuilder();
        while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            if (line.equalsIgnoreCase("exit")) {
                break;
            }
            inputText.append(line).append(" ");
        }
        scanner.close();

        HashMap<String, Integer> frequencyMap = countWordFrequency(inputText.toString());

        System.out.println("\nWord Frequency Count:");
//        System.out.println(frequencyMap);
//        frequencyMap.entrySet()
//                .stream()
//                .sorted(Map.Entry.comparingByKey()) // Sort output alphabetically
//                .forEach(entry -> System.out.println(entry.getKey() + ": " + entry.getValue()));

        frequencyMap.forEach((word, count) -> System.out.println(word + ": " + count));
    }

//    public static void main(String[] args) {
//        System.out.println("Please enter a sentence: ");
//        String sentence = new java.util.Scanner(System.in).nextLine();
//        String[] words = sentence.split(" ");
//
//        HashMap<String, Integer> wordMap = new HashMap<>();
//        for (String word : words) {
//            word = word.replaceAll("[^a-zA-Z0-9]", "").toLowerCase();
//            wordMap.put(word.strip(), wordMap.getOrDefault(word, 0) + 1);
//        }
//
//        for (String word : wordMap.keySet()) {
//            System.out.println(word + ": " + wordMap.get(word));
//        }
//    }


}