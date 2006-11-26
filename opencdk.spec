Summary:	Open Crypto Development Kit
Summary(pl):	Open Crypto Development Kit
Name:		opencdk
Version:	0.5.11
Release:	2
License:	GPL
Group:		Libraries
Source0:	ftp://ftp.gnutls.org/pub/gnutls/opencdk/%{name}-%{version}.tar.gz
# Source0-md5:	de16f52a7f2215e3df9e81067ebae60d
URL:		http://www.gnu.org/software/gnutls/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	libgcrypt-devel >= 1.1.94
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This library provides basic parts of the OpenPGP message format.

%description -l pl
Biblioteka dostarcza podstawow� obs�ug� formatu OpenPGP.

%package devel
Summary:	Header files etc to develop opencdk applications
Summary(pl):	Pliki nag��wkowe i inne do opencdk
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libgcrypt-devel >= 1.1.94
Requires:	zlib-devel

%description devel
Header files etc to develop opencdk applications.

%description devel -l pl
Pliki nag��wkowe i inne do opencdk.

%package static
Summary:	Static opencdk library
Summary(pl):	Biblioteka statyczna opencdk
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static opencdk library.

%description static -l pl
Biblioteka statyczna opencdk.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
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
%attr(755,root,root) %{_libdir}/libopencdk.so.*.*

%files devel
%defattr(644,root,root,755)
%doc doc/*.html doc/DETAILS
%attr(755,root,root) %{_bindir}/opencdk-config
%attr(755,root,root) %{_libdir}/libopencdk.so
%{_libdir}/libopencdk.la
%{_includedir}/opencdk.h
%{_aclocaldir}/opencdk.m4
%{_pkgconfigdir}/opencdk.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libopencdk.a
