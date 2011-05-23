# -*- coding: utf-8 -*-
# vi:si:et:sw=4:sts=4:ts=4

##
## Copyright (C) 2006-2009 Async Open Source <http://www.async.com.br>
## All rights reserved
##
## This program is free software; you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation; either version 2 of the License, or
## (at your option) any later version.
##
## This program is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU Lesser General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with this program; if not, write to the Free Software
## Foundation, Inc., or visit: http://www.gnu.org/.
##
## Author(s): Stoq Team <stoq-devel@async.com.br>
##
##

program_name    = "Stoq"
website         = 'http://www.stoq.com.br'
major_version   = 0
minor_version   = 9
micro_version   = 15
extra_version   = 99
release_date    = (2011, 2, 9)
stable          = False

version         = '%d.%d.%d' % (major_version, minor_version, micro_version)
if extra_version > 0:
    version += '.%d' % (extra_version, )

try:
    from kiwi.environ import Library
except ImportError:
    raise SystemExit("Could not find kiwi")

# XXX: Use Application
library = Library('stoq')
if library.uninstalled:
    library.add_global_resource('pixmaps', 'data/pixmaps')
    library.add_global_resource('glade', 'data/glade')
    library.add_global_resource('config', 'data/config')
    library.add_global_resource('docs', '.')
    library.add_global_resource('misc', 'data/misc')
library.enable_translation()
library.set_application_domain('stoq')
