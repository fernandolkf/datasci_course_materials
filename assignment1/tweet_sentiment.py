import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def test():
	afinnfile = open("AFINN-111.txt")
	scores = {} # initialize an empty dictionary
	for line in afinnfile:
  		term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
  		scores[term] = int(score)  # Convert the score to an integer.
	print scores.items() # Print every (term, score) pair in the dictionary

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    hw()
    lines(sent_file)
    #lines(tweet_file)
    i = 0
    twitter_text = {}
    for line in tweet_file:
    	jsonline = json.loads(line)
    	#jsonline.keys()
    	twitter_text[i] = jsonline["statuses"][i]["text"]
    	i = i+1
	print twitter_text.items()
    

if __name__ == '__main__':
    main()

