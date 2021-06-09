key_code   = 250
input_img  = "img-output.JPG"
output_img = "img-output.JPG"

file  = open( input_img, "rb" )
image = file.read() 
file.close()

imageBytes = bytearray( image ) 

for index, values in enumerate( imageBytes ): 
    imageBytes[ index ] = values ^ key_code

outputImage = open( output_img, "wb" )
outputImage.write( imageBytes ) 
outputImage.close()