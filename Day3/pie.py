import matplotlib.pyplot as plt

subjects = ["DSA","Web Development","SAD","AI","Python"]
marks = [90,80,85,95,99]

plt.pie(marks, labels=subjects, startangle=90)
plt.title("Marks in different subjects")

plt.show()