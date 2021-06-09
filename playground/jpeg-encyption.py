img_path = input(r'Enter path of Image:') 
    
# take input key for an image incryption
key = int(input('Enter Key for encryption or decryption of Image:')) 
        
# open file to read data
f = open(img_path, 'rb') 
    
# storing image data in image variable 
image = f.read() 
f.close() 
    
# converting image into byte array to 
# perform encryption on it's data 
image1 = bytearray(image) 
# perform XOR operation on each value of bytearray 
for index, values in enumerate(image1): 
    image1[index] = values ^ key 
# open file to write data
f1 = open(img_path, 'wb') 
    
# write encrypted data of image1
f1.write(image1) 
f1.close()
print('Encryption or Decryption Done...') 
print('Encryption or Decryption key is: ', key) 