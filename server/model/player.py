class Player:
    nickname = ""
    score = 0
    player_socket = None
    is_ready = False
    
    def __init__(self):
        self.player_socket = None
        self.nickname = ""
        self.score = 0
        self.is_ready = False
    
    def ready_up(self, nickname):
        self.nickname = nickname
        self.is_ready = True
    
    def increment_score(self):
        self.score += 1

    def get_score(self):
        return self.score

    def get_name(self):
        return self.nickname