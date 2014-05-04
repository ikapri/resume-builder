__author__ = 'ishaan'

TXT_TEMPLATE = '''\t\t\t\t{{resume.name}}\n{% if resume.dob %}DOB : {{resume.dob}}\n{% endif %}\
{% if resume.address %}ADDRESS : {{resume.address}}\n{% endif %}{% if resume.email %}EMAIL :\
{{resume.email}}\n{% endif %}{% if resume.education %}\t\t\t\tEDUCATION\n{% for e in resume.education %}\
{{e.school}}\n{{e.degree}}\n{{e.start_date}}-{{e.end_date}}\n{% if e.description %}{{e.description}}\n{% endif %}\n\
{%endfor%}{% endif %}{% if resume.experience %}\t\t\t\tEXPERIENCE\n{% for e in resume.experience %}{{e.company}}\n\
{{e.title}}\n{{e.start_date}}-{{e.end_date}}\n{%if e.description%}{{e.description}}\n{% endif %}\n{%endfor%}\
{% endif %}{% if resume.skills %}\t\t\t\tSKILLS\n{{resume.skills}}\n{% endif %}
'''

CSV_TEMPLATE = '''NAME,{{resume.name}}\n{% if resume.dob %}DOB,{{resume.dob}}\n{% endif %}\
{% if resume.address %}ADDRESS,{{resume.address}}\n{% endif %}{% if resume.email %}EMAIL,\
{{resume.email}}\n{% endif %}{% if resume.education %}EDUCATION{% for e in resume.education %},\
"{{e.school}}\n{{e.degree}}\n{{e.start_date}}-{{e.end_date}}\n{% if e.description %}{{e.description}}{% endif %}"\n\
{%endfor%}{% endif %}{% if resume.experience %}EXPERIENCE{% for e in resume.experience %},"{{e.company}}\n\
{{e.title}}\n{{e.start_date}}-{{e.end_date}}\n{%if e.description%}{{e.description}}{% endif %}"\n{%endfor%}\
{% endif %}{% if resume.skills %}SKILLS,"{{resume.skills}}"{% endif %}'''