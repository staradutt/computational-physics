

#### 7 ####

In question 7, the compute time for a grid of size 1024 was around 30 mins. So I have made two programs.

The first program namely data_generator_main.py,  uses tridiagonal solver to compute the function at t=1 for
128, 256, 512, 1024 grid points and dumps them into .txt files. This program takes around 30 minutes to run.

The second program p7.py uses the data in the .txt files created above to make final error calculations and visualisation.

#IMPORTANT 

#joblib library is used to dump the variables as text files. It is again used to read the text files.
#This library can be installed on linux by using pip in terminal
#command to install: pip3 install joblib 

#### 8 ####

In Q8,

the code for advection part is named p8_advection.py

the code for burgers part is named p8_burgers.py 
