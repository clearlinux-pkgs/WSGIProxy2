#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : WSGIProxy2
Version  : 0.4.2
Release  : 7
URL      : https://pypi.python.org/packages/source/W/WSGIProxy2/WSGIProxy2-0.4.2.zip
Source0  : https://pypi.python.org/packages/source/W/WSGIProxy2/WSGIProxy2-0.4.2.zip
Summary  : UNKNOWN
Group    : Development/Tools
License  : MIT
Requires: WSGIProxy2-python
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
Installation
============
With pip::
$ pip install WSGIProxy2
Install optionnal backends::

%package python
Summary: python components for the WSGIProxy2 package.
Group: Default

%description python
python components for the WSGIProxy2 package.


%prep
%setup -q -n WSGIProxy2-0.4.2

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
