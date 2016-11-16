import sys
import json

'''
Derive the sentiment of new terms from the twitter data
  a script that computes the sentiment for the terms that do not appear in the file AFINN-111.txt.
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

# Derive the sentiment of new terms
def build_non_sent_dict(sent_dict, tweet_file):
    non_sent_dict = {}
    for line in tweet_file:
        json_line = json.loads(line)
        if 'text' in json_line:
            tweet = json_line['text'].encode('utf-8')
            tweet = (tweet.replace('\n', '').replace('\t', '').replace(',', '').replace('.', '').rsplit(' '))
            tweet_sent_score = get_sent_score(tweet, sent_dict)
            for word in tweet:
                if word not in sent_dict and word in non_sent_dict:
                    non_sent_dict[word] += tweet_sent_score
                else:
                    non_sent_dict[word] = tweet_sent_score
    return non_sent_dict


def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])

    sent_dict = build_sent_dict(sent_file)
    sent_file.close()
    non_sent_dict = build_non_sent_dict(sent_dict, tweet_file)

    for key, value in non_sent_dict.items():
        print key, value

if __name__ == '__main__':
    main()
