import java.util.Map;
import java.util.TreeMap;

/**
 * Manages student records using a TreeMap sorted by student ID.
 */
public class StudentRecordManager {
    private TreeMap<Integer, Student> studentRecords;

    public StudentRecordManager() {
        this.studentRecords = new TreeMap<>();
    }

    /**
     * Adds a new student record to the TreeMap.
     */
    public boolean addStudent(int id, String name, double gpa) {
        if (studentRecords.containsKey(id)) {
            System.out.println("Error: Student ID already exists.");
            return false;
        }
        studentRecords.put(id, new Student(id, name, gpa));
        return true;
    }

    /**
     * Deletes a student record from the TreeMap using the student ID.
     */
    public boolean deleteStudent(int id) {
        if (studentRecords.remove(id) != null) {
            return true;
        } else {
            System.out.println("Error: Student ID not found.");
            return false;
        }
    }

    /**
     * Updates the GPA of a student given their ID.
     */
    public boolean updateGPA(int id, double newGPA) {
        Student student = studentRecords.get(id);
        if (student != null) {
            student.setGpa(newGPA);
            return true;
        }
        System.out.println("Error: Student ID not found.");
        return false;
    }

    /**
     * Displays all student records sorted by student ID.
     */
    public void displayAllRecords() {
        if (studentRecords.isEmpty()) {
            System.out.println("No student records available.");
            return;
        }
        System.out.println("\nStudent Records (Sorted by ID):");
        for (Student student : studentRecords.values()) {
            System.out.println(student);
        }
    }

    /**
     * Displays students whose GPA is above a specified value.
     */
    public void displayStudentsAboveGPA(double gpaThreshold) {
        System.out.println("\nStudents with GPA above " + gpaThreshold + ":");
        for (Student student : studentRecords.values()) {
            if (student.getGpa() > gpaThreshold) {
                System.out.println(student);
            }
        }
    }

    // Main method to test functionalities
    public static void main(String[] args) {
        StudentRecordManager manager = new StudentRecordManager();

        // Adding 5 student records
        manager.addStudent(1001, "Alice", 3.5);
        manager.addStudent(1002, "Bob", 3.2);
        manager.addStudent(1003, "Charlie", 2.8);
        manager.addStudent(1004, "David", 3.9);
        manager.addStudent(1005, "Eve", 3.1);

        // Display all records (should be sorted by ID)
        manager.displayAllRecords();

        // Update a student's GPA
        manager.updateGPA(1003, 3.3);
        manager.displayAllRecords();  // Check if updated

        // Delete a student record
        manager.deleteStudent(1002);
        manager.displayAllRecords();  // Check after deletion

        // Display students with GPA > 3.0
        manager.displayStudentsAboveGPA(3.0);
    }
}


