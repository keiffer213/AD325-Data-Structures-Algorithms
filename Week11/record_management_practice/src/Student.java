/**
 * Represents a student with ID, name, and GPA.
 */
class Student {
    private int id;
    private String name;
    private double gpa;

    public Student(int id, String name, double gpa) {
        this.id = id;
        this.name = name;
        this.gpa = gpa;
    }
    public int getId() {
        return id;
    }
    public String getName() {
        return name;
    }
    public double getGpa() {
        return gpa;
    }
    public void setGpa(double gpa) {
        this.gpa = gpa;
    }
    @Override
    public String toString() {
        return "ID: " + id + ", Name: " + name + ", GPA: " + gpa;
    }
}



//
//class Student {
//    private int id;
//    private String name;
//    private double gpa;
//
//    public Student (int id, String name, double gpa){
//        this.id = id;
//        this.name = name;
//        this.gpa = gpa;
//    }
//
//    public int getId(){
//        return this.id;
//    }
//
//    public String getName(){
//        return this.name;
//    }
//
//    public double getGpa(){
//        return this.gpa;
//    }
//
//    public void updateGpa(double gpa) {
//        this.gpa = gpa;
//    }
//
//    @Override
//    public String toString(){
//        return "ID: " + this.id + ", Name: " + this.name+ ", GPA: "+ this.gpa;
//    }
//
//}

