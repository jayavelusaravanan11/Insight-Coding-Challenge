# Insight-Coding-Challenge
This repository has the python code to solve the insight coding challenge 

Table of Contents
Problem
Input Dataset
Instructions
Output
Tips on getting an interview
Instructions to submit your solution
FAQ
Questions?
Problem
A newspaper editor was researching immigration data trends on H1B(H-1B, H-1B1, E-3) visa application processing over the past years, trying to identify the occupations and states with the most number of approved H1B visas. She has found statistics available from the US Department of Labor and its Office of Foreign Labor Certification Performance Data. But while there are ready-made reports for 2018 and 2017, the site doesn’t have them for past years.

As a data engineer, you are asked to create a mechanism to analyze past years data, specificially calculate two metrics: Top 10 Occupations and Top 10 States for certified visa applications.

Your code should be modular and reusable for future. If the newspaper gets data for the year 2019 (with the assumption that the necessary data to calculate the metrics are available) and puts it in the input directory, running the run.sh script should produce the results in the output folder without needing to change the code.

Input Dataset
Raw data could be found here under the Disclosure Data tab (i.e., files listed in the Disclosure File column with ".xlsx" extension). For your convenience we converted the Excel files into a semicolon separated (";") format and placed them into this Google drive folder. However, do not feel limited to test your code on only the files we've provided on the Google drive

Note: Each year of data can have different columns. Check File Structure docs before development.

Instructions

  The code is written in a modular and reusable manner with lot of comments .  The python program accepts seven arguments :
  
  1. The name of the program
  2. Relative pathname of input file
  3. Colname of Status_certified
  4. Colname of SOC_NAME
  5. Colname of Employer_statename
  6.  Outputfile for top 10 occupations
  7. Outputfile for top 10 states 
  
  Here's the logic
  
  1. Open and loop through the inputfile 
  2.  Filter out  the rows where CASE_STATUS is not CERTIFIED
  3. For two rows which are certified , build two lists viz distinct SOC_NAME's and distict EMPLOYER_STATE
  4.  Get a count of all disticnt SOC_NAME and employer_state based on CERTIFIED Filter data .
  5. Get the percentages of the distinct SOC_NAME
  6.  Write to two files top_10_occupations and top_10_states 
