# Cyber_Final

We are creating an intentionally vulnerable website. Users will download a virtual machine containing the website. They then must hack into the website through one of two methods (hydra or sql injections). They then must look at the information inside the cookie, using Inspect Element and the Network tab to do so, and decrypt it using a base64 decoder. Inside the decrypted cookie is the cipher text, and a hint that the key is hidden in the home page (it's in an html comment). The user will then solve the vigenere cipher and follow the link to the thank you page. 

Link to our Slides presentation: https://docs.google.com/presentation/d/1CqIaGt_E0U4ZZw52E8QZOd5UYJeimNgTgbVvbTkd-HA/edit?usp=sharing. 

Daily log:
-----
1/4/22:
Maret Rudin-Aulenbach: I removed the XSS injection and replaced it with looking at Session cookie information through Inspect Element and the Network tab. I also did a lot of bug fixing on that (for some reason if I add too much information to session it is no longer encrypted in base64, despite not being over the 4kb limit; not sure why, and I couldn't figure it out). And I worked on our slides, added an admin login requirement to access the home page, and finished the virtual machine. 

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