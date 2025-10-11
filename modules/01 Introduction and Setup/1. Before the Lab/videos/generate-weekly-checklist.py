import os
import jinja2
import yaml

# Template file name
template_file = "weekly_checklist_template.qmd"

# Output folder
output_folder = "generated_checklists"
os.makedirs(output_folder, exist_ok=True)

# Load weekly data from YAML
with open("weeks_data.yaml", "r") as file:
    week_data = yaml.safe_load(file)["weeks"]

# Load template
with open(template_file, "r") as file:
    template_content = file.read()

# Create Jinja2 template
template = jinja2.Template(template_content)

# Generate checklists
for week in week_data:
    output_file = os.path.join(output_folder, f"week_{week['week_number']}_checklist.qmd")
    with open(output_file, "w") as file:
        file.write(template.render(
            week_number=week["week_number"],
            week_topic=week["week_topic"],
            estimated_time=week["estimated_time"],
            week_objective=week["week_objective"],
            why_important=week["why_important"],
            before_lab=week.get("before_lab", []),
            lab_activities=week.get("lab_activities", []),
            extension=week.get("extension", []),
            reflection=week.get("reflection", {}),
            next_week=week.get("next_week", {})
        ))
    print(f"Generated: {output_file}")

print("✅ Weekly checklists generated successfully!")
