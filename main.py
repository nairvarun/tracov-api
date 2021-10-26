# todo:
    # add the covid update part after making the webscraping module
    # add requirements.txt

# good refrence
    # https://praw.readthedocs.io/en/stable/code_overview/models/comment.html
    # https://praw.readthedocs.io/en/stable/code_overview/models/submission.html 
    # https://praw.readthedocs.io/en/stable/tutorials/reply_bot.html

#region imports
import praw
import login
#endregion

# region function definitions

# starts the bot 
def run_bot(reddit):

    for item in reddit.inbox.stream():

        if item.body == 'u/'+login.username:
            print('bot request: OK')

            item.reply('test reply')
            print('reply: OK')

            item.mark_read()
            print('mark as read: OK')
        else:
            print('bot request: BAD')

        # uncomment 'break' if you want the bot to only run once
        # break

# main function
def main():

    reddit = praw.Reddit(client_id = login.client_id,
                        client_secret = login.client_secret,
                        username = login.username,
                        password = login.password,
                        user_agent = login.user_agent) 

    if reddit.user.me() == login.username:
        print('authentication: OK')
    else:
        print('authentication: FAILED')

    run_bot(reddit)

# endregion

if __name__ == '__main__':
    main()
