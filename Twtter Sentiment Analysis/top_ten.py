import sys
import json

'''
Get top ten hash tags
  a script that computes the frequency of hash tags in the twitter data
  Schamnad, 16 Nov 2016
'''

def build_hash_tag_dict(tweet_file):
    hashtag_dict = {}
    for line in tweet_file:
        json_line = json.loads(line)
        if 'entities' in json_line and 'hashtags' in json_line['entities']:
            if json_line['entities']['hashtags'] != []:
                for hashtag in json_line['entities']['hashtags']:
                    hashtag = hashtag['text'].encode('utf-8')
                    if hashtag in hashtag_dict:
                        hashtag_dict[hashtag] += 1
                    else:
                        hashtag_dict[hashtag] = 1
    return hashtag_dict

def main():
    tweet_file = open(sys.argv[1])
    hastag_freq_dict = build_hash_tag_dict(tweet_file)
    tweet_file.close()

    top_ten = sorted(hastag_freq_dict.items(), key=lambda x:-x[1])[:10]

    for x in top_ten:
        print "{0}: {1}".format(*x)

if __name__ == '__main__':
    main()
