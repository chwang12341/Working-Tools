# Reset File Name Tool

## Tool Introduction:

+ help us to reset disarray files in to an ordered files
+ help to reduce some repeat work

## Scenario:

a. You are a data scientist and you are ordered to analysis the customer data, the data was written by different Customer Service Representative (CSR) , so the files' name are not in a standard format,and it is not easy to load into dataframe (python) and analysis

b.  You are a new Customer Service Representative (CSR) and you are ordered to manage the customer data from Customer Service Representative (CSR) over the past, but the data was written by different Customer Service Representative (CSR) , so the files' name are not in a standard format,and it is not easy for you to manage

+ different file name, but same purpose file

![reset_file_name](C:\Users\user\Desktop\Working-Tools\tool_reset_filename\Images\reset_file_name.PNG)

c. You are a AI Engineer, different devices are automatically creating a lot of training data together,   but you need to combine all the data together into one dataset

ex. computer1 create test_data1~n.csv and computer2 also create  test_data1~n.csv, so you might need to reset computer2's test_data1~n.csv to test_datan+1~m.csv, then you can combine two dataset into test_data1~m.csv



## How To Use It

1. **Execute it**

   a. run the python file in command: python tool_reset_filename.py

   b. click the tool_reset_filename.exe

2. **you will see this:**

   a. write down the folder path where your files are(your own computer folder path)

   b. just press enter ,default folder is in the temp folder(suggest: put the files you want to change here)

3. **make sure it shows the correct current files in the console**

4. **new file name:** enter a new file name for them, ex. traindata(purpose:  **Analysis:** load into dataframe easity through python or any other languages)

5. **new files name order you want to start from(default: 0):** you can enter any number( if you enter 1: then the data will start from train_data1~traindatan)

6. 
