import tw2.core as twc
import tw2.forms as twf


class BsFileField(twf.InputField):
    template = "tw2.bs.templates.bs"
    type = 'file'
    # declare static resources here
    # you can remove either or both of these, if not needed
    resources = [
        twc.JSLink(modname=__name__, filename='static/bs.js'),
    ]

    @classmethod
    def post_define(cls):
        print "post define : %s" % cls
        # put custom initialisation code here

    def prepare(self):
        super(BsFileField, self).prepare()
        # put code here to run just before the widget is displayed
        print "prepare"
        #self.attrs['name'] = 'bloudiblou'
        self.safe_modify('resources')
        self.add_call(twc.js_function('bs_hide_fields')(self.compound_id))

    def _validate(self, value, state=None):
        print "validate : %s, %s" % (value, state)
        super(BsFileField, self)._validate(value, state)
