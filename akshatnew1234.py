import matplotlib.pyplot as plt

# Student data
names = []
marks = []

# Input 5 students' data
for i in range(5):
    name = input(f"Enter name of student {i+1}: ")
    mark = int(input(f"Enter marks of {name}: "))
    names.append(name)
    marks.append(mark)

# Analytics
print("\n--- Results ---")
print(f"Average Marks: {sum(marks)/len(marks)}")
print(f"Highest: {names[marks.index(max(marks))]} with {max(marks)} marks")
print(f"Lowest: {names[marks.index(min(marks))]} with {min(marks)} marks")

# Plotting
plt.bar(names, marks, color='orange')
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks Analysis")
plt.grid(True)
plt.show()
