import tw2.core as twc
import tw2.forms as twf
import tw2.dynforms as twd
import re
import cgi
import os


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
    template = "tw2.bs.templates.filefield"
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
        self.add_call(twc.js_function('bs_init_file_field')(self.compound_id))

    def _validate(self, value, state=None):
        super(BsFileField, self)._validate(value, state)


class MultipleBsFileField(twf.TextField):
    template = "tw2.bs.templates.multiple"
    type = 'text'
    placeholder = 'Enter url here'
    resources = [
        twc.JSLink(modname=__name__, filename='static/bs.js'),
    ]

    @classmethod
    def post_define(cls):
        pass

    def prepare(self):
        super(MultipleBsFileField, self).prepare()
        self.safe_modify('resources')
        self.add_call(twc.js_function('bs_init_multiple')(self.compound_id))

    def _validate(self, value, state=None):
        super(BsFileField, self)._validate(value, state)
