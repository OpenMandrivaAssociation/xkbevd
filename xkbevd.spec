Name:		xkbevd
Version:	1.1.3
Release:	7
Summary:	XKB event daemon
Group:		Development/X11
URL:		http://xorg.freedesktop.org
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires: pkgconfig(x11) >= 1.0.0
BuildRequires: pkgconfig(xkbfile) >= 1.0.1
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
mkdir -p %{buildroot}/%{_datadir}/X11/xkb
install -m 644 example.cf xkbevd.cf %{buildroot}/%{_datadir}/X11/xkb
%makeinstall_std

%files
%{_bindir}/xkbevd
%{_mandir}/man1/xkbevd.1*
%{_datadir}/X11/xkb/*.cf


%changelog
* Mon Mar 26 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.1.3-1
+ Revision: 786806
- version update 1.1.3

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.2-2
+ Revision: 671328
- mass rebuild

* Thu Dec 09 2010 Thierry Vignaud <tv@mandriva.org> 1.1.2-1mdv2011.0
+ Revision: 617320
- new release

* Tue Nov 02 2010 Thierry Vignaud <tv@mandriva.org> 1.1.1-1mdv2011.0
+ Revision: 591827
- new release

* Wed Nov 11 2009 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.1.0-1mdv2010.1
+ Revision: 464711
- New version: 1.1.0
  Patch 1 was integrated upstream in a different way
  Other patches were fully integrated upstream

* Sat Mar 07 2009 Michael Scherer <misc@mandriva.org> 1.0.2-8mdv2009.1
+ Revision: 351559
- add Patch3, fix format string error

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-7mdv2009.0
+ Revision: 226047
- rebuild

* Tue Feb 12 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-6mdv2008.1
+ Revision: 166582
- Revert to use upstream tarball, build requires and remove non mandatory local patches.
  Kept for now local patch to allow using xkbevd as a tool to debug xkb.

* Fri Jan 18 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-5mdv2008.1
+ Revision: 154671
- Update BuildRequires and resubmit.
  Add patch to allow using xkbevd in a similar way to xev, but printing
  XKB related events, that should be useful for debugging.
  Added mandriva branch git repository to store patch and new default
  configuration file.

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 31 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.2-4mdv2008.0
+ Revision: 76538
- rebuild for 2008
- add description
- slight spec clean

  + Thierry Vignaud <tv@mandriva.org>
    - do not hardcode lzma extension!!!

