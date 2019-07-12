#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 19:24:27 2019

@author: erikakimi
"""

import os
os.getcwd()
os.listdir()


# read a file as text and returns a looong string
def read_text(file_name):
    content = ""
    with open(file_name, encoding='utf-8') as f:
        content = f.read().replace('\n', ' ')
    return content


# remove punctuation, split the string into words and returns a list
def split_into_words(content):
    words = content.split(' ')
    return words

# word frequency table
def create_word_frequency_table(words, size = 10):
    words_dict = {}
    # make the frequency table
    total_words = len(words)
    for word in words:
        word = word.lower()
        word = word.strip('|©!@#$%^&*()-_=+,.;:?/<>''[]')
        if word.strip() == '':
            continue
        if word in words_dict:
            words_dict[word] += 1.0 / total_words
        else:
            words_dict[word] = 1.0 / total_words
    # return the top 10 most frequent words
    pair_list = sorted(words_dict.items(), key=lambda kv: kv[1], reverse=True)
    #print(pair_list[:100])
    most_frequent = dict(pair_list[:size])
    return most_frequent

# find the most frequent words
def find_most_frequent_words(file_name, size = 10):
    text = read_text(file_name)
    #print(text)
    words = split_into_words(text)
    #print(words)
    most_freq = create_word_frequency_table(words, size)
    #print(most_freq)
    return most_freq

# calculates distance between two dictionaries
def calculate_distance(known_dict, unknown_dict):
    distance = 0
    for known_word in known_dict.keys():
        #if known_word in unknown_dict:
            #known_freq = known_dict.get(known_word)
           # unknown_freq = unknown_dict.get(known_word)
            #distance += abs(known_freq - unknown_freq)
        if not known_word in unknown_dict:
            distance += 1
    return distance
    

##### main #######
number_of_words = 10

most_freq_english = find_most_frequent_words('eaton-boy-scouts_EN.txt', number_of_words)
#print(most_freq_english)

most_freq_finnish = find_most_frequent_words('pg50537.txt', number_of_words)
#print(most_freq_finnish)

most_freq_french = find_most_frequent_words('pg12566.txt', number_of_words)
#print(most_freq_french)

most_freq_german = find_most_frequent_words('schloemp-tolle-koffer_DE.txt', number_of_words)
#print(most_freq_german)

most_freq_spanish = find_most_frequent_words('cherbonnel-mi-tio_SP.txt', number_of_words)
#print(most_freq_spanish)

most_freq_unknown = find_most_frequent_words('unknown-lang.txt', number_of_words)
#print(most_freq_unknown)

distance_english = calculate_distance(most_freq_english, most_freq_unknown)
#print(distance_english)

distance_finnish = calculate_distance(most_freq_finnish, most_freq_unknown)
#print(distance_finnish)

distance_french = calculate_distance(most_freq_french, most_freq_unknown)
#print(distance_french)

distance_german = calculate_distance(most_freq_german, most_freq_unknown)
#print(distance_german)

distance_spanish = calculate_distance(most_freq_spanish, most_freq_unknown)
#print(distance_spanish)


language_distance = {'english' : distance_english,
                     'finnish': distance_finnish,
                     'french' : distance_french,
                     'german': distance_german,
                     'spanish': distance_spanish, }
print("Distance: ", language_distance)

language_distance_sorted = sorted(language_distance.items(), key=lambda kv: kv[1])
print("The unknown text is ", language_distance_sorted[0])