import tw2.core
import tw2.forms
import tw2.devtools
import tw2.bs
import tw2.jquery
import tw2.dynforms

import tw2.bs.widgets
tw2.bs.widgets.DEBUG = True

class Index(tw2.forms.FormPage):
    title = 'test'

    class child(tw2.forms.TableForm):
        class child(tw2.dynforms.HidingTableLayout):
            input_type = tw2.dynforms.HidingRadioButtonList(label='',
                options=('File upload', 'Url'),
                mapping={'File upload': ['fupload'], 'Url': ['url']})
            fupload = tw2.bs.BsFileField(validator=tw2.bs.BsFileFieldValidator(required=True), help_text="this is an help text.")
            url = tw2.forms.TextField()

        submit = tw2.forms.SubmitButton(id="submit", value="submit")


class Index2(tw2.forms.FormPage):
    title = 'test'

    class child(tw2.forms.TableForm):
        class child(tw2.dynforms.HidingTableLayout):
            input_type = tw2.dynforms.HidingRadioButtonList(label='',
                options=('File upload', 'Url'),
                mapping={'File upload': ['inputs'], 'Url': ['url']})
            class inputs(tw2.bs.BsMultiple):
                files = tw2.bs.BsFileField(validator=tw2.bs.BsFileFieldValidator(required=True))
            url = tw2.forms.TextField()

        submit = tw2.forms.SubmitButton(id="submit", value="submit")


class Double(tw2.forms.FormPage):
    title = 'BioScript Widgets'

    class child(tw2.forms.TableForm):
        one = tw2.bs.BsFileField(validator=tw2.bs.BsFileFieldValidator(required=True), help_text='hello help text.')


class Triple(tw2.forms.FormPage):
    title = 'BioScript Widgets'

    class child(tw2.forms.TableForm):
        one = tw2.bs.BsTripleFileField(validator=tw2.bs.BsFileFieldValidator(required=True),
            options=[('one', '{"p": "http://one", "d": "one"}'),
            ('two', '{"p": "http://two", "d": "two"}'),
            ('not valid', '{"p": "cdcsd", "d": "two"}')],
            help_text='hello help text.')


class Mult(tw2.forms.FormPage):
    title = 'BioScript multiple widget'

    class child(tw2.forms.TableForm):
        class inputs(tw2.bs.BsMultiple):
            files = tw2.bs.BsFileField(validator=tw2.bs.BsFileFieldValidator(required=False))


class Test(tw2.forms.FormPage):
    title = 'BioScript multiple widget'

    class child(tw2.forms.TableForm):
        class child(tw2.dynforms.GrowingGridLayout):
            toto = tw2.forms.TextField(validator=tw2.core.Validator(required=True))


class Mult3(tw2.forms.FormPage):
    title = 'BioScript multiple widget'

    class child(tw2.forms.TableForm):
        class multi(tw2.bs.BsMultiple):
            test = tw2.bs.BsTripleFileField(options=['one', 'two'])

tw2.devtools.dev_server(port=8000)
