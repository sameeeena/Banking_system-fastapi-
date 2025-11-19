# Bank System

## Features included

1. Deposit 
2. Authentication
3. Money Transfer
4. Balance

## Tech Stack 

1. Gemini CLI (Gemini cli is a coding agent. It generates code accordind to user's Prompts.)
2. Fastapi (Fastapi is a framework of python. it provides high perfomance API routes.)
3. Python (Programming language)

## Defining Endpoints with their functionality
1. ***Deposit***
####### Users allowed to  deposit funds after authentication.

1. ***authentication***
####### Through this endpoint users must authenticate with their name and Pin number.
####### if user's information is incorrect Exception raised. 

2. ## ***Bank transfer***

####### Any User can transfer the money to any account number.

3. ## ***Balance***

####### After the transaction, the balance of the sender and reciever will be showed.

## Example Endpoint Summary

#### Endpoint	       Method	Description

######## /authenticate	POST	Authenticates a user and returns a token
######## /deposit	    POST	 Deposits an amount into user account
######## /transfer	    POST	 Transfers money between accounts
######## /balance	    GET	    Returns current balance for user
