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
