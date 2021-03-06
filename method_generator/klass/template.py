class Template:
    """
    represents a C++ class or method template
    """

    def __init__(self):
        self._template_types = []

    @property
    def template_types(self):
        return self._template_types

    def add_template_type(self, template_type):
        self._template_types.append(template_type)

    def __str__(self):
        """
        renders a class or method template
        :return: str
        """

        template = "template <{content}>"
        render = []

        for template_type in self._template_types:
            render.append(str(template_type))

        return template.format(content=', '.join(render))