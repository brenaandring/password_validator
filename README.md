#Password Validator

##Background
<a href="https://www.nist.gov/" target="_blank">NIST</a> recently updated their 
<a href="https://pages.nist.gov/800-63-3/" target="_blank">Digital Identity Guidelines</a> in June 2017. The new 
guidelines specify general rules for handling the security of user supplied passwords. 
Previously, passwords were suggested to have certain composition rules (special characters,
 numbers, etc), hints and expiration times. Those have gone out the window and the new 
 suggestions are as follows: Passwords MUST:
 
1. Have an 8 character minimum
2. AT LEAST 64 character maximum
3. Allow all ASCII characters and spaces (unicode optional)
4. Not be a common password

##Project

The program accepts passwords from STDIN in newline delimited format and print invalid passwords to the command line. An example usage would look like the following: (asterisks used to print unprintable chars).

```
cat input_passwords.txt | ./password_validator.py weak_password_list.txt
Blah -> Error: Too Short
********** -> Error: Invalid Characters
Password1 -> Error: Too Common
```

##Usage
###Install Python3
Make sure you have Python3 installed on your machine. To check if you have Python installed, open a terminal and type in:
```
python3 --version
```
If you do not have Python3 installed, please make sure to follow the directions on <a href="https://www.python.org/downloads/" target="_blank">python.org/download</a> to install it.

###Clone the repository using the command line
* Click on the green **Code** button

* To clone the repository using HTTPS, under "Clone with HTTPS", click the clipboard.

* Open Terminal

* Change the current working directory to the location where you want the cloned directory

* Type `git clone` and then paste the URL you copied earlier
```
$ git clone https://github.com/brenaandring/password_validator.git
```

* Press Enter to create your local clone

###Run the program
Once you have cloned the repository to your local machine, `cd` into the password_validator root directory in your terminal and run the following:
`./password_validator.py weak_password_list.txt
` and type the password you want to validate.

```
./password_validator.py weak_password_list.txt
mypassword
mypassword -> Error: Too Common
text
text -> Error: Too Short
text -> Error: Too Common
aäzž
a*z* -> Error: Too Short
a*z* -> Error: Invalid Characters
``` 
*Control + d to exit*

Another way of running the programming is entering the following into command line:

```
cat input_passwords.txt | ./password_validator.py weak_password_list.txt
```
####*Sample of successful output*
```
Blah -> Error: Too Short
Password1 -> Error: Too Common
Pass1234 -> Error: Too Common
12345678 -> Error: Too Common
pass1234 -> Error: Too Common
********** -> Error: Invalid Characters
teeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeds;'gkljmsdfgkmdfgl;knmdfgkl;dfmgldfkgdfklgmdfgkmdfkl;mdfklgmdfklgmfldkgmlfkdgmfldkgmfdl;kgmsdl;mgfdlkgdfklgmf;klgmldkfsgl;kdmfglkdfgkldfgdflkdflkfkg;kldfgsdfklmsdlfkgsdfl;gmsdflkmsdflkmdfklmd;flgfkl;mfdklgdflkdkl;gdkl;gdlfkgmsldkfgsdklmsl;dg;lkdmg;dfkmg;kldgmk;flmgkldmgkl;fmgkldmgdfklg;klgmdlkgldfkdfklgdfklg;fklmglfkdgl;dfm -> Error: Too Long
Bj**rk****oacute* -> Error: Invalid Characters
  ..******* -> Error: Invalid Characters
```

####*Sample of failed output*
When a file cannot be found (make sure you provide the path if you decide to use a different file that is not in the project repository, ex: `cat ~/Desktop/input_passwords.txt | ./password_validator.py ~/Desktop/weak_password_list.txt`)
```
Traceback (most recent call last):
  File "./password_validator.py", line 43, in <module>
    main()
  File "./password_validator.py", line 33, in main
    weak_password_set = set(line.strip() for line in open(weak_password_list_filename))
FileNotFoundError: [Errno 2] No such file or directory: 'weak_password_list.txt'

```

##Run the Test
* Make sure to have python3 installed on your local machine
* Clone the repository with terminal
* `cd` into the root directory of password_validator in terminal
* Run the following script in your terminal:
```
python3 password_validator_test.py
```

####*Sample of test results*
```
python3 password_validator_test.py
.********** -> Error: Invalid Characters
..password -> Error: Too Common
.teeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeds;'gkljmsdfgkmdfgl;knmdfgkl;dfmgldfkgdfklgmdfgkmdfkl;mdfklgmdfklgmfldkgmlfkdgmfldkgmfdl;kgmsdl;mgfdlkgdfklgmf;klgmldkfsgl;kdmfglkdfgkldfgdflkdflkfkg;kldfgsdfklmsdlfkgsdfl;gmsdflkmsdflkmdfklmd;flgfkl;mfdklgdflkdkl;gdkl;gdlfkgmsldkfgsdklmsl;dg;lkdmg;dfkmg;kldgmk;flmgkldmgkl;fmgkldmgdfklg;klgmdlkgldfkdfklgdfklg;fklmglfkdgl;dfm -> Error: Too Long
.hi -> Error: Too Short
...
----------------------------------------------------------------------
Ran 8 tests in 0.001s

OK

```