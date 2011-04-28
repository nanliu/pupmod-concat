Summary: Concat Puppet Module
Name: pupmod-concat
Version: 1.0
Release: 0
License: GPL
Group: Applications/System
Source: %{name}-%{version}-%{release}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires: puppet-server >= 0.24.9
Buildarch: noarch

Prefix:"/etc/puppet/modules"

%description
This puppet module provides the concat_build and concat_fragment custom types.

%prep
%setup -q

%build

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

# Make your directories here.
mkdir -p %{buildroot}/%{prefix}/concat
mkdir -p %{buildroot}/%{prefix}/concat/files
mkdir -p %{buildroot}/%{prefix}/concat/manifests
mkdir -p %{buildroot}/%{prefix}/concat/templates
mkdir -p %{buildroot}/%{prefix}/concat/plugins

# Now install the files.
test -d plugins && cp -r plugins %{buildroot}/%{prefix}/concat

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f pupmod-concat.spec_files.txt
%defattr(0640,root,puppet)
%{prefix}/concat

%changelog
* Mon Feb 07 2011 Morgan Haskel <mhaskel@onyxpoint.com> - 1.0-0
- Initial implementation of concat_build and concat_fragment custom types.
