Name:		xkbevd
Version:	1.1.0
Release:	%mkrel 1
Summary:	XKB event daemon
Group:		Development/X11
URL:		http://xorg.freedesktop.org
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxkbfile-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1
BuildRequires:	bison

%description
The xkbevd event daemon listens for specified XKB events and executes
requested commands if they occur. The configuration file consists of a
list of event specification/action pairs and/or variable definitions.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir} \
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
