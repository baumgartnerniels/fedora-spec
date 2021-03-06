# Global variables for github repository
%global commit0 c1e168df0830a6b84295ebdd30cd48726a791103
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
%global debug_package %{nil}

# git clone https://github.com/x42/avldrums.lv2.git
# cd avldrums.lv2
# git checkout v0.4.1
# git submodule init
# git submodule update
# find . -name "*.git" -exec rm -rf {} \; -print
# cd ..
# tar cvfz avldrums.lv2.tar.gz avldrums.lv2

Name:    lv2-avldrums-x42-plugin
Version: 0.4.1.%{shortcommit0}
Release: 1%{?dist}
Summary: LV2 Analogue simulation of a tube preamp

Group:   Applications/Multimedia
License: GPLv2+
URL:     https://github.com/x42/avldrums.lv2.git
Source0: avldrums.lv2.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: lv2-devel
BuildRequires: cairo-devel
BuildRequires: pango-devel
BuildRequires: mesa-libGL-devel
BuildRequires: mesa-libGLU-devel

%description
avldrums.lv2 is a simple Drum Sample Player Plugin, dedicated to the http://www.bandshed.net/avldrumkits/

%prep
%setup -qn avldrums.lv2

%build

%make_build PREFIX=%{buildroot}%{_usr} LV2DIR=%{buildroot}%{_libdir}/lv2

%install 

make submodules
make PREFIX=%{buildroot}%{_usr} LV2DIR=%{buildroot}%{_libdir}/lv2 install

%files
%{_libdir}/lv2/avldrums.lv2/*

%changelog
* Tue Dec 31 2019 Yann Collette <ycollette.nospam@free.fr> - 0.4.1
- update to 0.4.1

* Thu Oct 17 2019 Yann Collette <ycollette.nospam@free.fr> - 0.4.0
- update to 0.4.0

* Tue Feb 12 2019 Yann Collette <ycollette.nospam@free.fr> - 0.3.3
- update to 0.3.3

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.3.0
- update for Fedora 29
- update to f670fcdd228f3abf291cc8ec8fd14fe09fa1bfaf

* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> - 0.3.0
- update to 43b28a761ea980d176b66347a6f8a44fb4e84611

* Mon Nov 20 2017 Yann Collette <ycollette.nospam@free.fr> - 0.2.2
- Initial build
