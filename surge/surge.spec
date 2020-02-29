# Disable production of debug package. Problem with fedora 23
%global debug_package %{nil}

# Global variables for github repository
%global commit0 da96f74b1cc96f936192282e300d93cf65d16c58
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    surge
Version: 1.6.6.%{shortcommit0}
Release: 1%{?dist}
Summary: A VST2 synthetizer

Group:   Applications/Multimedia
License: GPLv2+

# git clone https://github.com/surge-synthesizer/surge
# cd surge
# git checkout origin/release/1.6.6
# git submodule init
# git submodule update
# cd vst3dsk
# git submodule init
# git submodule update
# cd ..
# find . -name .git -exec rm -rf {} \;
# cd ..
# tar cvfz surge.tar.gz surge/*

URL:     https://github.com/surge-synthesizer/surge
Source0: surge.tar.gz
Source1: http://ycollette.free.fr/LMMS/vst.tar.bz2

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: libX11-devel
BuildRequires: premake5
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: rsync
BuildRequires: python2
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel

%description
A VST2 synthetizer

%prep
%setup -qn %{name}

%ifarch x86_64
  sed -i -e "s/lib\/vst/lib64\/vst/g" build-linux.sh
%endif

sed -i -e "s/python/python2/g" premake5.lua

%build

tar xvfj %{SOURCE1}

export VST2SDK_DIR=vst/vstsdk2.4/

./build-linux.sh clean-all
./build-linux.sh -p vst2 build

%install 

export HOME=.
mkdir .vst
mkdir .local/
mkdir .local/share

./build-linux.sh -p vst2 -l install

%__install -m 755 -d %{buildroot}%{_libdir}/vst/
%__install -m 644 .vst/*.so %{buildroot}/%{_libdir}/vst/

%__install -m 755 -d %{buildroot}%{_datadir}/Surge/
rsync -rav .local/share/Surge/* %{buildroot}/%{_datadir}/Surge/

%files
%{_libdir}/*
%{_datadir}/*

%changelog
* Sat Feb 29 2020 Yann Collette <ycollette.nospam@free.fr> - 1.6.6-1
- update to 1.6.6-1

* Tue Feb 4 2020 Yann Collette <ycollette.nospam@free.fr> - 1.6.5-1
- update to 1.6.5-1

* Sun Nov 3 2019 Yann Collette <ycollette.nospam@free.fr> - 1.6.3-1
- update to 1.6.3-1

* Thu Sep 26 2019 Yann Collette <ycollette.nospam@free.fr> - 1.6.2.1
- update to 1.6.2.1

* Fri May 3 2019 Yann Collette <ycollette.nospam@free.fr> - 1.6.0.b9
- update to beta9

* Mon Apr 29 2019 Yann Collette <ycollette.nospam@free.fr> - 1.6.0.b3
- Initial spec file
