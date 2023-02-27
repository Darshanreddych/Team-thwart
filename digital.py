import rsa

l=[]

def generate_keys():
        (pubkey, privkey) = rsa.newkeys(512)
        return pubkey, privkey
        
def sign(privkey, message):
        signature = rsa.sign(message.encode(), privkey, 'SHA-256')
        return signature
        
def verify(pubkey, message, signature):
        try:
            rsa.verify(message.encode(), signature, pubkey)
            return True
        except rsa.VerificationError:
            return False

def main():
	print("\nslect option\n _____________\n")
	print("1.Sign the messge\n2.Verify the messege\n")
	flag=0
	pubkey, privkey = generate_keys()
	print("Keys generated successfuly\n")
	while(True):
		a=int(input("Enter ur choice ==> "))
		if a==1:
			message =input("\nEnter a messege to be signed ==> ")
			print("Generating a signature\n")
			signature = sign(privkey, message)
			print("\nThe messege digitally signed\n")
			print(signature)
		elif a==2:
			m=input("\nEnter a messege to verify\n")
			is_valid = verify(pubkey, m, signature)
    
			if is_valid:
        			print("Messege or Signature is valid.\n")
        			flag=1
			else:
        			print("Messege or Signature is invalid.\n")
        			flag=1
		if flag==1:
			break
main()
