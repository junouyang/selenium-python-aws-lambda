# Selenium Python on AWS Lambda

# Checkin 1point3acres.
* Zip all the files in lambda_function folder
* Rename the zip file to lambda_function.zip
* Follow instructions https://medium.com/@manivannan_data/python-selenium-on-aws-lambda-b4b9de44b8e1
* Lambda setting
  * timeout: 5 min
  * trigger: cloud watch event, expression rate(1441 minutes) //1 day and 1 minute
* Add envirionment variables
  * USERNAME: your 1point3acres user name
  * PASSWORD: your 1point3acres password
