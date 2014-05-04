__author__ = 'ishaan'

TXT_TEMPLATE = '''\t\t\t\t{{resume.name}}\n{% if resume.dob %}DOB : {{resume.dob}}\n{% endif %}\
{% if resume.address %}ADDRESS : {{resume.address}}\n{% endif %}{% if resume.email %}EMAIL :\
{{resume.email}}\n{% endif %}{% if resume.education %}\t\t\t\tEDUCATION{% for e in resume.education %}\n\
SCHOOL : {{e.school}}\nDEGREE : {{e.degree}}\nTIME : {{e.start_date}}-{{e.end_date}}\n{% if e.description %}DESCRIPTION\
 : {{e.description}}\n{% endif %}\n{%endfor%}{% endif %}{% if resume.experience %}\t\t\t\tEXPERIENCE\
 {% for e in resume.experience %}\nCOMPANY : {{e.company}}\nTITLE : {{e.title}}\nTIME : {{e.start_date}}-{{e.end_date}}\
 \n{%if e.description%}DESCRIPTION : {{e.description}}\n{% endif %}\n{%endfor%}{% endif %}{% if resume.skills %}\t\t\t\
 \tSKILLS\n{{resume.skills}}\n{% endif %}
'''

CSV_TEMPLATE = '''NAME,"{{resume.name}}"\n{% if resume.dob %}DOB,"{{resume.dob}}"\n{% endif %}\
{% if resume.address %}ADDRESS,"{{resume.address}}"\n{% endif %}{% if resume.email %}EMAIL,\
"{{resume.email}}"\n{% endif %}{% if resume.education %}EDUCATION{% for e in resume.education %},\
"SCHOOL : {{e.school}}\nDEGREE : {{e.degree}}\nTIME : {{e.start_date}}-{{e.end_date}}\n{% if e.description %}\
DESCRIPTION : {{e.description}}{% endif %}"\n{%endfor%}{% endif %}{% if resume.experience %}EXPERIENCE\
{% for e in resume.experience %},"COMPANY : {{e.company}}\nTITLE : {{e.title}}\nTIME : {{e.start_date}}-{{e.end_date}}\
\n{%if e.description%}DESCRIPTION : {{e.description}}{% endif %}"\n{%endfor%}{% endif %}{% if resume.skills %}SKILLS,\
"{{resume.skills}}"{% endif %}'''