Lab1_wselemani
# Graide Evaluator & Archiver

An automated Python and Bash application created for ALU to process student grades from CSV files, perform grade and weight validations, calculate GPA, evaluate pass/fail criteria, and handle file archiving.

# Repository Structure
grade-evaluator.py: Python application that reads grade data, validates scores and weight balances, calculates GPA, determines pass/fail status, and identifies eligible resubmissions.

organizer.sh: Bash shell script that automates archiving processed CSV files with a timestamp, resets the workspace, and logs operations.
organizer.log: Append-only log file recording the history of archived files

archive/: Directory where processed and timestamped CSV files are stored.

Readme.md: Instructions on how to set up and run the scripts.

Setup & CSV Requirements
Ensure a CSV file (e.g., grades.csv) exists in the same directory with the following column header format:

assignment,group,score,weight
Assignment 1,Formative,80,20
Assignment 2,Formative,45,20
Assignment 3,Formative,70,20
Final Exam,Summative,85,40
---

## How to Run

Clone the repository and enter the folder:

```bash
git clone https://github.com/wselemani/Lab1_wselemani.git
cd Lab1_wselemani
```

Run the Python grade evaluator:

```bash
python3 grade-evaluator.py
```

Run the Bash archiver:

```bash
bash organizer.sh
```

To trigger the archive manually, press `Ctrl + C` while the 
script is running. The signal trap will archive the current 
state and clean up the workspace automatically.

To view the archive log:

```bash
cat organizer.log
```
