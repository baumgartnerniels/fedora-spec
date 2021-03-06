# Global variables for github repository
%global commit0 250844ade88552f0e481bc911cca7794c1e68a3f
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
#%global debug_package %{nil}

Name:    caps-lv2
Version: 0.9.26.%{shortcommit0}
Release: 1%{?dist}
Summary: Caps LV2 set of plugins from portalmod

Group:   Applications/Multimedia
License: GPLv2+

URL:     https://github.com/moddevices/caps-lv2
Source0: https://github.com/moddevices/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel

%description
Caps LV2 set of plugins from portalmod

%prep
%setup -qn %{name}-%{commit0}

%build

make LV2_DEST=%{buildroot}%{_libdir}/lv2 %{?_smp_mflags}

%install 
make LV2_DEST=%{buildroot}%{_libdir}/lv2 %{?_smp_mflags} install

%files
%{_libdir}/lv2/*

%changelog
* Sat Mar 23 2019 Yann Collette <ycollette.nospam@free.fr> - 0.9.26
- update to 0.9.26

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.9
- update for Fedora 29

* Wed Oct 25 2017 Yann Collette <ycollette.nospam@free.fr> - 0.9
- Update to latest master version

* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.9
- Initial build
