#
# Copyright (C) 2011 Onyx Point, Inc. <http://onyxpoint.com/>
#
# This file is part of the Onyx Point concat puppet module.
#
# The Onyx Point concat puppet module is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the License,
# or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more
# details.
#
# You should have received a copy of the GNU General Public License along with
# this program.  If not, see <http://www.gnu.org/licenses/>.
#
Summary: Concat Puppet Module
Name: pupmod-concat
Version: 1.0
Release: 0
License: GPLv3
Group: Applications/System
Source: %{name}-%{version}-%{release}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: puppet-server >= 2.6
Buildarch: noarch

%description
This puppet module provides the concat_build and concat_fragment custom types.

%prep
%setup -q

%build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

# Make your directories here.
mkdir -p %{buildroot}/etc/puppet/modules/concat/lib

# Now install the files.
cp -r lib %{buildroot}/etc/puppet/modules/concat
chmod -R u=rwX,g=rX,o-rwx %{buildroot}/etc/puppet/modules/concat

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,puppet)
/etc/puppet/modules/concat

%changelog
* Mon Feb 07 2011 Morgan Haskel <mhaskel@onyxpoint.com> - 1.0-0
- Initial implementation of concat_build and concat_fragment custom types.
