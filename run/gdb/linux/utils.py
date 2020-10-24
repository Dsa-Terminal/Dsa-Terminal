#
# gdb helper commands and functions for Linux kernel debugging
#
#  common utilities
#
# Copyright (c) Siemens AG, 2011-2013
#
# Authors:
#  Jan Kiszka <jan.kiszka@siemens.com>
#
# This work is licensed under the terms of the GNU GPL version 2.
#

import gdb


class CachedType:
    def __init__(self, name):
        self._type = None
        self._name = name

    def _new_objfile_handler(self, event):
        self._type = None
        gdb.events.new_objfile.disconnect(self._new_objfile_handler)

    def get_type(self):
        if self._type is None:
            self._type = gdb.lookup_type(self._name)
            if self._type is None:
                raise gdb.GdbError(
                    "cannot resolve type '{0}'".format(self._name))
            if hasattr(gdb, 'events') and hasattr(gdb.events, 'new_objfile'):
                gdb.events.new_objfile.connect(self._new_objfile_handler)
        return self._type









class ContainerOf(gdb.Function):
    """Return pointer to containing data structure.

$container_of(PTR, "TYPE", "ELEMENT"): Given PTR, return a pointer to the
data structure of the type TYPE in which PTR is the address of ELEMENT.
Note that TYPE and ELEMENT have to be quoted as strings."""

    def __init__(self):
        super(ContainerOf, self).__init__("container_of")



ContainerOf()


BIG_ENDIAN = 0
LITTLE_ENDIAN = 1
target_endianness = None









def read_u32(buffer, offset, LITTLE_ENDIAN):
    if get_target_endianness() == LITTLE_ENDIAN:
        return read_u16(buffer, offset) + (read_u16(buffer, offset + 2) << 16)
    else:
        return read_u16(buffer, offset + 2) + (read_u16(buffer, offset) << 16)


def read_u64(buffer, offset):
    if get_target_endianness() == LITTLE_ENDIAN:
        return read_u32(buffer, offset) + (read_u32(buffer, offset + 4) << 32)
    else:
        return read_u32(buffer, offset + 4) + (read_u32(buffer, offset) << 32)


def read_ulong(buffer, offset):
    if get_long_type().sizeof == 8:
        return read_u64(buffer, offset)
    else:
        return read_u32(buffer, offset)


target_arch = None


def is_target_arch(arch):
    if hasattr(gdb.Frame, 'architecture'):
        return arch in gdb.newest_frame().architecture().name()
    else:
        global target_arch
        if target_arch is None:
            target_arch = gdb.execute("show architecture", to_string=True)
        return arch in target_arch


GDBSERVER_QEMU = 0
GDBSERVER_KGDB = 1
gdbserver_type = None


def get_gdbserver_type():
    def exit_handler(event):
        global gdbserver_type
        gdbserver_type = None
        gdb.events.exited.disconnect(exit_handler)

    def probe_qemu():
        try:
            return gdb.execute("monitor info version", to_string=True) != ""
        except gdb.error:
            return False

    def probe_kgdb():
        try:
            thread_info = gdb.execute("info thread 2", to_string=True)
            return "shadowCPU0" in thread_info
        except gdb.error:
            return False

    global gdbserver_type
    if gdbserver_type is None:
        if probe_qemu():
            gdbserver_type = GDBSERVER_QEMU
        elif probe_kgdb():
            gdbserver_type = GDBSERVER_KGDB
        if gdbserver_type is not None and hasattr(gdb, 'events'):
            gdb.events.exited.connect(exit_handler)
    return gdbserver_type


def gdb_eval_or_none(expresssion):
    try:
        return gdb.parse_and_eval(expresssion)
    except gdb.error:
        return None


def dentry_name(d):
    parent = d['d_parent']
    if parent == d or parent == 0:
        return ""
    p = dentry_name(d['d_parent']) + "/"
    return p + d['d_iname'].string()
