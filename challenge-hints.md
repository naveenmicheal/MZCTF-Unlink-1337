# GENERAL:
	

 1. The flag is string format: mzctf{'something'}
 2. find that flag by solving the challenge
 3. check that in the box labeled as Enter the flag in a challenges section
 4. if it is correct contact the nearby event coordinator, update your status
 5. The event coordinator should be noted that person name and challenge points, with time


	

## Challenge 1:  Client Side Auth
	
The Authentication is done by in client side,
 - check the source code
 - see which user name and password validated by JS

## Challenge 2: I Agree Whatever (cookies)

	    

 - Logine page doesnot check anything, so no name doesn't make any sence
 - The page shows like a "You are not a admin"
 - Hint tells the  word "Cookie" a lot
 - learn what is a web cookie, ahd how to mainpulate in your browser
 - set Admin=True in browser section, Reload the webpage,You got the flag
 

## challenge 3: Robots Know Where it Is?

	
		

 - Read the clues carefully
 - learn more what is the robots.txt file and how to find that in server
 - read the robots.txt file
 - in the robots.txt file, the flag
 - location has been given

## Challenge 5: No Debug In Production (Intermediate Challenge)


	

 - tell to Check the  Responce headers [*if the contestent strugles
   more*]
 - Responce headers provide the debug pin, and where to go  [/shell]
 - in the exception page scroll to bottom
 - click that, enter the pin
 - now you are in a shell
 - The flag is located in the Application root directory
 - use file handlig or subprocess package for quering the system

  
*

# [*]Crypto / Number System




## Challenge 6: Also You Brutus

		

 - Its is ceaser Cipher
 - Clue ROT B  means so ROTATION 13
 - Key is 13
 -[Example] A becomes M 
 - use any online decoder

## challenge 7: Everywhere is a Numbers

		

 - learn what is mean by Number system

		Hint Given:
		()64 ->Base64 Encoding
		()16 ->Hex Encoding
		()2  ->Binary Encoding 


 - Use online decoder for that
 - the flag always looks like  mzctf{some_words}
OS / Network Analysis	

## Challenge 8: Sharks Likes Internet

		

 - Download the .pcap file by cliking the button
 - learn more about Wireshark Filters
 - Open the .pcap file by wireshark
 - tell to analyze the HTTP POST requests
 - 
		Solution Filter: 
			http.request.method =="POST"
	
 - open that packet information find out the flag

## Challenge 9: Steal Login credentials
 - Download the .pcap file from the download link
 - Analyze the file, and find out HTTP Post method packet,
 - Get the login credential from that
 - Open the Challenge website, Login with that

			

## Challenge 10: Version Control System
 - Download the git repository  by cliking the button and extract the
   zip file
 - learn more git and version control system
 - read again the clue
 - open the git bash application installed in your system
 - navigate to the correct directory
 - list out the git log
 - checkout that specific commit
 - get the flag
