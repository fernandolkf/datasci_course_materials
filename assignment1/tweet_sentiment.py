import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))


def assigment(jsonline)
    for i in range(0,len(jsonline["statuses"])):
        twitter_text[i] = jsonline["statuses"][i]["text"]
        #print twitter_text[i].encode('utf-8')
        


    afinnfile = open("AFINN-111.txt")
    scores = {} # initialize an empty dictionary
    for line in afinnfile:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.


    sentment_score  = [0]*len(twitter_text)
    for i in range(0,len(twitter_text)):
        word = twitter_text[i].split(" ")
        for j in range(0,len(word)):
            if word[j] in scores:
                #print word[j]
                sentment_score[i] = sentment_score[i]+scores[word[j]]
                #sentment_score[i] = scores[word[j]]
                
    
    print("\n".join(map(str, sentment_score)))            

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    #hw()
    #lines(sent_file)
    #lines(tweet_file)
   
    twitter_text = {}

    for line in tweet_file:
        jsonline = json.loads(line)
        #jsonline.keys()

    assigment(jsonline)

    #jsonline = json.loads(tweet_file)

   
            

    

	
    

if __name__ == '__main__':
    main()

