from slackclient import SlackClient
import sys
 
slack_client = SlackClient("xoxb-412432026433-414214512930-t0y3tau1n0IrMLTmhE43Qtjx")

attachment = sys.argv[1]

def slack_message(message, channel):
  token = 'xoxb-412432026433-414214512930-t0y3tau1n0IrMLTmhE43Qtjx'
  sc = SlackClient(token)
  filename='~/repo/reports/'+attachment
  with open(filename, 'rb') as f:
   sc.api_call(
          "files.upload",
          channels=channel,
          filename='~/repo/reports/container-scanning-report-2018-08-10-04-19-19.json',
          title='scanout',
          initial_comment='vuln scanning',
          file=io.BytesIO(f.read())
      )
      
   
                
slack_message("Hey","devopsifly")
