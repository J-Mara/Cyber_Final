# Cyber_Final

We have created an intentionally vulnerable website. First users must hack into the website through one of two methods (sql injection or hydra). They then must look at the information inside the cookie, using Inspect Element and the Network tab to do so, and decrypt it using a base64 decoder. Inside the decrypted cookie is a cipher text, and a hint that the key is hidden in the home page. The user will then solve the vigenere cipher and follow the link to the thank you page. If you need help, check the google slides linked below.

Link to our Slides presentation: https://docs.google.com/presentation/d/1CqIaGt_E0U4ZZw52E8QZOd5UYJeimNgTgbVvbTkd-HA/edit?usp=sharing. 

OUTDATED: Link to download our virtual machine (with project installed): https://drive.google.com/file/d/1m411BEUqBFGYlfM-qyO06kDmAeo2lHrt/view?usp=sharing. Previously I thought we had to share the project on a virtual machine because it was an intentionally vulnerable website, however a previous group had students git clone the repository and that worked fine. 

Instructions: Inside WSL or a linux based terminal, enter 'git clone https://github.com/MaretRA/Cybersecurity_Final.git' and go to the 'Cybersecurity_Final' directory. Then create a virtual environment using 'python3 -m venv venv', type '. venv/bin/activate' to activate it, and type 'pip install -r requirements.txt'. Finally, enter 'make', open firefox, and go to http://127.0.0.1:5000/login. 

Reminder: The database table is named user, and the relevant columns are username and password. The two methods to sign into the adm account are:
1. Creating an account and then copy pasting the hashed password into the adm account. 
2. Deleting the adm account and then creating a new adm account with a password of your choice. 

If you need help with reading the cookie information, check the slides, which contains step by step instructions.

Assignment: Submit the result of the vigenere cipher (it is a link). 

Daily log:
-----

1/5/22:
Maret Rudin-Aulenbach: I made small changes to the sql code, added requirements.txt (I tried to include the linux virtualenv in the repository however git add continued to throw errors), and I updated the website description and instructions.

1/4/22:
Maret Rudin-Aulenbach: I removed the XSS injection and replaced it with looking at Session cookie information through Inspect Element and the Network tab. I also did a lot of bug fixing on that (for some reason if I add too much information to session it is no longer encrypted in base64, despite not being over the 4kb limit; not sure why, and I couldn't figure it out. UPDATE: it is because itsdangerous compresses the cookie). And I finished our slides, added an admin login requirement to access the home page, and finished the virtual machine. 

12/22/21:
Maret Rudin-Aulenbach: I got the XSS injection mostly working (it prints the cookie name, rather than the cookie values, to an alert). I'm currently working on fixing that and I also worked on the slideshow. 

12/21/21:
Maret Rudin-Aulenbach: I changed the home page so that the vigenere puzzle reveals the javascript that must be inserted for the XSS attack, rather than leading to the Steg challenge. Now the XSS injection leads to the Steg challenge. I also worked on the slideshow. 

12/20/21:
Maret Rudin-Aulenbach: I started the slideshow (link above), and I researched using simple javascript to print the cookie data to the console (XSS). 

12/16/21:
Maret Rudin-Aulenbach: I finalized the header and worked on the intentional sql injection vulnerability.

12/15/21:
Maret Rudin-Aulenbach: I added a login requirement to see the homepage, a vigenere cipher puzzle, html templates, and started work on the header.

12/14/21:
Maret Rudin-Aulenbach: fixed bugs, caught Jordan up on project (he missed a day), made small changes (such as adding password hashing), and added comments