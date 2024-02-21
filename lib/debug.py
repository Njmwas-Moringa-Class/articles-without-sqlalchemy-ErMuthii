#!/usr/bin/env python3
import ipdb

from Article import Article
from Author import Author
from Magazine import Magazine

if __name__ == '__main__':
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")
  
    magazine1 = Magazine("Science Today", "Science")
    magazine2 = Magazine("Fashion Weekly", "Fashion")
   
    article1 = author1.add_article(magazine1, "New Discoveries in Physics")
    article2 = author1.add_article(magazine2, "Latest Fashion Trends")
    article3 = author2.add_article(magazine2, "How to Dress for Success")

    print("Magazines contributed by John Doe:", [magazine.name() for magazine in author1.magazines()])
    print("Authors contributing to Fashion Weekly:", [author.name() for author in magazine2.contributing_authors()])
    print("Article titles in Fashion Weekly:", magazine2.article_titles())
    print("Topic areas for John Doe:", author1.topic_areas())
  
    found_magazine = Magazine.find_by_name("Fashion Weekly")
    print("Magazine found by name:", found_magazine.name())

    ipdb.set_trace()
