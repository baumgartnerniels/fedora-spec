%global debug_package %{nil}

Name:    common-music
Version: 3.10.2
Release: 2%{?dist}
Summary: Common Music (CM) is a real-time music composition system implemented in JUCE/C++ and Scheme.
URL:     https://sourceforge.net/projects/commonmusic
Group:   Applications/Multimedia

License: GPLv2+

# original tarfile can be found here:
Source0: https://sourceforge.net/projects/commonmusic/files/cm/%{version}/cm-%{version}.zip

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++ make
BuildRequires: premake4
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: alsa-lib-devel
BuildRequires: gsl-devel
BuildRequires: freetype-devel
BuildRequires: gtk3-devel
BuildRequires: mesa-libGLU-devel
BuildRequires: libXext-devel
BuildRequires: libXinerama-devel

%description
Common Music is a music composition system that transforms high-level algorithmic representations of musical processes and structure into a variety of control protocols for sound synthesis and display.
Its main user application is Grace (Graphical Realtime Algorithmic Composition Environment) a drag-and-drop, cross-platform app implemented in JUCE (C++) and S7 Scheme.
In Grace musical algorithms can run in real time, or faster-than-real time when doing file-based composition.
Grace provides two coding languages for designing musical algorithms: S7 Scheme, and SAL, an easy-to-learn but expressive algol-like language. 

%prep
%setup -qn cm-%{version}

# For Fedora 29
%if 0%{?fedora} >= 29
  sed -i -e "112,123d" juce/modules/juce_graphics/colour/juce_PixelFormats.h
%endif

%build

find juce/modules -type f -exec chmod a-x {} \;

premake4 --with-jack
make config=release

%install

%__install -m 755 -d %{buildroot}/%{_bindir}/
%__install -m 755 bin/Grace %{buildroot}%{_bindir}/

%__install -m 755 -d %{buildroot}/%{_datadir}/cm/res/
cp -ra res/* %{buildroot}/%{_datadir}/cm/res/

%files
%doc readme.text
%{_bindir}/*
%{_datadir}/cm/res/*

%changelog
* Tue May 2 2019 Yann Collette <ycollette.nospam@free.fr> - 3.10.2-2
- Fix release mode and fix for Fedora 30

* Mon Mar 4 2019 Yann Collette <ycollette.nospam@free.fr> - 3.10.2-1
- initial specfile
