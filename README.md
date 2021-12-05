# Python-Student-Marks-Analyser

---
### CITS1401 - Computational Thinking with Python - Project_1 - (2020/SEM-1)
#### University of Western Australia

---
#### Overview
UWA, like every university around the country needs to deal with marks of the students in different courses. For the analysis of university’s performance, management needs to have a computer program which can read the data from a csv (comma separated values) file and return different statistical aspects of the marks of the students and their ranking.

---
#### Problem Specification
Your task is to write a program which follow the following specifications.

**Input:**

Your program must define the function `main` with the following signature:
~~~
def main(csvfile):
~~~
The input argument is the name of the csv file containing information and marks of the students which needs to be analysed. The first row of the csv file will contain the headers. From the second row, the first and second values of each row contain the names and any other information of the students. From third value onwards, it contains the marks student obtained in each subject. We do not have prior knowledge about the number of students and subjects available in the csv file.

---
**Output:**

The function is required to return the following outputs in the order provided below:

- List containing the **minimum** marks for each subject followed by minimum total marks obtained by a student. The order of the subjects should be same as the order of the subjects in the header row.
- List similar to above containing the **maximum** marks.
- List similar to above containing the **average** marks.
- List similar to above containing the **standard deviations** in marks.
- List similar to above containing the **correlation** of the ranks of the subject marks and total marks. The highest mark will be ranked as ‘1’, the second highest mark will be ranked ‘2’ and so on. If two or more students get the same marks then they should be ranked according to their names in alphabetical order. Two students cannot have the same rank for a course or total marks which means two student cannot be with the same name and marks. Use *Spearman’s rank correlation coefficient* for calculating the correlation of rankings.

All returned lists must contain numerical values rounded to four decimal places.
Remember not to round the values during calculations and round them only at the
time of saving them in the output lists.

---
**Example:**
An example interaction is:
~~~
>>> mn,mx,avg,std,cor = main('sample_student_marks.csv')
~~~
The output returned in the variables are:
~~~
>>> mn
[0.0, 6.0, 3.0, 5.0, 1.0, 7.0, 9.0, 2.0, 262.0]
>>> mx
[98.0, 96.0, 92.0, 92.0, 96.0, 97.0, 94.0, 100.0, 587.0]
>>> avg
[49.7667, 53.2333, 61.7333, 54.6333, 57.2333, 55.0, 50.5, 43.0, 425.1]
>>> std
[31.3706, 24.5678, 25.737, 26.1731, 31.6014, 27.3496, 23.8841, 30.7864, 83.7661]
>>> cor
[0.2654, 0.2908, 0.3286, 0.3428, 0.4051, 0.2863, 0.4309, 0.495, 1.0]
~~~

---
NOTE: THIS PROJECT WAS PART OF THE COMPUTATIONAL THINKING WITH PYTHON  UNIT (CITS1401) AT THE UNIVERSITY OF WESTERN AUSTRALIA.
