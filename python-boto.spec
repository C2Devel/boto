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
Release:        ROCKIT51%{?buildid}%{byte_code_mark}%{?dist}
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


%changelog
* Sat Nov 02 2024 Andrey Kulaev <akulaev@k2.cloud> - 2.46.1-ROCKIT51
- ec2: refactor attach_extnetwork and detach_extnetwork methods

* Tue Jul 23 2024 Linar Nasyyrov <lnasyyrov@k2.cloud> - 2.46.1-ROCKIT50
- ec2: add RamMonitoring Instance attribute
- spec: move to ROCKIT

* Thu Dec 21 2023 Ivan Konov <ikonov@croc.ru> - 2.46.1-CROC49
- tests: add parameter required since py3.8 to hmac.new() calls
- tests: replace deprecated cgi.escape() with html.escape()
- spec: fixes for redos build

* Thu Oct 12 2023 Grigoriy Kulagin <grkulagin@croc.ru> - 2.46.1-CROC48
- .github: remove old py version checks
- ec2: add os and new instance type format

* Thu Jan 26 2023 Andrey Kulaev <akulaev@croc.ru> - 2.46.1-CROC47
- spec: drop legacy support el6
- spec: add el8 support
- spec: remove python2

* Mon Dec 05 2022 Anastasia Berezko <aberezko@croc.ru> - 2.46.1-CROC46
- fix api field name

* Wed Apr 06 2022 Ivan Konov <ikonov@croc.ru> - 2.46.1-CROC45
- ec2: add tagging to CreateImage

* Tue Mar 01 2022 Ivan Konov <ikonov@croc.ru> - 2.46.1-CROC44
- ec2: fix setting empty description in modify_snapshot_attribute

* Mon Jan 10 2022 Andrey Kulaev <akulaev@croc.ru> - 2.46.1-CROC43
- vpc: add set_bgp_asn handler
- vpc: add unset_bgp_asn handler

* Fri Oct 29 2021 Alexander Chernev <achernev@croc.ru> - 2.46.1-CROC42
- ec2: import_task: remove duplicate "self.snapshot_details = None"
- ec2: export_task: add missed space
- ec2: export_task: remove volume_export_details field
- ec2: connection: remove modify_task_priority method
- ec2: connection: add ImageName to import_image method
- ec2: import_task: parse diskImageSize as integer

* Mon Sep 13 2021 Andrey Kulaev <akulaev@croc.ru> - 2.46.1-CROC41
- action: add github action
- ec2: remove deprecated attributes from modify_volume_attribute

* Mon Jul 12 2021 Andrey Kulaev <akulaev@croc.ru> - 2.46.1-CROC40
- vpc: remove unused description from vpc
- ec2: drop legacy Virtual Network API 
- vpc: add propagating_vgws field to RouteTable entity
- vpc: add route_propagation field to VPC entity

* Tue Jun 15 2021 Andrey Kulaev <akulaev@croc.ru> - 2.46.1-CROC39
- vpc: add create_default_vpc method
- ec2: remove suspend instances

* Tue Jun 01 2021 Evgeny Kovalev <evgkovalev@croc.ru> - 2.46.1-CROC38
- vpc: add supported VPN tunnel options constant
- vpc: handle new VPN tunnel options in create_vpn_connection
- vpc: support left/right subnet in create_vpn_connection
- vpc: support 'ReplayWindowSize' VPNC tunnel option

* Fri May 14 2021 Ivan Konov <ikonov@croc.ru> - 2.46.1-CROC37
- ec2: enable tagging on address allocation

* Mon Apr 12 2021 Ivan Konov <ikonov@croc.ru> - 2.46.1-CROC36
- ec2: add field is_shared to snap

* Thu Apr 1 2021 Andrey Kulaev <akulaev@croc.ru> - 2.46.1-CROC35
- ec2: add hibernate option to stop_instances

* Mon Mar 1 2021 Andrey Kulaev <akulaev@croc.ru> - 2.46.1-CROC34
- ec2: add modify_volume method

* Mon Jan 18 2021 Evgeny Kovalev <evgkovalev@croc.ru> - 2.46.1-CROC33
- vpc: remove description from vpc

* Mon Dec 14 2020 Andrey Kulaev <akulaev@croc.ru> - 2.46.1-CROC32
- vpc: add tags param in create_customer_gateway and create_vpn_connection

* Tue Dec 1 2020 Andrey Kulaev <akulaev@croc.ru> - 2.46.1-CROC31
- ec2: rename virtualization types

* Fri Nov 6 2020 Alexandr Chernev <achernev@croc.ru> - 2.46.1-CROC30
- ec2: allow multiple interfaces along with eip assoc
- tests: remove obsolete part of test_cant_use_public_ip
- tests: add case for multi-eni spec with eip assoc on primary

* Thu Oct 22 2020 Evgeny Kovalev <evgkovalev@croc.ru> - 2.46.1-CROC29
- ec2: remove description from modify_volume_attribute
- ec2: remove description from run_instances

* Tue Sep 29 2020 Aleksandr Rudenko <arudenko@croc.ru> - 2.46.1-CROC28
- spec: change requirements for centos 7.8 build

* Tue Sep 15 2020 Andrey Kulaev <akulaev@croc.ru> - 2.46.1-CROC27
- ec2: add private_ip_addresses to create_network_interface

* Tue Sep 08 2020 Andrey Kulaev <akulaev@croc.ru> - 2.46.1-CROC26
- utils, ec2: move tagging on creation for common usage
- vpc: add tagging on creation for subnets
- vpc: add tagging on creation for acls
- vpc: add tagging on creation for dopts
- ec2: add tagging on creation for network interfaces
- ec2: add tagging on creation for placement groups
- vpc: add tagging on creation for route tables
- ec2: add tagging on creation for security groups
- vpc: add tagging on creation for vpc

