# import matplotlib.pyplot as plt

# subjects = ["DSA","Web Development","SAD","AI","Python"]
# marks = [90,80,85,95,99]

# plt.pie(marks, labels=subjects, startangle=90)
# plt.title("Marks in different subjects")

# plt.show()


import matplotlib.pyplot as plt

# Data for the Pie chart
subjects = ["DSA", "Web Development", "SAD", "AI", "Python"]
marks = [90, 80, 85, 95, 99]


colors = ['#FF6347', '#FFD700', '#32CD32', '#8A2BE2', '#FF1493']  # Custom colors

# Creating the Pie chart with all features
plt.pie(marks, labels=subjects, startangle=90, colors=colors, shadow=True)

# Adding a Legend
plt.legend(subjects, loc="best")

# Adding a customized title
plt.title("Marks in different subjects", fontsize=16, fontweight='bold', family='serif', color='darkblue')

# Displaying the chart
plt.show()