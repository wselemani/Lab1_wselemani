import csv
import sys
import os

def load_csv_data():
    """
    Prompts the user for a filename, checks if it exists,
    and extracts all fields into a list of dictionaries.
    """
    filename = input("Enter the name of the CSV file to process (e.g., grades.csv): ")
    if not os.path.exists(filename):
        print(f"Error: The file '{filename}' was not found.")
        sys.exit(1)
        
    assignments = []
    try:
        with open(filename, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Convert numeric fields to floats for calculations
                assignments.append({
                    'assignment': row['assignment'],
                    'group': row['group'],
                    'score': float(row['score']),
                    'weight': float(row['weight'])
                })

        if not assignments:
            print("Error: The CSV file is empty.")
            sys.exit(1)
        return assignments
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        sys.exit(1)

def evaluate_grades(data):
    """
    Processes assignment records, validates data, and computes final score/GPA.
    """
    print("\n--- Processing Grades ---")
    
    # a) Check if all scores are percentage based (0-100)
    for item in data:
        score = item['score']
        if not (0 <= score <= 100):
            print(f"Grade Validation Error: Assignment '{item['assignment']}' has invalid score: {score}. (Must be 0-100)")
            sys.exit(1)
            
    # b) Validate total weights (Total=100, Summative=40, Formative=60)
    summative_weight = 0.0
    formative_weight = 0.0

    summative_weighted_score = 0.0
    formative_weighted_score = 0.0
    failed_formatives = []
    
    for item in data:
        group = item['group'].strip().capitalize()
        weight = item['weight']
        score = item['score']
        weighted_contrib = (score * weight) / 100.0
        
        if group == "Summative":
            summative_weight += weight
            summative_weighted_score += weighted_contrib
        elif group == "Formative":
            formative_weight += weight
            formative_weighted_score += weighted_contrib

            # Track failed formative assignments (score < 50%) safely inside Formative block
            if score < 50:
                failed_formatives.append({
                    'assignment': item['assignment'],
                    'score': score,
                    'weight': weight
                })
        else:
            print(f"Validation Error: Unknown group '{group}' for assignment '{item['assignment']}'.")
            sys.exit(1)
            
    # Validate weight sums
    total_weight = summative_weight + formative_weight
    if round(total_weight, 2) != 100.0 or round(summative_weight, 2) != 40.0 or round(formative_weight, 2) != 60.0:
        print("Weight Validation Error:")
        print(f" - Expected Total Weight: 100, Got: {total_weight}")
        print(f" - Expected Summative: 40, Got: {summative_weight}")
        print(f" - Expected Formative: 60, Got: {formative_weight}")
        sys.exit(1)
        
    # c) Calculate the Final Grade and GPA
    summative_percentage = (summative_weighted_score / 40.0) * 100.0
    formative_percentage = (formative_weighted_score / 60.0) * 100.0
    final_grade = summative_weighted_score + formative_weighted_score
    
    # GPA Formula: (Total Grade / 100) * 5.0
    gpa = (final_grade / 100.0) * 5.0
    
    # d) Determine Pass/Fail status (>= 50% in BOTH categories)
    has_passed = (summative_percentage >= 50.0) and (formative_percentage >= 50.0)
    status = "PASSED" if has_passed else "FAILED"
    
    # e) Check for failed formative assignments (< 50%)
    resubmit_list = []
    if failed_formatives:
        max_weight = max(f['weight'] for f in failed_formatives)
        resubmit_list = [f['assignment'] for f in failed_formatives if f['weight'] == max_weight]
        
    # f) Print the final decision (PASSED / FAILED) and resubmission options
    print("\n==========================================")
    print("        FINAL GRADE EVALUATION            ")
    print("==========================================")
    print(f"Summative Score : {summative_weighted_score:.2f} / 40 ({summative_percentage:.2f}%)")
    print(f"Formative Score : {formative_weighted_score:.2f} / 60 ({formative_percentage:.2f}%)")
    print(f"Final Grade     : {final_grade:.2f}%")
    print(f"Calculated GPA  : {gpa:.2f} / 5.0")
    print(f"Final Status    : {status}")
    print("------------------------------------------")

    if resubmit_list:
        print("Eligible for Resubmission (Highest-Weighted Failed Formative):")
        for assignment in resubmit_list:
            print(f" - {assignment}")
    else:
        print("Eligible for Resubmission: None")
    print("==========================================\n")

if __name__ == "__main__":
    course_data = load_csv_data()
    evaluate_grades(course_data)

