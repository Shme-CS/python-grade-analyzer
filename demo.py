#!/usr/bin/env python3
"""
Demo script for Grade Analyzer
This script demonstrates the key features of the Grade Analyzer application.
"""

from grade_analyzer import GradeAnalyzer, Student


def run_demo():
    """Run a demonstration of the Grade Analyzer features."""
    print("="*60)
    print("           GRADE ANALYZER DEMO")
    print("="*60)
    
    # Create analyzer instance
    analyzer = GradeAnalyzer()
    
    # Add sample students and grades
    print("\n1. Adding sample students and grades...")
    
    # Student 1
    alice = analyzer.add_student("Alice Johnson", "STU001")
    alice.add_grade(95)
    alice.add_grade(87)
    alice.add_grade(92)
    alice.add_grade(89)
    
    # Student 2
    bob = analyzer.add_student("Bob Smith", "STU002")
    bob.add_grade(78)
    bob.add_grade(82)
    bob.add_grade(75)
    bob.add_grade(80)
    
    # Student 3
    charlie = analyzer.add_student("Charlie Brown", "STU003")
    charlie.add_grade(88)
    charlie.add_grade(91)
    charlie.add_grade(85)
    charlie.add_grade(87)
    
    # Student 4
    diana = analyzer.add_student("Diana Prince", "STU004")
    diana.add_grade(92)
    diana.add_grade(95)
    diana.add_grade(98)
    diana.add_grade(94)
    
    # Student 5
    eve = analyzer.add_student("Eve Wilson", "STU005")
    eve.add_grade(65)
    eve.add_grade(70)
    eve.add_grade(68)
    eve.add_grade(72)
    
    print(f"✓ Added {len(analyzer.students)} students with grades")
    
    # Display all students
    print("\n2. Displaying all students:")
    print("-" * 70)
    print(f"{'Name':<20} {'ID':<10} {'Grades':<20} {'Average':<8} {'Letter'}")
    print("-" * 70)
    
    for student in analyzer.students:
        grades_str = ", ".join(f"{g:.0f}" for g in student.grades)
        avg = student.get_average()
        letter = student.get_letter_grade()
        print(f"{student.name:<20} {student.student_id:<10} {grades_str:<20} {avg:<8.2f} {letter}")
    
    # Show rankings
    print("\n3. Student Rankings:")
    print("-" * 50)
    print(f"{'Rank':<5} {'Name':<20} {'Average':<8} {'Letter'}")
    print("-" * 50)
    
    ranked_students = analyzer.get_ranked_students()
    for rank, (student, avg) in enumerate(ranked_students, 1):
        letter = student.get_letter_grade()
        print(f"{rank:<5} {student.name:<20} {avg:<8.2f} {letter}")
    
    # Generate comprehensive report
    print("\n4. Comprehensive Analysis Report:")
    print("="*60)
    
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
    print(f"\nTop 3 Performers:")
    for i, (student, avg) in enumerate(ranked_students[:3], 1):
        print(f"  {i}. {student.name}: {avg:.2f} ({student.get_letter_grade()})")
    
    # Students needing attention
    struggling_students = [(s, avg) for s, avg in ranked_students if avg < 70]
    if struggling_students:
        print(f"\nStudents Needing Attention ({len(struggling_students)} students):")
        for student, avg in struggling_students:
            print(f"  - {student.name}: {avg:.2f} ({student.get_letter_grade()})")
    
    # CSV operations demo
    print("\n5. CSV Operations Demo:")
    
    # Save to CSV
    csv_filename = "demo_grades.csv"
    if analyzer.save_to_csv(csv_filename):
        print(f"✓ Data saved to {csv_filename}")
    
    # Create new analyzer and load from CSV
    new_analyzer = GradeAnalyzer()
    if new_analyzer.load_from_csv(csv_filename):
        print(f"✓ Data loaded from {csv_filename}")
        print(f"✓ Loaded {len(new_analyzer.students)} students")
    
    print("\n" + "="*60)
    print("Demo completed! Run 'python grade_analyzer.py' for interactive mode.")
    print("="*60)


if __name__ == "__main__":
    run_demo()