import os

class Template:
    """Generate string from template"""

    def __init__(self, template):
        cur_dir = os.path.dirname(os.path.realpath(__file__))
        self.template = cur_dir + '/' + template
        self.vars = []

    def addVar(self, variable_name, value):
        self.vars.append({
            'name': variable_name.upper(),
            'value': value
        })

    def build(self):
        f = open(self.template, 'r')
        raw = f.read()
        f.close()

        res = raw
        for var in self.vars:
            res = res.replace('#{' + var['name'] +'}', var['value'])

        return res
