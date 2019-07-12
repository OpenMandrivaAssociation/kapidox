%define debug_package %{nil}
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)

Name: kapidox
Version:	5.60.0
Release:	1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: Scripts and data for building API documentation
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: cmake(KF5DocTools)

%description
Scripts and data for building API documentation (dox)
in a standard format and style.

%prep
%setup -q
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build

%files
%{_bindir}/depdiagram-generate
%{_bindir}/depdiagram-generate-all
%{_bindir}/depdiagram-prepare
%{_bindir}/kapidox_generate
%{_prefix}/lib/python*/site-packages/kapidox
%{_prefix}/lib/python*/site-packages/kapidox*.egg-info
%{_mandir}/man1/depdiagram-*.1.*
