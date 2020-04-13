from abc import ABCMeta, abstractstaticmethod

class LaLiga(metaclass = ABCMeta):
    @staticmethod
    def get_stats():
        """This is the stats Interface"""

class FCAltei(LaLiga):
    def __init__(self):
        self.wins = 11
        self.losses = 4
        self.draws = 12
        self.total_points = 45
    def get_stats(self):
        return {"wins": self.wins, "losses": self.losses, "draws": self.draws, "total points": self.total_points}
    
class FCBarcelona(LaLiga):
    def __init__(self):
        self.wins = 18
        self.losses = 5
        self.draws = 4
        self.total_points = 58
    def get_stats(self):
        return {"wins": self.wins, "losses": self.losses, "draws": self.draws, "total points": self.total_points}

class FCMadrid(LaLiga):
    def __init__(self):
        self.wins = 16
        self.losses = 3
        self.draws = 8
        self.total_points = 56
    def get_stats(self):
        return {"wins": self.wins, "losses": self.losses, "draws": self.draws, "total points": self.total_points}


class SoceerFactory():
    @staticmethod
    def get_info(stats):
        try:
            if stats == 'FCAleti':
                return FCAltei()
            if stats == 'FCBarcelona':
                return FCBarcelona()
            if stats == 'FCMadrid':
                return FCMadrid()
            raise AssertionError("Chair not found")
        except AssertionError as _error:
            print(_error)
if __name__ == '__main__':
    stats = SoceerFactory.get_info("FCBarcelona")
    print(stats.get_stats())

