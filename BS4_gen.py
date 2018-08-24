class BS4Gen:

    def __init__(self, OPTIONS):
        self.options = OPTIONS
        self.output = ''

        # strip whitespace for all options
        for key, val in self.options.items():
            self.options[key] = val.strip()

        if self.options['type'] == 'text':  # for text input type
            self.type_text()
        elif self.options['btn-type']:  # for button types
            self.type_button()

        return

    def type_button(self):
        """return a button"""


    def type_text(self):
        """return a full text widget"""

        widget = '<input type="{text_type}" class="form-control{size}" id="{id}" {placeholder}>'.format(
            size=' {}'.format(self.return_size_class('form-control-')) if not self.options['size'] == 'regular' else '',
            text_type=self.options['text-type'],
            placeholder=self.return_placeholder() if self.options['placeholder'] else '',
            id=self.options['id']
        )
        self.output = self.format_html(
            [
                self.label() if self.options['label'] else None,  # return label element
                widget,  # pass in widget
                self.return_small_hint() if self.options['small-hint'] else None,  # return small hint element
             ])
        return

    def get_widget(self):
        """return complete widget"""
        return self.output

    @staticmethod
    def format_html(element_list):
        """finalize widget for final output"""
        elements = ''

        for e in element_list:
            if not e:
                pass
            else:
                elements = elements + '  {ele}\n'.format(ele=e.strip())

        return '<div class ="form-group">\n{ele}</div>\n'.format(ele=elements)

    def return_size_class(self, class_prefix):
        """return the class for input size"""
        if self.options['size'] == 'regular':
            return ''
        elif self.options['size'] == 'large':
            tmp = 'lg'
        elif self.options['size'] == 'small':
            tmp = 'sm'
        return '{pref}{size}'.format(pref=class_prefix, size=tmp)

    def return_small_hint(self):
        """create small hint html"""
        if self.options['small-hint']:
            return '<small id="{id}Help" class="form-text text-muted">{small_hint}</small>'.format(
                small_hint=self.options['small-hint'],
                id=self.options['id']
            )
        return None

    def return_placeholder(self):
        """return placeholder tag"""
        if self.options['placeholder']:
            return 'placeholder="{placeholder}"'.format(placeholder=self.options['placeholder'])
        else:
            return ''

    def label(self):
        """return a label"""
        return '<label for="{id}">{label}</label>\n'.format(
            id=self.options['id'],
            label=self.options['label']
        )