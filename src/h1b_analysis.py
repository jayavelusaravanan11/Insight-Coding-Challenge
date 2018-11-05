import csv
import os
import sys
# Define function getabsfilename which converts relative filename to absolutefile. This is used to get absolute filenames of inputfile and outputfilenames
def getabsfilename(relfilename):
	absfilename=os.path.realpath(relfilename)
	return(absfilename)

#Define function get_unique_values which takes a list as argument. This function provides the list of unique SOC_NAMES and EMPLOYER_STATES depending on the list
def get_unique_values(valuelist):
	valuelist_l=list(set(valuelist))
	return(valuelist_l)

#Define function validate_and_accept_arguments  which processes and returns six command line  arguments apart from the program name 
#The arguments (apart from program name ) are inputfile , "column name in inputfile for case status" , "column name in inputfile for soc_name" , "column name in inputfile for employer state" , "output file name for top 10 occupations" , "output file name for top 10 states"
#The function returns the three columnnames passed as command line arguments in upper case.
def validate_and_accept_arguments():
	if len (sys.argv) != 7 :
    		print("Usage: python h1b_analaysis.py h1binputfile case_status_col_name socname_colname employer_state_colname h1b_top10occupations_outputfile h1b_top10states_outputfile")
    		sys.exit (1)
	counter = 0
	for value in sys.argv:
		if counter==1:
			relpathinputfilename = value
			abspathinputfilename=getabsfilename(relpathinputfilename)
		if counter==2:
			casestatus_colname = value
		if counter==3:
			socname_colname = value
		if counter==4:
			employerstate_colname = value
		if counter==5:
			relpathoutoccupationsfilename = value
			abspathoutoccupationsfilename = getabsfilename(relpathoutoccupationsfilename)
		if counter==6:
			relpathoutstatesfilename = value
			abspathoutstatesfilename = getabsfilename(relpathoutstatesfilename)
		counter = counter + 1

	return(abspathinputfilename,casestatus_colname.upper(),socname_colname.upper(),employerstate_colname.upper(),abspathoutoccupationsfilename,abspathoutstatesfilename)

#Define function input_file_sanity_check which takes file as input and sanity checks if the file exists with proper permissions . if not it exits with a proper message 
def input_file_sanity_check(inputfile):
	try:
    		with open(inputfile) as file:
       			return() 
	except IOError as e:
    		print("input file does not exist or does not have requisite permissions")
    		exit(2)

#Define function parse_header_for_index_values  takes inpufile and colname as argument and finds the column position 
def parse_header_for_index_values(inputfile,colstring):
	f = open(inputfile,'r')
	reader = csv.reader(f,delimiter=';')
	headers = next(reader, None)
	counter=0
	for colname in headers:
		if colname == colstring:
			return(counter)
		counter=counter+1

#Define function writefile which takes outputfiles , headers and datalist to be written as argument and writes to the outputfiles 
def writefile(filename,headerlist,datalist):
	with open(filename,'w') as writefile1:
                writer = csv.writer(writefile1,delimiter=';')
                writer.writerow(headerlist)
                for w1 in datalist:
                        writer.writerow(w1)
	
	
def main():
	#Define various lists 
	cert_occupations=[]
	cert_states=[]
	freq_list_occupations=[]
	freq_list_states=[]
	perc_list_occupations=[]
	perc_list_states=[]
	#Call function validate_and_accept_arguments and get the six command line arguments
	abspathinputfilename,casestatus_colname,socname_colname,employerstate_colname,abspathoutoccupationsfilename,abspathoutstatesfilename=validate_and_accept_arguments()
	#Call function input_file_sanity_check and check for the existence of inputfile
	input_file_sanity_check(abspathinputfilename)
	#Call function parse_header_for_index_values and get the column positions for casestatus , socname and employerstate
	index_soc_name=parse_header_for_index_values(abspathinputfilename,socname_colname)
	index_state_name=parse_header_for_index_values(abspathinputfilename,employerstate_colname)
	index_case_status=parse_header_for_index_values(abspathinputfilename,casestatus_colname)
	#Input file processing starts . Open file and read through a loop
	with open(abspathinputfilename,'r') as readfile:
		reader = csv.reader(readfile,delimiter=';')
		for row in reader:
			if row[index_case_status]=='CERTIFIED':
				#Insert soc_name and employer_state into the appropriate list
 				cert_occupations.append(row[index_soc_name])
 				cert_states.append(row[index_state_name])
		#Call function get_unique_values to get the list of unique certified occupations
		cert_occupations_l=get_unique_values(cert_occupations)
		#count(*) unique certified occupations and insert into list
		for x in cert_occupations_l:
     			freq_list_occupations.append(cert_occupations.count(x))
		#Calculate the percentage of each certified occupation
		certified_sum_occupations=sum(freq_list_occupations)
		for y in freq_list_occupations:
			per_value=(y/certified_sum_occupations)*100
			per_value_round=round(per_value,1)
			perc_list_occupations.append(per_value_round)
		#Join three lists , sort them in reverse order and get the top 10 values for occupations
		pair_occupations=[list(a) for a in zip(cert_occupations_l,freq_list_occupations,perc_list_occupations)]
		list_top_10_occupations=sorted(pair_occupations,key=lambda pair_occupations: pair_occupations[1], reverse=True)[:9]
		#Call function get_unique_values to get the list of unique states with certifications
		cert_states_l=get_unique_values(cert_states)
		#count(*) unique certified states and insert into list
		for x in cert_states_l:
     			freq_list_states.append(cert_states.count(x))
		#Calculate the percentage of each certified state
		certified_sum_states=sum(freq_list_states)
		for y in freq_list_states:
			per_value=(y/certified_sum_states)*100
			per_value_round=round(per_value,1)
			perc_list_states.append(per_value_round)
		#Join three lists , sort them in reverse order and get the top 10 values for states
		pair_states=[list(a) for a in zip(cert_states_l,freq_list_states,perc_list_states)]
		list_top_10_states=sorted(pair_states,key=lambda pair_states: pair_states[1], reverse=True)[:9]
	#Populate header lists and call function writefile to complete writing results to the top10_occupations and top10_states files
	header_occupations = ['TOP_OCCUPATIONS', 'NUMBER_CERTIFIED_APPLICATIONS', 'PERCENTAGE']
	header_states = ['TOP_STATES', 'NUMBER_CERTIFIED_APPLICATIONS' , 'PERCENTAGE']
	writefile(abspathoutoccupationsfilename,header_occupations,list_top_10_occupations)
	writefile(abspathoutstatesfilename,header_states,list_top_10_states)
if __name__== "__main__":
	main()
