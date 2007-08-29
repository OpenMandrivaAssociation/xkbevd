Name: xkbevd
Version: 1.0.2
Release: %mkrel 2
Summary: XKB event daemon
Group: Development/X11
Source: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT
BuildRoot: %{_tmppath}/%{name}-root

BuildRequires: libx11-devel >= 1.0.0
BuildRequires: libxkbfile-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1

%description
CHECK

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x	--x-includes=%{_includedir}\
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
%{_mandir}/man1/xkbevd.1x*


