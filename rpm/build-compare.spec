#
# spec file for package build-compare
#
# Copyright (c) 2022 Jolla Ltd.
# Copyright (c) 2017 SUSE LINUX GmbH, Nuernberg, Germany.
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
Summary:        Build Result Compare Script
License:        GPLv2+
Url:            https://github.com/sailfishos/build-compare
Version:        0
Release:        1
Source0:        %{name}-%{version}.tar.gz
Patch0:         0001-OBS-project-name-in-RPM-meta-data-causes-problems-in.patch
Patch1:         0002-fix-compatibility-with-older-sed.patch
Patch1:         0003-ignore-parts-of-NSS-checksum-files.patch
%if 0%{?suse_version}
Requires:       bash
Requires:       cpio
Requires:       coreutils
Requires:       diffutils
Requires:       file
Requires:       gawk
Requires:       grep
Requires:       rpm
Requires:       sed
Requires:       od
%endif
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
#!BuildIgnore:  build-compare

%description
This package contains scripts to find out if the build result differs
to a former build.


%prep
%autosetup -p1 -n %{name}-%{version}/%{name}

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/lib/build/ $RPM_BUILD_ROOT/%_defaultdocdir/%name
install -m 0755 *.sh $RPM_BUILD_ROOT/usr/lib/build/

%files
%defattr(-,root,root)
%license COPYING
/usr/lib/build
