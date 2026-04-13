Create a file – pom.xml
<project xmlns="http://maven.apache.org/POM/4.0.0"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xsi:schemaLocation="http://maven.apache.org/POM/4.0.0
http://maven.apache.org/xsd/maven-4.0.0.xsd">
<modelVersion>4.0.0</modelVersion>
<groupId>com.example</groupId>
<artifactId>simple-maven-app</artifactId>
<version>1.0-SNAPSHOT</version>
<dependencies>
 <dependency>
 <groupId>junit</groupId>
 <artifactId>junit</artifactId>
 <version>4.13.2</version>
 <scope>test</scope>
 </dependency>
</dependencies>
</project>



Create a Maven Project in Git
• Create a new Git repository
• Create a simple Maven project structure manually, including the following files and folders:
o pom.xml
o src/main/java/com/example/App.java
o src/test/java/com/example/AppTest.java

public class App {
 // Method to calculate average
 public double calculateAverage(int[] marks) {
 if (marks == null || marks.length == 0) {
 throw new IllegalArgumentException("Marks cannot be empty");
 }
 int sum = 0;
 for (int mark : marks) {
 sum += mark;
 }
 return (double) sum / marks.length;
 }
 // Method to assign grade
 public String calculateGrade(double average) {
 if (average >= 90) return "A";
 else if (average >= 75) return "B";
 else if (average >= 60) return "C";
 else if (average >= 50) return "D";
 else return "F";
 }
 // Main method
 public static void main(String[] args) {
 App app = new App();
 int[] marks = {85, 90, 80, 75, 95};
 double average = app.calculateAverage(marks);
 String grade = app.calculateGrade(average);
 System.out.println("Average Marks: " + average);
 System.out.println("Grade: " + grade);
 }

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.Test;
class AppTest {
 App app = new App();
 @Test
 void testCalculateAverage() {
 int[] marks = {80, 90, 100};
 assertEquals(90.0, app.calculateAverage(marks));
 }
 @Test
 void testGradeA() {
 assertEquals("A", app.calculateGrade(92));
 }
 @Test
 void testGradeB() {
 assertEquals("B", app.calculateGrade(80));
 }
 @Test
 void testGradeC() {
 assertEquals("C", app.calculateGrade(65));
 }
 @Test
 void testGradeD() {
 assertEquals("D", app.calculateGrade(55));
 }
 @Test
 void testGradeF() {
 assertEquals("F", app.calculateGrade(40));
 }
 @Test
 void testEmptyMarks() {
 assertThrows(IllegalArgumentException.class, () -> {
 app.calculateAverage(new int[]{});
 });
 }

}


THEN OPEN VSCODE:
1. CLONE YOUR GIT REPOSITORY IN VSCODE
2. In the TERMINAL type command: mvn clean test
mvn test
mvn compile

NOW OPEN JENKINS:
1. NEW ITEM
2. ENTER NAME AND SELECT PIPELINE
3. CLICK OK

IN THE PIPELINE SCRIPT ADD THE FOLLOWING CODE:
pipeline {
agent any
tools {
maven 'M3'
}
stages {
stage('Checkout Git') {
steps {
git branch: 'main',
url: 'https://github.com/balaganeshn/simple-maven-app'
}
}
stage('Build and Test') {
steps {
bat 'mvn clean test'
}
}
}
}
UPDATE THE GITHUB url TO YOUR REPOSITORY URL
