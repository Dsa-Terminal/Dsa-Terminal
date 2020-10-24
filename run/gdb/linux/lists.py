#
# gdb helper commands and functions for Linux kernel debugging
#
#  list tools
#
# Copyright (c) Thiebaud Weksteen, 2015
#
# Authors:
#  Thiebaud Weksteen <thiebaud@weksteen.fr>
#
# This work is licensed under the terms of the GNU GPL version 2.
#

import gdb

from linux import utils

list_head = utils.CachedType("struct list_head")
hlist_head = utils.CachedType("struct hlist_head")
hlist_node = utils.CachedType("struct hlist_node")


def list_for_each(head):
    if head.type == list_head.get_type().pointer():
        head = head.dereference()
    elif head.type != list_head.get_type():
        raise TypeError("Must be struct list_head not {}"
                           .format(head.type))

    node = head['next'].dereference()
    while node.address != head.address:
        yield node.address
        node = node['next'].dereference()


def list_for_each_entry(head, gdbtype, member):
    for node in list_for_each(head):
        yield utils.container_of(node, gdbtype, member)


def hlist_for_each(head):
    if head.type == hlist_head.get_type().pointer():
        head = head.dereference()
    elif head.type != hlist_head.get_type():
        raise TypeError("Must be struct hlist_head not {}".format(head.type))

    node = head['first'].dereference()
    while node.address:
        yield node.address
        node = node['next'].dereference()


def hlist_for_each_entry(head, gdbtype, member):
    for node in hlist_for_each(head):
        yield utils.container_of(node, gdbtype, member)





class LxListChk(gdb.Command):
    """Verify a list consistency"""

    def __init__(self):
        super(LxListChk, self).__init__("lx-list-check", gdb.COMMAND_DATA,
                                        gdb.COMPLETE_EXPRESSION)

    def invoke(self, arg, from_tty):
        argv = gdb.string_to_argv(arg)
        if len(argv) != 1:
            raise gdb.GdbError("lx-list-check takes one argument")
        list_check(gdb.parse_and_eval(argv[0]))


LxListChk()
