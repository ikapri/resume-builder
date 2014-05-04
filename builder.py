__author__ = 'ishaan'

from jinja2 import Template
from templates import *


class GroupedField(object):
    """
    Represents a Section like Work Experience , which can have multiple entries of the same fields
    """
    def __init__(self, group, fields, required=False):
        """
        Args -
        group - Section under which fields will be grouped - ex:Education
        fields - Fields which combine to make a single entry in the group
        required - If specified , then atleast one entry should be present in the group
        """
        self.group = group
        self.fields = [Field(**f) for f in fields]
        self.required = required


class Field(object):
    """
    Represents a Single field in the Resume
    """
    def __init__(self, text, required=False, default=None):
        """
        Args -
        text - Name of the field
        required fields cannot be left blank
        default  - If a field is left blank and default is specified , then default value is used
        """
        self.text = text
        self.default = default
        self.required = required


class Input(object):
    def __init__(self, field):
        self.field = field

    def take_input(self):
        """
        Takes Input from the User according to field type and Field constraints
        """
        if isinstance(self.field, Field):
            return Input.single_field_input(self.field)
        elif isinstance(self.field, GroupedField):
            print '\n' + self.field.group
            data = []
            while True:
                if not self.field.required or len(data) >= 1:
                    inp = raw_input("\nDo you want to add " + self.field.group + '? (y or n)')
                    print '\n'
                    if inp in ('n', 'N'):
                        break
                field_dict = {}
                for f in self.field.fields:
                    temp = Input.single_field_input(f)
                    field_dict[f.text.lower().replace('-', '_')] = temp
                data.append(field_dict)
            return data

    @staticmethod
    def single_field_input(field):
        while True:
            temp = raw_input(field.text + '(Required: ' + str(field.required) + ')')
            if not temp and field.required:
                print "Field is required...Enter again"
                continue
            elif not temp and field.default:
                return field.default
            return temp


class Resume(object):
    def __init__(self):
        self.name = Input(Field("NAME", required=True)).take_input()
        self.dob = Input(Field("DOB", required=True)).take_input()
        self.email = Input(Field("EMAIL", required=True)).take_input()
        self.address = Input(Field("ADDRESS", required=True)).take_input()
        self.experience = Input(GroupedField('EXPERIENCE', [{'text': 'COMPANY', 'required': True},
                                                            {'text': 'TITLE', 'required': True},
                                                            {'text': 'START-DATE', 'required': True},
                                                            {'text': 'END-DATE', 'default': 'Present'},
                                                            {'text': 'DESCRIPTION'}
                                                            ])).take_input()
        self.education = Input(GroupedField('EDUCATION', [{'text': 'SCHOOL', 'required': True},
                                                          {'text': 'DEGREE', 'required': True},
                                                          {'text': 'START-DATE', 'required': True},
                                                          {'text': 'END-DATE', 'default': 'Present'},
                                                          {'text': 'DESCRIPTION'}
                                                          ], required=True)).take_input()
        self.skills = Input(Field('SKILLS')).take_input()


if __name__ == '__main__':
    r = Resume()
    name = r.name.strip()
    while True:
        opt = raw_input('EXPORT TO \n1:PLAIN TEXT\n2:CSV\n')
        if opt == '1':
            template = TXT_TEMPLATE
            ext = '.txt'
            break
        elif opt == '2':
            template = CSV_TEMPLATE
            ext = '.csv'
            break
        print "Wrong Option..Try Again"
        continue
    t = Template(template)
    file_name = name + ext
    with open('resume/' + file_name, 'w') as f:
        f.write(t.render(resume=r))
    print '\nFile saved as {name} in resume folder'.format(name=file_name)