import java.util.TreeMap;

/**
 *Overview:
 * You will create a Java application that manages student records. Each record will contain a student's ID, name,
 * and GPA. The student ID will serve as the unique key.  * The application should allow adding new student records, deleting records,
 * updating records, and displaying all records sorted by student ID.
 *
 * @author Keiffer Tan
 */

public class StudentRecordManager {

    private TreeMap<Integer, Student> studentRecords;

    public StudentRecordManager() {
        this.studentRecords = new TreeMap<>();
    }

    public boolean addStudent(int id, String name, double gpa) {
        // check student id is unique
        if (studentRecords.containsKey(id)) {
            System.out.println("Student ID already exists!");
            return false;
        }
        //add student if unique, otherwise return false
        studentRecords.put(id, new Student(id, name, gpa));

        return true;
    }

    public boolean deleteStudent(int id) {
        //check if student exists, if not return false
        if (!studentRecords.containsKey(id)) {
            System.out.println("Student doesn't exist!");
            return false;
        }

        studentRecords.remove(id);
        return true;
    }

    public boolean updateStudent(int id, double gpa) {
        //check student id if exists, return false if doesn't exist
        if (!studentRecords.containsKey(id)) {
            System.out.println("Student doesn't exist!");
            return false;
        }
        //get address of student object for updating purposes
        Student currStudent = studentRecords.get(id);
        currStudent.updateGpa(gpa);

        return true;
    }

    public void displayAllRecords() {
        //iterate through treemap displaying the names
        for (Student student : studentRecords.values()) {
            System.out.println(student);
        }
    }

    public void displayStudentsAboveGpa(double gpa) {
        // find students that have a gpa larger than the passed in parameter

        System.out.println("\n Students with a GPA above " + gpa + ":");
        for (Student student : studentRecords.values()) {
            if (student.getGpa() > gpa) {
                System.out.println(student);
            }
        }
    }


    public static void main(String[] args) {
        StudentRecordManager studentRecordsManager = new StudentRecordManager();
        studentRecordsManager.displayAllRecords();

        studentRecordsManager.addStudent(1003, "Charlie", 2.8);
        studentRecordsManager.addStudent(1002, "Bob", 3.2);
        studentRecordsManager.addStudent(1005, "Eve", 3.1);
        studentRecordsManager.addStudent(1006, "Adam", 2.3);
        studentRecordsManager.addStudent(1004, "David", 3.9);
        studentRecordsManager.addStudent(1007, "Steve", 1.8);
        studentRecordsManager.addStudent(1001, "Alice", 3.5);

        studentRecordsManager.displayAllRecords();

        studentRecordsManager.displayStudentsAboveGpa(3.1);
//
//        studentRecordsManager.deleteStudent(1000);
////        System.out.println(studentRecordsManager.deleteStudent(1001));
//        studentRecordsManager.deleteStudent(1004);
//
//        studentRecordsManager.displayAllRecords();
//
//        studentRecordsManager.updateStudent(1001, 4.0);
//        studentRecordsManager.displayAllRecords();

    }
}

class Student {
    private int id;
    private String name;
    private double gpa;

    public Student (int id, String name, double gpa) {
        this.id = id;
        this.name = name;
        this.gpa = gpa;
    }

    public int getId() {
        return this.id;
    }

    public String getName() {
        return this.name;
    }

    public double getGpa() {
        return this.gpa;
    }

    public void updateGpa(double gpa) {
        // Possible return a boolean value if update is successful
        this.gpa = gpa;
    }

    @Override
    public String toString() {
        return "ID: " + this.id + ", Name: " + this.name + ", GPA: " + this.gpa;
    }

}
