'''
Level Manager Class
Adapted from
http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html
'''

class LevelManager():
    # Inner class
    class __LevelManager:
        def __init__(self):
            self._level_stack = []

        #Load a new level onto the stack
        def load_level(self, level):
            self._level_stack.append(level)

        #Removes a level from the stack
        def leave_level(self):
            self._level_stack.pop()

        #Peek at the top of the stack
        def get_current_level(self):
            if not self._level_stack:
                return None
            else:
                return self._level_stack[-1]

    # Instance variable
    instance = None
    def __init__(self):
        # create an object if one does not exist
        if not LevelManager.instance:
            LevelManager.instance = LevelManager.__LevelManager()

    #Pass attribute retrieval to the instance
    def __getattr__(self, name):
        return getattr(self.instance, name)

        
