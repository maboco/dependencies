class Package:
    def __init__(self, name, version):
        self.pack = name 
        self.version = version
        self.combine = { "package" : { "name" : name}, "version" : version }

    def get_name(self):
        return self.pack
    
    def get_version(self):
        return self.version
    
    def get_combine(self):
        return self.combine