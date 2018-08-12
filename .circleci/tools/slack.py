from slackclient import SlackClient
import sys
import io
import json
from collections import Counter
 
slack_client = SlackClient("xoxb-412432026433-414214512930-t0y3tau1n0IrMLTmhE43Qtjx")

attachment = sys.argv[1]

def getSummary(reportFile):
 '''
 Returns Summary stats to be posted to the slack room
 Arg - Vunerablity Scan Json File
 '''
 v_list=[]
 with open(reportFile) as json_data:
    data = json.load(json_data)
    for item in data['vulnerabilities']:
    	v_list.append(item['severity'])

mediumCount= Counter(v_list)['Medium']
highCount= Counter(v_list)['High']
lowCount= Counter(v_list)['Low']

return('Summary : High - {}, Medium - {}, Low - {}'.format(highCount,mediumCount,lowCount))
  

def slack_message(message, channel):
  token = 'xoxb-412432026433-414214512930-t0y3tau1n0IrMLTmhE43Qtjx'
  sc = SlackClient(token)
  reportFile='/home/circleci/repo/reports/'+attachment
  #sc.api_call("files.upload", filename=reportFile, channels=channel, file= io.BytesIO(str.encode(content)))
  summary = getSummary(reportFile)
  with open(reportFile, 'rb') as f:
    sc.api_call(
        "files.upload",
        channels=channel,
        filename=reportFile,
        title=summary,
        initial_comment='Please expand..',
        file=io.BytesIO(f.read())
    )
                      
slack_message("Hey","devopsifly")
