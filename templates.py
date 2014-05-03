__author__ = 'ishaan'

TXT_TEMPLATE = '''\t\t\t\t{{resume.name}}\n{%if resume.personal.dob or resume.personal.address or resume.personal.email%}\
\t\t\t\tPersonal\n{%endif%}{% if resume.personal.dob %}DOB : {{resume.personal.dob}}\n{% endif %}\
{% if resume.personal.address %}ADDRESS : {{resume.personal.address}}\n{% endif %}{% if resume.personal.email %}EMAIL :\
 {{resume.personal.email}}\n{% endif %}{% if resume.education %}\t\t\t\tEDUCATION\n{% for e in resume.education %}\
 {{e.school}}\n{{e.degree}}\n{{e.start_date}}-{{e.end_date}}\n{% if e.description %}{{e.description}}\n{% endif %}\n\
 {%endfor%}{% endif %}{% if resume.experience %}\t\t\t\tEXPERIENCE\n{% for e in resume.experience %}{{e.company}}\n\
 {{e.title}}\n{{e.start_date}}-{{e.end_date}}\n{%if e.description%}{{e.description}}\n{% endif %}\n{%endfor%}\
 {% endif %}{% if resume.skills %}\t\t\t\tSKILLS\n{% for s in resume.skills%}{{s.name}}\n{%endfor%}{% endif %}
'''