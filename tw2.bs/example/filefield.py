import tw2.core
import tw2.forms
import tw2.devtools
import tw2.bs
import tw2.jquery
import tw2.dynforms


class Multi(tw2.dynforms.GrowingGridLayout):
    """A modified GridLayout that is centered on multifile upload"""

    def _validate(self, value, state=None):
        value = [v for v in value if not ('del.x' in v and 'del.y' in v)]
        return value

bs_file_field_js = tw2.core.JSLink(
    modname=__name__,
    filename='static/bs.js',
    resources=[tw2.jquery.jquery_js],
    location='headbottom')


class Index(tw2.forms.FormPage):
    resources = [bs_file_field_js]
    title = 'BioScript Widgets'

    class child(tw2.forms.TableForm):
        one = tw2.bs.BsFileField(validator=tw2.bs.BsFileFieldValidator(required=True))
        # two = tw2.bs.BsFileField(validator=tw2.bs.BsFileFieldValidator(required=True, extensions=['bed']))
        three = tw2.forms.TextField(validator=tw2.core.Validator(required=True))


class Triple(tw2.forms.FormPage):
    resources = [bs_file_field_js]
    title = 'BioScript Widgets'

    class child(tw2.forms.TableForm):
        one = tw2.bs.BsTripleFileField(validator=tw2.bs.BsFileFieldValidator(required=True), options=[('one', '{"p": "http://one", "d": "one"}'), ('two', '{"p": "http://two", "d": "two"}'), ('not valid', '{"p": "cdcsd", "d": "two"}')])


class Index2(tw2.forms.FormPage):
    resources = [bs_file_field_js]
    title = 'BioScript multiple widget'

    class child(tw2.forms.TableForm):
        test = tw2.bs.MultipleBsFileField()

tw2.devtools.dev_server(port=8000)
