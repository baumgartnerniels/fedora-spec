Summary: zita-bls1 is a digital implementation of the 'Blumlein Shuffler', used to convert binaural signals into a form suitable for reproduction on a conventional stereo speaker pair. 
Name:    zita-bls1
Version: 0.3.3
Release: 1%{?dist}
License: GPL
Group:   Applications/Multimedia
URL:     http://kokkinizita.linuxaudio.org/linuxaudio/
Source0: https://kokkinizita.linuxaudio.org/linuxaudio/downloads/%{name}-%{version}.tar.bz2

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: cairo-devel
BuildRequires: clthreads-devel clxclient-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libX11-devel libXft-devel
BuildRequires: zita-convolver-devel
BuildRequires: fftw-devel

%description
zita-bls1 is a digital implementation of the 'Blumlein Shuffler', used to convert binaural signals into a form suitable for reproduction on a conventional stereo speaker pair.

%prep
%setup -q

%build
rm -rf $RPM_BUILD_ROOT

# Force Fedora's optflags
sed -i 's|-O2|%{optflags}|' source/Makefile

pushd source
make PREFIX=%{_prefix}
popd

%install
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_datadir}/zita-bls1/
mkdir -p $RPM_BUILD_ROOT%{_datadir}/doc/

pushd source
make PREFIX=%{_prefix} DESTDIR=$RPM_BUILD_ROOT install
popd

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc AUTHORS README doc
%license COPYING
%{_bindir}/*
%{_datadir}/zita-bls1/*

%changelog
* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 0.3.3-1
- update for Fedora 29

* Fri Sep 7 2018 Yann Collette <ycollette.nospam@free.fr> - 0.3.3-1
- initial release
