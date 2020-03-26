---
# Stock Monitor
   This program is create to keep watch over the stock price that you are interested in. When the stock price is lower the thersholing value, it will send e-mail to your specified mailbox.
##  Requirements
* requests
* smtplib
* email.mime.text

##	How to use
### Set the stock object and thershold value
This program uses the data api of sina company. You can put your stock id and thershold value to **stock_list.txt**. The format is:
`stock id`	`thershold value`

`sh000001`   `3000`

sh: It represent the stock of Shanghai stock market.	
sz: It represent the stock of Shenzhen stock market.
### Set the mail 
Firstly, you need to set the E-mail servers. You can use the 163 mail or gmail server to send monitor e-mail.
 
```
mail_user = 'XXX'			#set user name of your mail server
mail_pass = 'XXX'			#set user password of your mail server
sender = 'Stock Monitor'	#set the name of sender
receivers = ['XXX']			#set the email address of receivers		
```
Then you need to write a compete mail to you!!! You can modify the string `Subject` and `message` to whatever you like to write.
### Run
Finally, you can run this program to monitor your stock price! Use following command to run this program in **Command Line** at your servers.
> python main.py

You can read [guideline](https://zhuanlan.zhihu.com/p/36459081) to make this program resident in the background of the server.

