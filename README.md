# ImageRepo
-This is a Java application that I've created for the Shopify Data Engineer Intern Challenge (https://docs.google.com/document/d/1ijXrqQMOORukOWCWcwwcpxPcF_TczwvNE0wB4M2Orqg/edit#heading=h.n7bww7g70ipk)

## About ImageRepo
- This is a Java application that handles images 
- Users can use this application to store and get images that they have locally
- All images stored will be encrypted, only a 'display' call to the application can decrypt the images
- This application currently supports adding, displaying (decrypting), deleting, and listing images

## How to use this application
- Please make sure to have Java installed and can use **javac**
- Compile the program using:
```javac ImageRepo.java```
- Use the help command to get information on how to use the commands
```java ImageRepo -help```
- The commands flags currently available are -add, -display, -list, -delete, -help

## Testing
- The test suites are located in the **test** folder
- **test_master.py** is the master script and can run all tests at the same time
- To run any test, simply execute the python file
```python test_master.py```

## Encryption
- The images in the **database** folder are encrypted
- The encryption is done using a simple one-time pad cipher on each byte of the image along with cipher block chaining (CBC) applied on the bytes of an image
- This encryption scheme is not the most secured due to the usage of one-time pad cipher and reusing the same key but my code is designed in a way such that a better encryption method can be easily applied to the overall encryption scheme, see the **encrypt** and **decrypt** functions in ImageRepo.java
