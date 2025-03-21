import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.HashMap;

public class SimpleWordFrequencyCounterTest {

    @Test
    void testSingleSentence() {
        String input = "Hello world! Hello everyone.";
        HashMap<String, Integer> result = SimpleWordFrequencyCounter.countWordFrequency(input);
        assertEquals(2, result.get("hello"));
        assertEquals(1, result.get("world"));
        assertEquals(1, result.get("everyone"));
    }

    @Test
    void testCaseInsensitive() {
        String input = "Apple apple APPLE aPPle!";
        HashMap<String, Integer> result = SimpleWordFrequencyCounter.countWordFrequency(input);
        assertEquals(4, result.get("apple"));
    }

    @Test
    void testWithPunctuation() {
        String input = "Hello, world! Hello, again...";
        HashMap<String, Integer> result = SimpleWordFrequencyCounter.countWordFrequency(input);
        assertEquals(2, result.get("hello"));
        assertEquals(1, result.get("world"));
        assertEquals(1, result.get("again"));
    }

    @Test
    void testEmptyString() {
        String input = "";
        HashMap<String, Integer> result = SimpleWordFrequencyCounter.countWordFrequency(input);
        assertTrue(result.isEmpty());
    }

    @Test
    void testOnlyPunctuation() {
        String input = "!!! ??? ***";
        HashMap<String, Integer> result = SimpleWordFrequencyCounter.countWordFrequency(input);
        assertTrue(result.isEmpty());
    }
}
