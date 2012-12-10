Name:		jag
Version:	0.3.2
Release:	%mkrel 1
# README say "under the GPL" so that quite vague
License:	GPLv2+
Group:		Games/Puzzles
Summary:	An arcade-puzzle 2D game to break all of the target blocks
URL:		http://jag.xlabsoft.com
Source0:	http://jag.xlabsoft.com/files/%{name}-%{version}-src.zip
Source1:	http://jag.xlabsoft.com/files/%{name}-%{version}-data.zip

# adujst path to conform to FHS
# not sent upstream, too ugly
Patch0:		jag-0.3.2-path.patch

Patch1:		jag-0.3.2-dso.patch

BuildRequires:	gcc-c++
BuildRequires:	libmesagl-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	libxrandr-devel
BuildRequires:	libxrender-devel
BuildRequires:	qt4-devel
BuildRequires:	unzip

%description
JAG is a free and opensource arcade-puzzle 2D game.

The aim of JAG is to break all of the target pieces on each level, and to do
this before the time runs out. Keep doing this until you have beaten the last
level and won the game. Move game pieces using mouse into matches of 3 or more
in a straight line horizontally or vertically. Doing this on top of the target
cells will break them. The faster targets are removed, the bigger is score.
There are single and double targets. Unlike the single ones, double targets
are removed in two turns. Some pieces are blocked. Before removing such ones,
blocks should be destroyed. Blocks also can be single or double. By breaking
pieces and targets, you're earning score which can be spent for applying a
special tool. Tools make the life easier as they're mostly intended for
breaking several pieces at a time, including blocks and targets. By breaking
pieces of the same type, you're also increasing bonus counters. If you will
collect 500 and more items, you can remove all the same items from the field.

%prep
%setup -q -n %{name}-%{version}-src -a1
%patch0 -p1
%patch1 -p1
%__mv %{name}-%{version}-data/data .
%__rm -rf %{name}-%{version}-data
find . -type f -exec %__chmod 644 {} \;
find . -type d -exec %__chmod 755 {} \;

%build
%qmake_qt4 Game.pro
%make

%__cat > %{name}.desktop <<EOF
[Desktop Entry]
Name=JAG
GenericName=Arcade-puzzle 2D game
Comment=%{summary}
Exec=%{name}
Icon=%{_liconsdir}/%{name}
Type=Application
StartupNotify=false
Categories=Game;LogicGame;
Terminal=false
EOF

%install
%__rm -rf %{buildroot}
%makeinstall INSTALL_ROOT=%{buildroot}

%__mkdir_p %{buildroot}%{_datadir}/applications/
%__install -m644 %{name}.desktop %{buildroot}%{_datadir}/applications/%{name}.desktop

%__mkdir_p %{buildroot}%{_liconsdir}
%__install -m644 images/item4.png %{buildroot}%{_liconsdir}/%{name}.png

%clean
%__rm -rf %{buildroot}

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_liconsdir}/%{name}.png
%{_datadir}/%{name}



%changelog
* Tue Mar 06 2012 Andrey Bondrov <abondrov@mandriva.org> 0.3.2-1mdv2011.0
+ Revision: 782318
- Add patch for DSO issues in Cooker
- New version 0.3.2

* Mon Dec 06 2010 Oden Eriksson <oeriksson@mandriva.com> 0.3.1-2mdv2011.0
+ Revision: 612437
- the mass rebuild of 2010.1 packages

* Thu Feb 25 2010 Michael Scherer <misc@mandriva.org> 0.3.1-1mdv2010.1
+ Revision: 511258
- comment patch to explain why it is not sent upstream
- fix License tag
- adapt and clean rpm from MIB


* Sat Feb 13 2010 Andrey Bondrov <bondrov@math.dvgu.ru> 0.3.1-69.1mib2009.1
- New version 0.3.1
- Clean up and fix spec
- Add patch0 to fix path from usr/local to usr
- MIB (Mandriva Italia Backport) - http://mib.pianetalinux.org

* Thu Oct 15 2009 Beppe Florin <symbianflo@fastwebnet.it>  0.2.6-69.1mib2009.1
- New release
- MIB (Mandriva Italia Backport) - http://mib.pianetalinux.org

* Sun Aug 09 2009 Alberto Altieri <alberto.altieri@gmail.com> 0.2.5-69.1mib2009.1
- First version/release for MIB users
- MIB (Mandriva Italia Backport) new optimized

* Sun Jul 12 2009 Fr. Br. George <george@altlinux.ru> 0.2.3-alt1
- Initial build from scratch
