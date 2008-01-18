Name:		xkbevd
Version:	1.0.2
Release:	%mkrel 5
Summary:	XKB event daemon
Group:		Development/X11
URL: http://xorg.freedesktop.org
########################################################################
# git clone git://git.mandriva.com/people/pcpa/xorg/app/xman xorg/app/xkbevd
# cd xorg/app/xkbevd
# git-archive --format=tar --prefix=xkbevd-1.0.2/ xkbevd-1_0_2 | bzip2 -9 > xkbevd-1.0.2.tar.bz2
########################################################################
Source:		%{name}-%{version}.tar.bz2
License:	MIT
########################################################################
# git-format-patch xkbevd-1_0_2..origin/mandriva
Patch1: 0001-Rename-.cvsignore-to-.gitignore.patch
Patch2: 0002-Add-to-.gitignore-to-skip-patch-emacs-droppings.patch
Patch3: 0003-Add-all-option-to-allow-using-xkbdev-almost-as-xev.patch
Patch4: 0004-Add-xkbdev.cf-default-configuration-file.patch
########################################################################
BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires:	x11-util-macros		>= 1.1.5
BuildRequires:	libx11-devel		>= 1.1.3
BuildRequires:	libxkbfile-devel	>= 1.0.4

%description
The xkbevd event daemon listens for specified XKB events and executes
requested commands if they occur. The configuration file consists of a
list of event specification/action pairs and/or variable definitions.

%prep
%setup -q -n %{name}-%{version}

%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
autoreconf -ifs
%configure	--x-includes=%{_includedir} \
		--x-libraries=%{_libdir}

%make

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/%{_datadir}/X11/xkb
install -m 644 example.cf xkbevd.cf %{buildroot}/%{_datadir}/X11/xkb
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xkbevd
%{_mandir}/man1/xkbevd.1*
%{_datadir}/X11/xkb/*.cf
