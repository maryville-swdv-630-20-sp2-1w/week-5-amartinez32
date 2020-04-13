class TvShow(object):
    def tv_show_review(self):
        
        self.favorite = Favorite()
        self.favorite.favorite_show()
        
        self.average = Average()
        self.average.average_show()
        
        self.least = Least()
        self.least.least_favorite_show()
        
class Favorite(object):
    
    def favorite_show(self):
        print("The Wire is my favorite show.")

class Average(object):
    
    def average_show(self):
        print("Homeland is an average show at best.")

class Least(object):
    
    def least_favorite_show(self):
        print("Insecure is my least favorite show.")
        
shows = TvShow()
shows.tv_show_review()
