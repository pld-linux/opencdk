Summary:	Open Crypto Development Kit
Summary(pl):	Open Crypto Development Kit
Name:		opencdk
Version:	0.4.3
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.gnutls.org/pub/gnutls/opencdk/%{name}-%{version}.tar.gz
URL:		http://www.gnu.org/software/gnutls/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libgcrypt-devel >= 1.1.12
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library provides basic parts of the OpenPGP message format.

%description -l pl
Biblioteka dostarcza podstawow± obs³ugê formatu OpenPGP.

%package devel
Summary:	Header files etc to develop opencdk applications
Summary(pl):	Pliki nag³ówkowe i inne do opencdk
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files etc to develop opencdk applications.

%description devel -l pl
Pliki nag³ówkowe i inne do opencdk.

%package static
Summary:	Static opencdk library
Summary(pl):	Biblioteka statyczna opencdk
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static opencdk library.

%description static -l pl
Biblioteka statyczna opencdk.

%prep
%setup -q

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}
%{__make} -C doc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_aclocaldir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install src/opencdk.m4 $RPM_BUILD_ROOT%{_aclocaldir} 

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README THANKS NEWS ChangeLog
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/*.html doc/DETAILS
%attr(755,root,root) %{_bindir}/*-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h
%{_aclocaldir}/*.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
