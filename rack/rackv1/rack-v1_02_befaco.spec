# Global variables for github repository
%global commit0 1467acb4b4ba3257ffc93941b2bae61b42c0c6f5
%global gittag0 v0.6.0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
%global debug_package %{nil}

Name:    rack-v1-Befaco
Version: 0.6.0
Release: 3%{?dist}
Summary: A plugin for Rack

Group:   Applications/Multimedia
License: GPLv2+
URL:     https://github.com/VCVRack/Befaco

# git clone https://github.com/VCVRack/Rack.git Rack
# cd Rack
# git checkout v1.1.6
# git submodule init
# git submodule update
# find . -name ".git" -exec rm -rf {} \;
# cd dep
# wget https://bitbucket.org/jpommier/pffft/get/29e4f76ac53b.zip
# unzip 29e4f76ac53b.zip
# mkdir include
# cp jpommier-pffft-29e4f76ac53b/*.h include/
# rm  29e4f76ac53b.zip
# cd ../..
# tar cvfz Rack.tar.gz Rack/*

Source0: Rack.tar.gz
Source1: https://github.com/VCVRack/Befaco/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: cmake sed
BuildRequires: alsa-lib-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: libsamplerate-devel
BuildRequires: libzip-devel
BuildRequires: glew-devel
BuildRequires: glfw-devel
BuildRequires: portmidi-devel
BuildRequires: portaudio-devel
BuildRequires: libcurl-devel
BuildRequires: openssl-devel
BuildRequires: jansson-devel
BuildRequires: gtk2-devel
BuildRequires: rtaudio-devel
BuildRequires: rtmidi-devel
BuildRequires: speex-devel
BuildRequires: speexdsp-devel
BuildRequires: jq

%description
Based on Befaco - https://www.befaco.org/en/ Eurorack modules.

%prep
%setup -qn Rack

CURRENT_PATH=`pwd`

sed -i -e "s/-march=core2//g" compile.mk
sed -i -e "s/-march=nocona//g" compile.mk
sed -i -e "s/-ffast-math//g" compile.mk
sed -i -e "s/-fno-finite-math-only//g" compile.mk
sed -i -e "s/-O3/-O2/g" compile.mk

# %{build_cxxflags}
echo "CXXFLAGS += -I$CURRENT_PATH/include -I$CURRENT_PATH/dep/nanovg/src -I$CURRENT_PATH/dep/nanovg/example -I$CURRENT_PATH/dep/nanosvg/src -I/usr/include/rtaudio -I/usr/include/rtmidi -I$CURRENT_PATH/dep/oui-blendish -I$CURRENT_PATH/dep/osdialog -I$CURRENT_PATH/dep/jpommier-pffft-29e4f76ac53b -I$CURRENT_PATH/dep/include" >> compile.mk

sed -i -e "s/-Wl,-Bstatic//g" Makefile
sed -i -e "s/-lglfw3/dep\/lib\/libglfw3.a/g" Makefile

sed -i -e "s/dep\/lib\/libGLEW.a/-lGLEW/g" Makefile
sed -i -e "s/dep\/lib\/libglfw3.a/dep\/%{_lib}\/libglfw3.a/g" Makefile
sed -i -e "s/dep\/lib\/libjansson.a/-ljansson/g" Makefile
sed -i -e "s/dep\/lib\/libcurl.a/-lcurl/g" Makefile
sed -i -e "s/dep\/lib\/libssl.a/-lssl/g" Makefile
sed -i -e "s/dep\/lib\/libcrypto.a/-lcrypto/g" Makefile
sed -i -e "s/dep\/lib\/libzip.a/-lzip/g" Makefile
sed -i -e "s/dep\/lib\/libz.a/-lz/g" Makefile
sed -i -e "s/dep\/lib\/libspeexdsp.a/-lspeexdsp/g" Makefile
sed -i -e "s/dep\/lib\/libsamplerate.a/-lsamplerate/g" Makefile
sed -i -e "s/dep\/lib\/librtmidi.a/-lrtmidi/g" Makefile
sed -i -e "s/dep\/lib\/librtaudio.a/-lrtaudio/g" Makefile

mkdir befaco_plugin
tar xvfz %{SOURCE1} --directory=befaco_plugin --strip-components=1 

%build

cd befaco_plugin
make RACK_DIR=.. DESTDIR=%{buildroot} PREFIX=/usr LIBDIR=%{_lib} %{?_smp_mflags} dist

%install 

mkdir -p %{buildroot}%{_libexecdir}/Rack1/plugins-v1/Befaco/
cp -r befaco_plugin/dist/Befaco/* %{buildroot}%{_libexecdir}/Rack1/plugins-v1/Befaco/

%files
%{_libexecdir}/*

%changelog
* Thu Jan 30 2020 Yann Collette <ycollette.nospam@free.fr> - 0.6.0-3
- update to 1467acb4b4ba3257ffc93941b2bae61b42c0c6f5 to get plugin.json

* Sun Nov 18 2018 Yann Collette <ycollette.nospam@free.fr> - 0.6.0-2
- initial specfile
