#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    env.py

    Simplified access to environment variables in Python.

    @copyright: 2018 by Mike Miller
    @license: LGPL
'''
#
#  The implementation below is odd at times due to using the module as a
#  container.
#
import sys, os
try:
    from collections.abc import MutableMapping
except ImportError:
    from collections import MutableMapping  # Py2


__version__ = '0.91'


class EnvironmentVariable(str):
    ''' Represents a variable entry in the environment.  Base class.

        Contains the functionality of strings plus a number of convenience
        properties for type conversion.
    '''
    def __init__(self, *args):
        raise NotImplementedError('Use Entry() or NullEntry() instead.')


class Entry(EnvironmentVariable):
    ''' Represents an existing entry in the environment. '''
    def __new__(cls, name, value):
        return str.__new__(cls, value)  # Py2/3

    def __init__(self, name, value, sep=os.pathsep):
        self.name = name
        self.value = value
        self._pathsep = sep

    @property
    def truthy(self):
        ''' Convert a Boolean-like string value to a Boolean or None.
            Note: the rules are different than string type "truthiness."

            ''              --> False
            '0'             --> False
            '1'             --> True
            ('no', 'false') --> False       # case-insensitive
            ('yes', 'true') --> True        # case-insensitive
            else            --> None
        '''
        lower = self.lower()
        if lower.isdigit():
            return bool(int(lower))
        elif lower in ('yes', 'true'):
            return True
        elif lower in ('no', 'false'):
            return False
        elif self == '':
            return False
        else:
            return None
    bool = truthy  # deprecated

    @property
    def float(self):
        ''' Return a float. '''
        return float(self)

    @property
    def int(self):
        ''' Return an int. '''
        return int(self)

    @property
    def list(self):
        ''' Split a path string (defaults to os.pathsep) and return list.

            Use str.split instead when a custom delimiter is needed.
        '''
        return self.split(self._pathsep)

    @property
    def path(self):
        ''' Return a path string as a Path object. '''
        from pathlib import Path
        return Path(self)

    @property
    def path_list(self):
        ''' Return list of Path objects. '''
        from pathlib import Path
        return [ Path(pathstr) for pathstr in self.split(self._pathsep) ]

    @property
    def from_json(self):
        ''' Parse a JSON string. '''
        from json import loads
        return loads(self)

    def __repr__(self):
        return '%s(%r, %r)' % (self.__class__.__name__, self.name, self.value)


class NullEntry(EnvironmentVariable):
    ''' Represents an non-existent entry in the environment.

        This is a None-like convenience object that won't throw AttributeError
        on attribute lookups.  Attributes are instead returned as "falsey"
        numeric zero or empty string/containers.
    '''
    def __new__(cls, name):
        return str.__new__(cls, '')  # Py2/3

    def __init__(self, name):
        self.name = name
        self.value = None

    def __bool__(self):
        return False

    @property
    def truthy(self):
        return None if (self.value is None) else False

    @property
    def float(self):
        return 0.0

    @property
    def int(self):
        return 0

    @property
    def list(self):
        return []

    @property
    def path(self):
        return None

    @property
    def path_list(self):
        return []

    @property
    def from_json(self):
        return {}

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.name)


class Environment(MutableMapping):
    ''' A mapping object that presents a simplified view of the OS Environment.
    '''
    _Entry_class = Entry            # save for Python2 compatibility :-/
    _NullEntry_class = NullEntry

    def __init__(self, environ=os.environ,
                       sensitive=False if os.name == 'nt' else True,
                       writable=False,
                ):
        # setobj - prevents infinite recursion due to custom setattr
        # https://stackoverflow.com/a/16237698/450917
        setobj = object.__setattr__
        setobj(self, '_original_env', environ),
        setobj(self, '_sensitive', sensitive),
        setobj(self, '_writable', writable),

        if sensitive:
            setobj(self, '_envars', environ)
        else:
            setobj(self, '_envars', { name.lower(): value
                                      for name, value in environ.items() })

    def __contains__(self, name):
        return name in self._envars

    def __getattr__(self, name):
        ''' Customize attribute access, allow direct access to variables. '''

        # need a loophole for configuring a new instance
        if name == 'Environment':
            return Environment
        elif name == 'Entry':
            return Entry or self._Entry_class  # Py2 compat

        if not self._sensitive:
            name = name.lower()

        try:
            return self._Entry_class(name, self._envars[name])
        except KeyError:
            return self._NullEntry_class(name)

    def __setattr__(self, name, value):
        if self._writable:
            self._envars[name] = value

            if self._original_env is os.environ:  # push to environment
                os.environ[name] = value
        else:
            raise AttributeError('This Environment is read-only.')

    def __delattr__(self, name):
        del self._envars[name]

    # MutableMapping needs these implemented, defers to internal dict
    def __len__(self):
        return len(self._envars)
    def __delitem__(self, key):
        del self._envars[key]
    def __getitem__(self, key):
        return self._envars[key]
    def __setitem__(self, key, item):
        self.data[key] = item
    def __iter__(self):
        return iter(self._envars)

    def __repr__(self):
        entry_list = ', '.join([ ('%s=%r' % (k, v)) for k, v in self.items() ])
        return '%s(%s)' % (self.__class__.__name__, entry_list)

    def from_prefix(self, prefix, lowercase=True, strip=True):
        ''' Returns a dictionary of keys with the same prefix.
            Compat with kr/env, lowercased.

            > xdg = env.from_prefix('XDG_')

            > for key, value in xdg.items():
                 print('%-20s' % key, value[:6], '…')
            config_dirs      /etc/x…
            current_desktop  MATE
            data_dirs        /usr/s…
            …
        '''
        env_subset = {}
        for key in self._envars.keys():
            if key.startswith(prefix):
                if strip:  # cut prefix
                    new_key = key[len(prefix):]
                new_key = new_key.lower() if lowercase else new_key
                env_subset[new_key] = self._envars[key]

        return Environment(
            environ=env_subset,
            sensitive=self._sensitive,
            writable=self._writable,
        )
    prefix = from_prefix

    def map(self, **kwargs):
        ''' Change a name on the fly.  Compat with kr/env. '''
        return { key: self._envars[kwargs[key]]  # str strips Entry
                 for key in kwargs }


if __name__ == '__main__':

    # keep tests close
    testenv = dict(
        EMPTY='',
        JSON_DATA='{"one":1, "two":2, "three":3}',
        PI='3.1416',
        READY='no',
        PORT='5150',
        QT_ACCESSIBILITY='1',
        SSH_AUTH_SOCK='/run/user/1000/keyring/ssh',
        TERM='xterm-256color',
        USER='fred',
        XDG_DATA_DIRS='/usr/local/share:/usr/share',
        XDG_SESSION_ID='c1',
        XDG_SESSION_TYPE='x11',
    )
    __doc__ += '''

        Default::

            >>> env = Environment(testenv, sensitive=True, writable=True)

            >>> env.USER                                # exists, repr
            Entry('USER', 'fred')

            >>> str(env.USER)                           # exists, str
            'fred'

            >>> env.USER + '_suffix'                    # str ops
            'fred_suffix'

            >>> env.USER.title()                        # str ops II
            'Fred'

            >>> bool(env.USER)                          # check exists/not empty
            True

            >>> print(f'term: {env.TERM}')              # via interpolation
            term: xterm-256color

            >>> 'NO_EXISTO' in env                      # check existence, DNE
            False

            >>> env.NO_EXISTO or 'default'              # DNE with default
            'default'

            >>> env.NO_EXISTO                           # var DNE repr
            NullEntry('NO_EXISTO')

            >>> env.NO_EXISTO.value is None             # check existence II
            True

            >>> bool(env.NO_EXISTO)                     # check when DNE: False
            False

            >>> 'EMPTY' in env                          # check existence
            True

            >>> env.EMPTY                               # exists but empty
            Entry('EMPTY', '')

            >>> env.EMPTY.value is None                 # check existence II
            False

            >>> bool(env.EMPTY)                         # check when empty: False
            False

            >>> env.EMPTY or 'default'                  # exists, blank w/ def.
            'default'

            >>> key_name = 'PI'
            >>> env[key_name]                           # getitem syntax
            '3.1416'

            >>> env.PI.float                            # type conversion
            3.1416

            >>> env.PORT.int or 9000                    # type conv. w/ default
            5150

            >>> env.QT_ACCESSIBILITY.truthy             # 0/1/yes/no/true/false
            True

            >>> sorted(env.JSON_DATA.from_json.keys())  # sorted: compat < 3.6
            ['one', 'three', 'two']

            >>> env.XDG_DATA_DIRS.list
            ['/usr/local/share', '/usr/share']

            >>> env.XDG_DATA_DIRZ.list                  # DNE fallback
            []

            # using isinstance to avoid Platform errs:
            >>> from pathlib import Path
            >>> isinstance(env.SSH_AUTH_SOCK.path, Path)
            True

            >>> all(map(lambda p: isinstance(p, Path), env.XDG_DATA_DIRS.path_list))
            True

        KR/env compatibility::

            >>> sorted(env.prefix('XDG_', False).keys())
            ['DATA_DIRS', 'SESSION_ID', 'SESSION_TYPE']

            >>> sorted(env.prefix('XDG_', False).values())
            ['/usr/local/share:/usr/share', 'c1', 'x11']

            >>> env.map(username='USER')
            {'username': 'fred'}

        Writing is possible when writable is set to True (see above),
        though not exceedingly useful::

            >>> env.READY
            Entry('READY', 'no')

            >>> env.READY = 'yes'

            >>> env.READY
            Entry('READY', 'yes')

        Unicode test::

            >>> env.MÖTLEY = 'Crüe'
            >>> env.MÖTLEY
            Entry('MÖTLEY', 'Crüe')

        Sensitive False::

            >>> env = Environment(testenv, sensitive=False)
            >>> str(env.USER)                           # interactive repr
            'fred'
            >>> str(env.user)                           # interactive repr
            'fred'
    '''
    import doctest

    # testmod returns (failure_count, test_count):
    sys.exit(
        doctest.testmod(verbose=(True if '-v' in sys.argv else False))[0]
    )


else:
    # save original module for later, just in case it's needed.
    Environment._module = sys.modules[__name__]

    # Wrap module with instance for direct access
    sys.modules[__name__] = Environment()
