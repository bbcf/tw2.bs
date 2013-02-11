import tw2.core as twc
import tw2.forms as twf


class BsFileField(twf.TextField):
    #template = "genshi:tw2.bs.templates.bs"
    template = "tw2.forms.templates.input_field"

    # declare static resources here
    # you can remove either or both of these, if not needed
    resources = [
        twc.JSLink(modname=__name__, filename='static/bs.js'),
        twc.CSSLink(modname=__name__, filename='static/bs.css'),
    ]

    @classmethod
    def post_define(cls):
        print "post define : %s" % cls
        # put custom initialisation code here

    def prepare(self):
        super(BsFileField, self).prepare()
        # put code here to run just before the widget is displayed
        print "prepare"

    def _validate(self, value, state=None):
        super(BsFileField, self)._validate(value, state)
        print "validate : %s, %s" % (value, state)
