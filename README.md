# Budget-vs-Actual-Analysis
## 1.Project Overview
    M project focuses on Budget vs Actual Analysis, a core finance and business analytics use case used to monitor financial performance, control costs, and support managerial decision-making.
    The goal is to compare planned (budgeted) financial values with actual results, calculates variances, and interpret what these variances mean for the business.
    My project is designed as GitHub portfolio project using Python, following best practices in analytics documentation
## 2.Business Problem Statement
    Many organizations face the following problem:
    "We create budgets, but at the end of the period, actual expenses and revenues differ significantly. Management wants to understand where, why and how to take corrective actions"
    -Cost overruns go unnotices
    -Profit decreas
    -Financial planning becomes unreliable
## 3.Business Objectives
    The objectives of this analysis are:
    -Compare budgeted vs actual financial figures
    -Identify favorable and unfavorable variances
    -Highlight departments or categories responsible for deviations
    -Support management decisions with data-driven insights
## 4.Key Business Questions
     This project answes the following questions:
     1.Which cost or revenue categories exceeded the budget?
     2.Which categories performed better than excepted?
     3.What is the total budget variance?
     Where should management focus corrective actions?
  
## 5.Dataset Description 
      The dataset contains monthly financial data with the following fields:
       |Column Name||Description|
       |:----------|-----------:|
       |Month| Reporting month|
       |Category| Expense or revenue category|
       |Bugeted_Amount| Planned amount|
       |Actual_Amount| Real amount|
       Examples categories:
       -Marketing
       -Operations
       -Salaries
       -IT
       -Sales Revenue
## 6.Key Metrics & Formulas
## 6.1 Variance
  Variances measures the difference between actual and bugeted values 
  Formula:
  Variance =Actual Amount - Budgeted Amount
## 6.2 Variance Percentage
         Shows the relative size of the variance
  Formula:
   Variance % = (Variance / Budgeted Amount) * 100
## 6.3 Variance Interpretation
    -Positive variance(Revenue)--> Favorable
    -Negative variance(Revenue)-->Unfavorable
    -Positive variance(Cost)----->Unfavorable
    -Negative variance(Cost)----->Favorable
## 7.Tools & Technologies 
-Python
-pandas(data manipulation)
-numpy(calculations)
-matplotlib/ seaborn(visualization)
-Google Collab
-Git &GitHub
## 8.Projects Structure 
                  budget-vs-actual-analysis/
                  │
                  ├── data/
                  │ └── budget_actual_data.csv
                  │
                  ├── notebooks/
                  │ └── budget_vs_actual_analysis.ipynb
                  │
                  ├── src/
                  │ └── variance_analysis.py
                  │
                  ├── README.md
                  └── requirements.txt
## 9.Analysis Workflow 
   1.Load and explore the dataset
   2.Clean and validate financial data
   3.Compute variance and variance percentage
   4.Classify variances(favorable/unfavorable/ on budget)
   5.Visualize key insights
   6.Provide business recommentations
## 10. Insights 
    - January shows Marketing, IT, and Salaries exceeding their budgets, indicating areas of cost overrun.
    - February has Marketing and IT under buget, showing some efficiency gains.
    -  No category shows repeated unfavorable variances accross both month suggestng variability rathe than systemic issues.
    - Marketing has the largest total unfavorable variance and should be the primary focus for budget review.
## 11. Management Recommenations 
     - Prioritize review for Marketing, IT , and Salaries: Marketing has the highest overruns, IT has occasional spikes, and Salaries slightly exceeded the budget.
     - Strengthen budget control processes: Implement monthly checks to catch overruns early.
     - Adjust future budget based on actual trends: Use the insights to refine projections for upcoming months.
     - Visualize performance regularly: Use bar charts and variance dashboards to communicate results to management.
## 13.Conclusion
       Budget vs Actual Analysis provides actionable insights into financial performance.
       This project demonstrates how Python and Business Analytics can combine deliver clear,data-driver recommendations for management decisions.
  
                      
             
