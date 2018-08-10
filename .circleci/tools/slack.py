from slackclient import SlackClient
import sys
import io
 
slack_client = SlackClient("xoxb-412432026433-414214512930-t0y3tau1n0IrMLTmhE43Qtjx")

attachment = sys.argv[1]

def slack_message(message, channel):
  token = 'xoxb-412432026433-414214512930-t0y3tau1n0IrMLTmhE43Qtjx'
  sc = SlackClient(token)
  reportFile='/home/circleci/repo/reports/'+attachment
  sc.api_call("files.upload", filename=reportFile, channels=channel, file= io.BytesIO(str.encode(content)))
                      
slack_message("Hey","devopsifly")
