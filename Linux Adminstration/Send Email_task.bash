 #!/bin/bash
 
   history >> session3_history.txt       #get the history

    mail --version
    sudo apt install mailutils
    sudo apt-get  install ssmtp
    sudo nano /etc/ssmtp/ssmtp.conf
  
  << comment
	GNU nano 6.2                 /etc/ssmtp/ssmtp.conf                           
	#
	# Config file for sSMTP sendmail
	#
	# The person who gets all mail for userids < 1000
	# Make this empty to disable rewriting.
	#root=postmaster
	SERVER=khloud.khaled209@gmail.com

	# The place where the mail goes. The actual machine name is required no 
	# MX records are consulted. Commonly mailhosts are named mail.domain.com
	mailhub=smtp.gmail.com:587

	AuthUser=khloud.khaled209@gmail.com
	AuthPass=lfsrijyhsgxxlvoe
	UseTLS=YES
	UseSTARTTLS=YES

	# Where will the mail seem to come from?
	#rewriteDomain=
	rewriteDomain=gmail.com
	# The full hostname
	hostname=kholoud-VirtualBox

	# Are users allowed to set their own From: address?
	# YES - Allow the user to specify their own From: address
	# NO - Use the system generated From: address
	#FromLineOverride=YES
		  [ line  1/28 ( 3%), col  1/ 2 ( 50%), char   0/751 ( 0%) ]
	^G Help        ^O Write Out   ^W Where Is    ^K Cut         ^T Execute
	^X Exit        ^R Read File   ^\ Replace     ^U Paste       ^J Justify
comment

    mail -s "linux history" -A session3_history.txt khloud.khaled209@gmail.com

<<comment 
	press ctrl+D to send 
	
	"linux_history" ---> mail subject
	session3_history.txt ---> file to send
	rehamma215@gmail.com ---> mail send the file to
comment




