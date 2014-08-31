class Node:

    def __init__(self, name):
        self.children = {}
        self.name = name
            
    def get_child_names(self):
        return [value.name for key, value in self.children.items()]

    def get_children(self):
        return [value for key, value in self.children.items()]

    def add_child(self, name):
        if self.child_exists(name):
            return self.children[name]
        else:
            self.children[name] = Node(name)
            return self.children[name]

    def child_exists(self, name):
        try:
            if self.children[name]:
                return self.children[name]
            else:
                return None
        except:
            return None
    
