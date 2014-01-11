Name: kapidox
Version: 4.95.0
Release: 1
Source0: http://ftp5.gwdg.de/pub/linux/kde/unstable/frameworks/4.95.0/%{name}-%{version}.tar.xz
Summary: Base files for KDE Frameworks 5 API documentation
URL: http://kde.org/
License: GPL
Group: Development/KDE and Qt
BuildRequires: cmake
BuildArch: noarch

%description
Base files for KDE Frameworks 5 API documentation

%prep
%setup -q
%cmake

%build
%make -C build

%install
%makeinstall_std -C build

%files
%{_datadir}/LICENSES
%{_docdir}/HTML
