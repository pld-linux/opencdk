Summary:	Open Crypto Development Kit
Summary(pl):	Open Crypto Development Kit
Name:		opencdk
Version:	0.2.0
Release:	1
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.gnutls.org/pub/gnutls/opencdk/%{name}-%{version}.tar.gz
URL:		http://www.gnu.org/software/gnutls/
BuildRequires:	libgcrypt-devel >= 1.1.5
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
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS README THANKS
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
