Name:		jag
Version:	0.3.1
Release:	%mkrel 2
# README say "under the GPL" so that quite vague
License:	GPLv2+
Group:		Games/Puzzles
Summary:	An arcade-puzzle 2D game to break all of the target blocks
URL:		http://jag.xlabsoft.com
Source:		http://jag.xlabsoft.com/files/%name-%version-src.zip

# adujst path to conform to FHS
# not sent upstream, too ugly
Patch0:		%{name}-path.patch

BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  gcc-c++
BuildRequires:  libmesagl-devel
BuildRequires:  libSDL-devel
BuildRequires:  libSDL_mixer-devel
BuildRequires:  libxrandr-devel
BuildRequires:  libxrender-devel
BuildRequires:  qt4-devel
BuildRequires:  unzip

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
%setup -q -n %name-%version-src
%patch0 -p1

%build
%qmake_qt4 Game.pro
%make

cat > %name.desktop <<EOF
[Desktop Entry]
Name=JAG
GenericName=Arcade-puzzle 2D game
Comment=%summary
Exec=%name
Icon=%_liconsdir/%name
Type=Application
StartupNotify=false
Categories=Game;LogicGame;
Terminal=false
EOF

%install
rm -rf %buildroot
%makeinstall INSTALL_ROOT=%buildroot

install -d -m755 %buildroot/%_datadir/applications/
install -m644 %name.desktop %buildroot/%_datadir/applications/%name.desktop

install -d -m755 %buildroot/%_liconsdir
install -m644 images/item4.png %buildroot/%_liconsdir/%name.png

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%_bindir/%name
%_datadir/applications/%name.desktop
%_liconsdir/%name.png
%_datadir/%name/

