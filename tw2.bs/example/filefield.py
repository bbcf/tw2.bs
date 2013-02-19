import tw2.core
import tw2.forms
import tw2.devtools
import tw2.bs
import tw2.jquery
import tw2.dynforms


bs_file_field_js = tw2.core.JSLink(
    modname=__name__,
    filename='static/bs.js',
    resources=[tw2.jquery.jquery_js],
    location='headbottom')


class Double(tw2.forms.FormPage):
    resources = [bs_file_field_js]
    title = 'BioScript Widgets'

    class child(tw2.forms.TableForm):
        one = tw2.bs.BsFileField(validator=tw2.bs.BsFileFieldValidator(required=True))


class Triple(tw2.forms.FormPage):
    resources = [bs_file_field_js]
    title = 'BioScript Widgets'

    class child(tw2.forms.TableForm):
        one = tw2.bs.BsTripleFileField(validator=tw2.bs.BsFileFieldValidator(required=True), options=[('one', '{"p": "http://one", "d": "one"}'), ('two', '{"p": "http://two", "d": "two"}'), ('not valid', '{"p": "cdcsd", "d": "two"}')])


class Mult(tw2.forms.FormPage):
    title = 'BioScript multiple widget'
    resources = [bs_file_field_js]

    class child(tw2.forms.TableForm):
        class inputs(tw2.bs.BsMultiple):
            files = tw2.bs.BsFileField()


class Test(tw2.forms.FormPage):
    title = 'BioScript multiple widget'

    class child(tw2.forms.TableForm):
        class multi(tw2.bs.BsMultiple):
            toto = tw2.forms.TextField()


class Mult3(tw2.forms.FormPage):
    title = 'BioScript multiple widget'
    resources = [bs_file_field_js]

    class child(tw2.forms.TableForm):
        class multi(tw2.bs.BsMultiple):
            test = tw2.bs.BsTripleFileField(options=['one', 'two'])

tw2.devtools.dev_server(port=8000)
