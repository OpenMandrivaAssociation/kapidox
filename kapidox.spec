%define debug_package %{nil}

Name: kapidox
Version: 5.0.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/stable/frameworks/%{version}/%{name}-%{version}.tar.xz
Summary: Scripts and data for building API documentation
URL: http://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake
BuildRequires: qmake5
BuildRequires: extra-cmake-modules5
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: cmake(KF5DocTools)
BuildRequires: cmake(PythonInterp)
BuildRequires: ninja

%description
Scripts and data for building API documentation (dox)
in a standard format and style

%prep
%setup -q
%cmake -G Ninja

%build
ninja -C build

%install
DESTDIR="%{buildroot}" ninja -C build install %{?_smp_mflags}

%files
%{_bindir}/depdiagram-generate
%{_bindir}/depdiagram-generate-all
%{_bindir}/depdiagram-prepare
%{_bindir}/kgenapidox
%{_bindir}/kgenframeworksapidox
%{_prefix}/lib/python*/site-packages/kapidox
%{_prefix}/lib/python*/site-packages/kapidox*.egg-info
