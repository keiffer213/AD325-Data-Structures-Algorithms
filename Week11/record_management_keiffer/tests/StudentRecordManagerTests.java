import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.util.TreeMap;

import static org.junit.jupiter.api.Assertions.*;


public class StudentRecordManagerTests {

    private StudentRecordManager studentRecordManager;

    @BeforeEach
    void setUp() {
        studentRecordManager = new StudentRecordManager();

        studentRecordManager.addStudent(1003, "Charlie", 2.8);
        studentRecordManager.addStudent(1002, "Bob", 3.2);
        studentRecordManager.addStudent(1005, "Eve", 3.1);
        studentRecordManager.addStudent(1006, "Adam", 2.3);
        studentRecordManager.addStudent(1004, "David", 3.9);
        studentRecordManager.addStudent(1007, "Steve", 1.8);
        studentRecordManager.addStudent(1001, "Alice", 3.5);
    }

    @Test
    void testAddStudent() {
        assertTrue(studentRecordManager.addStudent(1010, "Keiffer", 3.99));
        assertFalse(studentRecordManager.addStudent(1010, "Keiffer", 3.99));
    }

    @Test
    void testDeleteStudent() {
        assertTrue(studentRecordManager.deleteStudent(1002));
        assertFalse(studentRecordManager.deleteStudent(1002));
        assertFalse(studentRecordManager.deleteStudent(1053));
    }

    @Test
    void testUpdateStudent() {
        assertTrue(studentRecordManager.updateStudent(1003, 4.0));
        assertFalse(studentRecordManager.updateStudent(9199, 4.0));
    }


}


