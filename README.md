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
  2.  Only accept the rows where status is Certified
  3. For those rows which are certified , build two lists viz distinct SOC_NAME's and distict EMPLOYER_STATE
  4.  Get a count of all distinct SOC_NAME and employer_state .
  5. Get the percentages of the distinct SOC_NAME and distinct employer_states
  6.  Append three lists into one list for SOC_NAME ( SOC_NAME , COUNT , Percentage) 
  7.  Write to file top_10_occupations 
  8. Append three lists into one list for Employer_state ( Employer_state, COUNT , Percentage) 
  9.  Write to file top_10_states 
