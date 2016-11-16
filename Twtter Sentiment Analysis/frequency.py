import sys
import json

'''
Compute Term Frequency
  a script that computes the frequency of each unique term in the twitter data
  Schamnad, 16 Nov 2016  
'''

def create_recurrence_dict(input_file):
    recurrence_dict = {}
    total_terms = 0
    for line in input_file:
        json_line = json.loads(line)
        if 'text' in json_line:
            tweet = json_line['text'].encode('utf-8')
            tweet = (tweet.replace('\n', '').replace('\t', '').replace(',', '').replace('.', '').rsplit(' '))
            for word in tweet:
                total_terms+=1
                if word in recurrence_dict:
                    recurrence_dict[word]+=1
                else:
                    recurrence_dict[word] = 1
    return total_terms, recurrence_dict


def create_frequency_dict(total_terms, term_recurrence_dict):
    term_frequence_dict = {}
    for term, value in term_recurrence_dict.items():
        term_frequence_dict[term] = float(value)/total_terms
    return term_frequence_dict


def main():
    tweet_file = open(sys.argv[1])
    total_terms, term_recurrence_dict = create_recurrence_dict(tweet_file)
    tweet_file.close()

    term_frequence_dict = create_frequency_dict(total_terms, term_recurrence_dict)
    for term, freq in term_frequence_dict.items():
        print term, freq









if __name__ == '__main__':
    main()
