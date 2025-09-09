# Top 10 Largest Economies by GDP (IMF Data)

This project extracts and displays the **Top 10 largest economies in the world** (in Billion USD) based on data logged by the **International Monetary Fund (IMF)**.  
The script uses **Pandas** to scrape and clean GDP data from an archived Wikipedia page (stable snapshot).

---

## Project Structure
top-10-economies/
│── top_10_economies.py # Main Python script
│── README.md # Project documentation

---

#Requirements
Make sure you have Python 3 installed.  
You’ll also need the following Python libraries:

- `pandas`
- `numpy`
- `lxml`  

Install them using:

```bash
pip install pandas numpy lxml
▶ Usage
Run the script from your terminal:

bash
Copy code
python top_10_economies.py

Future Improvements
Allow user to specify how many top economies to display (e.g., top 5, top 20).

Add option to export results as CSV/Excel.

Automate updates with the latest IMF/Wikipedia data.
