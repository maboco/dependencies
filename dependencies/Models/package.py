class Package:
    def __init__(self, name, version):
        self.pack = name 
        self.version = version

    def get_name(self):
        return self.pack
    
    def get_version(self):
        return self.version
    
    def get_osv_format(self):
        return { "package" : { "name" : self.pack }, "version" : self.version }
    
    def get_pack(self):
        return { "name" : self.pack, "version": self.version }