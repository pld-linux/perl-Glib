#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pnam	Glib
Summary:	Perl Glib bindings
Summary(pl):	Wi±zania Glib dla Perla
Name:		perl-Glib
Version:	1.071
Release:	1
License:	LGPL v2.1+
Group:		Development/Languages/Perl
Source0:	http://dl.sourceforge.net/gtk2-perl/%{pnam}-%{version}.tar.gz
# Source0-md5:	c29d87669a2b056c10ac9bef2b729854
URL:		http://gtk2-perl.sf.net/
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	perl-ExtUtils-Depends >= 0.201
BuildRequires:	perl-ExtUtils-PkgConfig >= 1.06
BuildRequires:	perl-devel >= 1:5.8.0
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

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{perl_vendorarch}/Glib/*.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README*
%{perl_vendorarch}/*.pm
%dir %{perl_vendorarch}/Glib
%{perl_vendorarch}/Glib/*.pm
%{perl_vendorarch}/Glib/Install
%{perl_vendorarch}/Glib/Object
%dir %{perl_vendorarch}/auto/Glib
%attr(755,root,root) %{perl_vendorarch}/auto/Glib/Glib.so
%{perl_vendorarch}/auto/Glib/Glib.bs
%{_mandir}/man3/*
