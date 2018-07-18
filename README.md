# Tweetegram


In this tutorial we create a simple app that send your tweet into your telegram channel. At the end of tutorial you will be able to:


1.   Familar with tweepy (famous library for usign twitter API)
2.   Learn how to use twitter Stream API
3.   Familar with Telegram Core API
4.   Make http request in telegram

---

# Twitter

First of all, let's do twitter part. Go to [this](https://apps.twitter.com/) link and create a new App. Fill all necessary forms (name, description, and webiste) in that page and press `Create your Twitter application`. 

![Create an application](https://github.com/hadifar/tweetegram/blob/master/images/create_an_application.png)


In the next page go to the `Keys and Access Tokens` tab section, to see your *API key* and *API secret*. In this tab and at the end of the page, click on `Create my access token` button. It will generate *Access token* and *Acess token secret*. These 4 keys are necessary for communicating with Twitter API.

![Generate All nessary keys and tokens](https://github.com/hadifar/tweetegram/blob/master/images/token_access.png)


Twitter part is almost done. You can test your tokens simple application like bellow:
"""

    !pip install tweepy

    import json

    from tweepy import OAuthHandler
    from tweepy import Stream
    from tweepy import StreamListener

    class Listener(StreamListener):
  
      def on_data(self, data):
      
            all_data = json.loads(data)

            tweet = all_data.get("text")
            print(tweet)
            return True



# Replace your keys otherwise its not work
    API_KEY= "JXyUTTY5PDumdFave6JS2xbVC"
    API_SECRET = "W9DCxTEX5HlL2Hb5i6UAZaSZ7CdLgTvHpluJv39Ce2rO0Zjp4U"
    ACCESS_TOKEN  = "2819616027-clMvryugR0JtRcPCKJqTZsllGm8YlY14CAOjOPi"
    ACCESS_TOKEN_SECRET = "uq0UQna5r24K5wISlro7e1quH5AXo9s5EzIdkapxtZjoP"
    
    auth = OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    stream = Stream(auth, Listener())
    stream.filter(track=['google'])

"""This piece of code will track all tweets with 'google' keyword and print the text for you. That's cool isn't it? Now let's inetegrate our Twitter API with Telegram.

# Telegram

In order to send your tweets into telegram channel you can create a Telegram Bot to do it for you. There are 3 steps to go:


*   Create public Channel
*   Create a telegram bot with [BotFather](https://core.telegram.org/bots#3-how-do-i-create-a-bot)
*   Set the bot as administrator in your channel


Creating Channel, Telegram Bot and set Bot as administrator is fairly easy. When you create a bot with BotFather it will send you a key similar to mine (Use your own key otherwise it not going to work):



> **`665963134:AAGYRZ4cMbP_Q2zoCVusiFawSi5bsX9G05U`**


Change your Listener class in previous section to bellow:
"""

class Listener(StreamListener):
  
    ENDPOINT = "https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"
    TELEGRAM_BOT_API_KEY = "665963134:AAGYRZ4cMbP_Q2zoCVusiFawSi5bsX9G05U"
    TELEGRAM_CHANNEL_NAME = "@my_channel_name" # @ symbol is mandatory
    
    def on_data(self, data):
        all_data = json.loads(data)

        tweet = all_data["text"]
        print(tweet)

        req = self.ENDPOINT.format(self.TELEGRAM_BOT_API_KEY,
                                   self.TELEGRAM_CHANNEL_NAME,
                                   tweet)
        requests.get(req)

        return True

    def on_error(self, status):
        print ('error with status code' + str(status))

"""As you can see, we make HTTP request with `requests` package. So before executing above script **do not forget to install requests**.



```
pip install requests
```





If you want to stream specific user time-line, you should change your code a little.

First, find out twitter account ID with http://mytwitterid.com/ or search google for **How to find our twitter ID"**. For example my twitter ID is **2810616827**. 

Change your code into:
"""

# Replace your keys otherwise its not work
    API_KEY= "JXyUTTY5PDumdFave6JS2xbVC"
    API_SECRET = "W9DCxTEX5HlL2Hb5i6UAZaSZ7CdLgTvHpluJv39Ce2rO0Zjp4U"
    ACCESS_TOKEN  = "2819616027-clMvryugR0JtRcPCKJqTZsllGm8YlY14CAOjOPi"
    ACCESS_TOKEN_SECRET = "uq0UQna5r24K5wISlro7e1quH5AXo9s5EzIdkapxtZjoP"

    auth = OAuthHandler(API_KEY, API_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    stream = Stream(auth, Listener())
    stream.filter(follow=['2810616827'])  # Listen to my Twitter ID
