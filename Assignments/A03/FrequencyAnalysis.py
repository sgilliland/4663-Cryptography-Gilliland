# I used this code, provided by Dr. Griffin, and added the graph of Typical Frequency Distribution to give the matches of letter frequency
import sys
import os
import requests

alphabet = [chr(x+97) for x in range(26)]

class Frequency():
    def __init__(self):
        self.text = ""
        self.freq = {}
        self.sort_freq = None

        for l in alphabet:
            self.freq[l] = 0
    
    def count(self,text):
        for l in text:
            l = l.lower()
            if l in alphabet:
                self.freq[l] += 1

        # https://realpython.com/python-lambda/
        self.sort_freq = sorted(self.freq.items(), key=lambda x: x[1], reverse=True)

    def print(self, graph):
        i = 0
        if self.sort_freq:
            for f in self.sort_freq:
                print(f"{f[0]} " + graph[i])
                i = i + 1
        else:
            print(self.freq)
    
if __name__=='__main__':

    # for first encryption assignment
    f = open("in1.txt","r")
    
    # for second encryption assignment
    # f = open("in2.txt", "r")
    
    if f.mode == "r":
      text = f.read()
    # data set with the alphabet in order of Typical Frequency Distribution
    graph = ['e','t','a','o','i','n','s','r','h','d','l','u','c','m','f','y','w','g','p','b','v','k','x','q','j','z']

    print("Calculating frequency...")
    
    F = Frequency()

    F.count(text)
    
    F.print(graph)
