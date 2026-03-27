# Python Grade Analyzer 📊

A comprehensive CLI-based application for analyzing student grades and generating detailed reports. This tool helps educators manage student data, compute statistics, and track academic performance efficiently.

## 🎯 Description

The Grade Analyzer is a command-line application that provides a complete solution for grade management and analysis. It offers an intuitive menu-driven interface for adding students, recording grades, generating rankings, and producing comprehensive reports. The application supports CSV file operations for data persistence and bulk operations.

## ✨ Features

- **Student Management**: Add and manage student records with unique IDs
- **Grade Recording**: Input and validate individual student grades (0-100 scale)
- **Statistical Analysis**: Calculate averages, rankings, and grade distributions
- **Letter Grade Assignment**: Automatic conversion to standard letter grades (A-F)
- **Comprehensive Reports**: Generate detailed class performance reports
- **CSV Support**: Import/export data for backup and bulk operations
- **Data Validation**: Input validation and error handling
- **Interactive Menu**: User-friendly command-line interface

## 🎓 Learning Outcomes

By working with this project, you'll learn:

- **Object-Oriented Programming**: Classes, methods, and encapsulation
- **Data Structures**: Lists, dictionaries, and structured data handling
- **File I/O Operations**: CSV reading/writing and file management
- **Data Analysis**: Statistical calculations and data processing
- **Input Validation**: Error handling and user input validation
- **Menu-Driven Programming**: Interactive CLI application design
- **Code Organization**: Modular functions and clean code practices

## 🛠️ Technologies Used

- **Python 3.7+**: Core programming language
- **CSV Module**: For data import/export functionality
- **Type Hints**: For better code documentation and IDE support
- **Standard Library Only**: No external dependencies required

## 📦 Installation

1. **Clone or download** this repository
2. **Ensure Python 3.7+** is installed on your system
3. **Navigate** to the project directory

```bash
cd python-grade-analyzer
```

No additional dependencies need to be installed as the project uses only Python's standard library.

## 🚀 How to Run

### Method 1: Direct Execution
```bash
python grade_analyzer.py
```

### Method 2: Make Executable (Linux/Mac)
```bash
chmod +x grade_analyzer.py
./grade_analyzer.py
```

### Method 3: Python Module
```bash
python -m grade_analyzer
```

## 💡 Example Usage

### Basic Workflow

1. **Start the application**
   ```bash
   python grade_analyzer.py
   ```

2. **Add students** (Option 1)
   - Enter student name and optional ID
   - Repeat for multiple students

3. **Add grades** (Option 2)
   - Select a student by name
   - Enter grades one by one
   - Press Enter with empty input to finish

4. **View results** (Options 3-5)
   - View all students and their data
   - Check student rankings
   - Generate comprehensive reports

5. **Save/Load data** (Options 6-7)
   - Export data to CSV for backup
   - Import existing CSV data

### Sample CSV Format

```csv
name,student_id,grade1,grade2,grade3,grade4
Alice Johnson,STU001,95,87,92,89
Bob Smith,STU002,78,82,75,80
Charlie Brown,STU003,88,91,85,87
```

## 📋 Sample Output

### Main Menu
```
==================================================
           GRADE ANALYZER SYSTEM
==================================================
1. Add Student
2. Add Grades to Student
3. View All Students
4. View Student Rankings
5. Generate Summary Report
6. Load Data from CSV
7. Save Data to CSV
8. Exit
==================================================
```

### Student Rankings
```
--- Student Rankings ---
Rank  Name                 Average  Letter Grade
---------------------------------------------
1     Diana Prince         94.75    A
2     Henry Davis          90.25    A
3     Alice Johnson        90.75    A
4     Charlie Brown        87.75    B
5     Grace Lee            85.25    B
```

### Summary Report
```
============================================================
                    GRADE ANALYSIS REPORT
============================================================
Total Students: 10
Class Average: 81.45

Grade Distribution:
  A: 3 students (30.0%)
  B: 4 students (40.0%)
  C: 2 students (20.0%)
  D: 0 students (0.0%)
  F: 1 students (10.0%)

Top 3 Performers:
  1. Diana Prince: 94.75 (A)
  2. Henry Davis: 90.25 (A)
  3. Alice Johnson: 90.75 (A)

Students Needing Attention (1 students):
  - Frank Miller: 48.75 (F)
============================================================
```

## 📁 Project Structure

```
python-grade-analyzer/
├── grade_analyzer.py      # Main application file
├── sample_grades.csv      # Sample data file
├── README.md             # Project documentation
├── .gitignore           # Git ignore file
└── LICENSE              # MIT License
```

### File Descriptions

- **`grade_analyzer.py`**: Main application containing all classes and functions
- **`sample_grades.csv`**: Example CSV file with sample student data
- **`README.md`**: Comprehensive project documentation
- **`.gitignore`**: Excludes unnecessary files from version control
- **`LICENSE`**: MIT license for open-source usage

## 🔧 Code Structure

### Classes

- **`Student`**: Represents individual student with grades and calculations
- **`GradeAnalyzer`**: Main application class handling all operations

### Key Functions

- **`validate_grade_input()`**: Input validation for grades
- **`display_menu()`**: Shows the main menu interface
- **`add_student_interactive()`**: Interactive student addition
- **`add_grades_interactive()`**: Interactive grade entry
- **`view_all_students()`**: Display all student data
- **`view_rankings()`**: Show ranked student list
- **`generate_report()`**: Create comprehensive analysis report
- **`load_csv_interactive()`**: CSV data import
- **`save_csv_interactive()`**: CSV data export

## 🚀 Future Improvements

### Potential Enhancements

1. **Graphical User Interface (GUI)**
   - Tkinter or PyQt implementation
   - Visual charts and graphs
   - Drag-and-drop CSV import

2. **Advanced Analytics**
   - Grade trend analysis over time
   - Statistical measures (median, mode, standard deviation)
   - Performance prediction algorithms

3. **Database Integration**
   - SQLite for persistent storage
   - Multi-class support
   - Historical data tracking

4. **Visualization Features**
   - Matplotlib integration for charts
   - Grade distribution histograms
   - Performance trend graphs

5. **Export Options**
   - PDF report generation
   - Excel file support
   - Email report functionality

6. **Advanced Features**
   - Weighted grade categories
   - Attendance tracking
   - Parent/student portals

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add some AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### Contribution Guidelines

- Follow PEP 8 style guidelines
- Add docstrings to new functions
- Include type hints where appropriate
- Test your changes thoroughly
- Update documentation as needed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### MIT License Summary

- ✅ Commercial use
- ✅ Modification
- ✅ Distribution
- ✅ Private use
- ❌ Liability
- ❌ Warranty

## 👨‍💻 Author

**Python Developer**
- GitHub: [@Shme-CS](https://github.com/Shme-CS)
- Email: shme.solo@gmail.com

## 🙏 Acknowledgments

- Python Software Foundation for the excellent standard library
- The open-source community for inspiration and best practices
- Educators who provided requirements and feedback

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/Shme-CS/python-grade-analyzer/issues) page
2. Create a new issue with detailed description
3. Contact the author directly

---

**Happy Coding! 🐍✨**