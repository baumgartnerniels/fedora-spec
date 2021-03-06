# Disable production of debug package. Problem with fedora 23
# %global debug_package %{nil}

# Global variables for github repository
%global commit0 094dec9b009268814751d3801fc7a5068381c90b
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    glava
Version: 1.6.3
Release: 1%{?dist}
Summary: GLava is an OpenGL audio spectrum visualizer
URL:     https://github.com/wacossusca34/glava.git
Group:   Applications/Multimedia

License: GPLv2+

# original tarfile can be found here:
Source0: https://github.com/wacossusca34/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++ make
BuildRequires: libXrender-devel
BuildRequires: libX11-devel
BuildRequires: pulseaudio-libs-devel
BuildRequires: glfw-devel
BuildRequires: libXcomposite-devel
BuildRequires: libXext-devel

%description
GLava is an OpenGL audio spectrum visualizer. Its primary use case is for desktop windows or backgrounds. Displayed to the left is the radial shader module. Development is active, and reporting issues is encouranged.

%prep
%setup -qn %{name}-%{commit0}

%build

make  %{?_smp_mflags} CFLAGS="%{build_cxxflags}" 

%install

make  %{?_smp_mflags} CFLAGS="%{build_cxxflags}" DESTDIR=%{buildroot} install

%files
%doc README.md LICENSE CONTRIBUTING.md

%{_bindir}/*
%{_sysconfdir}/*

%changelog
* Wed Nov 13 2019 Yann Collette <ycollette.nospam@free.fr> - 1.6.3-1
- update to 1.6.3-1

* Wed Nov 6 2019 Yann Collette <ycollette.nospam@free.fr> - 1.5.8-1
- fix for Fedora 31

* Sun Dec 2 2018 Yann Collette <ycollette.nospam@free.fr> - 1.5.8-1
- initial spec file
