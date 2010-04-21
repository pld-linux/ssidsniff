Summary:	Wireless network audit tools
Summary(pl.UTF-8):	Narzędzia do audytu sieci bezprzewodowych
Name:		ssidsniff
Version:	0.53
Release:	3
Epoch:		0
License:	GPL v2
Group:		Networking/Utilities
Source0:	http://www.bastard.net/~kos/wifi/%{name}-%{version}.tar.gz
# Source0-md5:	fefdb94e5c5ca4a8085b8531a679638c
Patch0:		%{name}-ncurses.patch
URL:		http://www.bastard.net/~kos/wifi/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libpcap-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A curses based tool that allows identification, classification and
data capturing of wireless networks. The interface is inspired from
the unix top(1) utility.

%description -l pl.UTF-8
Oparte na curses narzędzie pozwalające na identyfikację, klasyfikację
i wychwytywanie danych z sieci bezprzewodowych. Interfejs jest
zainspirowany uniksowym narzędziem top(1).

%prep
%setup -q
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-libcurses=%{_includedir}/ncurses
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man8/*
