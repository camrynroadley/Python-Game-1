
class File():
    ''' This class will create, open and read from a file'''
    def __init__(self, file_name):
        ''' Constructor function'''
        self.file_name = file_name
        
    def read_file(self):
        '''
        Open and read from a text file
        Return a list of all the values in file
        '''
        self.file = open(self.file_name, 'r')

        # Get list of lines in file
        self.lines = self.file.readlines()
        self.number_of_lines = len(self.lines)
        self.file_list = list()
        
        # Separate values from each line and store in file_list
        for line in range(self.number_of_lines):
            self.temp_list = self.lines[line].split(',')
            self.file_list.extend(self.temp_list)

        # Return list of all values in file
        return self.file_list

    def get_item_name(self, key):
        '''
        Return the item name of the object key passed in
        '''
        self.file_list = self.read_file()

        # Loop through all values in file to search for key
        for item in self.file_list:
            if item == key:
                next_item = self.file_list[self.file_list.index(item) + 1]
                return next_item

    def get_points(self, key):
        '''
        Return the points related with the object key passed in
        '''
        self.file_list = self.read_file()

        # Loop through all values in file to search for key
        for item in self.file_list:
            if item == key:
                next_item = self.file_list[self.file_list.index(item) + 2]
                return int(next_item)
