%global debug_package %{nil}

# Global variables for github repository
%global commit0 e9c834e51f407fd33d7175c0dad421cdad44e154
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    airwindows
Version: 0.0.1
Release: 1%{?dist}
Summary: A set of VST2 plugins

License: MIT
URL:     https://github.com/airwindows/airwindows

Source0: https://github.com/airwindows/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
# Source1: https://web.archive.org/web/20181016150224/https://download.steinberg.net/sdk_downloads/vstsdk3610_11_06_2018_build_37.zip
Source1: http://ycollette.free.fr/LMMS/vstsdk3610_11_06_2018_build_37.zip

BuildRequires: gcc gcc-c++
BuildRequires: wget
BuildRequires: unzip
BuildRequires: cmake

%description
A set of VST plugins

%prep
%setup -qn %{name}-%{commit0}

unzip %{SOURCE1}

mkdir -p plugins/LinuxVST/include/vstsdk/
mkdir -p plugins/LinuxVST/include/vstsdk/pluginterfaces/vst2.x/

cp VST_SDK/VST2_SDK/pluginterfaces/vst2.x/*    plugins/LinuxVST/include/vstsdk/pluginterfaces/vst2.x/
cp VST_SDK/VST2_SDK/public.sdk/source/vst2.x/* plugins/LinuxVST/include/vstsdk/

sed -i -e "s/add_subdirectory/include_directories/g"     plugins/LinuxVST/CMakeLists.txt
sed -i -e "s/add_compile_options/#add_compile_options/g" plugins/LinuxVST/CMakeLists.txt

%build

cd plugins/LinuxVST

rm -rf build
mkdir build
cd build

%cmake ..

%make_build 

%install 

cd plugins/LinuxVST/

cd build

%__install -m 755 -d %{buildroot}%{_libdir}/vst/
%__install -m 644 *.so %{buildroot}/%{_libdir}/vst/

%files
%doc plugins/LinuxVST/README.md
%license plugins/LinuxVST/LICENSE
%{_libdir}/*

%changelog
* Wed Jul 29 2020 Yann Collette <ycollette.nospam@free.fr> - 1.0.0-1
- Initial spec file
