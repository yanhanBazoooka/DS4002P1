# DS4002P1
## Section 1: Software and platform section
For this project we used tools including Rstudio and Python. Rsutdio was used for a variety of data processing purposes. First, Rstudio was used for data processing including appending columns such as percent change in price for later analysis. Rstudio was once again used to retreive sentiment and append scores using the VADER package. Finally, Rstudio was used to run the final regression and GGplot2 was used to visualize. Rstudio for Windows was used for regression and visualisation, and all other processes were run on MacOS. Python was used to obtain date data from the URL's using regex.
## Section 2: A Map of your documentation.
This respository is organized into folders:
- Scripts:
The Scripts folder holds all necessary scripts in order to reproduce the results of this project. This also includes a Master Script file that calls all other scripts to reproduce these results.

MasterScript

Regression.r

data.py

etc.
- Data:
The Data folder contains the base and analysis datasets. Following the scripts folder allows for the transformation process to be replicated. Adittionally this folder contains a data dictionary which explains all data that is analyzed.

LCID.xlsx

NVDA.xlsx

analysis.xlsx

DataAppendix.pdf

- Output:
  This folder includes all outputs. This includes regression results and all visualizations.
  
## Section 3: Instructions for reproducing your results. 
**This will need to be updated once we have final file names, and Master Scripts file to make sure the order is correct.**
This project takes 4 base data files and performs sentiment analysis and linear regression to achieve the given results. First, take the base data files NVDA.xlsx and LCID.xlsx. Running the (insert) file will pull date data from the URL's which will be important for merging later on. Second, run the (insert) file in Rstudio to append the VADER compound sentiment scores to the text data. 

For the other two base data files run the (insert) file to find the percent price change for each respective stock. Now the files are ready to be merged on date. Run the (insert file) to merge the files into the final analysis file. Finally run the (insert) file to achieve the final regression and outputs. 


*In this section, you should give explicit step-by-step instructions to reproduce the Results of your study. These instructions should be written in straightforward plain English, but they must be concise, but detailed and precise enough, to make it possible for an interested user to reproduce your results without much difficulty. N.B. This section will be crucial for the CS1 assignment, where you'll be required to reproduce the results of other groups. Therefore, make sure to explain this section thoroughly.*
