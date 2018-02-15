class BaseballPlayer(object):
    def __init__(self, first_name, last_name, team, position):
        self.first_name = first_name
        self.last_name = last_name
        self.team = team
        self.position = position
        self.hits = 0
        self.at_bats = 0

    def record_atbat(self, hit_or_not):
        if hit_or_not:
            self.hits += 1
        self.at_bats += 1

    def batting_average(self):
        try:
            return self.hits/self.at_bats
        except ZeroDivisionError:
            return None

    def __eq__(self, other):
        return self.batting_average() == other.batting_average() \
               and self.last_name == other.last_name \
               and self.first_name == other.first_name

    def __gt__(self, other):
        if self.batting_average() == other.batting_average():
            if self.last_name == other.last_name:
                return self.first_name > other.first_name
            return self.last_name > other.last_name
        return self.batting_average() > other.batting_average()

    def __ge__(self, other):
        if self.batting_average() == other.batting_average():
            if self.last_name == other.last_name:
                return self.first_name >= other.first_name
            return self.last_name >= other.last_name
        return self.batting_average() >= other.batting_average()
    # __lt__, __le__, and __ne__ are not implemented
        # because of the existence of the methods above made them unnecessary.
