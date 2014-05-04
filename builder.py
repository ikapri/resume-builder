__author__ = 'ishaan'

from jinja2 import Template
from templates import *


class GroupedField(object):
    def __init__(self, group, fields, required=False):
        self.group = group
        self.fields = [Field(**f) for f in fields]
        self.required = required


class Field(object):
    def __init__(self, text, required=False, default=None):
        self.text = text
        self.default = default
        self.required = required


class Input(object):
    def __init__(self, field):
        self.field = field

    def take_input(self):
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


r = Resume()
t = Template(TXT_TEMPLATE)
with open('cv.txt', 'w') as f:
    f.write(t.render(resume=r))