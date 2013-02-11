import tw2.core as twc


class Bs(twc.Widget):
    template = "genshi:tw2.bs.templates.bs"

    # declare static resources here
    # you can remove either or both of these, if not needed
    resources = [
        twc.JSLink(modname=__name__, filename='static/bs.js'),
        twc.CSSLink(modname=__name__, filename='static/bs.css'),
    ]

    @classmethod
    def post_define(cls):
        pass
        # put custom initialisation code here

    def prepare(self):
        super(Bs, self).prepare()
        # put code here to run just before the widget is displayed
