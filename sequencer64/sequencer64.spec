# Global variables for github repository
%global commit0 e0873f073af03ac69d48dfe91c98fb4baf4b04c8
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global debug_package %{nil}

Name:    sequencer64
Version: 0.96.8
Release: 2%{?dist}
Summary: MIDI sequencer

License: GPL
URL:     https://github.com/ahlstromcj/sequencer64
Source0: https://github.com/ahlstromcj/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source1: https://github.com/ahlstromcj/sequencer64-doc/archive/0.95.2.tar.gz#/%{name}-doc-0.95.2.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: alsa-lib-devel
BuildRequires: gtkmm24-devel
BuildRequires: lash-devel
BuildRequires: rtmidi-devel
BuildRequires: git
BuildRequires: autoconf
BuildRequires: automake
BuildRequires: libtool
BuildRequires: pkgconfig

%description
Sequencer64 is a reboot of seq24, extending it with many new features.
The heart of seq24 remains intact.

%package devel
Summary:  Development files for %{name}
Requires: %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains header files for %{name}.

%package doc
Summary:  Documentation for %{name}
Requires: %{name} = %{version}-%{release}

%description doc
The %{name}-doc package contains documentation for %{name}.

%prep
%autosetup -n %{name}-%{commit0}

tar xvfz %{SOURCE1}

%build

sh autogen.sh

%configure
%make_build CXXFLAGS="-include string %{build_cxxflags}" 

%install

%make_install

%__install -m 755 -d %{buildroot}/%{_datadir}/%{name}/doc/
%__install -m 644 %{name}-doc-0.95.2/pdf/sequencer64-user-manual.pdf %{buildroot}%{_datadir}/%{name}/doc/

%files
%doc ChangeLog INSTALL NEWS README README.jack VERSION TODO
%{_bindir}/*
%{_libdir}/*
%{_datadir}/*
%exclude %{_datadir}/%{name}/doc/**

%files devel
%{_includedir}/*

%files doc
%{_datadir}/%{name}/doc/**

%changelog
* Mon Jul 6 2020 Yann Collette <ycollette.nospam@free.fr> - 0.96.8-2
- update to 0.96.8-2

* Tue May 5 2020 Yann Collette <ycollette.nospam@free.fr> - 0.96.7-2
- update to 0.96.7-2 - add documentation

* Tue May 5 2020 Yann Collette <ycollette.nospam@free.fr> - 0.96.7-1
- update to 0.96.7-1

* Mon Nov 19 2018 L.L.Robinson <baggypants@fedoraproject.org> - 0.96.1-1
- initial version
