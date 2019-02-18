
import sys
import re
from datetime import datetime

startTime = datetime.now()  

# main function: process inputfile and write on outputfile with format:drug_name,num_prescriber,total_cost

def main(inputfile, outputfile):
    
    # dict_cost is a dictionay: {drug : cost}
    dict_cost={}
    
    # dict_prescriber is a dictionay: {drug: subscriber list}
    dict_prescriber={}
    
    # start to process inputfile
    try:
        f = open(inputfile) 
    except:
        print ('Input file can not be opened!')
        return 0

    line = f.readline() # skip header line in input dataset
    line = f.readline()
    
    count=0
    # update drug_name dictionary line by line
    while line:       
        dict_cost,dict_prescriber=dict_newdata(line, dict_cost, dict_prescriber)
        line = f.readline()   
        count+=1
        # print whenver 2 million data is processed
        if (count%2000000)==0:
            print (int(count/1000000),'M lines processed')
    
    #print ('dict_cost',dict_cost)
    #print ('dict_prescriber', dict_prescriber)
    
    print (count, 'total lines of data processed')
    
    f.close()
    
    # calcualte the number of unique prescribers and sort results in descending order
    
    lines=[]
    for key, value in sorted(dict_cost.items(), key=lambda x: (x[1], x[0]),reverse=True):
        if key=='NA':
            drug_name='Unknown'
        else:
            drug_name=key  
            
        # all input and output value are integers regarding input and output sample  
        
        line=drug_name+','+str(len(set(dict_prescriber[key])))+','+ str(int(value))+'\n'
        
        #print ("line", line)
        
        lines.append(line)
    
    #print(lines)
    # write results to desired folder
    try:
        f = open(outputfile, "w")
    except:
        print ('Output file can not be opened!')
        return 0
        
    f.writelines('drug_name,num_prescriber,total_cost\n')
    f.writelines(lines)
    f.close()
   
    return 1

# check_num to check if splited drug_cost value is numerical value
def check_num (value):
    try:
        value=int(value)  # if smaple is float, could modify this as value = float(value)
        return (True,value)
    except ValueError:
        return (False,-1)

# Construct new data line by line 
# using re.sub to refill space with "NA"
def dict_newdata (line, dict_cost, dict_prescriber):
    
    line=line.strip()
    
    # fill missing data space with NA, except for drug_cost
    
    line = re.sub(',,', ',NA,', line) 
                  
    # fill missing data space with NA
    
    current_line=line.split(',')
    
    # check if line is splited correctly, otherwise use Regular expression to split line 
    if len(current_line)!=5:
        current_line=re.findall(r'(?:[^,"]|"(?:\\.|[^"])*")+', line)
        
    #current_line structure: 1000000001,Smith,James,AMBIEN,100
    line=current_line
       
    cost_flag,drug_cost=check_num(line[4])
    
    # check if splited drug_cost value is numerical value and is positive
    # double check line is splited correctly
    # otherwise skip this function
    
    if cost_flag&(len(line)==5)&(drug_cost>0):
        
        # if drug_name isn't in dictonary key(dict_cost) list, create one
        
        if line[3] in dict_cost.keys():
            dict_cost[line[3]]=dict_cost[line[3]]+drug_cost
            dict_prescriber[line[3]].append((line[1]+' '+line[2]))
        else:
            dict_cost[line[3]]=drug_cost
            dict_prescriber[line[3]]=[((line[1]+' '+line[2]))]  
    else:        
        print ('This line is not splited correctly/invalid cost value and is skipped:',line)
    
    return (dict_cost,dict_prescriber)


#inputfile = 'de_cc_data.txt'

#inputfile = 'itcont1.txt'
#outputfile = 'top_cost_drug1.txt'

inputfile=sys.argv[1] 
outputfile=sys.argv[2]


return_value = main(inputfile,outputfile)

if return_value==1:
    print ('Process Complete!')
    print("Time taken:", datetime.now() - startTime)
else:
    print ('Error!')
