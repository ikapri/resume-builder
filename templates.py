__author__ = 'ishaan'

TXT_TEMPLATE = '''\t\t\t\t{{name}}\n{% if dob or address or email %}\t\t\t\tPersonal\n{%endif%}{% if dob %}DOB : \
{{dob}}\n{% endif %}{% if address %}ADDRESS : {{address}}\n{% endif %}{% if email %}EMAIL : {{email}}\
\n{% endif %}{% if education %}\t\t\t\tEDUCATION\n{% for e in education %}{{e.school}}\n{{e.degree}}\n{{e.start_date}}-\
{{e.end_date}}\n{% if e.description %}{{e.description}}\n{% endif %}\n{%endfor%}{% endif %}{% if experience %}\t\t\t\t\
EXPERIENCE\n{% for e in experience %}{{e.company}}\n{{e.title}}\n{{e.start_date}}-{{e.end_date}}\n{%if e.description%}\
{{e.description}}\n{% endif %}\n{%endfor%}{% endif %}{% if skills %}\t\t\t\t\SKILLS\n{% for s in skills%}{{s.name}}\n\
{% endif %}\n{%endfor%}{% endif %}
'''