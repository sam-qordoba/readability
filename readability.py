#!/usr/bin/env python

import math

from utils import get_char_count
from utils import get_words
from utils import get_sentences
from utils import count_syllables
from utils import count_complex_words


class Readability:
    analyzedVars = {}

    def __init__(self, text):
        self.analyze_text(text)

    def analyze_text(self, text):
        words = get_words(text)
        char_count = get_char_count(words)
        word_count = len(words)
        sentence_count = len(get_sentences(text))
        syllable_count = count_syllables(words)
        complexwords_count = count_complex_words(text)
        averageWordsPerSentence = word_count/sentence_count
        
        self.analyzedVars = {
            'words': words,
            'charCount': float(char_count),
            'wordCount': float(word_count),
            'sentenceCount': float(sentence_count),
            'syllableCount': float(syllable_count),
            'complexwordCount': float(complexwords_count),
            'averageWordsPerSentence': float(averageWordsPerSentence)
        }

    def ARI(self):
        score = 4.71 * (self.analyzedVars['charCount'] / self.analyzedVars['wordCount']) + 0.5 * (self.analyzedVars['wordCount'] / self.analyzedVars['sentenceCount']) - 21.43
        return score
        
    def FleschReadingEase(self):
        score = 0.0
        score = 206.835 - (1.015 * (self.analyzedVars['averageWordsPerSentence'])) - (84.6 * (self.analyzedVars['syllableCount']/ self.analyzedVars['wordCount']))
        return round(score, 4)
        
    def FleschKincaidGradeLevel(self):
        score = 0.39 * (self.analyzedVars['averageWordsPerSentence']) + 11.8 * (self.analyzedVars['syllableCount']/ self.analyzedVars['wordCount']) - 15.59
        return round(score, 4)
        
    def GunningFogIndex(self):
        score = 0.4 * ((self.analyzedVars['averageWordsPerSentence']) + (100 * (self.analyzedVars['complexwordCount']/self.analyzedVars['wordCount'])))
        return round(score, 4)

    def SMOGIndex(self):
        score = (math.sqrt(self.analyzedVars['complexwordCount']*(30/self.analyzedVars['sentenceCount'])) + 3)
        return score

    def ColemanLiauIndex(self):
        score = (5.89*(self.analyzedVars['charCount']/self.analyzedVars['wordCount']))-(30*(self.analyzedVars['sentenceCount']/self.analyzedVars['wordCount']))-15.8
        return round(score, 4)

    def LIX(self):
        longwords = 0.0
        for word in self.analyzedVars['words']:
            if len(word) >= 7:
                longwords += 1.0
        score = self.analyzedVars['wordCount'] / self.analyzedVars['sentenceCount'] + float(100 * longwords) / self.analyzedVars['wordCount']
        return score

    def RIX(self):
        score = 0.0
        longwords = 0.0
        for word in self.analyzedVars['words']:
            if len(word) >= 7:
                longwords += 1.0
        score = longwords / self.analyzedVars['sentenceCount']
        return score
        

if __name__ == "__main__":
    text = """We are close to wrapping up our 10 week Rails Course. This week we will cover a handful of topics commonly encountered in Rails projects. We then wrap up with part 2 of our Reddit on Rails exercise!  By now you should be hard at work on your personal projects. The students in the course just presented in front of the class with some live demos and a brief intro to to the problems their app were solving. Maybe set aside some time this week to show someone your progress, block off 5 minutes and describe what goal you are working towards, the current state of the project (is it almost done, just getting started, needs UI, etc.), and then show them a quick demo of the app. Explain what type of feedback you are looking for (conceptual, design, usability, etc.) and see what they have to say.  As we are wrapping up the course you need to be focused on learning as much as you can, but also making sure you have the tools to succeed after the class is over."""

    rd = Readability(text)
    print 'Test text:'
    print '"%s"\n' % text
    print 'ARI: ', rd.ARI()
    print 'FleschReadingEase: ', rd.FleschReadingEase()
    print 'FleschKincaidGradeLevel: ', rd.FleschKincaidGradeLevel()
    print 'GunningFogIndex: ', rd.GunningFogIndex()
    print 'SMOGIndex: ', rd.SMOGIndex()
    print 'ColemanLiauIndex: ', rd.ColemanLiauIndex()
    print 'LIX: ', rd.LIX()
    print 'RIX: ', rd.RIX()

