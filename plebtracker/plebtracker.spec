%global debug_package %{nil}

# Global variables for github repository
%global commit0 f6aa7078c3f39e9c8b025e70e7dbeab19119e213
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Summary: PLEBtracker is a chiptune tracker for making chiptune-like music on a modern computer.
Name:    plebtracker
Version: 0.1
Release: 1%{?dist}
License: GPL
Group:   Applications/Multimedia
URL:     https://github.com/danfrz/PLEBTracker

Source0: https://github.com/danfrz/PLEBTracker/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: make
BuildRequires: alsa-lib-devel
BuildRequires: ncurses-devel
BuildRequires: fftw-devel

Requires: alsa-utils
Requires: inotify-tools

%description
PLEBTracker is a chiptune tracker for making chiptune-like music on a modern computer.

%prep
%setup -qn PLEBTracker-%{commit0}

sed -i -e "s|-lncurses|-lncurses -lncursesw|g"  Tracker/src/Makefile
sed -i -e "s|CFLAGS=|CFLAGS=%{build_cflags} |g" Tracker/src/Makefile
sed -i -e "s|CFLAGS=|CFLAGS=%{build_cflags} |g" Interpreter/src/Makefile

%build

cd Interpreter/src
%{__make} DESTDIR=%{buildroot} PREFIX=/usr
cd ../..
cd Tracker/src
%{__make} DESTDIR=%{buildroot} PREFIX=/usr

%install

%{__rm} -rf %{buildroot}

%__install -m 755 -d %{buildroot}/%{_bindir}/
%__install -m 755 -d %{buildroot}/%{_datadir}/man/man1
%__install -m 755 -d %{buildroot}/%{_datadir}/plebtracker/docs/
%__install -m 755 -d %{buildroot}/%{_datadir}/plebtracker/examples/

## INTERPRETER

cd Interpreter/src
%__install -m 644 plebplay   %{buildroot}/%{_bindir}/
%__install -m 644 plebitp    %{buildroot}/%{_bindir}/
%__install -m 644 plebrender %{buildroot}/%{_bindir}/

%__install -m 644 ../doc/plebitp.1    %{buildroot}/%{_datadir}/man/man1/
%__install -m 644 ../doc/plebplay.1   %{buildroot}/%{_datadir}/man/man1/
%__install -m 644 ../doc/plebrender.1 %{buildroot}/%{_datadir}/man/man1/
cd ../..

## TRACKER

cd Tracker/src
%__install -m 644 plebtrk       %{buildroot}/%{_bindir}/
%__install -m 644 plebtrkdaemon %{buildroot}/%{_bindir}/
%__install -m 644 plebtrkraw    %{buildroot}/%{_bindir}/

%__install -m 644 ../doc/plebtrk.1       %{buildroot}/%{_datadir}/man/man1/
%__install -m 644 ../doc/plebtrkdaemon.1 %{buildroot}/%{_datadir}/man/man1/
%__install -m 644 ../doc/plebtrkraw.1    %{buildroot}/%{_datadir}/man/man1/
cd ../..

## DIVERS

%__install -m 644 docs/*.txt %{buildroot}/%{_datadir}/plebtracker/docs/
%__install -m 644 docs/*.pdf %{buildroot}/%{_datadir}/plebtracker/docs/

%__install -m 644 examples/*.plb %{buildroot}/%{_datadir}/plebtracker/examples/

%clean

%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENSE README.md
%{_bindir}/*
%{_datadir}/*

%changelog
* Fri Jun 7 2019 Yann Collette <ycollette dot nospam at free.fr> 0.1-1
- Initial release of spec file
