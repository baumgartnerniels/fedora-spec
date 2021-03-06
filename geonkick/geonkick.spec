Name:    geonkick
Version: 2.3.3
Release: 1%{?dist}
Summary: Drum Software Synthesizer
URL:     https://gitlab.com/iurie-sw/geonkick
License: GPLv3

Source0: https://gitlab.com/iurie-sw/%{name}/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: lv2-devel
BuildRequires: libsndfile-devel
BuildRequires: rapidjson-devel
BuildRequires: cmake make
BuildRequires: desktop-file-utils
BuildRequires: redkite
BuildRequires: libX11-devel
BuildRequires: cairo-devel

%description
Geonkick is a synthesizer that can synthesize elements of percussion.
The most basic examples are: kick drums, snares, hit-hats, shakers, claps, steaks.

%prep
%autosetup -n %{name}-v%{version}

sed -i -e "s|\${CMAKE_INSTALL_PREFIX}/lib|\${CMAKE_INSTALL_PREFIX}/%{_lib}|g" plugin/lv2/CMakeLists.txt

%build

%set_build_flags

mkdir build
cd build

%cmake -DCMAKE_BUILD_TYPE=RELEASE \
       -DCMAKE_CXX_FLAGS="$CXXFLAGS -I/usr/include/redkite" \
       -DCMAKE_C_FLAGS="$CFLAGS -I/usr/include/redkite" \
       -DREDKITE_LIBRARY_DIR="/usr/%{_lib}" \
       ..

%make_build

%install

cd build

%make_install

%files
%doc README.md doc/Documentation.md
%license LICENSE
%{_bindir}/*
%{_libdir}/*
%{_datadir}/*

%changelog
* Mon Jul 27 2020 Yann Collette <ycollette.nospam@free.fr> - 2.3.3-1
- Update to 2.3.3-1

* Sat Jul 25 2020 Yann Collette <ycollette.nospam@free.fr> - 2.3.2-1
- Update to 2.3.2-1

* Fri Jul 24 2020 Yann Collette <ycollette.nospam@free.fr> - 2.3.1-1
- Update to 2.3.1-1

* Fri Jun 12 2020 Yann Collette <ycollette.nospam@free.fr> - 2.2.3-1
- Update to 2.2.3-1

* Thu Jun 11 2020 Yann Collette <ycollette.nospam@free.fr> - 2.2.1-1
- Update to 2.2.1

* Wed May 13 2020 Yann Collette <ycollette.nospam@free.fr> - 2.1.1-1
- Update to 2.1.1

* Sat May 09 2020 Bruno Vernay <brunovern.a@gmail.com> - 2.1.0-1
- Update to 2.1.0, update the URL, add make dependency, add doc

* Fri Apr 17 2020 Yann Collette <ycollette.nospam@free.fr> - 2.0.0-1
- update to 2.0.0

* Sun Apr 5 2020 Yann Collette <ycollette.nospam@free.fr> - 1.10.0-1
- update to 1.10.0

* Sat Dec 28 2019 Yann Collette <ycollette.nospam@free.fr> - 1.9.2-1
- update to 1.9.2

* Mon Oct 7 2019 Yann Collette <ycollette.nospam@free.fr> - 1.9.0-1
- update to 1.9.0

* Sun Aug 11 2019 Yann Collette <ycollette.nospam@free.fr> - 1.8.1-1
- update to 1.8.1

* Fri Aug 9 2019 Yann Collette <ycollette.nospam@free.fr> - 1.8.0-1
- update to 1.8.0

* Wed Jun 5 2019 Yann Collette <ycollette.nospam@free.fr> - 1.6.0-1
- update to 1.6.0

* Thu May 23 2019 Yann Collette <ycollette.nospam@free.fr> - 1.5.3-1
- update to 1.5.3

* Wed May 22 2019 Yann Collette <ycollette.nospam@free.fr> - 1.5.2-1
- update to 1.5.2

* Tue May 21 2019 Yann Collette <ycollette.nospam@free.fr> - 1.5.1-1
- update to 1.5.1

* Mon May 20 2019 Yann Collette <ycollette.nospam@free.fr> - 1.5-1
- initial version of the spec file
