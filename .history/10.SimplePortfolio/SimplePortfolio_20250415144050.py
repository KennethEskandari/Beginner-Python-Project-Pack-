name = 'Kenneth Eskandari'
bio = "The Most Dedicated Business Analyst You Will Ever Meet."

projects = [
    {'title':'My First 10 projects in Python. 1000 more to go.','link':'https://github.com/KennethEskandari/Beginner-Python-Project-Pack-'}
]

#hmtl template 
html_template = """
<!DOCTYPE html>
<html>
<head>
     <title>{name}'s Portfolio</title>
    <style>
        body {{ font-family: Arial; padding: 20px; }}
        .project {{ margin-bottom: 20px; }}
        .project-title {{ font-weight: bold; }}
    </style>
</head>
<body>
    <h1>{name}</h1>
    <p>{bio}</p>
    <h2>Projects</h2>
    {projects_section}
</body>
</html>
"""

#Projects Sections 
projects_section = ""
for project in projects_section:
    projects_section += f"""
 <div class="project">
        <div class="project-title">{project['title']}</div>
        <p>{project['description']}</p>
        <a href="{project['link']}">View Project</a>
    </div>
    """

#Merge
final_html = html_template.format(name=name,bio=bio,projects_section=projects_section)

