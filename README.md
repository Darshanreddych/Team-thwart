# Basic implementation of blockchain using python
This is a simple implementation of blockchain working using python 

In this we used the basic concepts of blockchain which are:
1.genisis_block
2.Hashing
3.consensus
4.nonce

Working of this program:
in this program we stored an some dummy keys for transactions , we use those keys while running the program
the keys are = ['12345678','1235678','345678']

when you run the program it will ask for the select options,
the options are 
1. Show Blockchain:
    it will show the cuurrent blocks in the blockchain
2. Make transactions: 
    in this option we can do some dummy transactions , by entering reciever key ( which are already in the list ), after the key enter it will verify the key in the list, then initiate the transaction, it will send to the miner to verify ( here in mining we have used the hashcash algorithm for the generation of nonce with difficulty level 4 ). After the successfull verification of transaction, the block will be added to the network.
3. Alter a block :
    in this step we can try to alter a block , it will give some imbalanced output of the blockchain.

block consists of:
1. Hash of Previous block 
2. Transaction details
3. time stamp
4. hash of the block
5. nonce


#Two-factor authentication
  Two-factor authentication provides higher level of security than other methods like single-factor authentication, two-factor authentication is also known as two-step verification where a authentication system verifies user by asking
two factors to prove his identity.

In the program name "auth.py" we have implemented a python program to authenticate the user by asking two factors i.e password and OTP number, the email address and password is stored using dictionary in the program itself, "twilio"
application is used to send OTP to the provided mobile number, python has inbuilt module called twilio to provide this functionality.

steps:
1) firstly, it will ask for email address.
2) If provided mail id is correct, it will ask for password.
3) If provided password is correct it will ask mobile number to send OTP.
4) Entering correct OTP gives access to user account.
