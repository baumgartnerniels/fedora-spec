# Global variables for github repository
%global commit0 d404edc4d79fb59ee77bb9e87ce51de050e70a88
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
%global debug_package %{nil}

Name:    mod-pitchshifter
Version: 0.9.%{shortcommit0}
Release: 1%{?dist}
Summary: mod-pitchshifter LV2 set of plugins from portalmod

Group:   Applications/Multimedia
License: GPLv2+

URL:     https://github.com/portalmod/mod-pitchshifter
Source0: https://github.com/portalmod/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: fftw-devel
BuildRequires: fftw
BuildRequires: python3
BuildRequires: python3-mpmath
BuildRequires: armadillo-devel
BuildRequires: SuperLU-devel

%description
mod-pitchshifter LV2 set of plugins from portalmod

%prep
%setup -qn %{name}-%{commit0}

%build
make INSTALL_PATH=%{buildroot}%{_libdir}/lv2 %{?_smp_mflags}

%install 
make INSTALL_PATH=%{buildroot}%{_libdir}/lv2 %{?_smp_mflags} install

%files
%{_libdir}/lv2/*

%changelog
* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.9
- update for Fedora 29

* Wed Oct 25 2017 Yann Collette <ycollette.nospam@free.fr> - 0.9
- update to latest master version

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.9
- Initial build
