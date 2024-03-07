**CS_UK_Immigration**  

Author: Patrick Smith  
Date: 03/03/24  
Contact: patrick.b.smith@gmail.com

**Project Overview**
-----------------------
**Problem Area**  
o	Area of Interest: Immigration and asylum seekers in western europe or north america, over a 10+ year period  
o	Is there a way to use historical data to predict the possibility of someone applying for citizenship/refugee/asylum status?  
o	Challenges: Understanding trends, patterns, and factors influencing immigration and asylum-seeking behaviors over time. Addressing issues   related to integration, policy effectiveness, and societal impact.  

**Those Affected**  
o	Individuals who want to immigrate to select countries. Maybe they have a few to choose from and it is difficult to figure out which would have the best odds. With the model’s help that can know whether it is worth the effort. This could also include organizations, policymakers, and researchers interested in understanding immigration dynamics, policy evaluation, and societal integration  
o	Benefits: Could provide assistance to people that are unsure on making one of their most important life decisions, by taking everything and moving to another country. Also improved decision-making and better policy formulation   
o	Societal value: Enhanced understanding of immigration dynamics can lead to more informed policy decisions, improved integration efforts, and better societal outcomes.  
o	Quantification: Potential impacts can include economic benefits from optimized immigration policies and improved cultural diversity. 

**Summary**

We have combined x excel sheets from the UK gov' for more than 1M rows. We began with ~350K with one spreadsheet.

**Flowchart**

1. Data Collection
  - Obtained 15 seperate xls files from an offical UK government website(1)
  - These original filenames are:
    - 1) asylum-appeals-lodged-datasets-mar-2023(1)  
    - 2) asylum-applications-awaiting-decision-datasets-sep-2023  
    - 3) asylum-applications-datasets-sep-2023(1)  
    - 4) asylum-seekers-receipt-support-datasets-sep-2023  
    - 5) citizenship-datasets-sep-2023  
    - 6) detention-datasets-sep-2023  
    **- 7) entry-clearance-visa-outcomes-datasets-sep-2023**  
    - 8) extensions-datasets-sep-2023  
    - 9) migration-study-sponsorship-datasets-sep-2023  
    - 10) migration-work-sponsorship-datasets-sep-2023  
    - 11) occupation-visas-datasets-sep-2023  
    - 12) outcome-analysis-asylum-applications-datasets-jun-2022  
    **13) returns-datasets-sep-2023**  
    - 14) settlement-datasets-sep-2023  
        
  - Some of the files have similar columns. Others have different date ranges. For example, some go back to 2001, moving to 2023. Others are 2010-2023, 2014-2023, or shortest at 2021-2023. These have been filtered to 'Annual' and 'Quarterly' directories (Q1, Q2, Q3, and Q4), and filtered again in those yearly ranges noted above.  
  
  - Most relevant xls files were linked together. These are mapped out below:  
    - entries-clean(7) <-> returns-clean(13) <->

    returns #1 -> entries #2 -> asylum #3-> grants #4 ->  
    
asylum_applications #5 -> applications_jobs #6  

From oldest read data to new 1-2-3-4-5-6, data is pasted on top, so it is 6-5-4-3-2-1 unfiltered.



  - The remaining were dropped.

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
