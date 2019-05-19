# ALPR-BR

Brazilian ALPR using Python, OPENALPR and verifying the plate on a API

Links to their repositories:


https://github.com/openalpr/openalpr - OpenALPR
https://github.com/victor-torres/sinesp-client - SINESP Client

Right now it only work with images, but I plan to add video/cam suport soon.
Modify bdConnection to match your database (now i'm thinking, 
maybe i souldve used the name dbConnection, but anyways...)

by the way 'testeImagens' and 'PlacasTeste' are useless, dont bother reading it


___________________________OLD__________________________________

At first i was using tesseract ocr, but since i was unable to preprocess the images
correctly to use it in a wide gamma of images, i started looking for other tools to do
 read the licence plates.
 
 Now im using OPENALPR. It can also be used in raspberry pi, wich is great.
 The changes ive already made are for take the first AAA-2222 pattern it finds.
 More coming soon, also i will link to the OPENALPR github later.