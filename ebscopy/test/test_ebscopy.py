#!/usr/bin/python

from ebscopy import ebscopy
#import pprint

connection	= ebscopy.Connection()
connection.connect()
results = connection.search("blue")
print "---------------"
print "Search Results"
print "---------------"
results.pretty_print()
print "---------------"
print "Total Hits:"
print results.stat_total_hits
print "---------------"
print "Available Facets:"
print results.avail_facets_labels
print "---------------"
print 
connection.disconnect()


