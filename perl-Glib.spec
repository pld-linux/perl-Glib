#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pnam	Glib
Summary:	Perl Glib bindings
Summary(pl):	Wi±zania Glib dla Perla
Name:		perl-Glib
Version:	0.92
Release:	0.1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	3b66871d22fdffdb645a33c7e1e19192
URL:		http://gtk2-perl.sf.net/
BuildRequires:	glib2-devel
BuildRequires:	perl-ExtUtils-Depends
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	pkgconfig
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides perl access to Glib and GLib's GObject libraries.

%description -l pl
Ten modu³ daje dostêp z poziomu Perla do bibliotek GLib i GObject.

%prep
%setup -q -n %{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README*
%{perl_vendorarch}/*.pm
%dir %{perl_vendorarch}/Glib
%{perl_vendorarch}/Glib
%dir %{perl_vendorarch}/auto/Glib
%attr(755,root,root) %{perl_vendorarch}/auto/Glib/Glib.so
%{perl_vendorarch}/auto/Glib/Glib.bs
%{_mandir}/man3/*
