input_img  = "json-output.json"
test_img   = "test-write.json"
checksum   = "0123456789"

file  = open( input_img, "rb" )
image = file.read() 
file.close()

for test_key_code in range( 1, 255 ):
    file  = open( input_img, "rb" )
    image = file.read() 
    file.close()

    imageBytes = bytearray( image ) 

    for index, values in enumerate( imageBytes ): 
        imageBytes[ index ] = values ^ test_key_code

    try:
        if checksum in imageBytes.decode():
            print( imageBytes.decode() )
            print( "Code: ", test_key_code )
    except:
        print( "error" )