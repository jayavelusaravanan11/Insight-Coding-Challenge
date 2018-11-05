# Insight-Coding-Challenge

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
