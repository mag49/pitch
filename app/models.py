from . import db
class USER:
    user = []
    def __init__(self,title,pitch):
        self.title = title
        self.pitch = pitch
    def user(self):
        USER.all_user.append(self)


class PICKUPLINES:
    all_pickuplines = []
    def __init__(self,title,pitch):
        self.title = title
        self.pitch = pitch

    def save_pickupline(self):
        PICKUPLINES.all_pickuplines.append(self)

    @classmethod
    def clear_pitchs(cls):
        PICKUPLINES.all_pickuplines.clear()
    @classmethod
    def get_pitchs(cls):
        response = []
        for pitchs in cls.all_pickuplines:
            response.append(pitchs)
        return response

class INTERVIEW:
    all_interview = []
    def __init__(self,title,pitch):
        self.title = title
        self.pitch = pitch
    def save_interview(self):
        INTERVIEW.all_interview.append(self)

class BUSINESSPLAN:
    all_businessplan = []
    def __init__(self,title,pitch):
        self.title = title
        self.pitch = pitch
    def save_businessplan(self):
        BUSINESSPLAN.all_businessplan.append(self)


class PITCH():
    all_pitch = []
    def __init__(self,title,pitch):
        self.title = title
        self.pitch = pitch
    def save_businessplan(self):
        PITCH.pitch.append(self)

