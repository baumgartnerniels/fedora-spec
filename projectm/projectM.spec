# Global variables for github repository
%global commit0 64f54507dc6a84ae3d765fd946cf9a4689742a75
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

Name:    projectM-mao
Version: 3.1.1rc7
Release: 11%{?dist}
Summary: The libraries for the projectM music visualization plugin
Group:   Applications/Multimedia
License: LGPLv2+
URL:     https://github.com/projectM-visualizer/projectm
Source0: https://github.com/projectM-visualizer/projectm/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Source1: milkdrop-script.txt

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires: gcc gcc-c++
BuildRequires: automake autoconf libtool
BuildRequires: ftgl-devel glew-devel
BuildRequires: libgomp pulseaudio-libs-devel
BuildRequires: SDL2-devel
BuildRequires: jack-audio-connection-kit-devel desktop-file-utils
BuildRequires: pulseaudio-libs-devel
BuildRequires: dejavu-sans-mono-fonts, dejavu-sans-fonts
BuildRequires: glm-devel
BuildRequires: ftgl-devel

Requires: dejavu-sans-mono-fonts, dejavu-sans-fonts

%description
projectM is an awesome music visualizer. There is nothing better in the world
of Unix. projectM's greatness comes from the hard work of the community. Users
like you can create presets that connect music with incredible visuals.
projectM is an LGPL'ed reimplementation of Milkdrop under OpenGL. All projectM
requires is a video card with 3D acceleration and your favorite music.

%package    devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name}%{?_isa} = %{version}-%{release}, pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package -n projectM-mao-jack
Summary:    The projectM visualization plugin for jack
Group:      Applications/Multimedia
License:    GPLv2+ and MIT

%description -n projectM-mao-jack
This package allows the use of the projectM visualization plugin through any
JACK compatible applications.

%package -n projectM-mao-pulseaudio
Summary:    The projectM visualization plugin for pulseaudio
Group:      Applications/Multimedia
License:    GPLv2+ and MIT

%description -n projectM-mao-pulseaudio
This package allows the use of the projectM visualization plugin through any
pulseaudio compatible applications.

%package -n projectM-mao-alsa
Summary:    The projectM visualization plugin for ALSA
Group:      Applications/Multimedia
License:    GPLv2+ and MIT

%description -n projectM-mao-alsa
This package allows the use of the projectM visualization plugin through any
ALSA compatible applications.

%package -n projectM-mao-SDL
Summary:    The projectM visualization plugin for SDL
Group:      Applications/Multimedia
License:    GPLv2+ and LGPLv2+ and MIT

%description -n projectM-mao-SDL
This package allows the use of the projectM visualization plugin through any
SDL compatible applications.

%prep
%setup -qn projectm-%{commit0}

sed -i -e "s/\$(pm_presets_dir)/\$(DESTDIR)\$(pm_presets_dir)/g" Makefile.am

%build

./autogen.sh

export QT_SELECT=5
%configure --prefix=%{_prefix} --libdir=%{_libdir} --datadir=%{_datadir} --enable-sdl

make DESTDIR=%{buildroot} PREFIX=%{_prefix} %{?_smp_mflags}

%install

make install DESTDIR=%{buildroot} PREFIX=%{_prefix}

#
# Write bash command to select the audio driver
#

# Jack
cat > %{buildroot}/%{_bindir}/%{name}-jack <<EOF
#!/bin/bash

SDL_AUDIODRIVER=jack projectMSDL
EOF
chmod a+x %{buildroot}/%{_bindir}/%{name}-jack

# PulseAudio
cat > %{buildroot}/%{_bindir}/%{name}-pulse <<EOF
#!/bin/bash

SDL_AUDIODRIVER=pulse projectMSDL
EOF
chmod a+x %{buildroot}/%{_bindir}/%{name}-pulse

# ALSA
cat > %{buildroot}/%{_bindir}/%{name}-alsa <<EOF
#!/bin/bash

SDL_AUDIODRIVER=alsa projectMSDL
EOF
chmod a+x %{buildroot}/%{_bindir}/%{name}-alsa

# SDL
mv %{buildroot}/%{_bindir}/projectMSDL %{buildroot}/%{_bindir}/%{name}-sdl

#
# Write desktop files
#
cat > projectM-mao-jack.desktop <<EOF
[Desktop Entry]
Name=projectM Jack Audio Visualization
GenericName=JACK Audio Stream Visualization
Comment=A milkdrop based music visualizer visualizing JackAudio streams on a SDL GUI
Exec=projectM-mao-jack
Icon=projectM
Type=Application
Categories=AudioVideo;Audio;
Terminal=false
EOF

cat > projectM-mao-pulse.desktop <<EOF
[Desktop Entry]
Name=projectM Pulse Audio Visualization
GenericName=Pulse Audio Stream Visualization
Comment=A milkdrop based music visualizer visualizing Pulse Audio streams on a SDL GUI
Exec=projectM-mao-pulse
Icon=projectM
Type=Application
Categories=AudioVideo;Audio;
Terminal=false
EOF

