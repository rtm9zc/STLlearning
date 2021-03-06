

#Class to store and track robustness values
class Trajectory():
    def __init__(self, trajectories, time, variables, paramDict, values=[]):
        self.trajectories = trajectories #trajectories comparing against from training sets
        self.time = time  #total time list
        self.variables = variables #list of variables
        self.paramDict = paramDict
        self.values = values #track robustness for each variable