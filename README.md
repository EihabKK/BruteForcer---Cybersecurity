# BruteForcer---Cybersecurity
With a fast speed of trying thousands of passwords per second on an account, it allows us to break into it in just a matter of seconds or minutes in case the password for that account is not strong enough. 

** In this project, I coded a the BruteForcer to bruteforce the login credentials on my own Metasploitable machine. You mgiht have to change some parts of the code (check comments in the python code) to BruteForce the website you want to do it on. **

# Brutforcer

Brutforcer is a Python script designed for ethical hacking purposes. It automates the brute-forcing of a login page by attempting different combinations of usernames and passwords to find the correct login credentials. This tool is intended for use in controlled environments, such as testing your own Metasploitable website, and should not be used for any illegal activities.

## Features

- Automates the process of brute-forcing login pages.
- Supports custom lists of usernames and passwords.
- Displays the correct username and password if found.
- Allows customization of error messages and form fields to adapt to different websites.

## How It Works

1. The user provides the URL of the target website.
2. The user specifies the username they want to test.
3. The user provides a text file containing a list of passwords to try.
4. The script sends POST requests to the login page with each username-password combination.
5. If the login fails, it checks for the presence of a specific error message.
6. If the login is successful, it prints the correct username and password and exits.

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/EihabKK/BruteForcer---Cybersecurity
    cd brutforcer
    ```

2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Run the script:
    ```bash
    python brutforcer.py
    ```

4. Provide the necessary inputs:
    - The URL of the website you want to test.
    - The username for the account you want to access.
    - A text file containing a list of potential passwords.
    - The error message displayed on the website when login fails.

5. The script will try each password in the list and output the correct combination if found.

## Requirements

- Python 3.x
- Requests library

## Important Notice

This tool is for educational purposes only. Unauthorized use of this tool to gain access to a website is illegal and unethical. Always ensure you have explicit permission from the website owner before attempting to brute-force any login page.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
