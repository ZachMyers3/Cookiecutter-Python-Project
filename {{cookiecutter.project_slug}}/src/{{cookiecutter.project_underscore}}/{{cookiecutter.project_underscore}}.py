{%- if cookiecutter.add_sqlalchemy_dependencies == 'y' %}
import models
{%- endif %}

def {{ cookiecutter.project_underscore }}():
    print("Hello world")

if __name__ == "__main__":
    {{ cookiecutter.project_underscore }}()
