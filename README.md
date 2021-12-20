# Cyber_Final

We are creating an intentionally vulnerable website. Users will download a virtual machine containing the website. They then must hack into the website through one of two methods (sql injections or hyrda). Inside they find a vigenere cipher, which leads them to a hidden directory containing an image. They download that image, use steganography to find the hidden link, and follow it to the message. We will leave hints along the way as for what to do. We are also considering adding a hacking tool that we haven't learned in class. 

12/20/21 update: we are considering using basic XSS to steal cookie information, which will contain the link to the next problem. We know that most of the class does not know javascript, so we will supply them with basic commands to print the cookie data which can be followed without knowing javascript itself. 

Link to our Slides presentation (in progress): https://docs.google.com/presentation/d/1CqIaGt_E0U4ZZw52E8QZOd5UYJeimNgTgbVvbTkd-HA/edit?usp=sharing. 

Daily log:
-----
12/20/21:
Maret Rudin-Aulenbach: I started the slideshow (link above), and I researched using simple javascript to print the cookie data to the console (XSS). 

12/16/21:
Maret Rudin-Aulenbach: I finalized the header and worked on the intentional sql injection vulnerability.

12/15/21:
Maret Rudin-Aulenbach: I added a login requirement to see the homepage, a vigenere cipher puzzle, html templates, and started work on the header.

12/14/21:
Maret Rudin-Aulenbach: fixed bugs, caught Jordan up on project (he missed a day), made small changes (such as adding password hashing), and added comments