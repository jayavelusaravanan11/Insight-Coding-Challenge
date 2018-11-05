#The python program written by me accepts five arguments 
#1. The name of the program viz h1b_analysis.py
#2. The name of the input file 
#3. The column name of case_status as column names change between inputfiles . Note the awkward case . The program converts to uppsercase
#4. The column name of soc_name as column names change between inputfiles . Note the awkward case . The program converts to uppsercase
#5. The column name of employer_statel as column names change between inputfiles . Note the awkward case . The program converts to uppsercase
#6 Two outputfiles provided as individual arguments
python3 ./src/h1b_analysis.py ./input/H1B_FY_2015-split1.csv case_statuS soc_NamE EMPLOyER_state ./output/top_10_occupations.txt ./output/top_10_states.txt
