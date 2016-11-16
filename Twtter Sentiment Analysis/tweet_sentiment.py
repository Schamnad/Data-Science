import sys
import json

# Derive the sentiment of each tweet
def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = {}

    for line in sent_file:
        term, score = line.split('\t')
        scores[term] = int(score)

    for line in tweet_file:
        output_line = json.loads(line)
        sent_score = 0
        if "text" in output_line:
            tweet = output_line["text"].encode('utf-8')
            tweet = (tweet.replace('\n', '').replace('\t', '').replace(',', '').replace('.', '').rsplit(' '))
            for word in tweet:
                if word in scores:
                    sent_score += scores[word]
        print sent_score


if __name__ == '__main__':
    main()
