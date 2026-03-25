class AutoScaler:

    def __init__(self):
        self.servers = 2

    def analyze(self, cpu):

        if cpu > 85:
            self.servers += 1
            return "Horizontal Scaling Applied"

        elif cpu > 60:
            return "Vertical Scaling Recommended"

        else:
            return "System Stable"