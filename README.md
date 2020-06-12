# Serverless remote shell #

### Goal:
Minimal footprint, minimal cost remote cloud shell, directly from terminal.

### Tools: ###

 - AWS Lambda
 - AWS IAM
 - Python3
 - CFN
 - Static binaries
 
### Status: ###

PoC done, static binaries to be added ...

### Example usage ###

```
$ ./slss 
Welcome! Type ? to list commands
lambda> echo $AWS_DEFAULT_REGION
us-east-1

lambda> set REGION eu-west-2
Setup REGION eu-west-2
lambda> echo $AWS_DEFAULT_REGION
eu-west-2

lambda> help

Documented commands (type help <topic>):
========================================
exit  help  set

lambda> exit
Bye
```
