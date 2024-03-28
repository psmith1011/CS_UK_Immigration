# UK Immigration 

## A Deep Analysis of Asylum Seekers for the years of 2001 to 2023*

Author: Patrick Smith  
Date: 27/03/24  
Contact: patrick.b.smith@gmail.com

-----------------------


           o x o x o x o . . .
         o      _____            _______________ ___=====__T___
       .][__n_n_|DD[  ====_____  |    |.\/.|   | |   |_|     |_
      >(________|__|_[_________]_|____|_/\_|___|_|___________|_|
      _/oo OOOOO oo`  ooo   ooo   o^o       o^o   o^o     o^o
-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-

-----------------------

### Population of the United Kingdom 1971-2021

|                | 1971  | 1981  | 1991  | 2001  | 2011  | 2021  |
|----------------|-------|-------|-------|-------|-------|-------|
| All People     | 52.6M | 53.6M | 54.9M | 57.1M | 63.3M | -M |
| Born Abroad    | 3.2M  | 3.4M  | 3.8M  | 4.9M  | 8.0M  | -M |
| % T            | 4.6%  |  6.2%  | 6.7%  | 8.3% | 12.7%  | % |
| % Δ Decade     | 24.0%  | 7.5%  | 11.8%  | 27.7% | 63.0% | - |

### Forward

Like many G7 nations like Canada, the cost of immigration, both illegal, and legal, is rising. The United Kingdom, the focus of this study, is having a historic rise in the cost of its asylum system, mainly due to "under enormous and unsustainable pressure due to the challenges of the pandemic and significant increase in small boat crossings."

Here is a press release from the UK Home Office, aka Home Department, (department of the British Government), which is responsible for immigration, security, and law and order.


    Home Office news team, 14 April 2022
    
    Home Office statistics released in February 2022 showed that 28,526 migrants crossed the Channel in 2021- up from 299 in 2018. Almost all claim asylum.

    The United Kingdom has legal obligations under ECHR and the 1999 Immigration and Asylum Act to provide asylum seekers who would otherwise be destitute, with accommodation and other support whilst their claim for asylum is being considered.

    The current asylum system is costing the taxpayer £1.5 billion a year [annual budget of £10.8 billion], the highest amount in over two decades.

    And the severe pressure on the system means claims from those in genuine need of protection are taking too long to process and is taking away from resources to support people through safe and legal routes to the UK.

    Before the pandemic and the rise in small boat crossings, destitute asylum seekers would be provided with accommodation sourced from the rental housing sector.

    The sharp increase in crossings and the pandemic has led to approximately 37,000 destitute migrants and those on resettlement schemes being accommodated in hotels, costing the taxpayer £4.7 million every day.

    The pandemic significantly impacted the government’s ability to remove people with no right to be in the UK.

    As we work to reform the broken and outdated system, we must ensure we have sufficient capacity to meet our statutory duty to provide accommodation to those in need of our support.
    It is only controlled immigration through safe and legal routes that allows us to make generous offers of sanctuary, while managing pressures on public services, with the proper support people need to rebuild their lives, integrate and thrive.
    The New Plan for Immigration will reform the asylum system, enabling the government to support those in genuine need while preventing abuse of the system and deterring illegal entry to the UK.

-----------------------
## Project Overview
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

------

              |    |    |                 
             )_)  )_)  )_)              
            )___))___))___)\            
           )____)____)_____)\\
         _____|____|____|____\\\__

-----

## Summary

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

  ------

## Proposed Data Science Solution



- The analysis is to predict trends in UK immigration using data science methods. Here are the most important components of the project:

- Data exploration: Cleaning and finding the most important variables.

Descriptive Analysis: Conducting basic statistical analysis to look at trends related to case outcome. Secondary importance on countries as well.

Are there any seasonal patterns or long-term trends?

Does visa type, application type, or socio-economic, or demographic factors have a meaningful impact on immigration to the UK?

Eventually, we want to build a predictive model to forecast future immigration patterns. This would be based on historical data.

## Dataset Description

The dataset consists of the following fields:


| Column                         | Descriptor                                                                 | Datatype |
|--------------------------------|----------------------------------------------------------------------------|----------|
| Year                           | The period in which the event occurred.                                    | int32    |
| Quarter                        | Quarter of the year (Q1=1, Q2=2, Q3=3, Q4=4).                              | object   |
| Nationality                    | Nationality of the individual.                                             | object   |
| Region                         | World region of the country of nationality for the individual.              | object   |
| Return type group              | Grouped type of return (enforced, voluntary, refused entry at port).         | object   |
| Return type                    | Specific type of return (enforced, voluntary, refused entry).               | object   |
| Age                            | Age of the individual at the time of the event.                             | object   |
| Sex                            | Gender of the individual (male, female, other/unknown).                     | int32    |
| Return destination group       | Grouped destination country for return (Home country, EU, Other country).   | object   |
| Return destination             | Specific destination country for return.                                    | object   |
| Number of returns              | Count of returns.                                                           | float64  |
| Visa type group                | Grouped type of sponsored work visa applied for.                            | object   |
| Visa type subgroup             | Detailed type of sponsored work visa applied for.                           | object   |
| Applicant type                 | Type of applicant (main applicant, dependant).                             | object   |
| Case outcome                   | Outcome of the case (granted, refused, withdrawn, resettlement).             | object   |
| Decisions                      | Number of decisions made.                                                   | float64  |
| Case type                      | Type of case (asylum, resettlement).                                       | object   |
| Case outcome group             | Grouped outcome of the case (granted protection, grant of other leave, refused, withdrawn). | object   |
| UASC                           | Indicates if the applicant is an Unaccompanied Asylum-Seeking Child.       | object   |
| Host Country                   | Country where the individual first sought asylum for resettlement cases.    | object   |
| Location of application        | Location where the application was submitted.                               | object   |
| Applications                   | Number of applications made.                                               | float64  |
| Occupation                     | Occupation of the individual.                                              | object   |
| Industry                       | Industry sector for which the application to work was made.                 | object   |
| SOC code                       | Standard Occupational Classification code.                                 | object   |
| Occ. major group               | Major group classification of the occupation.                              | object   |
| Occ. sub-major group           | Sub-major group classification of the occupation.                          | object   |
| Occ. minor group               | Minor group classification of the occupation.                              | object   |
| Occ. unit group                | Unit group classification of the occupation.                               | object   |
| Category of leave group        | Grouped category of extension applied for (work, study, family, other).     | object   |
| Category of leave              | Category of extension applied for.                                         | object   |
| Category of leave subgroup     | Detailed category of extension applied for.                                | object   |
| Current category of leave group| Grouped current category of leave (work, study, family, other).            | object   |
| Current category of leave      | Current category of leave.                                                 | object   |
| Previous category of leave group | Grouped previous category of leave (work, study, family, other).         | object   |
| Previous category of leave     | Previous category of leave.                                                | object   |
| Sex_Male                       | Dummy variable for male (1 if male, 0 otherwise).                          | object   |
| Sex_Female                     | Dummy variable for female (1 if female, 0 otherwise).                      | object   |
| Sex_Other                      | Dummy variable for other or NA (1 if other/unknown, 0 otherwise).          | object   |
| Local authority                | The local authority in which a citizenship ceremony took place.            | object   |
| UK Region                      | The UK region in which the citizenship ceremony took place.                | object   |
| Ceremonies attended            | The number of citizenship ceremonies attended in each local authority.     | float64  |

------
## Flowchart

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

------
## Acknowledgements and Sources

Dataset link:  

o	UK Home Office Immigration Statistics: Provides detailed statistics on various aspects of immigration, including nationality, visa type, asylum applications, and outcomes.  
  o	https://www.gov.uk/government/statistical-data-sets/immigration-system-statistics-data-tables
