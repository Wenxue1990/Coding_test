# Table of Contents
1. [Problem](README.md#problem)
1. [Input Dataset](README.md#input-dataset)
1. [Instructions](README.md#instructions)
1. [Output](README.md#output)
1. [Tips on getting an interview](README.md#tips-on-getting-an-interview)
1. [Questions?](README.md#questions?)

# Problem

Imagine you are a data engineer working for an online pharmacy. You are asked to generate a list of all drugs, the total number of UNIQUE individuals who prescribed the medication, and the total drug cost, which must be listed in descending order based on the total drug cost and if there is a tie, drug name in ascending order. 

Disclosure: The projects that Insight Data Engineering Fellows work on during the program are much more complicated and interesting than this coding challenge. This challenge only tests you on the basics. 



### Submitting a link to your repository
* Link to the specific repo for this project is submitted to the submission box provided through the coding challenge email


# Input Dataset

The original dataset was obtained from the Centers for Medicare & Medicaid Services but has been cleaned and simplified to match the scope of the coding challenge. It provides information on prescription drugs prescribed by individual physicians and other health care providers. The dataset identifies prescribers by their ID, last name, and first name.  It also describes the specific prescriptions that were dispensed at their direction, listed by drug name and the cost of the medication. 

# Instructions

The code is writen and tested in jupyter notebook. 
System version: 3.6.1 |Anaconda 4.4.0 (64-bit)| (default, May 11 2017, 13:25:24) [MSC v.1900 64 bit (AMD64)]
All tests passed and proved the final confirmation as: "Process Complete!"
Details of input vs output will be detailed in the following chapter. 


***The objective here is to see if you can implement the solution using basic data structure building blocks and software engineering best practices (by writing clean, modular, and well-tested code).*** 

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
This line is not splited correctly/invalid cost value and is skipped: ['1000000001', 'Smith', 'James', 'AMBIEN', '-100']
This line is not splited correctly/invalid cost value and is skipped: ['1000000007', 'Johnson', 'James', 'CHLORPROMAZINE', '$1000']
This line is not splited correctly/invalid cost value and is skipped: ['1000000008', 'Rodriguez', 'NA', 'CHLORPROMAZINE', '']
This line is not splited correctly/invalid cost value and is skipped: ['1000000009', 'Smith', 'David', 'BENZTROPINE MESYLATE', '...']
dict_cost {'AMBIEN': 400.0, 'CHLORPROMAZINE': 3000.0, 'BENZTROPINE MESYLATE': 1500.0}
dict_prescriber {'AMBIEN': ['Garcia Maria', 'Garcia NA'], 'CHLORPROMAZINE': ['Johnson James', 'Rodriguez Maria'], 'BENZTROPINE MESYLATE': ['Smith David']}
9 total lines of data processed
Process Complete!
Time taken: 0:00:00.006615
```

These files are provided in the `insight_testsuite/tests/test_1/input` and `insight_testsuite/tests/test_1/output` folders, respectively.


# Tips on getting an interview

## Writing clean, scalable and well-tested code

As a data engineer, it’s important that you write clean, well-documented code that scales for a large amount of data. For this reason, it’s important to ensure that your solution works well for a large number of records, rather than just the above example.

<a href="https://drive.google.com/file/d/1fxtTLR_Z5fTO-Y91BnKOQd6J0VC9gPO3/view?usp=sharing">Here</a> you can find a large dataset containing over 24 million records. Note, we will use it to test the full functionality of your code, along with other tests.

It's also important to use software engineering best practices like unit tests, especially since data is not always clean and predictable.

Before submitting your solution you should summarize your approach and run instructions (if any) in your `README`.

You may write your solution in any mainstream programming language, such as C, C++, C#, Go, Java, Python, Ruby, or Scala. Once completed, submit a link of your Github or Bitbucket repo with your source code.

In addition to the source code, the top-most directory of your repo must include the `input` and `output` directories, and a shell script named `run.sh` that compiles and runs the program(s) that implement(s) the required features.

If your solution requires additional libraries, environments, or dependencies, you must specify these in your `README` documentation. See the figure below for the required structure of the top-most directory in your repo, or simply clone this repo.

## Repo directory structure

The directory structure for your repo should look like this:

    ├── README.md 
    ├── run.sh
    ├── src
    │   └── pharmacy-counting.py
    ├── input
    │   └── itcont.txt
    ├── output
    |   └── top_cost_drug.txt
    ├── insight_testsuite
        └── run_tests.sh
        └── tests
            └── test_1
            |   ├── input
            |   │   └── itcont.txt
            |   |__ output
            |   │   └── top_cost_drug.txt
            ├── your-own-test_1
                ├── input
                │   └── your-own-input-for-itcont.txt
                |── output
                    └── top_cost_drug.txt

**Don't fork this repo** and don't use this `README` instead of your own. The content of `src` does not need to be a single file called `pharmacy-counting.py`, which is only an example. Instead, you should include your own source files and give them expressive names.

## Testing your directory structure and output format

To make sure that your code has the correct directory structure and the format of the output files are correct, we have included a test script called `run_tests.sh` in the `insight_testsuite` folder.

The tests are stored simply as text files under the `insight_testsuite/tests` folder. Each test should have a separate folder with an `input` folder for `itcont.txt` and an `output` folder for `top_cost_drug.txt`.

You can run the test with the following command from within the `insight_testsuite` folder:

    insight_testsuite~$ ./run_tests.sh 

On a failed test, the output of `run_tests.sh` should look like:

    [FAIL]: test_1
    [Thu Mar 30 16:28:01 PDT 2017] 0 of 1 tests passed

On success:

    [PASS]: test_1
    [Thu Mar 30 16:25:57 PDT 2017] 1 of 1 tests passed



One test has been provided as a way to check your formatting and simulate how we will be running tests when you submit your solution. We urge you to write your own additional tests. `test_1` is only intended to alert you if the directory structure or the output for this test is incorrect.

Your submission must pass at least the provided test in order to pass the coding challenge.

For a limited time we also are making available a <a href="http://ec2-18-210-131-67.compute-1.amazonaws.com/test-my-repo-link">website</a> that will allow you to simulate the environment in which we will test your code. It has been primarily tested on Python code but could be used for Java and C++ repos. Keep in mind that if you need to compile your code (e.g., javac, make), that compilation needs to happen in the `run.sh` file of your code repository. For Python programmers, you are able to use Python2 or Python3 but if you use the later, specify `python3` in your `run.sh` script.

# Questions?
Email us at cc@insightdataengineering.com
