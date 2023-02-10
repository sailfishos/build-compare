#
# spec file for package build-compare
#
# Copyright (c) 2022 Jolla Ltd.
# Copyright (c) 2022 SUSE LLC
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name:           build-compare
Version:        0
Release:        1
Summary:        Build Result Compare Script
License:        GPLv2+
Url:            https://github.com/sailfishos/build-compare
Source0:        %{name}-%{version}.tar.gz
Patch0:         0000-OBS-project-name-in-RPM-meta-data-cause.patch
Patch1:         0001-ignore-parts-of-NSS-checksum-files.patch
Patch2:         0002-ignore-OS-version-recorded-in-Perl-conf.patch
Patch3:         0003-Ignore-rpmlint-output-differences.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
#!BuildIgnore:  build-compare
BuildArch:      noarch
%if 0%{?suse_version}
Requires:       bash
Requires:       coreutils
Requires:       cpio
Requires:       diffutils
Requires:       file
Requires:       gawk
Requires:       grep
Requires:       rpm
Requires:       sed
%endif

%description
This package contains scripts to find out if the build result differs
to a former build.

%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build

%install
mkdir -p %{buildroot}%{_prefix}/lib/build/
install -m 0755 *.sh %{buildroot}%{_prefix}/lib/build/

%files
%if 0%{?suse_version} && 0%{?suse_version} < 1500
%defattr(-,root,root)
%doc COPYING
%else
%license COPYING
%endif
%{_prefix}/lib/build
