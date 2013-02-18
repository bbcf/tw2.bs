import tw2.core as twc
import tw2.forms as twf
import tw2.dynforms as twd
import re
import cgi
import os
try:
    import simplejson as json
except ImportError:
    import json


class BsFileFieldValidator(twc.Validator):
    """
    Validate the file field if there is one or validate the url.
    """

    regex = re.compile('^https?://', re.IGNORECASE)
    extensions = None

    def to_python(self, value, state=None):
        """Convert an external value to Python and validate it."""
        if self._is_empty(value):
            if self.required:
                raise twc.ValidationError('required', self)
            return None
        if self.strip and isinstance(value, basestring):
            value = value.strip()
        self._validate_python(value, state)
        return value

    @staticmethod
    def _is_empty(value):
        """Check whether the given value should be considered "empty"."""
        return value is None or value == '' or (
            isinstance(value, (list, tuple, dict)) and not value)

    def _validate_python(self, value, state=None):
        if isinstance(value, basestring):
            try:
                value = json.loads(value)
                value = value['p']
            except:
                pass
            if not self.regex.search(value):
                raise twc.ValidationError('"%s" is not a valid URL.' % value, self)
        elif isinstance(value, cgi.FieldStorage):
            if self.required and not getattr(value, 'filename', None):
                raise twc.ValidationError('required', self)
            if self.extensions:
                ext = os.path.splitext(value.filename)[-1][1:]
                if ext not in self.extensions:
                    raise twc.ValidationError('"%s" is not a valid extension :  only "%s" are allowed' % (ext, ', '.join([e for e in self.extensions])), self)


class BsFileField(twf.TextField):
    template = "tw2.bs.templates.doublefilefield"
    type = 'text'
    placeholder = 'Enter url here'
    resources = [
        twc.JSLink(modname=__name__, filename='static/bs.js'),
    ]

    @classmethod
    def post_define(cls):
        pass

    def prepare(self):
        super(BsFileField, self).prepare()
        self.safe_modify('resources')
        start_field = 'text'
        if isinstance(self.value, cgi.FieldStorage):
            start_field = 'file'
        self.add_call(twc.js_function('bs_init_file_field')(self.compound_id, start_field))

    def _validate(self, value, state=None):
        print "validate %s, %s" % (value, state)
        super(BsFileField, self)._validate(value, state)


class BsTripleFileField(twf.TextField):
    template = "tw2.bs.templates.triplefilefield"
    type = 'text'
    placeholder = 'Enter url here'
    resources = [
        twc.JSLink(modname=__name__, filename='static/bs.js'),
    ]
    options = []

    @classmethod
    def post_define(cls):
        pass

    def prepare(self):
        super(BsTripleFileField, self).prepare()
        self.safe_modify('resources')
        start_field = 'text'
        if isinstance(self.value, cgi.FieldStorage):
            start_field = 'file'
        else:
            try:
                json.loads(self.value)
                start_field = 'select'
            except:
                pass
        self.add_call(twc.js_function('bs_init_triple_file_field')(self.compound_id, start_field))
        opts = []
        for opt in self.options:
            d = {}
            if len(opt) == 2:
                d['value'] = opt[1]
                d['display'] = opt[0]
            else:
                d['value'] = opt
                d['display'] = opt
            opts.append(d)
        self.safe_modify('attrs')
        self.attrs['opts'] = opts

    def _validate(self, value, state=None):
        print "validate %s, %s" % (value, state)
        super(BsTripleFileField, self)._validate(value, state)


class MultipleBsFileField(twf.RowLayout):
    template = "tw2.bs.templates.multiple"
    resources = [
        twc.JSLink(modname=__name__, filename='static/bs.js'),
    ]
    compounds = []

    @classmethod
    def post_define(cls):
        pass

    def prepare(self):
        super(MultipleBsFileField, self).prepare()
        self.safe_modify('resources')
        self.add_call(twc.js_function('bs_init_multiple')(self.compound_id))
        self.safe_modify('attrs')
        self.attrs['compounds'] = self.compounds

    def _validate(self, value, state=None):
        super(BsFileField, self)._validate(value, state)
