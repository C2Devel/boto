%{!?__python3: %global __python3 /usr/bin/python3}
%{!?python3_sitelib: %global python3_sitelib %(%{__python3} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%if 0%{?rhel} == 8 || 0%{?redos} == 7
%global el_python3_pkgversion 3
%else
%global el_python3_pkgversion 36
%endif

%define pkgname boto
%define buildid @BUILDID@
%global sum AWS authentication for Amazon S3 for the python requests module
%global descr \
Boto is a Python package that provides interfaces to Amazon Web Services.\
It supports over thirty services, such as S3 (Simple Storage Service),\
SQS (Simple Queue Service), and EC2 (Elastic Compute Cloud) via their\
REST and Query APIs.  The goal of boto is to support the full breadth\
and depth of Amazon Web Services.  In addition, boto provides support\
for other public services such as Google Storage in addition to private\
cloud systems like Eucalyptus, OpenStack and Open Nebula.

Summary:        A simple, lightweight interface to Amazon Web Services
Name:           python-%{pkgname}
Version:        2.46.1
Release:        ROCKIT52.rc1%{?buildid}%{?byte_code_mark}%{?dist}
License:        MIT
Group:          Development/Languages
URL:            https://github.com/c2devel/boto
Source0:        https://pypi.io/packages/source/b/boto/boto-%{version}.tar.gz

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{el_python3_pkgversion}-httpretty
BuildRequires:  python%{el_python3_pkgversion}-mock
BuildRequires:  python%{el_python3_pkgversion}-nose
BuildRequires:  python%{el_python3_pkgversion}-requests
BuildArch:      noarch

%description
%{descr}

%package -n python%{python3_pkgversion}-%{pkgname}
Summary:        A simple, lightweight interface to Amazon Web Services

Requires:       python%{python3_pkgversion}-requests

%description -n python%{python3_pkgversion}-%{pkgname}
%{descr}

%prep
%setup -q -n %pkgname-%version

%build
%{py3_build}

%install
%{py3_install}
rm -f %buildroot/%{_bindir}/*

%check
%{__python3} tests/test.py default

%files -n python%{python3_pkgversion}-%{pkgname}
%defattr(-,root,root,-)
%{python3_sitelib}/boto
%{python3_sitelib}/boto-%{version}-*.egg-info
%doc LICENSE README.rst
