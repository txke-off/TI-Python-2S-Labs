import pandas as pd

students_df = pd.read_csv('students.csv')
grades_df = pd.read_csv('grades.csv')
merged = pd.merge(students_df, grades_df, on='StudentID', how='left')

grade_mapping = {
    'A': 5.0, 'A-': 4.7,
    'B+': 4.3, 'B': 4.0, 'B-': 3.7,
    'C+': 3.3, 'C': 3.0, 'C-': 2.7,
    'D+': 2.3, 'D': 2.0, 'F': 1.0
}
merged['NumGrade'] = merged['Grade'].map(grade_mapping)

avg = merged.groupby(['StudentID','Name'])['NumGrade'].mean().reset_index()
top = avg.loc[avg['NumGrade'].idxmax()]
cs = students_df[students_df['Major'] == 'Computer Science']

print("Средний балл студентов:")
print(avg.to_string(index=False))
print(f"Студент с наивысшим средним баллом: {top['Name']} ({top['NumGrade']:.2f})")
print("Студенты Computer Science:")
print(cs.to_string(index=False))