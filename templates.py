__author__ = 'ishaan'

TXT_TEMPLATE = '''\t\t\t\t{{name}}\n{% if dob %}DOB : {{dob}}\n{% endif %}{% if address %}ADDRESS : {{address}}\n{% endif %}{% if email %}EMAIL : {{email}}\
\n{% endif %}{% if education %}\t\t\t\tEDUCATION\n{% for e in education %}{{e.school}}\n{{e.degree}}\n{{e.start_date}}-\
{{e.end_date}}\n{% if e.description %}{{e.description}}\n{% endif %}\n{%endfor%}{% endif %}{% if experience %}EXPERIENCE\
{% for e in experience %}{{e.company}}\n{{e.title}}\n{{e.start_date}}-{{e.end_date}}\n{% if e.description %}\
{{e.description}}\n{% endif %}\n{%endfor%}{% endif %}
'''