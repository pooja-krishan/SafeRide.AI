from googleapiclient import discovery

API_KEY = 'AIzaSyA6PYGpdbLZuRozjaNpHTnZ60izcCWrO5U'

client = discovery.build(
  "commentanalyzer",
  "v1alpha1",
  developerKey=API_KEY,
  discoveryServiceUrl="https://commentanalyzer.googleapis.com/$discovery/rest?version=v1alpha1",
  static_discovery=False,
)

def getAttributes(text):	# Returns list of THREAT, INSULT, IDENTITY ATTACK, and SEVERE_TOXICITY ratings
                            # Example: [0.31531, 0.7524, 0.76324, 0.3516]
    analyze_request = {
        'comment': { 'text': str(text) },
        'requestedAttributes': {'THREAT': {}, 'INSULT': {}, 'IDENTITY_ATTACK': {}, 'SEVERE_TOXICITY': {}, }
    }
    
    response = client.comments().analyze(body=analyze_request).execute()
    return({
        "THREAT": response["attributeScores"]["THREAT"]["summaryScore"]["value"],
        "INSULT": response["attributeScores"]["INSULT"]["summaryScore"]["value"],
        "IDENTITY_ATTACK": response["attributeScores"]["IDENTITY_ATTACK"]["summaryScore"]["value"],
        "SEVERE_TOXICITY": response["attributeScores"]["SEVERE_TOXICITY"]["summaryScore"]["value"], 
    })