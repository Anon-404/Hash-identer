import os
BLUE = "\033[1;34m"
os.system("clear")
banner1 ="""
    dMP dMP .aMMMb  .dMMMb  dMP dMP                        
   dMP dMP dMP"dMP dMP" VP dMP dMP                         
  dMMMMMP dMMMMMP  VMMMb  dMMMMMP                          
 dMP dMP dMP dMP dP .dMP dMP dMP                           
dMP dMP dMP dMP  VMMMP" dMP dMP                            
"""
banner2 = """
        dMP dMMMMb  dMMMMMP dMMMMb dMMMMMMP dMMMMMP dMMMMb 
       amr dMP VMP dMP     dMP dMP   dMP   dMP     dMP.dMP 
      dMP dMP dMP dMMMP   dMP dMP   dMP   dMMMP   dMMMMK"  
     dMP dMP.aMP dMP     dMP dMP   dMP   dMP     dMP"AMF   
    dMP dMMMMP" dMMMMMP dMP dMP   dMP   dMMMMMP dMP dMP                                                             """
def banner():
	print(BLUE+"#"*64)
	print(banner1,banner2)
	print("powerd by team Anon404 \ncreated by MRZ724")
	print()
	print("#"*64)
banner()
print("Avlable hashes ")
print("[+] CRC16 ")
print("[+] MD5  ")
print("[+] SHA-1 ")
print("[+] SHA-224 ")
print("[+] SHA-256")
print("[+] SHA-384")
print("[+] SHA-512")
hash = input("[+] Enter Your hash : ")
if len(hash) <= 3:
	print("[!] Invalid hash")
elif len(hash) == 4:
    print("[+] CRC16  hash")
elif len(hash) == 32:
    print("[+] MD5 hash")    
elif len(hash) == 40:
    print("[+] SHA-1 hash")   
elif len(hash) == 56:
    print("[+] SHA-224 hash")    
elif len(hash) == 64:
    print("[+] SHA-256 hash")    
elif len(hash) == 96:
    print("[+] SHA-384 hash")   
elif len(hash) == 128:
    print("[+] SHA-512 hash")    
else:
	print("[-] Unknown hash")