cat > projectM-mao-sdl.desktop <<EOF
[Desktop Entry]
Name=projectM SDL Audio Visualization
GenericName=SDL Audio Stream Visualization
Comment=A milkdrop based music visualizer visualizing SDL Audio streams on a SDL GUI
Exec=projectM-mao-sdl
Icon=projectM
Type=Application
Categories=AudioVideo;Audio;
Terminal=false
EOF

cat > projectM-mao-alsa.desktop <<EOF
[Desktop Entry]
Name=projectM ALSA Audio Visualization
GenericName=ALSA Audio Stream Visualization
Comment=A milkdrop based music visualizer visualizing ALSA Audio streams on a SDL GUI
Exec=projectM-mao-alsa
Icon=projectM
Type=Application
Categories=AudioVideo;Audio;
Terminal=false
EOF

desktop-file-install --dir=%{buildroot}%{_datadir}/applications projectM-mao-jack.desktop
desktop-file-install --dir=%{buildroot}%{_datadir}/applications projectM-mao-pulse.desktop
desktop-file-install --dir=%{buildroot}%{_datadir}/applications projectM-mao-sdl.desktop
desktop-file-install --dir=%{buildroot}%{_datadir}/applications projectM-mao-alsa.desktop

chmod a-x %{buildroot}%{_datadir}/projectM/presets/*.milk

# Install the documentation related to scripts
cp %{SOURCE1} %{buildroot}%{_datadir}/projectM/

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc src/libprojectM/ChangeLog
%license src/libprojectM/COPYING
%{_libdir}/libprojectM.so.*
%{_datadir}/projectM/

%files devel
%{_includedir}/*
%{_libdir}/libprojectM.so
%exclude %{_libdir}/*.a
%exclude %{_libdir}/*.la

%files -n projectM-mao-jack
%{_bindir}/projectM-mao-jack
%{_datadir}/applications/projectM-mao-jack.desktop

%files -n projectM-mao-pulseaudio
%{_bindir}/projectM-mao-pulse
%{_datadir}/applications/projectM-mao-pulse.desktop

%files -n projectM-mao-SDL
%{_bindir}/projectM-mao-sdl
%{_datadir}/applications/projectM-mao-sdl.desktop

%files -n projectM-mao-alsa
%{_bindir}/projectM-mao-alsa
%{_datadir}/applications/projectM-mao-alsa.desktop

%changelog
* Sat Nov 30 2019 Yann Collette <ycollette.nospam@free.fr> - 3.1.1-rc7-11
- install only sdl interface. The Qt one is too buggy. Add scripts to select audio drivers

* Sat Nov 30 2019 Yann Collette <ycollette.nospam@free.fr> - 2.2.1-10
- update to 3.1.1-rc7

* Mon Oct 15 2018 Yann Collette <ycollette.nospam@free.fr> - 2.1.0-10
- update for Fedora 29

* Wed Oct 3 2018 Yann Collette <ycollette.nospam@free.fr> - 2.1.0-10
- Rebuilt for bug fix

* Thu Aug 23 2018 Nicolas Chauvet <kwizart@gmail.com> - 2.1.0-9
- Rebuilt for glew 2.1.0

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Aug 03 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.1.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Tue Jan 10 2017 Orion Poplawski <orion@cora.nwra.com> - 2.1.0-3
- Rebuild for glew 2.0.0

* Sat Mar 19 2016 Sérgio Basto <sergio@serjux.com> - 2.1.0-2
- On epel (6 and 7) disable projectM-libvisual. 

* Wed Mar 16 2016 Sérgio Basto <sergio@serjux.com> - 2.1.0-1
- Update to 2.1.0 .
- deleted: 01-change-texture-size.patch, upstreamed.
- deleted: 04-change-preset-duration.patch, upstreamed.
- deleted: libprojectM-USE_THREADS.patch, configurable.
- deleted: libprojectM-soname.patch, configurable.
- deleted: libprojectM-fonts.patch, configurable.
- deleted: libprojectM-freetype25.patch, it is build well with freetype.
- Add patch to fix FTBFS with GCC6, courtesy of Ralf Corsepius.
- Add as sub packages: libprojectM-qt, libprojectM-qt-devel, projectM-jack,
  projectM-libvisual and projectM-pulseaudio.
- Also checked that remove_pulse_browser_h.patch, projectM-pulseaudio-stat.patch
  and projectM-libvisual-gcc46.patch are upstreamed.
- Add libprojectM-2.1.0-paths.patch and libprojectM-qt-2.1.0-paths.patch, to fix
  _libdir paths 
- Using fedora-review fixed: mix tabs and spaces,
  unused-direct-shlib-dependency, wrong-script-end-of-line-encoding and
  spurious-executable-perm.

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.1-28
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Jan 14 2016 Adam Jackson <ajax@redhat.com> - 2.0.1-27
- Rebuild for glew 1.13

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-26
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat May 02 2015 Kalev Lember <kalevlember@gmail.com> - 2.0.1-25
- Rebuilt for GCC 5 C++11 ABI change

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-24
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Mon Jun 30 2014 Yaakov Selkowitz <yselkowi@redhat.com> - 2.0.1-23
- Fix FTBFS with freetype-2.5 (#1106066)

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Nov 18 2013 Dave Airlie <airlied@redhat.com> - 2.0.1-21
- rebuilt for GLEW 1.10

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-20
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec 13 2012 Adam Jackson <ajax@redhat.com> - 2.0.1-18
- Rebuild for glew 1.9.0

* Thu Jul 26 2012 Rex Dieter <rdieter@fedoraproject.org> 2.0.1-17
- rebuild (glew)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jun  1 2012 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.1-15
- Enhancement of the patch in 2.0.1-11: also override invalid font paths
  passed in by applications as these lead to an immediate crash. (#664088)
- Make -devel base pkg dep arch-specific.

* Tue Feb 28 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-14
- Rebuilt for c++ ABI breakage

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.1-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Jun 20 2011 ajax@redhat.com - 2.0.1-12
- Rebuild for new glew soname

* Sat May  7 2011 Michael Schwendt <mschwendt@fedoraproject.org> - 2.0.1-11
- Also BuildRequires the desired font packages for the safety-checks.
- Drop obsolete README.fedora file since users need not modify their
  config file manually anymore to prevent projectM from crashing.
- Revise fonts patch: check that user's configured font files exist,
  fall back to our defaults, add safety-check in spec file, replace
  font paths in prep section. (#698404, #698381)

* Mon Apr 25 2011 Jameson Pugh <imntreal@gmail.com> - 2.0.1-10
- Fixed fonts patch

* Wed Mar 23 2011 Jameson Pugh <imntreal@gmail.com> - 2.0.1-9
- Correct typo in requirements

* Tue Mar 15 2011 Jameson Pugh <imntreal@gmail.com> - 2.0.1-8
- Replace obsolete bitstream-vera font requirements with dejavu

* Sat Jul 17 2010 Jameson Pugh (imntreal@gmail.com) - 2.0.1-7
- Updated font patch with Orcan's changes

* Sat Jul 10 2010 Jameson Pugh (imntreal@gmail.com) - 2.0.1-6
- Added patches so clementine can be built against it

* Fri May 21 2010 Jameson Pugh (imntreal@gmail.com) - 2.0.1-5
- Don't create fonts directory
- Add a README.fedora for instructions on upgrading from -3

* Mon Apr 05 2010 Jameson Pugh (imntreal@gmail.com) - 2.0.1-4
- Got rid of font symlinks

* Mon Feb 08 2010 Jameson Pugh (imntreal@gmail.com) - 2.0.1-3
- Patch to remove the USE_THREADS option pending an update from upstream

* Sun Jan 10 2010 Jameson Pugh (imntreal@gmail.com) - 2.0.1-2
- Made needed soname bump

* Sun Dec 13 2009 Jameson Pugh (imntreal@gmail.com) - 2.0.1-1
- New release

* Mon Oct 12 2009 Jameson Pugh (imntreal@gmail.com) - 1.2.0r1300-1
- SVN Release to prepare for v2

* Wed Feb 25 2009 Jameson Pugh (imntreal@gmail.com) - 1.2.0-9
- Aparently stdio.h didn't need to be included in BuiltinParams.cpp before, but is now

* Tue Feb 24 2009 Jameson Pugh (imntreal@gmail.com) - 1.2.0-8
- Font packages renamed

* Fri Jan 02 2009 Jameson Pugh (imntreal@gmail.com) - 1.2.0-7
- Per recommendation, switched font packages from bitstream to dejavu

* Mon Dec 22 2008 Jameson Pugh (imntreal@gmail.com) - 1.2.0-6
- Updated font package names

* Tue Nov 04 2008 Jameson Pugh (imntreal@gmail.com) - 1.2.0-5
- Moved sed command from prep to install
- Correct libprojectM.pc patch

* Thu Oct 30 2008 Jameson Pugh (imntreal@gmail.com) - 1.2.0-4
- Removed patch for ChangeLog, and used sed command in the spec
- Added VERBOSE=1 to the make line
- Added patch to correct libprojectM.pc

* Wed Oct 29 2008 Jameson Pugh (imntreal@gmail.com) - 1.2.0-3
- Added a patch to correct ChangeLog EOL encoding
- Cleaned up all Requires and BuildRequires
- Corrected ownership of include/libprojectM and data/projectM
- Removed unnecessary cmake arguments

* Wed Sep 24 2008 Jameson Pugh (imntreal@gmail.com) - 1.2.0-2
- Removed fonts from package
- Added symlinks to the fonts due to hard coded programing

* Tue Sep 02 2008 Jameson Pugh (imntreal@gmail.com) - 1.2.0-1
- New release
- 64-bit patch no longer needed

* Mon Mar 31 2008 Jameson Pugh (imntreal@gmail.com) - 1.1-1
- New release

* Wed Dec 05 2007 Jameson Pugh <imntreal@gmail.com> - 1.01-1
- Initial public release of the package