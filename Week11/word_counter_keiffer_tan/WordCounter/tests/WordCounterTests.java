import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.util.HashMap;

public class WordCounterTests {

    @Test
    public void testSingleSentence() {
        String input = "hello hello hello hello 1 2 1 2 well";
        HashMap<String, Integer> result = WordCounter.countWordFrequency(input);
        assertEquals(4, result.get("hello"));
        assertEquals(2, result.get("1"));
        assertEquals(2, result.get("2"));
        assertEquals(1, result.get("well"));
    }

    @Test
    public void testCaseInsensitive() {
        String input = "Hello hello Hello hello";
        HashMap<String, Integer> result = WordCounter.countWordFrequency(input);
        assertEquals(4, result.get("hello"));
        assertNull(result.get("Hello"));

    }

    @Test
    public void testEmptyString() {
        String input = "";
        HashMap<String, Integer> result = WordCounter.countWordFrequency(input);
        assertTrue(result.isEmpty());
    }


}
