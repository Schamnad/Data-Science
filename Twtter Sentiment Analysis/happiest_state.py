import sys
import json

'''
Which State is happiest in USA
  a script that computes the average sentiment scores in each state of USA and find the happiest city
  Schamnad, 16 Nov 2016  
'''

# build the dicionary of sentiment of each word form the AFINN-111 file
def build_sent_dict(sent_file):
    sent_dict = {}

    for line in sent_file:
        term, score = line.split('\t')
        sent_dict[term] = int(score)

    return sent_dict

# evaluate the sentiment score of each tweet
def get_sent_score(tweet, sent_dict):
    sent_score = 0
    for word in tweet:
        if word in sent_dict:
            sent_score += sent_dict[word]
    return sent_score

def get_avg_state_score(tweet_file, sent_dict, states):
    tweet_state_sent = {}
    tweet_state_num = {}
    avg_state_sent_score = {}
    for line in tweet_file:
        json_line = json.loads(line)
        if all(k in json_line for k in ('text','place')):
            if json_line['place'] is not None and "country_code" in json_line['place']:
                if json_line['place']['country_code'] in states:
                    tweet = json_line['text'].encode('utf-8')
                    tweet_state = json_line['place']['country_code']
                    tweet = (tweet.replace('\n', '').replace('\t', '').replace(',', '').replace('.', '').rsplit(' '))
                    tweet_sent_score = get_sent_score(tweet, sent_dict)

                    if tweet_state in tweet_state_sent:
                        tweet_state_sent[tweet_state] += tweet_sent_score
                        tweet_state_num[tweet_state] += 1
                    else:
                        tweet_state_sent[tweet_state] = tweet_sent_score
                        tweet_state_num[tweet_state] = 1
    for tweet_state in tweet_state_sent.keys():
        avg_state_sent_score[tweet_state] = float(tweet_state_sent[tweet_state])/tweet_state_num[tweet_state]

    return avg_state_sent_score


def main():
    states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
    }

    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    sent_dict = build_sent_dict(sent_file)
    sent_file.close()
    avg_state_score_dict = get_avg_state_score(tweet_file, sent_dict, states)

    max_avg = max(avg_state_score_dict.values())
    for state, value in avg_state_score_dict.items():
        if value == max_avg:
            print state, value


if __name__ == '__main__':
    main()
