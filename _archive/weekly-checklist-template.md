---
title: "Week {{week_number}}: Student Checklist – {{week_topic}}"
format:
    html: default
    pdf: default
    docx: default
---

# 🚀 Week {{week_number}}: {{week_topic}}

---

## ✅ Before the Lab  
**⏳ Estimated Time: {{estimated_time}} minutes**

{% for module in before_lab %}
### 📌 {{ module.title }}
- **Type:** {{ module.type }}
- 🔹 [Resource]({{ module.link }})
{% if module.prompt %}- 🤔 *{{ module.prompt }}*{% endif %}
{% endfor %}

---

## 💻 In-Lab Activities (Guided by Tutor)  
**⏳ Estimated Time: {{lab_duration}} minutes**  

{% for activity in lab_activities %}
### ✅ {{ activity.title }}  
- 🔹 {{ activity.description }}  
- 🔹 [Activity Link]({{ activity.link }})
{% endfor %}

---

{% if extension %}
## 🚀 Extension (For Advanced Learners)  
{% for ext in extension %}
### 🔹 {{ ext.title }}
- **Description:** {{ ext.description }}
- 🔗 [Extension Activity]({{ ext.link }})
{% endfor %}
{% endif %}

---

## 📌 After-Class Reflection (Exit Ticket)  
📝 **Type:** {{ reflection.type }}
- **Title:** {{ reflection.title }}
- 🔗 [Submit Here]({{ reflection.link }})

---

## 💡 Looking Ahead to Next Week  
✅ **Next Week’s Topic:** {{ next_week.topic }}  
✅ **Key Skills to Focus On:** {{ next_week.skills }}  

### 📖 Recommended Readings:
{% for reading in next_week.readings %}
- 🔹 [{{ reading.title }}]({{ reading.link }})
{% endfor %}

### 🎯 Additional Practice:
{% for practice in next_week.additional_practice %}
- 🔹 [{{ practice.title }}]({{ practice.link }})
{% endfor %}
