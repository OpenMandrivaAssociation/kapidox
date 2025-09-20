%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 80 ] && echo -n un; echo -n stable)
%define debug_package %{nil}

Name: kapidox
Version:	6.18.0
Release:	1
Source0: http://download.kde.org/%{stable}/frameworks/%(echo %{version} |cut -d. -f1-2)/%{name}-%{version}.tar.xz
Summary: Scripts and data for building API documentation
URL: https://kde.org/
License: GPL
Group: System/Libraries
BuildRequires: cmake(ECM)
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: cmake(KF6DocTools)
BuildRequires: python%{pyver}dist(setuptools)

%description
Scripts and data for building API documentation (dox)
in a standard format and style.

%prep
%autosetup -p1

%build
python setup.py build

%install
python setup.py install --prefix=%{_prefix} --root=%{buildroot}

%files
%{_bindir}/kapidox-generate
%{_bindir}/kapidox-depdiagram-generate
%{_bindir}/kapidox-depdiagram-prepare
%{_bindir}/depdiagram_generate_all
%{_prefix}/lib/python*/site-packages/kapidox
%{_prefix}/lib/python*/site-packages/kapidox*.egg-info
