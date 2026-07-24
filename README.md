# Lab1_wselemani
# Grade Evaluator & Archiver

An automated Python and Bash application created for ALU to process student grades from CSV files, perform grade and weight validations, calculate GPA, evaluate pass/fail criteria, and handle file archiving.

---

## Repository Structure

* `grade-evaluator.py`: Python application that reads grade data, validates scores and weight balances, calculates GPA, determines pass/fail status, and identifies eligible resubmissions.
* `organizer.sh`: Bash shell script that automates archiving processed CSV files with a timestamp, resets the workspace, and logs operations.
* `organizer.log`: Append-only log file recording the history of archived files.
* `archive/`: Directory where processed and timestamped CSV files are stored.
* `Readme.md`: Instructions on how to set up and run the scripts.

---

## Setup & CSV Requirements

Ensure a CSV file (e.g., `grades.csv`) exists in the same directory with the following column header format:

```csv
assignment,group,score,weight
Assignment 1,Formative,80,20
Assignment 2,Formative,45,20
Assignment 3,Formative,70,20
Final Exam,Summative,85,40
