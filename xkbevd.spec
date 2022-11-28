Name:		xkbevd
Version:	1.1.5
Release:	1
Summary:	XKB event daemon
Group:		Development/X11
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
License:	MIT
BuildRequires:	pkgconfig(xorg-macros)
BuildRequires:	pkgconfig(x11) >= 1.0.0
BuildRequires:	pkgconfig(xkbfile) >= 1.0.1
BuildRequires:	bison

%description
The xkbevd event daemon listens for specified XKB events and executes
requested commands if they occur. The configuration file consists of a
list of event specification/action pairs and/or variable definitions.

%prep
%autosetup -p1

%build
%configure \
	--x-includes=%{_includedir} \
	--x-libraries=%{_libdir}

%make_build

%install
mkdir -p %{buildroot}/%{_datadir}/X11/xkb
install -m 644 example.cf xkbevd.cf %{buildroot}/%{_datadir}/X11/xkb
%make_install

%files
%{_bindir}/xkbevd
%doc %{_mandir}/man1/xkbevd.1*
%{_datadir}/X11/xkb/*.cf
