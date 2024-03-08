**CS_UK_Immigration**  

Author: Patrick Smith  
Date: 03/03/24  
Contact: patrick.b.smith@gmail.com

**Project Overview**
-----------------------
**Problem Area**  
- Area of Interest: Immigration and asylum seekers in western europe or north america, over a 10+ year period  
- Is there a way to use historical data to predict the possibility of someone applying for citizenship/refugee/asylum status?  

**Those Affected**  
- Individuals who want to immigrate to select countries. Maybe they have a few to choose from and it is difficult to figure out which would have the best odds. With the model’s help that can know whether it is worth the effort. This could also include organizations, policymakers, and researchers interested in understanding immigration dynamics, policy evaluation, and societal integration  

**Potential Impact**
- Could provide a useful free to for assistance to people that are unsure on making one of their most important life decisions, by taking everything and moving to another country. 
- Improved decision-making and better policy formulation, including transparency, for evidence-based immigration policies or disclosure. 
- Societal value: Enhanced understanding of immigration dynamics can lead to more informed policy decisions, improved integration efforts, and better societal outcomes.  

**Summary**

We have combined 6 excel sheets from the UK gov' for more than 1M rows. We began with ~350K with one spreadsheet.

**Flowchart**

1. Data Collection
  - Obtained 15 seperate xls files from an offical UK government website(1)
  - These original filenames are:
    - 1) asylum-appeals-lodged-datasets-mar-2023(1)**  
    - 2) asylum-applications-awaiting-decision-datasets-sep-2023  
    - 3) asylum-applications-datasets-sep-2023(1)  
    - 4) asylum-seekers-receipt-support-datasets-sep-2023  
    - 5) citizenship-datasets-sep-2023  
    - 6) detention-datasets-sep-2023  
    - 7) entry-clearance-visa-outcomes-datasets-sep-2023  
    - 8) extensions-datasets-sep-2023  
    - 9) migration-study-sponsorship-datasets-sep-2023  
    - 10) migration-work-sponsorship-datasets-sep-2023  
    - 11) occupation-visas-datasets-sep-2023  
    - 12) outcome-analysis-asylum-applications-datasets-jun-2022  
    - 13) returns-datasets-sep-2023  
    - 14) settlement-datasets-sep-2023  
        
  - Some of the files have similar columns. Others have different date ranges. For example, some go back to 2001, moving to 2023. Others are 2010-2023, 2014-2023, or shortest at 2021-2023. These have been filtered to 'Annual' and 'Quarterly' directories (Q1, Q2, Q3, and Q4), and filtered again in those yearly ranges noted above.  
  
  - Most relevant 7 xls files were linked together. These are mapped out below:  
    - #1 returns-clean(13) <-> #2 entries-clean(7) <-> #3 asylum(12) <-> #4 grants(5) <-> #5 asylum_applications(3) <-> #6 applications_jobs(11) <-> #7 grants_jobs(12)
    
    - From oldest read data to new 1-2-3-4-5-6, data is pasted on top, so it is 6-5-4-3-2-1 unfiltered.

  - The remaining were not used but saved for possible addition later
  - Note that the UK Gov regularly puts out new data, so it should be easy to rewrite the raw excel files and rerun the data to use new datapoints for later in 2023 and 2024

**Proposed Data Science Solution**

- The analysis is to predict trends in UK immigration using data science methods. Here are the most important components of the project:

- Data exploration: Cleaning and finding the most important variables.

Descriptive Analysis: Conducting basic statistical analysis to look at trends related to case outcome. Secondary importance on countries as well.

Are there any seasonal patterns or long-term trends?

Does visa type, application type, or socio-economic, or demographic factors have a meaningful impact on immigration to the UK?

Eventually, we want to build a predictive model to forecast future immigration patterns. This would be based on historical data.

**Dataset Description**

The dataset consists of the following fields:

Year: Year of observation.  
Quarter: Quarter of observation (Q1=1,Q2=2,Q3=3,Q4=4).  
Nationality: Nationality of individual.  
Region: Region of observation.  
Return type group: Type of return.  
Age: Age of individual. Outputted in ranges ie: 18+.  
Return destination group: Destination of return.  
Number of returns: Count of returns.  
Visa type group: Type of visa that the individual is applying to.  
Applicant type: Type of applicant.  
Case outcome: Outcome of case. This is the dependent variable. Issued/Rejected/Withdrawl/Resettlement.   
Decisions: Number of decisions made.  
Case type: Type of case    
Case outcome group: Group of case outcome.  
Host Country: Country of host. Similar to Nationality.  
Application type group: Type of application grouped.    
Application type: Type of application.  
Grants: Number of grants.  
Applications: Number of applications.  
Occupation: Occupation of individual.  
Industry: Industry of individual.  
Sex_Male: Male dummy set to 1-0.  
Sex_Female: Female dummy set to 1-0.  
Sex_Other: Other or NAs dummy set to 1-0.  

**Flowchart**

    Data Collection & Merge:
        Find and download all spreadsheets of interest
        Filter to choose which ones make most sense and have optimal infomation, but not too large a file
        Perform minor cleaning

    Exploratory Data Analysis:
        Further cleaning
        Analyze variables distribution
        Visualize patterns via plotting
        Establish best dependent variable
        Figure out initial questions prior to modelling

    Baseline Modeling:
        tbd 

    Advanced Modeling (Sprint 3):
        x
        y
        z


**Repository Navigation Instructions**

Folders


**Notebook Usage Instructions**
Execution Order

Part 1:
Part 2:
Part 3:
Part 4:

**Acknowledgements and Sources**

Dataset link:  

o	UK Home Office Immigration Statistics: Provides detailed statistics on various aspects of immigration, including nationality, visa type, asylum applications, and outcomes.  
  o	https://www.gov.uk/government/statistical-data-sets/immigration-system-statistics-data-tables
