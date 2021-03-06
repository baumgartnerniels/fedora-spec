Name:      sfizz
Version:   0.4.0
Release:   2%{?dist}
License:   BSD-2-Clause
Summary:   Sampler plugin and library for SFZ instruments
Url:       https://github.com/sfztools/sfizz
Source:    sfizz-0.4.0.tar.gz

# git clone https://github.com/sfztools/sfizz sfizz-0.4.0
# cd sfizz-0.4.0
# git checkout 0.4.0
# git submodule init
# git submodule update
# find . -name .git -exec rm -rf {} \;
# cd ..
# tar cvfz sfizz-0.4.0.tar.gz sfizz-0.4.0/*

Requires:  libsndfile
Requires:  jack-audio-connection-kit

BuildRequires: gcc gcc-c++
BuildRequires: cmake
BuildRequires: libatomic
BuildRequires: libsndfile-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libX11-devel
BuildRequires: freetype-devel
BuildRequires: xcb-util-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: cairo-devel
BuildRequires: jack-audio-connection-kit-devel

%description
Sfizz is a musical sampler, available as a LV2 plugin for musicians, and
a library for developers.

%package devel
Summary:   Header files for Sfizz
Requires:  %{name} = %{version}-%{release}

%description devel
Header files for the Sfizz library.

%prep
%autosetup -n %{name}-%{version}

%build

mkdir build
cd build
%cmake -DLV2PLUGIN_INSTALL_DIR=%{_libdir}/lv2 \
       -DVSTPLUGIN_INSTALL_DIR=%{_libdir}/vst \
       -DSFIZZ_JACK=ON \
       -DSFIZZ_LV2=ON \
       -DSFIZZ_VST=ON \
       -DENABLE_LTO=OFF \
       -DCMAKE_CXX_FLAGS="-include cstdio" \
       -DBUILD_SHARED_LIBS=OFF \
       ..

%make_build VERBOSE=1

%install

cd build
%make_install

%files
%doc README.md GOVERNANCE.md CONTRIBUTING.md AUTHORS.md
%license LICENSE.md
%{_bindir}/sfizz_jack
%{_bindir}/sfizz_render
%{_libdir}/libsfizz.so.*
%dir %{_libdir}/lv2
%dir %{_libdir}/lv2/sfizz.lv2
%{_libdir}/lv2/sfizz.lv2/*
%{_libdir}/vst/sfizz.vst3/*

%files devel
%{_libdir}/libsfizz.so
%{_includedir}/sfizz.h
%{_includedir}/sfizz.hpp
%dir %{_libdir}/pkgconfig
%{_libdir}/pkgconfig/sfizz.pc
%exclude %{_libdir}/libsfizz.a

%changelog
* Fri Jul 24 2020 Yann Collette <ycollette.nospam@free.fr> - 0.4.0-2
- update to 0.4.0-2

* Sun Apr 5 2020 Yann Collette <ycollette.nospam@free.fr> - 0.3.2-2
- update to 0.3.2-2

* Sun Mar 15 2020 Yann Collette <ycollette.nospam@free.fr> - 0.3.1-1
- update to 0.3.1

* Sun Feb 2 2020 Yann Collette <ycollette.nospam@free.fr> - 0.2.0-1
- update for Fedora

* Fri Jan 31 2020 Jean Pierre Cimalando <jp-dev@inbox.ru> - 0.2.0-1
- initial release of the spec file
