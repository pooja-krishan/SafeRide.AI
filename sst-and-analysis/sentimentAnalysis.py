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
        'requestedAttributes': {'TOXICITY': {}, 'SEVERE_TOXICITY': {}, 'PROFANITY': {}, 'THREAT': {}, 'INSULT': {}, 'IDENTITY_ATTACK': {}}
    }
    
    response = client.comments().analyze(body=analyze_request).execute()
    return({
        "TOXICITY": response["attributeScores"]["TOXICITY"]["summaryScore"]["value"], 
        "SEVERE_TOXICITY": response["attributeScores"]["SEVERE_TOXICITY"]["summaryScore"]["value"], 
        "PROFANITY": response["attributeScores"]["PROFANITY"]["summaryScore"]["value"], 
        "THREAT": response["attributeScores"]["THREAT"]["summaryScore"]["value"],
        "INSULT": response["attributeScores"]["INSULT"]["summaryScore"]["value"],
        "IDENTITY_ATTACK": response["attributeScores"]["IDENTITY_ATTACK"]["summaryScore"]["value"],
    })

def getScore(text):
    analyze_request = {
        'comment': { 'text': str(text) },
        'requestedAttributes': {'TOXICITY': {}, 'SEVERE_TOXICITY': {}, 'PROFANITY': {}, 'THREAT': {}, 'INSULT': {}, 'IDENTITY_ATTACK': {}}
    }
    
    response = client.comments().analyze(body=analyze_request).execute()
    return(
      (0.7*response["attributeScores"]["TOXICITY"]["summaryScore"]["value"]) + 
      (response["attributeScores"]["SEVERE_TOXICITY"]["summaryScore"]["value"]) + 
      (0.5*response["attributeScores"]["PROFANITY"]["summaryScore"]["value"]) + 
      (response["attributeScores"]["THREAT"]["summaryScore"]["value"]) + 
      (0.8*response["attributeScores"]["INSULT"]["summaryScore"]["value"]) + 
      (response["attributeScores"]["TOXICITY"]["summaryScore"]["value"])
      )
    # Formula: 0.7 toxic  1 severe toxic  0.5 obscene 1 threat  0.7 insult  1 identity hate