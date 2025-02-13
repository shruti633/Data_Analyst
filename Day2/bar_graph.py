# import matplotlib.pyplot as plt

# fruits = ["apple","banana","orange"]
# quantity =[10,1,11]

# plt.bar(fruits,quantity,color='#FF5733')

# plt.xlabel('fruits')
# plt.ylabel('quantity')
# plt.title("Fruits vs Quantity")

# plt.show()



# import matplotlib.pyplot as plt

# fruits = ["apple", "banana", "orange", "grapes", "mango"]
# quantity = [10, 1, 11, 7, 6]

# # Add color variation to the bars
# colors = ['#FF6347', '#FFD700', '#32CD32', '#8A2BE2', '#FF1493']

# plt.bar(fruits, quantity, color=colors)

# # Add value labels on top of each bar
# for i, value in enumerate(quantity):
#     plt.text(i, value + 0.2, str(value), ha='center', va='bottom', fontsize=12, color='black')

# # Rotate x-axis labels for better readability
# plt.xticks(rotation=45)

# # Add gridlines for better readability of values
# plt.grid(axis='y', linestyle='--', alpha=0.7)

# # Set background color
# plt.gcf().set_facecolor('#f0f0f0')

# # Set the labels and title
# plt.xlabel('Fruits', fontsize=14)
# plt.ylabel('Quantity', fontsize=14)
# plt.title('Fruits vs Quantity', fontsize=16)

# plt.show()





import matplotlib.pyplot as plt

fruits = ["apple", "banana", "orange", "grapes", "mango"]
quantity = [10, 1, 11, 7, 6]

# Assigning colors based on the natural color of each fruit
fruit_colors = {
    "apple": "#FF0800",   # Red
    "banana": "#FFD700",  # Yellow
    "orange": "#FFA500",  # Orange
    "grapes": "#6A0DAD",  # Purple
    "mango": "#FFB347"    # Mango Yellow
}

# Getting the corresponding colors for each fruit in the list
colors = [fruit_colors[fruit] for fruit in fruits]

plt.bar(fruits, quantity, color=colors)

# Add value labels on top of each bar
for i, value in enumerate(quantity):
    plt.text(i, value + 0.2, str(value), ha='center', va='bottom', fontsize=12, color='black')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

# Add gridlines for better readability of values
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Set background color
plt.gcf().set_facecolor('#f0f0f0')

# Set the labels and title
plt.xlabel('Fruits', fontsize=14)
plt.ylabel('Quantity', fontsize=14)
plt.title('Fruits vs Quantity', fontsize=16)

plt.show()