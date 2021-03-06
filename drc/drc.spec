%global debug_package %{nil}

Name:    drc
Version: 3.2.3
Release: 1%{?dist}
Summary: Digital Room Correction
Group:   Applications/Multimedia
License: LGPLv2+
URL:     https://sourceforge.net/projects/drc-fir/
Source0: https://sourceforge.net/projects/drc-fir/files/drc-fir/%{version}/drc-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gsl-devel gcc gcc-c++ make

%description
Welcome to the home page of DRC. DRC is a program used to generate correction filters for acoustic compensation of HiFi and audio systems in general, including listening room compensation. DRC generates just the FIR correction filters, which can be used with a real time or offline convolver to provide real time or offline correction. DRC doesn't provide convolution features, and provides only some simplified, although really accurate, measuring tools.
For further informations see the documentation section, which includes the full manual of the current version of DRC and a complete set of measurements showing the effect of the DRC correction in a real life situation.
DRC is available for free and is released under the terms of the GNU General Public License. See the documentation for details.

%prep
%setup -q -n drc-%{version}

%build

cd source

make %{?_smp_mflags} VERBOSE=1

%install

cd source

make install DESTDIR=%{buildroot}

cd ..

mkdir %{buildroot}%{_datadir}/drc/doc
cp -r doc/* %{buildroot}%{_datadir}/drc/doc

mkdir %{buildroot}%{_datadir}/drc/samples
cp sample/*.drc sample/*.txt sample/*.pcm %{buildroot}%{_datadir}/drc/samples/

%files
%doc readme.txt drc-%{version}.lsm
%license COPYING
%{_bindir}/*
%{_datadir}/*

%changelog
* Mon Aug 5 2019 Yann Collette <ycollette.nospam@free.fr> - 3.2.3-1
- initial spec file
