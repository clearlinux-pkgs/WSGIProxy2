#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : WSGIProxy2
Version  : 0.4.6
Release  : 58
URL      : https://files.pythonhosted.org/packages/9e/db/3e8d6877cc12de58ff67eecfab58acc50b2e2803381a06e21c78fa99713c/WSGIProxy2-0.4.6.tar.gz
Source0  : https://files.pythonhosted.org/packages/9e/db/3e8d6877cc12de58ff67eecfab58acc50b2e2803381a06e21c78fa99713c/WSGIProxy2-0.4.6.tar.gz
Summary  : A WSGI Proxy with various http client backends
Group    : Development/Tools
License  : MIT
Requires: WSGIProxy2-license = %{version}-%{release}
Requires: WSGIProxy2-python = %{version}-%{release}
Requires: WSGIProxy2-python3 = %{version}-%{release}
Requires: WebOb
Requires: requests
Requires: six
Requires: urllib3
BuildRequires : WebOb
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : requests
BuildRequires : six
BuildRequires : tox
BuildRequires : urllib3
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
Provides: pypi(wsgiproxy2)
Requires: pypi(six)
Requires: pypi(webob)

%description python3
python3 components for the WSGIProxy2 package.


%prep
%setup -q -n WSGIProxy2-0.4.6
cd %{_builddir}/WSGIProxy2-0.4.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583525093
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/WSGIProxy2
cp %{_builddir}/WSGIProxy2-0.4.6/COPYING %{buildroot}/usr/share/package-licenses/WSGIProxy2/c0955b5351b1dcafdd0b9bb2d7e84fe0e3d731ca
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/WSGIProxy2/c0955b5351b1dcafdd0b9bb2d7e84fe0e3d731ca

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
