import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ✅ Generate a lengthy DataFrame with 50 rows
np.random.seed(42)  # For reproducibility

categories = [f"Category_{i}" for i in range(1, 51)]
values = np.random.randint(10, 100, size=50)  # Random values between 10 and 100
percentages = np.round(np.random.uniform(0, 1, size=50) * 100, 2)  # Random percentages
dates = pd.date_range(start="2024-01-01", periods=50, freq="D")  # Generate 50 consecutive dates

df = pd.DataFrame({
    "Category": categories,
    "Values": values,
    "Percentage": percentages,
    "Date": dates
})
df2=pd.read_excel('test2.xlsx')
list_0ne=[1,2,3,4,5,]

# ✅ Plot a graph
plt.figure(figsize=(12, 6))
plt.plot(df["Date"], df["Values"], marker="o", linestyle="-", label="Values")
plt.plot(df["Date"], df["Percentage"], marker="s", linestyle="--", label="Percentage")

plt.xlabel("Date")
plt.ylabel("Values / Percentage")
plt.title("Trend of Values and Percentages Over Time")
plt.xticks(rotation=45)
plt.legend()
plt.grid()
print('Done and dusted')

 
import json
import io
import base64
import matplotlib.pyplot as plt
import numpy as np
from pandas import DataFrame

# ✅ Define a set of excluded system variables
excluded_vars = {"json", "pd", "plt", "np", "io", "base64", "DataFrame", "excluded_vars", "get_user_variables", "capture_plot"}

# ✅ Capture all user-defined variables, excluding system objects
def get_user_variables():
    return {
        k: v for k, v in globals().items()
        if not k.startswith("__") and k != "__annotations__" 
        and k not in excluded_vars
    }

# ✅ Function to capture and encode Matplotlib plots
def capture_plot():
    buf = io.BytesIO()  # Create buffer for image
    plt.savefig(buf, format="png", bbox_inches='tight')  # Save figure to buffer
    plt.close()  # Close the plot to prevent overlapping figures
    buf.seek(0)  # Move to beginning of buffer
    return base64.b64encode(buf.read()).decode("utf-8")  # Convert to Base64 string

global_vars = get_user_variables()  # ✅ Extract only valid user-defined variables

# ✅ Process and print detected variables
for var_name, value in global_vars.items():
    try:
        if isinstance(value, DataFrame):
            table_html = value.to_html(border=1, classes="styled-table")  
            # print(f"##VAR##{var_name}##HTML##{table_html}")  
        else:
            json_value = json.dumps(value, default=str)  
            # print(f"##VAR##{var_name}##JSON##{json_value}")
    except Exception as e:
        print(f"##VAR##{var_name}##ERROR##{str(e)}")  

# ✅ Capture Matplotlib output if any figures exist
if plt.get_fignums():  
    plot_base64 = capture_plot()
    # print(f"##VAR##matplotlib_plot##IMG##{plot_base64}")  
