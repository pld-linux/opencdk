Summary:	Open Crypto Development Kit
Summary(pl.UTF-8):	Open Crypto Development Kit
Name:		opencdk
Version:	0.6.6
Release:	4
License:	GPL v2+
Group:		Libraries
Source0:	ftp://ftp.gnutls.org/pub/gnutls/opencdk/%{name}-%{version}.tar.bz2
# Source0-md5:	813d62d7afe7b2c2d8f3df0a6c9d9331
URL:		http://www.gnu.org/software/gnutls/
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake >= 1:1.10
BuildRequires:	libtool
BuildRequires:	libgcrypt-devel >= 1.2.2
BuildRequires:	zlib-devel
Requires:	libgcrypt >= 1.2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library provides basic parts of the OpenPGP message format.

%description -l pl.UTF-8
Biblioteka dostarcza podstawową obsługę formatu OpenPGP.

%package devel
Summary:	Header files etc to develop opencdk applications
Summary(pl.UTF-8):	Pliki nagłówkowe i inne do opencdk
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libgcrypt-devel >= 1.2.2
Requires:	zlib-devel

%description devel
Header files etc to develop opencdk applications.

%description devel -l pl.UTF-8
Pliki nagłówkowe i inne do opencdk.

%package static
Summary:	Static opencdk library
Summary(pl.UTF-8):	Biblioteka statyczna opencdk
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static opencdk library.

%description static -l pl.UTF-8
Biblioteka statyczna opencdk.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

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
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %ghost %{_libdir}/libopencdk.so.10
%attr(755,root,root) %{_libdir}/libopencdk.so.*.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/*.html
%attr(755,root,root) %{_bindir}/opencdk-config
%attr(755,root,root) %{_libdir}/libopencdk.so
%{_libdir}/libopencdk.la
%{_includedir}/opencdk.h
%{_aclocaldir}/opencdk.m4
%{_pkgconfigdir}/opencdk.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libopencdk.a
