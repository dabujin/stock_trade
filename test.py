import requests
 
def post_message(token, channel, text):
    response = requests.post("https://slack.com/api/chat.postMessage",
        headers={"Authorization": "Bearer "+token},
        data={"channel": channel,"text": text}
    )
    print(response)
 
myToken = "xoxb-2049051962662-2053907188695-ZxvssiNQCzhGhCGCIbSTDMox"
 
post_message(myToken,"#creon","jocoding")

