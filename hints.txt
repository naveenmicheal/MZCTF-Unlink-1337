GENERAL:
	The flag is string
	always looks in the format  mzctf{some_random_words}
	find that flag by solving the challenge
	put that in the box labeled as Enter the flag
	click the submit button
	if it is correct contact the nearby event coordinator

	The event coordinator should be noted that person name and challenge points, with time




Challenge 1:
	Client Side Auth
		The Authentication is done by in client side,
		check the source code
		how the user name and password validated

Challenge 2:
	I Agree Whatever
		The page shows like a "You are not a admin"
		Hint tells a word "Cookie" a lot
		learn what is a web cookie
		check the source code
		and learn to know the default cookie value

challenge 3:
	Robots Know Where it Is?
		Read the clues carefully
		learn more what is the robots.txt file and how to find that in server
		read the robots.txt file, 
		in the robots.txt file, the flag location has been given

Challenge 4:
	I love Google Bots
		Read the clue
		learn more what is mean by user agent
		and what is mean by google bot
		and learn how to change your browser agent

Challenge 5:
	No Debug In Production [tought one]

		tell to Check the  Responce headers [*if the contestent strugles more*]
		Responce headers provide the debug pin, and where to go  [/shell]
		in the exception page scroll to bottom
		click that, enter the pin
		how you are in a shell
		The flag is located in the Application root directory
		use file handlig or subprocess package for quering the system
====================================================================================================

[*]Crypto / Number System



Challenge 6:
	Also You Brutus

		Its is ceaser Cipher
		Clue ROT B  means so ROTATION 13
		Key is 13
		A becomes M 
		use any online decoder

challenge 7:
	Everywhere is a Numbers
		learn what is mean by Number system
		Hint Given:
		()64 ->Base64 Encoding
		()16 ->Hex Encoding
		()2  ->Binary Encoding 

		Use online decoder for that
		the flag always looks like  mzctf{some_words}

=====================================================================================================

OS / Network Analysis	

Challenge 8:
	Sharks Likes Internet
		Download the .pcap file by cliking the button
		Open the .pcap file by wireshark
		tell to analyze the HTTP POST requests
		learn more about Wireshark Filters

		Solution Filter: 
			http.request.method =="POST"
		open that packet information find out the flag

Challenge 9:
	Steal Login credentials
		Download the .pcap file from the download link <br>
         Analyze the file, and find out HTTP Post method packet, 
         Get the login credential from that
         Open the Challenge website, Login with that 

			
Challenge 10:
	Version Control System
		Download the git repository  by cliking the button and extract the zip file
		learn more git and version control system
		read again the clue
		open the git bash application installed in your system 
		navigate to the correct directory
		list out the git log 
		checkout that specific commit
		get the flag



