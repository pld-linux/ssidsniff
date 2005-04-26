Summary:	Wireless network audit tools
Name:		ssidsniff
Version:	0.41
Release:	0.1
Epoch:		0
License:	GPL v2
Group:		Networking/Utilities
Source0:	http://www.bastard.net/~kos/wifi/%{name}-%{version}.tar.gz
# Source0-md5:	dec36c915e7dc544cd275594e3da7e44
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

%prep
%setup -q -n %{name}-%{version}
%patch0 -p1

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
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
