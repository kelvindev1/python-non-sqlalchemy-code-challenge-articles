# import ipdb

class Article:
    # initialize a empty list to store all instances.
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title

        # we append the new Article object(self) to all list 
        Article.all.append(self)

    @property
    def title (self):
        return self._title
    
    @title.setter
    def title(self, new_title):
        if hasattr(self, "title"):
#  if the above condition is true then title cannot be changed.
            AttributeError ("Title cannot be changed")
        else:
            if isinstance(new_title, str):
                if 5 <= len(new_title) <= 50:
                    #  if this condition is met we set title to new_title
                    self._title = new_title
                else:
                    # If the length of new_title is not between 5 and 50 characters we raise the error.
                    ValueError("Title must be between 5 and 50 characters")
            else:
                TypeError("Title must be a string")
            
    @property
    def author (self):
        return self._author
    
    @author.setter
    def author (self, new_author):
        # check if new_author is an instance of of the Author class
        if isinstance(new_author, Author):
            self._author = new_author
        else:
            # if new_author isn't an instance of the Author raise a error.
            TypeError("Author must be an instance of Author")
        
    @property
    def magazine (self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, new_magazine):
        # check if new_magazine is an instance of the magazine
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine
        else:
            # if not an instance error
            TypeError("Magazine must be an instance of Magazine")



class Author:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name (self, new_name):
        # check if the Author object has a name attribute set
        if hasattr(self, "name"):
            AttributeError("Name cannot be changed")
        
        # if Author object doesn't have a name attribute set
        else:
            if isinstance(new_name, str):
                # check if it has atleast one character
                if len(new_name):
                    self._name = new_name
                else:
                    # throw an error if the it's zero.
                    ValueError("Name must be longer than 0 characters")
            else:
                # throw an error if new_name isn't a string.
                TypeError("Name must be a string")

    # articles method to return list of all articles authored by Author.
    def articles(self):
        # list comprehension
        # filter Article.all and check if author attribute of each article matches current Author object.
        return [article for article in Article.all if self == article.author]
    
    # magazines method to return list of unique magazines where the Author has published the articles.
    # set comprehension
    def magazines(self):
        # convert the set of unique magazines to a list and returns it.
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        # create and return the new Article object
        return Article(self, magazine, title)

    # return unique categories across all magazines where Author has published articles.
    # set comprehension to eliminate duplicates.
    def topic_areas(self):
        topic_areas = list({magazine.category for magazine in self.magazines()})
        if topic_areas:
            return topic_areas
        else:
            return None



class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        # check if new name is a string
        if isinstance(new_name, str):
            # ipdb.set_trace()
            if 2 <= len(new_name) <= 16:
                self._name = new_name
            else: 
                ValueError("Name must be between 2 and 16 characters")
        else:
            TypeError("Name must be a string")   
        
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, new_category):
        # check if it's a string
        if isinstance(new_category, str):
            # check if not empty
            if len(new_category):
                self._category = new_category
            else:
                # error if empty
                ValueError("Category must be longer than 0 characters")
        else:
            # error if not a string.
            TypeError("Category must be a string")   

    # method should return list of all articles published in Magazine object
    def articles(self):
        # list comprehenison to filter Article.all based on whether magazine attribute of each article matches the current magazine object
        return [article for article in Article.all if self == article.magazine]

    # method to return list of unique authors who have contributed to the magazine.
    # set comprehension to remove duplicates
    def contributors(self):
        # convert the set of unique authors to a list and returns it.
        return list({article.author for article in self.articles()})

    # method to return list of titles of all articles published in this magazine.
    # list comprehension to collect the titles
    def article_titles(self):
        article_titles = [magazine.title for magazine in self.articles()]
        # check if article_titles list is not empty.
        if article_titles:
            return article_titles
        else:
            # when empty 
            return None

    # method to identify authors who have contributed more than once to the magazine.
    def contributing_authors(self):
        # initialize dictionary and list to track authors and their contributions.
        authors = {}
        list_of_authors = []
        # iterate over all articles published in this magazine.
        for article in self.articles():
            # check if the author of the current article is already in the authors dictionary.
            if article.author in authors:
                # increment in authors dictionary if author found.
                authors[article.author] += 1
            else:
                # author not found
                authors[article.author] = 1  
        
        # loop to iterate over all authors tracked in the authors dictionary.
        for author in authors:
            # check if the author has contributed more than once.
            if authors[author] >= 2:
                # add author to list_of_authors if contributed => 2
                list_of_authors.append(author) 
                  
            # check if list_of_authors not empty
        if (list_of_authors):
            return list_of_authors
        else:
            return None
        


    """
    The code defines three classes (Article, Author, Magazine)
    Each class should use properties to manage how its attributes are accessed and modified.
    
    In Article class we have author, magazine, title as attributes

    In Author class we have name as attribute

    In Magazine class we have name and category as attributes

    """