* Wed Aug 05 2020 Evgeny Kovalev <evgkovalev@croc.ru> - 2.46.1-CROC25
- tariff: add deprecation status to instance type, volume type, other

* Mon Jul 13 2020 Alexandr Chernev <achernev@croc.ru> - 2.46.1-CROC24
- connection,utils: convert max_retry_delay to float before comparison

* Tue Jun 30 2020 Andrey Kulaev <akulaev@croc.ru> - 2.46.1-CROC23
- vpc: support vpnc_create options specification

* Mon Jun 15 2020 Evgeny Kovalev <evgkovalev@croc.ru> - 2.46.1-CROC22
- ec2: add new method 'CreateDefaultSubnet'

* Mon Jun 08 2020 Andrey Kulaev <akulaev@croc.ru> - 2.46.1-CROC21
- ec2: allow tagging keypair on creation and import

* Mon May 18 2020 Andrey Kulaev <akulaev@croc.ru> - 2.46.1-CROC20
- ec2: add filters for get_all_public_ipv4_pools
- ec2: add id and tags to keypairs
- ec2: add tags and id to placement groups

* Wed Apr 01 2020 Andrey Kulaev <akulaev@croc.ru> - 2.46.1-CROC19
- EC2Connection: add tags to create_volume
- EC2Connection: add tags to create_snapshot
- EC2Connection: add tags to run_instances

* Mon Feb 03 2020 Andrey Kulaev <akulaev@croc.ru> - 2.46.1-CROC18
- ec2 module: modify 'get_all_extnetworks' method

* Tue Dec 24 2019 Andrey Kulaev <akulaev@croc.ru> - 2.46.1-CROC17
- ec2: add ability to modify security group's attribute.
- ec2: add address pool entities
- ec2: add address pool methods
- ec2: add allocate_address() address pool support
- ec2 tests: add tests for address pool methods
- ec2: add public_ipv4_pool field handling 

* Mon Nov 11 2019 Andrey Kulaev <akulaev@croc.ru> - 2.46.1-CROC16
- [cloudtrail] add aws_sudo_id support 

* Wed Aug 07 2019 Vladislav Odinstov <odivlad@gmail.com> - 2.46.1-CROC15
- spec: add support for py2/py3 epel build

* Fri Jul 26 2019 Andrey Kulaev <akulaev@croc.ru> - 2.46.1-CROC14
- ec2: methods for changing sg.rule description
- ec2: add 'description' for GroupOrCIDR

* Thu Jun 06 2019 Pavel Kulyov <pkulev@croc.ru> - 2.46.1-CROC13
- ec2: add parser for Network Interface Association
- ec2: add missing Reset/Describe NI methods
- ec2: drop PrivateIps support
- ec2: add private DNS name parsing to NetworkInterface
- ec2: add switch_id to NetworkInterface

* Wed May 22 2019 Nikita Kretov <kretov995@gmail.com> - - 2.46.1-CROC12
- ec2: add get_tariff method
- travis: pin ubuntu dist
- travis: fix auto-build

* Fri Apr 05 2019 Kretov Nikita <kretov995@gmail.com> - - 2.46.1-CROC11
- cw: add new parameters for MetricAlarms
- ec2: Allow Tags deletion by resource ID only

* Thu Feb 28 2019 Nikita Kretov <kretov995@gmail.com> - 2.46.1-CROC10
- ec2: Add 'modify-instance-placemenet' method

* Thu Jan 10 2019 Mikhail Ushanov <gm.mephisto@gmail.com> - 2.46.1-CROC9
- requirements: pin idna version
- ec2: add to VirtualSwitch an optional parameter 'AvailabilityZone'

* Fri Oct 05 2018 Mikhail Ushanov <gm.mephisto@gmail.com> - 2.46.1-CROC8
- requirements: pin pycparser version
- ec2: update PrivateIp according NAPI
- ec2: update ExtNet according Switch and Subnet API

* Tue Aug 07 2018 Mikhail Ushanov <gm.mephisto@gmail.com> - 2.46.1-CROC7
- ec2: add 'cidr_ipv6' in SecurityGroup entity
- ec2: remove group_type
- ec2: add VirtualSwitch and CRD operations on it
- ec2: add switch_ids to instance
- s3: add AccessDenied error processing

* Mon Apr 02 2018 Mikhail Ushanov <gm.mephisto@gmail.com> - 2.46.1-CROC6
- compat: dont use strict requires to ordereddict

* Tue Dec 26 2017 Mikhail Ushanov <gm.mephisto@gmail.com> - 2.46.1-CROC5
- Freeze max versions for paramiko and cryptography
- boto: dont decode bytes string in PY2 when parse error message

* Tue Oct 03 2017 Mikhail Ushanov <gm.mephisto@gmail.com> - 2.46.1-CROC4
- Add address parameter to address allocation
- ec2: remove 'attach_type' from blockdevicemapping
- ec2: remove 'attach_type' argument from attach volume method

* Tue Jun 27 2017 Mikhail Ushanov <gm.mephisto@gmail.com> - 2.46.1-CROC3
- ec2: fix 'AllowReassociation' param according to AWS API
- ec2: fix tests for addresses.associate

* Fri May 26 2017 Mikhail Ushanov <gm.mephisto@gmail.com> - 2.46.1-CROC2
- ec2: preserved blockdevicemapping order
- rpm: added ordereddict requires on legacy platforms

* Fri Apr 14 2017 Anton Vazhnetsov <dragen15051@gmail.com> - 2.46.1-CROC1
- Update to latest boto - 2.46.1
