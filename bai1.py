import csv
from collections import defaultdict

def read_csv(file_path):
    """
    Reads a CSV file and returns a list of dictionaries.
    Each dictionary represents a row in the CSV file.
    """
    data = []
    with open(file_path, mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

def process_data(data):
    """
    Processes the data to calculate average age and average score.
    """
    total_age = 0
    total_score = 0
    count = 0
    score_by_age_group = defaultdict(list)

    for row in data:
        age = int(row['age'])
        score = float(row['score'])
        
        total_age += age
        total_score += score
        count += 1

        # Categorize scores by age group
        age_group = (age // 10) * 10
        score_by_age_group[age_group].append(score)

    average_age = total_age / count if count > 0 else 0
    average_score = total_score / count if count > 0 else 0

    return average_age, average_score, score_by_age_group

def generate_report(average_age, average_score, score_by_age_group):
    """
    Generates a summary report.
    """
    report = f"Summary Report\n"
    report += f"--------------\n"
    report += f"Average Age: {average_age:.2f}\n"
    report += f"Average Score: {average_score:.2f}\n\n"
    report += f"Scores by Age Group:\n"

    for age_group, scores in score_by_age_group.items():
        average_group_score = sum(scores) / len(scores) if scores else 0
        report += f"  Age {age_group}-{age_group + 9}: {average_group_score:.2f}\n"

    return report

def main():
    file_path = 'sample_data.csv'  # Update with your CSV file path
    data = read_csv(file_path)
    average_age, average_score, score_by_age_group = process_data(data)
    report = generate_report(average_age, average_score, score_by_age_group)
    print(report)

if __name__ == "__main__":
    main()
