#!/usr/bin/env python3
"""
Grade Analyzer - A CLI-based application for analyzing student grades
Author: Python Developer
License: MIT
"""

import csv
import os
import sys
from typing import List, Dict, Tuple, Optional


class Student:
    """Represents a student with their grades."""
    
    def __init__(self, name: str, student_id: str = ""):
        self.name = name
        self.student_id = student_id
        self.grades = []
    
    def add_grade(self, grade: float) -> None:
        """Add a grade to the student's record."""
        if 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            raise ValueError("Grade must be between 0 and 100")
    
    def get_average(self) -> float:
        """Calculate the student's average grade."""
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)
    
    def get_letter_grade(self) -> str:
        """Convert average to letter grade."""
        avg = self.get_average()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'
    
    def __str__(self) -> str:
        return f"{self.name} (ID: {self.student_id})"


class GradeAnalyzer:
    """Main class for grade analysis functionality."""
    
    def __init__(self):
        self.students = []
    
    def add_student(self, name: str, student_id: str = "") -> Student:
        """Add a new student to the analyzer."""
        student = Student(name, student_id)
        self.students.append(student)
        return student
    
    def find_student(self, name: str) -> Optional[Student]:
        """Find a student by name."""
        for student in self.students:
            if student.name.lower() == name.lower():
                return student
        return None
    
    def get_class_average(self) -> float:
        """Calculate the overall class average."""
        if not self.students:
            return 0.0
        
        total_avg = sum(student.get_average() for student in self.students)
        return total_avg / len(self.students)
    
    def get_ranked_students(self) -> List[Tuple[Student, float]]:
        """Get students ranked by their average grades."""
        student_averages = [(student, student.get_average()) for student in self.students]
        return sorted(student_averages, key=lambda x: x[1], reverse=True)
    
    def get_grade_distribution(self) -> Dict[str, int]:
        """Get distribution of letter grades."""
        distribution = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
        for student in self.students:
            letter_grade = student.get_letter_grade()
            distribution[letter_grade] += 1
        return distribution
    
    def load_from_csv(self, filename: str) -> bool:
        """Load student data from CSV file."""
        try:
            with open(filename, 'r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    student = self.add_student(row['name'], row.get('student_id', ''))
                    # Load grades (assuming they're in columns like grade1, grade2, etc.)
                    for key, value in row.items():
                        if key.startswith('grade') and value:
                            try:
                                student.add_grade(float(value))
                            except ValueError:
                                continue
            return True
        except FileNotFoundError:
            print(f"File {filename} not found.")
            return False
        except Exception as e:
            print(f"Error loading CSV: {e}")
            return False
    
    def save_to_csv(self, filename: str) -> bool:
        """Save student data to CSV file."""
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as file:
                if not self.students:
                    return True
                
                # Determine maximum number of grades
                max_grades = max(len(student.grades) for student in self.students)
                
                fieldnames = ['name', 'student_id'] + [f'grade{i+1}' for i in range(max_grades)]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                
                for student in self.students:
                    row = {'name': student.name, 'student_id': student.student_id}
                    for i, grade in enumerate(student.grades):
                        row[f'grade{i+1}'] = grade
                    writer.writerow(row)
            return True
        except Exception as e:
            print(f"Error saving CSV: {e}")
            return False


def validate_grade_input(grade_str: str) -> float:
    """Validate and convert grade input."""
    try:
        grade = float(grade_str)
        if 0 <= grade <= 100:
            return grade
        else:
            raise ValueError("Grade must be between 0 and 100")
    except ValueError:
        raise ValueError("Invalid grade format")


def display_menu() -> None:
    """Display the main menu."""
    print("\n" + "="*50)
    print("           GRADE ANALYZER SYSTEM")
    print("="*50)
    print("1. Add Student")
    print("2. Add Grades to Student")
    print("3. View All Students")
    print("4. View Student Rankings")
    print("5. Generate Summary Report")
    print("6. Load Data from CSV")
    print("7. Save Data to CSV")
    print("8. Exit")
    print("="*50)


def add_student_interactive(analyzer: GradeAnalyzer) -> None:
    """Interactive function to add a student."""
    print("\n--- Add New Student ---")
    name = input("Enter student name: ").strip()
    if not name:
        print("Name cannot be empty!")
        return
    
    student_id = input("Enter student ID (optional): ").strip()
    
    if analyzer.find_student(name):
        print(f"Student '{name}' already exists!")
        return
    
    analyzer.add_student(name, student_id)
    print(f"Student '{name}' added successfully!")


def add_grades_interactive(analyzer: GradeAnalyzer) -> None:
    """Interactive function to add grades to a student."""
    print("\n--- Add Grades ---")
    name = input("Enter student name: ").strip()
    
    student = analyzer.find_student(name)
    if not student:
        print(f"Student '{name}' not found!")
        return
    
    print(f"Adding grades for {student}")
    print("Enter grades one by one (press Enter with empty input to finish):")
    
    while True:
        grade_input = input("Grade (0-100): ").strip()
        if not grade_input:
            break
        
        try:
            grade = validate_grade_input(grade_input)
            student.add_grade(grade)
            print(f"Grade {grade} added successfully!")
        except ValueError as e:
            print(f"Error: {e}")


def view_all_students(analyzer: GradeAnalyzer) -> None:
    """Display all students and their information."""
    print("\n--- All Students ---")
    if not analyzer.students:
        print("No students found!")
        return
    
    print(f"{'Name':<20} {'ID':<10} {'Grades':<15} {'Average':<8} {'Letter'}")
    print("-" * 70)
    
    for student in analyzer.students:
        grades_str = ", ".join(f"{g:.1f}" for g in student.grades) if student.grades else "No grades"
        avg = student.get_average()
        letter = student.get_letter_grade()
        print(f"{student.name:<20} {student.student_id:<10} {grades_str:<15} {avg:<8.2f} {letter}")


def view_rankings(analyzer: GradeAnalyzer) -> None:
    """Display student rankings."""
    print("\n--- Student Rankings ---")
    if not analyzer.students:
        print("No students found!")
        return
    
    ranked_students = analyzer.get_ranked_students()
    
    print(f"{'Rank':<5} {'Name':<20} {'Average':<8} {'Letter Grade'}")
    print("-" * 45)
    
    for rank, (student, avg) in enumerate(ranked_students, 1):
        letter = student.get_letter_grade()
        print(f"{rank:<5} {student.name:<20} {avg:<8.2f} {letter}")


def generate_report(analyzer: GradeAnalyzer) -> None:
    """Generate and display a comprehensive report."""
    print("\n" + "="*60)
    print("                    GRADE ANALYSIS REPORT")
    print("="*60)
    
    if not analyzer.students:
        print("No data available for report generation!")
        return
    
    # Basic statistics
    total_students = len(analyzer.students)
    class_avg = analyzer.get_class_average()
    
    print(f"Total Students: {total_students}")
    print(f"Class Average: {class_avg:.2f}")
    
    # Grade distribution
    distribution = analyzer.get_grade_distribution()
    print(f"\nGrade Distribution:")
    for grade, count in distribution.items():
        percentage = (count / total_students) * 100 if total_students > 0 else 0
        print(f"  {grade}: {count} students ({percentage:.1f}%)")
    
    # Top performers
    ranked_students = analyzer.get_ranked_students()
    print(f"\nTop 3 Performers:")
    for i, (student, avg) in enumerate(ranked_students[:3], 1):
        print(f"  {i}. {student.name}: {avg:.2f} ({student.get_letter_grade()})")
    
    # Students needing attention (grade F or D)
    struggling_students = [(s, avg) for s, avg in ranked_students if avg < 70]
    if struggling_students:
        print(f"\nStudents Needing Attention ({len(struggling_students)} students):")
        for student, avg in struggling_students:
            print(f"  - {student.name}: {avg:.2f} ({student.get_letter_grade()})")
    
    print("="*60)


def load_csv_interactive(analyzer: GradeAnalyzer) -> None:
    """Interactive function to load data from CSV."""
    print("\n--- Load Data from CSV ---")
    filename = input("Enter CSV filename: ").strip()
    
    if not filename:
        print("Filename cannot be empty!")
        return
    
    if analyzer.load_from_csv(filename):
        print(f"Data loaded successfully from {filename}!")
        print(f"Loaded {len(analyzer.students)} students.")
    else:
        print("Failed to load data from CSV.")


def save_csv_interactive(analyzer: GradeAnalyzer) -> None:
    """Interactive function to save data to CSV."""
    print("\n--- Save Data to CSV ---")
    filename = input("Enter CSV filename: ").strip()
    
    if not filename:
        print("Filename cannot be empty!")
        return
    
    if analyzer.save_to_csv(filename):
        print(f"Data saved successfully to {filename}!")
    else:
        print("Failed to save data to CSV.")


def main():
    """Main function to run the Grade Analyzer application."""
    analyzer = GradeAnalyzer()
    
    print("Welcome to the Grade Analyzer System!")
    print("This application helps you manage and analyze student grades.")
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (1-8): ").strip()
        
        if choice == '1':
            add_student_interactive(analyzer)
        elif choice == '2':
            add_grades_interactive(analyzer)
        elif choice == '3':
            view_all_students(analyzer)
        elif choice == '4':
            view_rankings(analyzer)
        elif choice == '5':
            generate_report(analyzer)
        elif choice == '6':
            load_csv_interactive(analyzer)
        elif choice == '7':
            save_csv_interactive(analyzer)
        elif choice == '8':
            print("\nThank you for using Grade Analyzer!")
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice! Please enter a number between 1-8.")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()