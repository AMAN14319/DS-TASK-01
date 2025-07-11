import pandas as pd
import matplotlib.pyplot as plt
from fpdf import FPDF

# Step 1: Create sample population data
data = {
    'Country': ['India', 'China', 'USA', 'Indonesia', 'Brazil'],
    '2015': [1311, 1376, 321, 258, 207],
    '2016': [1324, 1378, 323, 261, 209],
    '2017': [1339, 1380, 325, 264, 211],
    '2018': [1354, 1382, 327, 267, 213],
    '2019': [1369, 1384, 329, 270, 215],
    '2020': [1380, 1386, 331, 273, 217]
}
df = pd.DataFrame(data)
df.set_index('Country', inplace=True)

# Step 2: Plot bar chart for 2020 population
plt.figure(figsize=(10, 6))
df['2020'].plot(kind='bar', color='skyblue')
plt.title('Population of Countries in 2020 (in millions)')
plt.xlabel('Country')
plt.ylabel('Population (millions)')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Task_01_Population_Bar_Chart.png")  # Save image for PDF
plt.close()

# Step 3: Create PDF Report
class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Task-01: Population Visualization", ln=True, align="C")
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

pdf = PDF()
pdf.add_page()

# Step 4: Add task description
pdf.set_font("Arial", size=12)
description = (
    "Objective:\n"
    "Create a bar chart or histogram to visualize the distribution of a categorical or continuous variable, "
    "such as the distribution of ages or genders in a population.\n\n"
    "Dataset:\n"
    "Sample data used includes population data (in millions) from 2015 to 2020 for 5 countries: India, China, "
    "USA, Indonesia, and Brazil.\n\n"
    "Visualization:\n"
    "A bar chart has been created below to show the population of these countries in the year 2020."
)
pdf.multi_cell(0, 10, description)

# Step 5: Add chart image
pdf.image("Task_01_Population_Bar_Chart.png", x=10, y=None, w=180)

# Step 6: Save the PDF
pdf.output("Task_01_Report_with_Chart.pdf")
