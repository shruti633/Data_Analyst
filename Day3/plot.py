
# import matplotlib.pyplot as plt

# days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
# sales = [160,150,140,145,175,165,180]

# plt.plot(days,sales,marker="o")
# plt.title("Sales over Days")

# plt.xlabel("Days")
# plt.ylabel("Sales")
# plt.show()


import matplotlib.pyplot as plt  

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
sales = [160, 150, 140, 145, 175, 165, 180]  

plt.plot(days, sales, marker="o", markersize=8, markerfacecolor="red", markeredgecolor="black",
         linestyle="-.", color="blue", linewidth=2)  # Changed line to blue and dash-dot style

plt.title("Sales over Days", fontsize=14, fontweight='bold', color="darkblue")  
plt.xlabel("Days", fontsize=12, color="darkgreen")  
plt.ylabel("Sales", fontsize=12, color="darkgreen")  
plt.grid(True, linestyle="--", alpha=0.5, color="gray")  # Changed grid to light gray  

# Highlighting the maximum sales day
max_sales = max(sales)  
max_index = sales.index(max_sales)  
plt.text(days[max_index], max_sales + 3, f"Max: {max_sales}", 
         ha='center', fontsize=12, color='purple', fontweight='bold')  # Changed text color to purple

plt.show()  
