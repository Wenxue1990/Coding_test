# Table of Contents
1. [Problem](README.md#problem)
1. [Input Dataset](README.md#input-dataset)
1. [Instructions](README.md#instructions)
1. [Input vs Output](README.md#output)
1. [Summarize my approach and run instructions](README.md#tips-on-getting-an-interview)
1. [What to improve](README.md#questions?)

# Problem

Imagine you are a data engineer working for an online pharmacy. You are asked to generate a list of all drugs, the total number of UNIQUE individuals who prescribed the medication, and the total drug cost, which must be listed in descending order based on the total drug cost and if there is a tie, drug name in ascending order. 

Disclosure: The projects that Insight Data Engineering Fellows work on during the program are much more complicated and interesting than this coding challenge. This challenge only tests you on the basics. 



### Submitting a link to your repository
* Link to the specific repo for this project is submitted to the submission box provided through the coding challenge email


# Input Dataset

The original dataset was obtained from the Centers for Medicare & Medicaid Services but has been cleaned and simplified to match the scope of the coding challenge. It provides information on prescription drugs prescribed by individual physicians and other health care providers. The dataset identifies prescribers by their ID, last name, and first name.  It also describes the specific prescriptions that were dispensed at their direction, listed by drug name and the cost of the medication. 

# Instructions

The code is created and tested in Jupyter notebook. 
System version: 3.6.1 |Anaconda 4.4.0 (64-bit)| (default, May 11 2017, 13:25:24) [MSC v.1900 64 bit (AMD64)]
All tests passed and proved the final confirmation as: "Process Complete!"
Additional Libraries used: sys, re, datetime
Details of input vs output will be detailed in the following chapter. 



# Input vs Output 

The program aims at creating the output file, for example: `top_cost_drug.txt`, that contains comma (`,`) separated fields in each line.

Each line of this file should contain these fields:
* drug_name: the exact drug name as shown in the input dataset
* num_prescriber: the number of unique prescribers who prescribed the drug. For the purposes of this challenge, a prescriber is considered the same person if two lines share the same prescriber first and last names
* total_cost: total cost of the drug across all prescribers

Test case 1: 

My input data, **`itcont.txt`**, is
```
id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost
1000000001,Smith,James,AMBIEN,100
1000000002,Garcia,Maria,AMBIEN,200
1000000003,Johnson,James,CHLORPROMAZINE,1000
1000000004,Rodriguez,Maria,CHLORPROMAZINE,2000
1000000005,Smith,David,BENZTROPINE MESYLATE,1500
```

My output file, **`top_cost_drug.txt`**, would contain the following lines
```
drug_name,num_prescriber,total_cost
CHLORPROMAZINE,2,3000
BENZTROPINE MESYLATE,1,1500
AMBIEN,2,300
```

Test case 2, self created case so that the input data are not clean and contains erros such as missing prescriber name, negative cost value, wrong data format, etc, that could be contained in the real word:

My input data, **`itcont.txt1`**, is
```
id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost
1000000001,Smith,James,AMBIEN,-100
1000000002,Garcia,Maria,AMBIEN,200
1000000003,Johnson,James,CHLORPROMAZINE,1000
1000000004,Rodriguez,Maria,CHLORPROMAZINE,2000
1000000005,Smith,David,BENZTROPINE MESYLATE,1500
1000000006,Garcia,,AMBIEN,200
1000000007,Johnson,James,CHLORPROMAZINE,$1000
1000000008,Rodriguez,,CHLORPROMAZINE,
1000000009,Smith,David,BENZTROPINE MESYLATE,...
```

My output file, **`top_cost_drug_1.txt`**, would contain the following lines
```
drug_name,num_prescriber,total_cost
CHLORPROMAZINE,2,3000
BENZTROPINE MESYLATE,1,1500
AMBIEN,2,400
```


System output by running jupyter notebook:
```
This following line is skipped (not splited correctly/invalid cost value): ['1000000001', 'Smith', 'James', 'AMBIEN', '-100']
This following line is skipped (not splited correctly/invalid cost value): ['1000000007', 'Johnson', 'James', 'CHLORPROMAZINE', '$1000']
This following line is skipped (not splited correctly/invalid cost value): ['1000000008', 'Rodriguez', 'NA', 'CHLORPROMAZINE', '']
This following line is skipped (not splited correctly/invalid cost value): ['1000000009', 'Smith', 'David', 'BENZTROPINE MESYLATE', '...']
9 total lines of data processed
['CHLORPROMAZINE,2,3000\n', 'BENZTROPINE MESYLATE,1,1500\n', 'AMBIEN,2,400\n']
Process Complete!
Time taken: 0:00:00.005361
```

Test case 3, using a large data set provided by the the link below and use datetime library to evaluate processing time of the program:

My input data is downloaded from the provided link <a href="https://drive.google.com/file/d/1fxtTLR_Z5fTO-Y91BnKOQd6J0VC9gPO3/view?usp=sharing">Here</a>:

The output data is written on file top_cost_drug1.txt

System output by running jupyter notebook:

```
2 M lines processed
4 M lines processed
6 M lines processed
8 M lines processed
10 M lines processed
12 M lines processed
14 M lines processed
16 M lines processed
18 M lines processed
20 M lines processed
22 M lines processed
24 M lines processed
24525859 total lines of data processed
Process Complete!
Time taken: 0:03:54.917637
```


First two testing files are provided in the `Coding_test/tests/test_1/input` and `Coding_test/tests/test_1/output` folders, respectively.




# summarize your approach and run instructions

The approach is as follows:
0)main(inputfile, outputfile), requires inputfile and outputfile as input. 
1)Construct two libraries: 1)dict_cost: {drug : cost} 2) dict_prescriber: {drug: subscriber list}
2)open inputfile 
3)process data line by line 
4)Using dict_newdata(line, dict_cost, dict_prescriber ) to update and process dicttionaries: dict_cost and dict_prescriber, so that drug_cost could be added up for same drug name and prescribers are unique and calculated. 
For large dataset, each million lines processed will be printed out
5)Construct correct structure for lines to be written in the ouput file
6)If main program processed successfully, calculate total processing time and print "Process Complete!"

## My Repo directory structure

The directory structure for your repo should look like this:

    ├── README.md 
    ├── run.sh
    ├── src
    │   └── WZ_pharmacy-counting.py
    ├── input
    │   └── itcont1.txt
    ├── output
    |   └── top_cost_drug_1.txt
    ├── insight_testsuite
        └── run_tests.sh
        └── tests
            └── test_1
                ├── input
                │   └── itcont.txt
                |__ output
                    └── top_cost_drug.txt
         

**Don't fork this repo** and don't use this `README` instead of your own. The content of `src` does not need to be a single file called `pharmacy-counting.py`, which is only an example. Instead, you should include your own source files and give them expressive names.

## Testing result of my directory structure and output format

My submission has passed the provided test in order to pass the coding challenge.

I also tested my repository through the following link: <a href="http://ec2-18-210-131-67.compute-1.amazonaws.com/test-my-repo-link">website</a> by simulating the environment end test out that all tests are passed. 


# What to improve
If different types of error data examples are provided/summed up, I could dig more into the error data handling process using libraries such as:NumPy, Pandas, etc

