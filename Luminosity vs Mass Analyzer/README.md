# 🌟 Luminosity vs Mass Analyzer
👨‍💻 Author

Md. Mahiuddin Zilani
---
## 🧠 Overview

This Python project analyzes the relationship between a star’s mass and luminosity using real or sample data.
In stellar physics, stars roughly follow a power-law relation:

L∝Ma
L∝M
a

where

L = Luminosity (brightness)

M = Mass (in solar masses)

a ≈ 3.5 for main-sequence stars

This script reads data from a CSV file, performs a log-log power-law fit, and plots both linear and log-log graphs for visualization.

---
## 🚀 Features

✅ Reads data from a CSV file (e.g. stars_data.csv)
✅ Checks for missing or invalid data automatically
✅ Fits a power law 
L=kMa
L=kM
a
 to find constants k and a
✅ Saves both linear and log-log plots as .png images
✅ Compares the fitted exponent with the theoretical value (≈3.5)

---
## 📂 Example CSV Format

Your CSV file must contain the following columns:

Name,Mass_solar,Luminosity_solar
Sun,1,1
Sirius,2.1,25
AlphaCentauriA,1.1,1.5
ProximaCentauri,0.12,0.0017
Vega,2.14,40
Rigel,18,120000
Betelgeuse,20,90000

---
## 💡 Tip:
Make sure there are commas (,) between values, not spaces or tabs!

## ⚙️ How to Run
🪜 Step-by-Step

Prepare your CSV file
Save it as stars_data.csv in the same folder as the Python file.

Run the program
Open a terminal or command prompt, then type:

python luminosity_vs_mass.py --csv stars_data.csv
You’ll see the fitted power-law equation printed in the terminal:

Fitted power-law: L ≈ 1.2 * M^3.8
Compare theoretical exponent a = 3.5 (main-sequence approximation).
Two plots will be saved in the folder:

luminosity_mass_linear.png

luminosity_mass_loglog.png

## 📊 Output Graphs
🔹 Linear Scale

Shows the general trend of luminosity increasing rapidly with mass.

🔹 Log–Log Scale

Displays a straight-line fit showing the power-law nature of the relation.

Plot Type	Example Output
Linear	

Log-Log	
## 📚 Learning Outcome

By exploring this project, you’ll learn:

How stellar luminosity scales with mass

How to perform data fitting using NumPy

How to read and clean CSV data with Pandas

How to plot and save figures with Matplotlib

How to write structured and modular Python programs

---





