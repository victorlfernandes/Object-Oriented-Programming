class Movie:

    def __init__(self):
        self.name = ''
        self.description = ''
        self.grade = -1
        self.imageLink = ''

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setDescription(self, description):
        self.description = description

    def getDescription(self):
        return self.description

    def setGrade(self, grade):
        self.grade = grade

    def getGrade(self):
        return self.grade

    def setImageLink(self, imageLink):
        self.imageLink = imageLink
    
    def getImageLink(self):
        return self.imageLink
    
    def __str__(self) -> str:
        return (self.name + ":\n" + self.grade + "\n" + self.description + "\n" + str(self.imageLink))