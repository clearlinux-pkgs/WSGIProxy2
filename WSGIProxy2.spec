#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : WSGIProxy2
Version  : 0.4.5
Release  : 42
URL      : https://files.pythonhosted.org/packages/48/29/4a6aa18fd530d31ee6e0c99fc8b771baa607970d0909f858531fb44d2757/WSGIProxy2-0.4.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/48/29/4a6aa18fd530d31ee6e0c99fc8b771baa607970d0909f858531fb44d2757/WSGIProxy2-0.4.5.tar.gz
Summary  : A WSGI Proxy with various http client backends
Group    : Development/Tools
License  : MIT
Requires: WSGIProxy2-license = %{version}-%{release}
Requires: WSGIProxy2-python = %{version}-%{release}
Requires: WSGIProxy2-python3 = %{version}-%{release}
Requires: requests
Requires: six
Requires: urllib3
BuildRequires : WebOb
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : six
BuildRequires : tox
BuildRequires : virtualenv

%description
============

%package license
Summary: license components for the WSGIProxy2 package.
Group: Default

%description license
license components for the WSGIProxy2 package.


%package python
Summary: python components for the WSGIProxy2 package.
Group: Default
Requires: WSGIProxy2-python3 = %{version}-%{release}
Provides: wsgiproxy2-python

%description python
python components for the WSGIProxy2 package.


%package python3
Summary: python3 components for the WSGIProxy2 package.
Group: Default
Requires: python3-core

%description python3
python3 components for the WSGIProxy2 package.


%prep
%setup -q -n WSGIProxy2-0.4.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1538143884
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/WSGIProxy2
cp COPYING %{buildroot}/usr/share/package-licenses/WSGIProxy2/COPYING
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(-,root,root,-)
/usr/share/package-licenses/WSGIProxy2/COPYING

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
