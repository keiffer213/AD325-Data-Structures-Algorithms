import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

public class StudentRecordManagerTest {
    private StudentRecordManager manager;

    @BeforeEach
    void setUp() {
        manager = new StudentRecordManager();
        manager.addStudent(1001, "Alice", 3.5);
        manager.addStudent(1002, "Bob", 3.2);
        manager.addStudent(1003, "Charlie", 2.8);
    }

    @Test
    void testAddStudent() {
        assertTrue(manager.addStudent(1004, "David", 3.9));
        assertFalse(manager.addStudent(1001, "Duplicate Alice", 3.5));  // Duplicate ID should fail
    }

    @Test
    void testDeleteStudent() {
        assertTrue(manager.deleteStudent(1002)); // Deleting existing student
        assertFalse(manager.deleteStudent(9999)); // Non-existing ID
    }

    @Test
    void testUpdateGPA() {
        assertTrue(manager.updateGPA(1003, 3.5));
        assertFalse(manager.updateGPA(9999, 3.0)); // Non-existing student
    }

    @Test
    void testDisplayStudentsAboveGPA() {
        manager.displayStudentsAboveGPA(3.0);
    }
}
