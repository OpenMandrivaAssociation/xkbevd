Name:		xkbevd
Version:	1.0.2
Release:	%mkrel 4
Summary:	XKB event daemon
Group:		Development/X11
Source:		http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires:	libx11-devel >= 1.0.0
BuildRequires:	libxkbfile-devel >= 1.0.1
BuildRequires:	x11-util-macros >= 1.0.1

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
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/xkbevd
%{_mandir}/man1/xkbevd.1*

