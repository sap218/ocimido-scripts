#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 16:10:07 2019

@author: samantha
"""

from textblob import TextBlob

"""
import Standford CoreNLP output for OV or UVE and find the tags for posts
"""

drug_scores = { # using biological therapies as an example
        "adalimumab":[],
        "aflibercept":[],
        "bevacizumab":[],
        "certolizumab":[],
        "etanercept":[],
        "golimumab":[],
        "infliximab":[],
        "ranibizumab":[],
        "rituximab":[],
        "tocilizumab":[],
        "ustekinumab":[],
        }

for drug in posts: # this is the list of posts which included that tag
    for post in posts[drug]: 
        post = TextBlob(post)
        drug_scores[drug].append(post.sentiment.polarity)

