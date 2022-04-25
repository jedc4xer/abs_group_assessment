# abs_group_assessment
This repository contains files related to the Group Assesment for Dev10 Module 8. An API was used to access data from the US Census 2019 Annual Business Survey and visualizations were generated to answer questions about that data.

Repository Structure:
    
    data:
        This folder only holds a state codes dataset that was used for mapping.
        
    utils:
        This folder holds a helper python file that was assistive in the analysis process. 
        It's primary function was to display information about variables in the analysis.
    
    backup_data_exploration.ipynb:
        This file is aptly named. We had a lot of issues with branches crashing, and wanted to
        preserve at least a portion of our progress.
        
    data_exploration.ipynb:
        This file is the primary ETL Documentation and Analysis Notebook. It contains the ETL documentation
        and all of the code to analyze and generate visuals for each of the group members.
        
    m08_final_report.pdf:
        This file is the project report that summarizes the findings of our data exploration.
    
Dataset Variables (Sample Table):

    |Name|Common_Vars|Tech Labels|Owner Labels|Characteristic Labels|Company Summary Labels
    |BUSCHAR|BUSCHAR|-|-|Business characteristic code|-
    |CBSA|CBSA|-|Geography|Geography|Geography
    |EMP|EMP|Number of employees|-|Number of employees|Number of employees
    |EMPSZFI|EMPSZFI|-|-|Employment size of firms code|Employment size of firms code
    |EMP_PCT|EMP_PCT|Percent of employees (%)|-|Percent of employees (%)|-|
    |ETH_GROUP|ETH_GROUP|Ethnicity code|-|Ethnicity code||Ethnicity code
    |FACTORS_P|FACTORS_P|Factors adversely affecting technology product...|-|-|-|
    |FACTORS_U|FACTORS_U|Factors adversely affecting technology use code|-|-|-
    |FIRMPDEMP|FIRMPDEMP|Number of employer firms|-|Number of employer firms|Number of employer firms
    |FIRMPDEMP_PCT|FIRMPDEMP_PCT|Percent of employer firms (%)|-|Percent of employer firms (%)|-
    |GEOCOMP|GEOCOMP|GEO_ID Component|GEO_ID Component|GEO_ID Component|GEO_ID Component
    |GEO_ID|GEO_ID|Geographic identifier code||Geographic identifier code|Geographic identifier code|Geographic identifier code

Team Members:

    Jake Thompson
    Ryan Lippe
    Marjea Mckoy
    Jed Dryer
