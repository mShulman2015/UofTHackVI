# PythonSampleCode
Sample code for python

# Steps:

1) Clone the repository
2) Make sure you have the latest version a package manager for python installed. 
3) Install the following modules to the your python project environment:
    * 'requests'
    * 'hash'
    * 'json'
   
4) Now simply go to the main.py file and fill the following parameters with your information generated from your developer account:
   * 'secretKey'
   * 'thirdPartyAccessid'
   * 'apiRegistrationId'
   * 'email'
   
5) Define a fromDate and toDate in the specified format in the API documentation
   * 'fromDate' (Make sure its a valid date)
   * 'toDate'  (Make sure its a valid date)
   
6) Uncomment the auth function and run the project, this will generate the access token.

7) Now, simply keep uncommenting the the functions as and when you need them from the main file. 

# Note:
When you generate a new access_token by running the auth function, the previous one is deemed invalid
