class Bs4Gen:
    def __init__(self, OPTIONS):
        self.options = OPTIONS

    def type_text(self):
        """return a full text widget"""

        # check if label is required. if so, generate a label
        if self.options['label']:
            label = self.label()

        size = self.size()


    def size(self):
        """return the class for input size"""
        if not self.options['size']:
            return ''
        else:
            return 'form-control-{}'.format(self.options['size'])

    def label(self):
        """return a label"""
        return '<label for="{id}">{label}</label>\n'.format(
            id=self.options['id'],
            label=self.options['label']
        )

    #def placeholder(self):
    #    if self.options['placeholder'] !=

        #<div class ="form-group">
        #<label for="formGroupExampleInput"> Example label </label>
        #<input type = "text" class ="form-control" id="formGroupExampleInput" placeholder="Example input">
        #</div>