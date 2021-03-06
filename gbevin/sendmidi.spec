%global debug_package %{nil}

Name:    sendmidi
Version: 1.0.14
Release: 2%{?dist}
Summary: A command line tool to send MIDI event
License: GPLv3

URL:     https://github.com/gbevin/SendMIDI
Source0: https://github.com/gbevin/SendMIDI/archive/%{version}.tar.gz#/SendMIDI-%{version}.tar.gz

BuildRequires: gcc gcc-c++
BuildRequires: libX11-devel
BuildRequires: xcb-util-cursor-devel
BuildRequires: libxkbcommon-x11-devel
BuildRequires: cairo-devel
BuildRequires: fontconfig-devel
BuildRequires: freetype-devel
BuildRequires: xcb-util-keysyms-devel
BuildRequires: xcb-util-devel
BuildRequires: libcurl-devel
BuildRequires: alsa-lib-devel

%description
SendMIDI is a multi-platform command-line tool makes it very easy to quickly
send MIDI messages to MIDI devices from your computer.

%prep
%autosetup -n SendMIDI-%{version}

%build

cd Builds/LinuxMakefile

# %make_build STRIP=true CPPFLAGS="%{optflags}"
%make_build CPPFLAGS="%{optflags}"

%install 

cd Builds/LinuxMakefile

%__install -m 755 -d %{buildroot}%{_bindir}/
%__install -m 755 -p build/sendmidi %{buildroot}/%{_bindir}/

%files
%{_bindir}/*

%changelog
* Thu Jul 16 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.14-2
- fix permission

* Thu Jul 16 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.14-1
- Initial spec file
