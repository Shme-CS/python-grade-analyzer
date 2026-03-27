# Code Explanation - Python Grade Analyzer

This document provides a detailed explanation of the code structure, design decisions, and implementation details of the Grade Analyzer application.

## 🏗️ Architecture Overview

The application follows an object-oriented design with two main classes and supporting utility functions:

```
┌─────────────────┐    ┌─────────────────┐
│     Student     │    │  GradeAnalyzer  │
│                 │    │                 │
│ - name          │    │ - students[]    │
│ - student_id    │◄───┤                 │
│ - grades[]      │    │ + add_student() │
│                 │    │ + find_studen