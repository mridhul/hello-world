from slackclient import SlackClient
 
slack_client = SlackClient("xoxb-412432026433-414214512930-t0y3tau1n0IrMLTmhE43Qtjx")
         
def slack_message(message, channel):
    token = 'xoxb-412432026433-414214512930-t0y3tau1n0IrMLTmhE43Qtjx'
    sc = SlackClient(token)
    sc.api_call('chat.postMessage', channel=channel, 
                text=message, username='vuln-scan',
                icon_emoji=':robot_face:')
                
slack_message("Hey","devopsifly")
